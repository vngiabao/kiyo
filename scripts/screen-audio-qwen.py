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

def normalize(text, digit_sequence=False, year_digits=False):
    text=convert.convert(text)
    if year_digits:
        digits='零一二三四五六七八九'
        text=re.sub(r'(?<!\d)\d{4}(?=年)',lambda match:''.join(digits[int(c)] for c in match.group()),text)
    def number(match):
        digits='零一二三四五六七八九'
        if digit_sequence or match.group().startswith('0'):
            return ''.join(digits[int(c)] for c in match.group())
        n=int(match.group())
        if n<10:return digits[n]
        if n<100:return (digits[n//10] if n>=20 else '')+'十'+(digits[n%10] if n%10 else '')
        if n<1000:
            rest=n%100
            tail='' if rest==0 else ('零'+digits[rest] if rest<10 else digits[rest//10]+'十'+(digits[rest%10] if rest%10 else ''))
            return digits[n//100]+'百'+tail
        return match.group()
    text=re.sub(r'\d+',number,text)
    return re.sub(r'[^\u4e00-\u9fff0-9]', '', text)

def transcript_status(expected_text, transcript, authored_pinyin=None):
    digit_sequence='幺' in expected_text or bool(re.fullmatch(r'[零一二三四五六七八九幺]+',normalize(expected_text)))
    year_digits=bool(re.search(r'[零一二三四五六七八九]{4}年',expected_text))
    expected,heard=normalize(expected_text,digit_sequence,year_digits),normalize(transcript,digit_sequence,year_digits)
    if expected==heard:return 'text-match'
    # ASR writes spoken phone-number yao as 一. Synthesis still receives 幺.
    if '幺' in expected and expected.replace('幺','一')==heard:return 'phone-number-transcript'
    if '幺' in expected:expected=expected.replace('幺','一')
    # Whisper often omits the orthographic 儿 suffix for rhotic vowels. This is
    # an explicitly labelled transcript equivalence, not a pronunciation check.
    without_erhua=lambda t:re.sub(r'([点玩哪这那会])儿',r'\1',t)
    if expected!=without_erhua(expected) and without_erhua(expected)==heard:
        return 'erhua-transcript'
    if expected and heard and lazy_pinyin(expected,style=Style.TONE3,neutral_tone_with_five=True)==lazy_pinyin(heard,style=Style.TONE3,neutral_tone_with_five=True):
        return 'homophone-transcript'
    # The dictionary-only reading of 地 is dì, even in a de adverbial.
    # Use the independently checked authored reading only at that exact
    # position; ground dì and missing/different syllables remain failures.
    syllables=re.findall(r"[a-züāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ]+",(authored_pinyin or '').lower())
    if len(expected)==len(heard)==len(syllables):
        differences=[i for i,(a,b) in enumerate(zip(expected,heard)) if a!=b]
        if differences and all(expected[i]=='地' and heard[i]=='的' and syllables[i]=='de' for i in differences):
            return 'homophone-transcript'
    return 'needs-review'

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
    scripts={entry['text']:entry for entry in read(ROOT/'content/audio-scripts.json')}
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
            if previous and previous['status'].startswith('carrier-') and len(normalize(job['text']))>3:
                # A carrier may contain the whole sentence while the crop contains
                # only its ending. Long crops must match their own transcription.
                previous.update(status=transcript_status(job['text'],previous.get('transcript','')),cropCheckVersion=1)
                atomic(path,report)
            if previous and previous['status']=='needs-review':
                cue=record.get('pronunciationContext',{})
                expected_text=cue.get('synthesisText',job['text']) if cue.get('extract')=='whole' else job['text']
                status=transcript_status(expected_text,previous.get('transcript',''),scripts.get(job['text'],{}).get('pinyin'))
                if status!='needs-review':
                    previous.update(status=status,orthographicCheckVersion=2)
                    atomic(path,report)
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
                cue=record.get('pronunciationContext',{})
                expected_text=cue.get('synthesisText',job['text']) if cue.get('extract')=='whole' else job['text']
                expected,heard=normalize(expected_text),normalize(transcript)
                status=transcript_status(expected_text,transcript,scripts.get(job['text'],{}).get('pinyin'))
                if repeat and heard in [expected*2,expected*3]:status='repeated-text-match'
                if status=='needs-review' and expected and heard and lazy_pinyin(expected,style=Style.TONE3,neutral_tone_with_five=True)==lazy_pinyin(heard,style=Style.TONE3,neutral_tone_with_five=True):
                    status='homophone-transcript'
                result=dict(text=job['text'],transcript=transcript,status=status,rawSha256=hash)
                if carrier:
                    tail=heard[-len(expected):]
                    if len(expected)<=3:
                        if tail==expected:status='carrier-text-match'
                        elif lazy_pinyin(tail,style=Style.TONE3,neutral_tone_with_five=True)==lazy_pinyin(expected,style=Style.TONE3,neutral_tone_with_five=True):status='carrier-homophone-transcript'
                    else:
                        status=transcript_status(job['text'],previous.get('transcript',''))
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
