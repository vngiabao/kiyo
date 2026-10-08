"""Install authored character entries without reserializing accepted lessons."""
import json,sys
from common import ROOT
number=int(sys.argv[1])
assert 1<=number<=12
name=f's4-u{number:02}.json'
target=ROOT/'content/packs'/name
pack=json.loads(target.read_text('utf-8'))
draft=json.loads((ROOT/'output/advanced-course-drafts'/name).read_text('utf-8'))
unchanged={k:v for k,v in pack.items() if k!='characters'}
pack['characters']=draft['characters']
assert unchanged=={k:v for k,v in pack.items() if k!='characters'}
target.write_text(json.dumps(pack,ensure_ascii=False,indent=2)+'\n','utf-8')
print(name,len(pack['characters']),'connected character entries installed; other fields preserved.')
