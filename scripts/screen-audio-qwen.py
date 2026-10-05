"""Resume advisory Mandarin transcription checks without supplying the expected text."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
import time
import librosa
import numpy as np
from opencc import OpenCC
from pypinyin import lazy_pinyin, Style
import soundfile as sf
import torch
import whisper

ROOT=Path(__file__).resolve().parents[1]
CACHE=ROOT/'.cache/sayo-qwen-approved'
digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda p:json.loads(p.read_text('utf-8'))
convert=OpenCC('t2s')

def normalize(text):
    text=convert.convert(text)
    def number(match):
        n=int(match.group());digits='零一二三四五六七八九'
        if n<10:return digits[n]
        if n<100:return (digits[n//10] if n>=20 else '')+'十'+(digits[n%10] if n%10 else '')
        return match.group()
    text=re.sub(r'\d+',number,text)
    return re.sub(r'[^\u4e00-\u9fff0-9]', '', text)

def atomic(path,data):
    tmp=path.with_suffix('.tmp');tmp.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n','utf-8');tmp.replace(path)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--follow',action='store_true')
    parser.add_argument('--device',default='cuda')
    parser.add_argument('--repeat-short',action='store_true')
    parser.add_argument('--carrier',action='store_true')
    args=parser.parse_args()
    sys.stdout.reconfigure(encoding='utf-8')
    torch.set_num_threads(3)
    path=CACHE/'screening.json'
    report=read(path) if path.exists() else dict(method='Whisper medium, Chinese, no expected text prompt. OpenCC t2s orthography only; tone-number pinyin comparison flags homophone transcripts separately. Not tone or naturalness certification.',clips={})
    model=None
    while True:
        plan=read(CACHE/'plan.json')
        report['planSha256']=digest(CACHE/'plan.json')
        waiting=0
        for job in plan['jobs']:
            receipt=ROOT/job['receipt']
            if not receipt.exists():waiting+=1;continue
            record=read(receipt);hash=record['rawSha256']
            source=ROOT/record['rawFile']
            assert digest(source)==hash
            id=hash+':'+job['text']
            previous=report['clips'].get(id)
            repeat=bool(args.repeat_short and previous and previous['status']=='needs-review'
                and len(normalize(job['text']))<=3 and 'repeatedTranscript' not in previous)
            carrier=bool(args.carrier and previous and previous['status']=='needs-review' and record.get('carrierFile') and 'carrierTranscript' not in previous)
            if previous and not repeat and not carrier:continue
            if record.get('approvedTake'):
                result=dict(text=job['text'],transcript=None,status='owner-approved-take',rawSha256=hash)
            else:
                if model is None:model=whisper.load_model('medium',device=args.device,download_root=str(ROOT/'.models/whisper'))
                if carrier:
                    source=ROOT/record['carrierFile']
                    assert digest(source)==record['carrierSha256']
                audio,sr=sf.read(source)
                audio=librosa.resample(audio.astype(np.float32),orig_sr=sr,target_sr=16000)
                if repeat and not carrier:
                    # More acoustic context, with no expected-text prompt or changed pronunciation.
                    audio=np.concatenate([audio,np.zeros(8000,dtype=np.float32),audio,np.zeros(8000,dtype=np.float32),audio])
                transcript=model.transcribe(audio,language='zh',temperature=0,beam_size=5,condition_on_previous_text=False,fp16=args.device=='cuda')['text']
                expected,heard=normalize(job['text']),normalize(transcript)
                status='text-match' if expected==heard else 'needs-review'
                if repeat and heard in [expected*2,expected*3]:status='repeated-text-match'
                if status=='needs-review' and expected and heard and lazy_pinyin(expected,style=Style.TONE3,neutral_tone_with_five=True)==lazy_pinyin(heard,style=Style.TONE3,neutral_tone_with_five=True):
                    status='homophone-transcript'
                result=dict(text=job['text'],transcript=transcript,status=status,rawSha256=hash)
                if carrier:
                    tail=heard[-len(expected):]
                    if tail==expected:status='carrier-text-match'
                    elif lazy_pinyin(tail,style=Style.TONE3,neutral_tone_with_five=True)==lazy_pinyin(expected,style=Style.TONE3,neutral_tone_with_five=True):status='carrier-homophone-transcript'
                    result=dict(previous,carrierTranscript=transcript,status=status)
                if repeat and not carrier:
                    result.update(transcript=previous['transcript'],repeatedTranscript=transcript)
            report['clips'][id]=result
            print(result['status'],job['text'],job['mood'],result['transcript'],flush=True)
            atomic(path,report)
        current=[]
        extra_checks=False
        for job in plan['jobs']:
            receipt=ROOT/job['receipt']
            if receipt.exists():
                record=read(receipt)
                result=report['clips'].get(record['rawSha256']+':'+job['text'],{'status':'needs-review'})
                current.append(result)
                if result['status']=='needs-review':
                    extra_checks |= bool((args.repeat_short and len(normalize(job['text']))<=3 and 'repeatedTranscript' not in result)
                        or (args.carrier and record.get('carrierFile') and 'carrierTranscript' not in result))
        report['pendingGeneration']=waiting
        report['unreviewed']=waiting+sum(c['status']=='needs-review' for c in current)
        report['homophoneTranscripts']=sum(c['status']=='homophone-transcript' for c in current)
        atomic(path,report)
        if extra_checks:continue
        if not args.follow or not waiting:break
        time.sleep(10)
    print('SCREENED',len(current),'unreviewed',report['unreviewed'],'homophones',report['homophoneTranscripts'],flush=True)

if __name__=='__main__':main()
