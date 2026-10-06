"""Report distinct context shortages; vocabulary introductions are separate."""
import argparse,json
from pathlib import Path
parser=argparse.ArgumentParser()
parser.add_argument('root',type=Path)
parser.add_argument('--prefix',default='s3-')
args=parser.parse_args()
def sentences(value):
    result=[]
    if isinstance(value,dict):
        if 'zh' in value:result.append(value['zh'].replace('【','').replace('】',''))
        for key,child in value.items():
            if key!='zh':result.extend(sentences(child))
    elif isinstance(value,list):
        for child in value:result.extend(sentences(child))
    return result
for file in sorted(args.root.glob(args.prefix+'*.json')):
    pack=json.loads(file.read_text('utf-8'))
    context=[s for key in ['dialogue','reading','extraReadings','grammar','tasks'] for s in sentences(pack.get(key))]
    needs=[]
    for word in pack['vocabulary']:
        seen={s for s in context if word['hanzi'] in s}
        if len(seen)>=2:continue
        seen.add(word['example']['zh'])
        if len(seen)<2:needs.append(word['hanzi'])
    print(pack['unit']['id'],', '.join(needs) or 'No new context needed beyond the authored introduction example')
