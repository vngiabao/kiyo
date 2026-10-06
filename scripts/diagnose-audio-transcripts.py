"""Independent local ASR diagnosis; never changes screening or installs speech."""
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import librosa
import soundfile as sf
import torch
import whisper

ROOT=Path(__file__).resolve().parents[1]
read=lambda p:json.loads(p.read_text('utf-8'))
spec=importlib.util.spec_from_file_location('screen',ROOT/'scripts/screen-audio-qwen.py')
screen=importlib.util.module_from_spec(spec)
spec.loader.exec_module(screen)

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    torch.set_num_threads(3)
    cache=ROOT/'.cache/sayo-qwen-approved'
    plan=read(cache/'plan.json')
    primary=read(cache/'screening.json')['clips']
    grouped={}
    for job in plan['jobs']:
        receipt=read(ROOT/job['receipt'])
        status=primary.get(receipt['rawSha256']+':'+job['text'],{})
        grouped.setdefault(job['text'],[]).append((job,receipt,status))
    pending=[item for rows in grouped.values() if all(item[2].get('status')=='needs-review' for item in rows) for item in rows if item[0]['mood']=='clear']
    model=whisper.load_model('large-v3',device='cuda',download_root=str(ROOT/'.models/whisper'))
    model_hash=hashlib.sha256((ROOT/'.models/whisper/large-v3.pt').read_bytes()).hexdigest()
    scripts={e['text']:e for e in read(ROOT/'content/audio-scripts.json')}
    report=dict(model='Whisper large-v3',modelSha256=model_hash,method='Independent Mandarin transcription without expected text or prompt; diagnostic only.',clips=[])
    out=ROOT/'output/gates/batch-03-large-transcripts.json'
    for job,receipt,previous in pending:
        path=ROOT/receipt['rawFile']
        assert hashlib.sha256(path.read_bytes()).hexdigest()==receipt['rawSha256']
        samples,rate=sf.read(path)
        samples=librosa.resample(samples.astype('float32'),orig_sr=rate,target_sr=16000)
        heard=model.transcribe(samples,language='zh',temperature=0,beam_size=5,condition_on_previous_text=False,fp16=True)['text']
        result=dict(text=job['text'],receipt=job['receipt'],rawSha256=receipt['rawSha256'],primaryTranscript=previous.get('transcript'),transcript=heard,status=screen.transcript_status(job['text'],heard,scripts[job['text']].get('pinyin')))
        report['clips'].append(result)
        out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n','utf-8')
        print(result['status'],job['text'],repr(heard),flush=True)

if __name__=='__main__':main()
