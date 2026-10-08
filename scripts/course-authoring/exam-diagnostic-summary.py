"""Compact dictionary-level diagnostics only; never used to accept content."""
import json,re,sys
from common import levels
limit=int(sys.argv[2]);seen=set();above=set()
for raw in open(sys.argv[1],encoding='utf-8-sig'):
    row=json.loads(raw);text=row['text']
    if text in seen:continue
    seen.add(text);han=''.join(re.findall(r'[\u4e00-\u9fff]',text))
    best={len(han):(0,[])}
    for i in range(len(han)-1,-1,-1):
        candidates=[]
        for j in range(i+1,min(len(han),i+8)+1):
            ref=levels.get(han[i:j])
            if ref and j in best and isinstance(ref.get('hsk3'),int):
                candidates.append((max(ref['hsk3'],best[j][0]),[(han[i:j],ref['hsk3']),*best[j][1]]))
        if candidates:best[i]=min(candidates,key=lambda v:(v[0],len(v[1])))
    if 0 in best:
        high=[t for t in best[0][1] if t[1]>limit];above.update(high)
        offset=0
        for word,rank in best[0][1]:
            if rank>limit:print('HIGH',rank,han[max(0,offset-7):offset]+' | '+word+' | '+han[offset+len(word):offset+len(word)+9])
            offset+=len(word)
        if not high:print('READING CHECK',text[:110],row['py'][:180])
    else:
        reachable={0}
        for i in range(len(han)):
            if i in reachable:
                for j in range(i+1,min(len(han),i+8)+1):
                    ref=levels.get(han[i:j])
                    if ref and isinstance(ref.get('hsk3'),int) and ref['hsk3']<=limit:reachable.add(j)
        end=max(reachable);print('BOUNDARY',han[max(0,end-8):end]+' | '+han[end:end+16])
print('ABOVE LEVEL',sorted(above))
