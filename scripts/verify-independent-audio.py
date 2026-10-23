"""Verify blind local ASR receipts with the unchanged phonetic acceptance rules."""
import argparse
import copy
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
read=lambda p:json.loads(p.read_text('utf-8'))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
spec=importlib.util.spec_from_file_location('screen',ROOT/'scripts/screen-audio-qwen.py')
screen=importlib.util.module_from_spec(spec);spec.loader.exec_module(screen)

def verified_report(root,plan,primary,report,scripts,model_sha):
    assert report['model']=='Whisper large-v3' and report['modelSha256']==model_sha, 'Unverified recognizer'
    jobs={job['receipt']:job for job in plan['jobs']}
    updated=copy.deepcopy(primary)
    accepted=[]
    for row in report['clips']:
        job=jobs[row['receipt']]
        assert job['mood']=='clear' and row['text']==job['text'], 'Wrong target'
        raw=read(root/job['receipt'])
        assert raw.get('take',0)>=1, 'A genuine recording repair is required'
        assert raw['rawSha256']==row['rawSha256']==sha(root/raw['rawFile']), 'Changed source'
        cue=raw.get('pronunciationContext',{})
        expected=cue.get('synthesisText',job['text']) if cue.get('extract')=='whole' else job['text']
        status=screen.transcript_status(expected,row['transcript'],scripts[job['text']].get('pinyin'))
        assert status==row['status'], 'Claimed transcription result does not match the existing screen'
        if status=='needs-review':continue
        key=raw['rawSha256']+':'+job['text']
        previous=updated['clips'][key]
        if previous.get('independentVerification',{}).get('modelSha256')==model_sha:continue
        assert previous['status']=='needs-review', 'Only unresolved recordings may be rescued'
        proof=dict(model=report['model'],modelSha256=model_sha,rawSha256=raw['rawSha256'],
                   transcript=row['transcript'],status=status,
                   method='Blind local transcription, no expected-text prompt; unchanged exact-text and phonetic comparison.')
        updated['clips'][key]=dict(previous,primaryScreen=copy.deepcopy(previous),
            transcript=row['transcript'],status=status,independentVerification=proof)
        accepted.append(dict(text=job['text'],receipt=job['receipt'],**proof))
    return updated,accepted

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('report',type=Path)
    args=parser.parse_args()
    sys.stdout.reconfigure(encoding='utf-8')
    cache=ROOT/'.cache/sayo-qwen-approved'
    plan_path=cache/'plan.json'
    primary=read(cache/'screening.json')
    assert primary['planSha256']==sha(plan_path), 'Stale primary screening plan'
    report=read(args.report)
    scripts={e['text']:e for e in read(ROOT/'content/audio-scripts.json')}
    plan=read(plan_path)
    assert plan['scriptsSha256']==sha(ROOT/'content/audio-scripts.json'), 'Stale manifest'
    updated,accepted=verified_report(ROOT,plan,primary,report,scripts,sha(ROOT/'.models/whisper/large-v3.pt'))
    evidence=dict(date=datetime.now(timezone.utc).isoformat(),planSha256=sha(plan_path),
        method='Independent blind local recognition with unchanged acceptance criteria. Not a reviewed/pronunciation-certified flag.',
        accepted=accepted,diagnosis=report)
    screen.atomic(ROOT/'content/voices/independent-audio-verification.json',evidence)
    screen.atomic(cache/'screening.json',updated)
    print('Independently verified recordings:',len(accepted))

if __name__=='__main__':main()
