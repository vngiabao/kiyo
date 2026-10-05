"""Build a local listening checklist from the installed or staged Sayo library."""
import html
import json
from pathlib import Path
import random
import re

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'output/approved-voice-rollout'
CACHE=ROOT/'.cache/sayo-qwen-approved'
read=lambda p:json.loads(p.read_text('utf-8'))
key=lambda s:re.sub(r'[\s，。！？,.!?、]','',s)
esc=html.escape

def main():
    OUT.mkdir(exist_ok=True,parents=True)
    assets=read(CACHE/'assets.json')
    index={key(text):voices for text,voices in assets.items()}
    scripts={key(s['text']):s for s in read(ROOT/'content/audio-scripts.json')}
    report=read(CACHE/'provenance.json')
    screening=read(CACHE/'screening.json')
    tasks=read(OUT/'tasks.json')
    rates=read(ROOT/'content/voices/playback-rates.json')
    def player(text,mood):
        url=index.get(key(text),{}).get(mood)
        if not url:return '<p>Clip pending.</p>'
        rate=rates.get(text,1)
        return f'<audio controls preload="none" onplay="this.playbackRate={rate};this.preservesPitch=true" aria-label="{esc(text+" · "+mood)}" src="{esc(url)}"></audio>'
    def line(text,mood,py='',en=''):
        return f'<article><h3 lang="zh-CN">{esc(text)}</h3><p>{esc(py)}</p><p>{esc(en)} · {esc(mood)}</p>{player(text,mood)}</article>'
    selected=[]
    for task in tasks['spotChecks']:
        selected.append(f'<section><h2>{esc(task["id"])}</h2>'+''.join(line(l['zh'],l['mood'],l['py'],l['en']) for l in task['lines'])+'</section>')
    eligible=[c for c in report['clips'] if not c.get('parts')]
    reactions=[c for c in eligible if c.get('delivery')]
    sample_pool=eligible
    sample=random.Random(20261005).sample(sample_pool,min(20,len(sample_pool)))
    singles=[c for c in eligible if len(re.findall(r'[\u4e00-\u9fff]',c['text']))==1]
    def record_line(c):
        entry=scripts.get(key(c['text']),{})
        return line(c['text'],c['mood'],entry.get('pinyin',''),entry.get('meaning',''))
    flags=[]
    for c in eligible:
        item=screening['clips'].get(c['rawSha256']+':'+c['text'])
        if item and item['status'] not in ['text-match','owner-approved-take','repeated-text-match','carrier-text-match']:
            flags.append(dict(text=c['text'],mood=c['mood'],**{k:v for k,v in item.items() if k!='text'}))
    flags_html=''.join(line(f['text'],f['mood'],scripts.get(key(f['text']),{}).get('pinyin',''))+
        f'<p>Automatic transcript: {esc(f.get("transcript") or "—")} · {esc(f["status"])}</p>' for f in flags)
    counts={m:sum(c['mood']==m for c in eligible) for m in ['clear','cool','playful','soft','deadpan','intense']}
    receipt=dict(clipCounts=counts,totalBytes=report['totalBytes'],tasks=tasks['taskCount'],
        taskMoodClips=tasks['moodClips'],taskPerMood=tasks['perMood'],
        randomSample=[dict(text=c['text'],mood=c['mood'],file=c['file']) for c in sample],
        singleSyllables=[dict(text=c['text'],mood=c['mood'],file=c['file']) for c in singles],flags=flags,
        pronunciationFirstSubstitutions=report.get('pronunciationFirstSubstitutions',[]))
    (OUT/'listening-checklist.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n','utf-8')
    page='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Sayo · Approved voice rollout</title><style>body{margin:0;background:#101c2b;color:#eef2f7;font:17px/1.5 system-ui}main{max-width:1000px;margin:auto;padding:36px 22px}a{color:#b7d8fa}section{border-top:1px solid #536780;margin-top:32px;padding-top:18px}article{padding:12px 0}p{margin:5px 0}h3{margin:8px 0}audio{width:min(100%,440px);margin:10px 0}.grid{display:grid;grid-template-columns:1fr 1fr;gap:24px}summary{cursor:pointer;padding:14px 0}a:focus-visible,summary:focus-visible{outline:3px solid #b7d8fa;outline-offset:4px}@media(max-width:700px){.grid{grid-template-columns:1fr}}</style><main><a href="/">Back to Kiyo</a><h1>Sayo’s approved voice.</h1><p>The locked half-semitone choice, mapped to lessons and the new practice tasks. One synthetic voice, with delivery references for each mood.</p><p>Start with the three conversations and five fill-in lines below. Check that each word is clear and speaker turns are distinguishable. Automatic transcription is a screening aid; it cannot certify Mandarin tones or naturalness.</p><nav><a href="#random">20 sample clips</a> · <a href="#syllables">Every single-syllable clip</a> · <a href="#flags">Listening flags</a></nav>'''+''.join(selected)+f'''<section id="random"><h2>20 sample clips</h2><div class="grid">{''.join(record_line(c) for c in sample)}</div></section><section id="syllables"><h2>Every single-syllable clip</h2><p>Short syllables are the least reliable for automatic transcription. Please check their tones by ear.</p><details><summary>Listen to {len(singles)} clips</summary><div class="grid">{''.join(record_line(c) for c in singles)}</div></details></section><section id="flags"><h2>Listening flags</h2><p>These transcripts need interpretation; matching pronunciation does not always give the same written character. No native-speaker approval is claimed.</p><details><summary>Show {len(flags)} flags</summary>{flags_html}</details></section><a href="listening-checklist.json">Download the checklist</a></main><script>document.querySelectorAll('audio').forEach(a=>a.addEventListener('play',()=>document.querySelectorAll('audio').forEach(b=>{{if(a!==b)b.pause()}})))</script></html>'''
    reaction_html='<section id="reactions"><h2>100 lesson reactions</h2><p>One voice, six moods. Pitch stays between −0.5 and −1 semitone relative to the previous audition. Single-pass resampling gently slows lower takes; no additional time stretch.</p>'+''.join(record_line(c)+f'<p>Relative pitch: {-0.5+c["delivery"]["pitchOffset"]:g} semitones.</p>' for c in reactions)+'</section>'
    page=page.replace('<section id="random">',reaction_html+'<section id="random">')
    (OUT/'index.html').write_text(page,'utf-8')
    print(json.dumps(dict(counts=counts,singleSyllables=len(singles),flags=len(flags),totalBytes=report['totalBytes'])))

if __name__=='__main__':main()
