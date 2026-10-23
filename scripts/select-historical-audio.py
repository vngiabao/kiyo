"""Reuse a verified earlier repair when newer takes remain unresolved."""
import argparse,hashlib,importlib.util,json,re
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
read=lambda p:json.loads(p.read_text('utf-8'))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def module(name,file):
    spec=importlib.util.spec_from_file_location(name,ROOT/'scripts'/file)
    value=importlib.util.module_from_spec(spec);spec.loader.exec_module(value);return value
prepare=module('prepare','prepare-audio-gap-repair.py')
screen=module('screen','screen-audio-qwen.py')

def candidate(root,entry,path,profile_sha,roster_sha,screening):
    if not path.exists():return None
    row=read(path)
    if row.get('profileSha256')!=profile_sha or row.get('rosterSha256')!=roster_sha:return None
    if row.get('pipeline')!=1 or row.get('take',0)<1 or row.get('mood')!='clear' or row.get('text')!=entry['text']:return None
    if row.get('delivery')!=entry.get('delivery') or row.get('approvedTake'):return None
    fields=['text','mood','model','profileSha256','rosterSha256','pipeline','take']
    if any(field not in row for field in fields):return None
    recipe={field:row[field] for field in fields}
    for field in ['delivery','pronunciationContext']:
        if field in row:recipe[field]=row[field]
    token=hashlib.sha256(json.dumps(recipe,sort_keys=True,ensure_ascii=False).encode()).hexdigest()[:12]
    if path.name!=f'{entry["id"]}-clear-{token}.json':return None
    if not re.fullmatch(r'\.cache/sayo-qwen-approved/[A-Za-z0-9_-]+\.wav',row['rawFile'].replace('\\','/')):return None
    source=root/row['rawFile']
    if not source.exists() or sha(source)!=row['rawSha256']:return None
    evidence=screening['clips'].get(row['rawSha256']+':'+entry['text'])
    if not evidence:return None
    cue=row.get('pronunciationContext',{})
    expected=cue.get('synthesisText',entry['text']) if cue.get('extract')=='whole' else entry['text']
    if screen.normalize(expected)!=screen.normalize(entry['text']):
        try:prepare.checked_cue(entry['text'],expected,entry.get('pinyin'))
        except AssertionError:return None
    status=screen.transcript_status(expected,evidence.get('transcript',''),entry.get('pinyin'))
    if status=='needs-review':return None
    return dict(text=entry['text'],token=entry['id']+'-clear',take=row['take'],
                receipt=path.relative_to(root).as_posix(),rawSha256=row['rawSha256'],
                context=row.get('pronunciationContext'),status=status,transcript=evidence.get('transcript'))

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--baselines',type=Path,nargs='+',required=True)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--apply',action='store_true')
    args=parser.parse_args();sys.stdout.reconfigure(encoding='utf-8')
    targets=set(read(ROOT/'content/voices/audio-deferred.json')['texts'])
    entries={e['text']:e for e in read(ROOT/'content/audio-scripts.json')}
    profile_sha=sha(ROOT/'content/voices/approved-b-half/profile.json')
    roster_sha=sha(ROOT/'content/voices/sayo-roster-staged.json')
    screening=read(ROOT/'.cache/sayo-qwen-approved/screening.json')
    paths={e['receipt'] for p in args.baselines for row in read(p).get('entries',[]) if row['text'] in targets for e in row.get('evidence',[])}
    choices={}
    for rel in sorted(paths):
        path=ROOT/rel
        if not path.exists():continue
        row=read(path);text=row.get('text')
        if text not in targets:continue
        result=candidate(ROOT,entries[text],path,profile_sha,roster_sha,screening)
        if result:choices.setdefault(text,[]).append(result)
    picked=[min(rows,key=lambda r:(r['status']!='text-match',-r['take'])) for rows in choices.values()]
    base=ROOT/'content/voices/approved-b-half'
    retries=read(base/'retries.json');contexts=read(base/'pronunciation-contexts.json')
    highest_path=base/'highest-takes.json'
    highest=read(highest_path) if highest_path.exists() else {}
    before=dict(retries=dict(retries),contexts=dict(contexts),highest=dict(highest))
    for row in picked:
        key=row['token'];highest[key]=max(highest.get(key,0),retries.get(key,0),row['take'])
        retries[key]=row['take']
        if row['context'] is not None:contexts[key]=row['context']
        else:contexts.pop(key,None)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    screen.atomic(args.output,dict(selected=picked,inspectedReceipts=len(paths),before=before,applied=args.apply))
    if args.apply:
        screen.atomic(base/'retries.json',retries);screen.atomic(base/'pronunciation-contexts.json',contexts);screen.atomic(highest_path,highest)
    print('Verified earlier repairs selected:',len(picked))

if __name__=='__main__':main()
