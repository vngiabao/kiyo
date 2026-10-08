"""Correct an overlapping word-boundary reading, without changing any Chinese text."""
import json,re
from common import ROOT

for folder in ['content/packs','output/advanced-course-drafts','output/parity-editorial-drafts']:
    for path in (ROOT/folder).glob('s*-u*.json'):
        pack=json.loads(path.read_text('utf-8'));changed=[]
        def walk(value):
            if isinstance(value,dict):
                if '没收到' in value.get('zh','') and 'py' in value:
                    new=re.sub(r'mò\s+shōu\s+dào','méi shōu dào',value['py'])
                    if new!=value['py']:changed.append(value['zh']);value['py']=new
                for child in value.values():walk(child)
            elif isinstance(value,list):
                for child in value:walk(child)
        walk(pack)
        if changed:
            path.write_text(json.dumps(pack,ensure_ascii=False,indent=2)+'\n','utf-8')
            print(folder,path.name,len(changed),'contextual readings corrected; Chinese/audio keys unchanged')
