"""Explain failed draft strings without altering a gate or any content."""
import json,re,sys
from common import levels
seen=set()
for raw in open(sys.argv[1],encoding='utf-8-sig'):
    row=json.loads(raw); text=row['text']
    if text in seen:continue
    seen.add(text)
    han=''.join(re.findall(r'[\u4e00-\u9fff]',text))
    best={len(han):(0,[])}
    for i in range(len(han)-1,-1,-1):
        candidates=[]
        for j in range(i+1,min(len(han),i+8)+1):
            w=han[i:j];v=levels.get(w)
            if v and j in best and isinstance(v.get('hsk3'),int):
                candidates.append((max(v['hsk3'],best[j][0]),[(w,v['hsk3'],v['pinyin']),*best[j][1]]))
        if candidates:best[i]=min(candidates,key=lambda v:(v[0],len(v[1])))
    print(text,'\n GIVEN',row['py'],'\n MINIMUM',best.get(0,'unsegmentable'))
