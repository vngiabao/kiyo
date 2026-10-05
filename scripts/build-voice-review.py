"""Build the local listening page after generate-voice-compare.py completes."""
import html
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
out = root/'output/voice-compare'
roster = json.loads((root/'content/voices/roster.json').read_text('utf-8'))
if roster.get('auditionArchive'):
    roster = json.loads((root/roster['auditionArchive']).read_text('utf-8'))
sentences = json.loads((out/'sentences.json').read_text('utf-8'))
columns = [('baseline', 'Current voice')] + [(m['id'], m['id'].title()) for m in roster['moods']]
escape = html.escape

def player(mood, i, text, revision=None, label='Play'):
    src = f'baseline-{i}.mp3' if mood == 'baseline' else f'{revision or roster["revision"]}/{mood}-{i}.wav'
    # Missing clips are a generation error, never silently exposed as broken players.
    if not (out/src).is_file():
        raise FileNotFoundError(src)
    return f'<button class="play" data-src="{src}" data-label="{escape(label)}" aria-label="Play {escape(label)} {mood}: {escape(text)}"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5l11 7-11 7z"/></svg><span>{escape(label)}</span></button>'

rows = ''.join('<tr><th scope="row" lang="zh-CN">'+escape(text)+'</th>'+''.join('<td>'+player(m,i,text)+'</td>' for m,_ in columns)+'</tr>' for i,text in enumerate(sentences))
featured = [('intense',8,'Praise'),('deadpan',7,'The tone?'),('playful',9,'Teasing'),('soft',10,'Try again')]
samples = ''.join(f'<div class="sample"><span>{label}</span><strong lang="zh-CN">{escape(sentences[i])}</strong>'+ (player(m,i,sentences[i],roster['previousRevision'],'Previous') if roster.get('previousRevision') else '') + player(m,i,sentences[i],label='New take' if roster.get('previousRevision') else 'Play')+'</div>' for m,i,label in featured)
descriptions = ''.join(f'<div><strong>{escape(m["id"].title())}</strong><p>{escape(m["description"])}</p></div>' for m in roster['moods'])
page = '''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Sayo · Voice audition</title>
<style>
:root{color-scheme:dark;--bg:#101b2b;--surface:#17263a;--ink:#f0f3f5;--muted:#aabccd;--accent:#b3d2f5;--rule:#304359}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.6 system-ui,sans-serif}main{max-width:1320px;margin:auto;padding:36px 32px 80px}a{color:var(--accent)}header{display:flex;gap:28px;align-items:center;border-bottom:1px solid var(--rule);padding-bottom:24px}header img{width:170px;height:190px;object-fit:contain}h1{font:500 clamp(32px,5vw,52px)/1.15 Georgia,serif;margin:8px 0 16px}h2{font:500 28px/1.3 Georgia,serif;margin:32px 0 16px}p{max-width:70ch;color:var(--muted);margin:8px 0}.label{color:var(--accent);font-size:13px;letter-spacing:.08em;text-transform:uppercase}.samples{display:grid;grid-template-columns:repeat(4,1fr);border-block:1px solid var(--rule);margin:24px 0}.sample{padding:18px 14px;display:grid;gap:10px}.sample>span{color:var(--muted);font-size:14px}.sample strong{font-size:23px;font-weight:500}.play{min-height:44px;background:var(--surface);border:1px solid #657f98;color:var(--accent);border-radius:8px;padding:8px 12px;display:inline-flex;align-items:center;justify-content:center;gap:8px;font:inherit;cursor:pointer}.play svg{width:14px;height:14px;fill:currentColor}.play[aria-pressed=true]{background:var(--accent);color:var(--bg)}button:focus-visible,a:focus-visible{outline:2px solid var(--accent);outline-offset:4px}.table-wrap{overflow:auto;border:1px solid var(--rule);border-radius:10px}table{border-collapse:collapse;width:100%;min-width:1050px}th,td{text-align:left;border-bottom:1px solid var(--rule);padding:14px 12px}thead th{font-size:14px;color:var(--accent);background:var(--surface)}tbody th{font-size:19px;min-width:235px;font-weight:500}td .play{font-size:14px}.moods{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin-top:24px}.moods strong{font-size:16px}.moods p{font-size:14px}#status{min-height:1.6em;color:var(--accent);font-size:14px}.note{font-size:14px;margin-top:28px;border-top:1px solid var(--rule);padding-top:20px}footer{margin-top:36px;font-size:14px}::selection{background:#b3d2f5;color:#101b2b}@media(max-width:640px){main{padding:24px 18px 48px}header{gap:8px;align-items:flex-start}header img{width:85px;height:120px}header p{font-size:15px}.samples{grid-template-columns:repeat(2,1fr)}.moods{grid-template-columns:1fr 1fr;gap:20px}.sample{padding:16px 6px}.sample strong{font-size:21px}}
</style><main>
<a href="/">← Back to Kiyo</a>
<header><div><p class="label">小夜 Sayo · audition, not installed</p><h1>A voice with a little bite.</h1><p>One synthetic voice, six performances. More expression, stronger emphasis, a little mischief. Start with her reactions, then compare the same words across moods.</p></div><img src="/mascot/web/smug.webp" alt="Sayo looking quietly pleased"></header>
<h2>Hear her in the app’s moments</h2><div class="samples">SAMPLES</div>
<p id="status" role="status">Tap a sample. Starting another stops the first.</p>
<h2>Same words. Different attitude.</h2><p>The first eight rows test pronunciation and everyday phrases. The last four test praise and encouragement. On a phone, swipe the table sideways.</p>
<div class="table-wrap" tabindex="0" role="region" aria-label="Voice comparisons"><table><thead><tr><th scope="col">Mandarin</th>HEADERS</tr></thead><tbody>ROWS</tbody></table></div>
<div class="moods">DESCRIPTIONS</div>
<p class="note">Listen for accurate tones, the same person across moods, and personality without strained or sing-song pronunciation. These are unapproved synthetic auditions. The reference is generated from the existing female model voice; no real person’s recording was used. Emotion labels describe the intended delivery, not a guarantee that every take achieves it.</p>
<footer><p>Tell me which mood fits Sayo best, and which lines need another take. The new voice will stay out of the app until you choose.</p><a href="REVISION/provenance.json">Generation details</a> · <a href="https://github.com/QwenAudio/CosyVoice">CosyVoice source</a></footer>
</main><script>
let active=null,button=null;const status=document.querySelector('#status');
function reset(){if(button){button.setAttribute('aria-pressed','false');button.querySelector('span').textContent=button.dataset.label}button=null}
document.querySelectorAll('[data-src]').forEach(b=>b.addEventListener('click',async()=>{const same=b===button;active?.pause();reset();if(same){status.textContent='Stopped.';return}button=b;active=new Audio(b.dataset.src);const sound=active;b.setAttribute('aria-pressed','true');b.querySelector('span').textContent='Stop';status.textContent=b.getAttribute('aria-label').replace('Play ','Playing ');sound.onended=()=>{if(active===sound){reset();status.textContent='Choose another take to compare.'}};try{await sound.play()}catch(e){if(active===sound){reset();status.textContent='Could not play this sample. Tap again to retry.'}}}));
window.addEventListener('pagehide',()=>active?.pause());
</script></html>'''
page = page.replace('SAMPLES',samples).replace('HEADERS',''.join(f'<th scope="col">{label}</th>' for _,label in columns)).replace('ROWS',rows).replace('DESCRIPTIONS',descriptions).replace('REVISION',roster['revision'])
if roster.get('reviewTitle'):
    page = page.replace('A voice with a little bite.',escape(roster['reviewTitle']))
    page = page.replace('One synthetic voice, six performances. More expression, stronger emphasis, a little mischief. Start with her reactions, then compare the same words across moods.',escape(roster['reviewIntro']))
if roster.get('previousRevision'):
    page = page.replace('<footer>', '<footer><p><a href="'+escape(roster['previousRevision'])+'.html">Open the previous audition</a></p>')
candidate_file = out/'base/candidates.json'
if candidate_file.exists():
    candidates = json.loads(candidate_file.read_text('utf-8'))['candidates']
    if len(candidates) != 6:
        raise ValueError('Wait for all six base candidates before rebuilding the page.')
    def candidate_player(record,label):
        src = 'base/'+record['file']
        if not (out/src).is_file():
            raise FileNotFoundError(src)
        return f'<button class="play" data-src="{escape(src)}" data-label="{escape(label)}" aria-label="Play {escape(label)}"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5l11 7-11 7z"/></svg><span>{escape(label)}</span></button>'
    cards = ''.join(f'<article class="candidate"><p class="label">Voice {c["id"]}</p><h3>{escape(c["name"])}</h3><p>{escape(c["description"])}</p>'+candidate_player(c['base'],'Voice '+c['id']+' · full sample')+'</article>' for c in candidates)
    moods = candidates[0]['previews']
    headings = ''.join(f'<th scope="col">{escape(m["mood"].title())}<small lang="zh-CN">{escape(m["text"])}</small></th>' for m in moods)
    candidate_rows = ''.join(f'<tr><th scope="row">{c["id"]} · {escape(c["name"])}</th>'+''.join('<td>'+candidate_player(m,c['id']+' · '+m['mood'])+'</td>' for m in c['previews'])+'</tr>' for c in candidates)
    block = '<section aria-labelledby="base-title"><h2 id="base-title">First, choose her voice.</h2><p>Six synthetic directions, from restrained huskiness to stronger grit and power. Names describe the targets; choose by ear. None is selected or installed.</p><div class="candidates">'+cards+'</div><h2>One candidate, nine moods.</h2><p>Compare Cool with Cool-accent on the same line. Growl and Whisper are new reaction options. Clear remains standard Mandarin for lessons. These short previews help choose the base before generating its full library.</p><div class="table-wrap" tabindex="0" role="region" aria-label="Candidate mood previews"><table class="candidate-table"><thead><tr><th scope="col">Candidate</th>'+headings+'</tr></thead><tbody>'+candidate_rows+'</tbody></table></div><p class="note">Tell me the voice number (01–06) and whether to keep Cool-accent. All nine previews in a row use that candidate’s synthetic reference. No singer recordings are used.</p></section>'
    page = page.replace('</header>','</header>'+block,1)
    page = page.replace('More presence. A dry little grin.','Find her voice. Then her attitude.')
    page = page.replace(escape(roster.get('reviewIntro','')), 'A dark, full voice with conviction, a little grit, and dry humor. Start with six base candidates, then compare their moods. The earlier auditions remain below.')
    page = page.replace('</style>', '.candidates{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px;margin:24px 0 36px}.candidate{border-top:1px solid var(--rule);padding:16px 0;display:flex;flex-direction:column;gap:10px}.candidate h3{font-size:22px;font-weight:500;margin:0}.candidate p{font-size:14px;margin:0}.candidate .play{margin-top:auto}.candidate-table{min-width:1700px}.candidate-table small{display:block;font-weight:400;color:var(--muted);margin-top:8px;font-size:13px;max-width:180px}.candidate-table tbody th{min-width:180px}.candidate-table .play{white-space:nowrap}@media(max-width:900px){.candidates{grid-template-columns:repeat(2,minmax(0,1fr))}}@media(max-width:520px){.candidates{grid-template-columns:1fr;gap:12px}}\n</style>')
range_file = out/'range-v5/provenance.json'
if range_file.exists():
    range_data = json.loads(range_file.read_text('utf-8'))
    takes = []
    for clip in range_data['clips']:
        src = 'range-v5/'+clip['file']
        if not (out/src).is_file():
            raise FileNotFoundError(src)
        label = 'Range: '+clip['label']
        takes.append('<article class="candidate"><h3>'+escape(clip['label'])+'</h3><p>'+escape(clip['description'])+'</p><button class="play" data-src="'+escape(src)+'" data-label="'+escape(label)+'" aria-label="Play '+escape(label)+'"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5l11 7-11 7z"/></svg><span>'+escape(label)+'</span></button></article>')
    block = '<section id="range" aria-labelledby="range-title"><h2 id="range-title">Deeper lows. Higher comic jumps.</h2><p>A focused range test: identical words and one synthetic reference, with three delivery instructions. These are targets for you to judge by ear; none is approved.</p><p lang="zh-CN">'+escape(range_data['clips'][0]['text'])+'</p><p>Lái le? Kāishǐ ba. Shēngdiào ne? Nǐ yòu wàng le? Bú cuò ma! Zhè cì quán duì le! Hǎo, zài lái yí cì.</p><p>You’re here? Let’s start. What about the tones? Forgot again? Not bad! All correct this time! Okay, once more.</p><div class="candidates">'+''.join(takes)+'</div><p>Does the low register have enough weight—and does the high register feel funny while still sounding like her?</p></section>'
    page = page.replace('</header>','</header>'+block,1)
for revision, section_id in [('introvert-v6', 'introvert'), ('drawl-v7', 'drawl')]:
    audition_file = out/revision/'provenance.json'
    if not audition_file.exists():
        continue
    audition = json.loads(audition_file.read_text('utf-8'))
    brief = json.loads((root/f'content/voices/{revision}.json').read_text('utf-8'))
    takes = []
    for clip in audition['clips']:
        src = revision+'/'+clip['file']
        if not (out/src).is_file():
            raise FileNotFoundError(src)
        label = clip['label']
        takes.append('<article class="candidate"><h3>'+escape(label)+'</h3><p>'+escape(clip['description'])+'</p><button class="play" data-src="'+escape(src)+'" data-label="'+escape(label)+'" aria-label="Play '+escape(label)+'"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5l11 7-11 7z"/></svg><span>'+escape(label)+'</span></button></article>')
    title = brief.get('title', 'Quietly funny. A little flustered.')
    intro = brief.get('intro', 'Three takes aimed at introverted humor and Japanese-speaker inflection in Mandarin. The same synthetic voice reference and words throughout; judge the accent and personality by ear.')
    block = '<section id="'+section_id+'" aria-labelledby="'+section_id+'-title"><h2 id="'+section_id+'-title">'+escape(title)+'</h2><p>'+escape(intro)+'</p><p lang="zh-CN">'+escape(brief['text'])+'</p><p>'+escape(brief['pinyin'])+'</p><p>'+escape(brief['english'])+'</p><div class="candidates">'+''.join(takes)+'</div><p>Reaction auditions only. Lesson pronunciation stays standard Mandarin. Earlier comparisons remain below.</p></section>'
    page = page.replace('</header>','</header>'+block,1)
(out/'index.html').write_text(page,'utf-8')
print(out/'index.html')
