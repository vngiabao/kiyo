import urllib.request,urllib.parse,pathlib,re,html,json,time,concurrent.futures,hashlib
root=pathlib.Path('.cache/advanced-course-research'); out=pathlib.Path('prompts/research')
root.mkdir(parents=True,exist_ok=True)
base='https://admin.chinesetest.cn/newhsk/standardsAction.do'
kinds={'words':'getStandardWordsList','characters':'getStandardChineseList','grammar':'getSummaryList'}
levels=['四级','五级','六级']
def load(kind,level,offset):
 p=root/f'{kind}-{level}-{offset}.html'
 u=base+'?'+urllib.parse.urlencode({'means':kinds[kind],'leves':level,'pager.offset':offset})
 if not p.exists():
  for attempt in range(3):
   try:
    t=urllib.request.urlopen(u,timeout=20).read().decode('utf8');p.write_text(t,encoding='utf8');break
   except Exception:
    if attempt==2:raise
    time.sleep(attempt+1)
 else:t=p.read_text(encoding='utf8')
 rows=[]
 for tr in re.findall(r'<tr\b[^>]*>(.*?)</tr>',t,re.S):
  cells=[html.unescape(re.sub(r'<[^>]+>',' ',c)) for c in re.findall(r'<td\b[^>]*>(.*?)</td>',tr,re.S)]
  cells=[' '.join(c.split()) for c in cells]
  if cells and cells[0].isdigit(): rows.append(cells)
 n=re.search(r'共有\s*(\d+)\s*条记录',t)
 if not n:raise ValueError(f'Missing total: {kind} {level} {offset}')
 return rows,int(n[1])
result={'standard':'GF0025-2021','retrievedAt':'2026-10-07','source':base+'?means=standardInfo','note':'Official query tables. Row numbers are source No. values, not invented grammar codes. Word alternatives remain grouped exactly as published. Research only, never runtime imported.','levels':{}}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
 for lno,level in enumerate(levels,4):
  result['levels'][str(lno)]={}
  for kind in kinds:
   first,total=load(kind,level,0)
   more=list(pool.map(lambda offset:load(kind,level,offset),range(10,total,10)))
   rows=first+[r for rr,n in more for r in rr]
   if len(rows)!=total:raise ValueError(f'{kind} {level}: {len(rows)} != {total}')
   if len({r[0] for r in rows})!=total:raise ValueError('Duplicate source No.')
   result['levels'][str(lno)][kind]=rows
   print(kind,level,len(rows),flush=True)
out.joinpath('gf2021-advanced-inventory.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('Saved verified query inventory',flush=True)

