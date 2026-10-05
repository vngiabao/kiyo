"""Small synthetic-voice audition informed by aggregate delivery observations."""
import os
os.environ['HF_HUB_OFFLINE']='1'
os.environ['TOKENIZERS_PARALLELISM']='false'
import hashlib,html,json,random,re,sys
from pathlib import Path
import librosa,numpy as np,soundfile as sf,torch,whisper
root=Path(__file__).resolve().parent.parent
sys.stdout.reconfigure(encoding='utf-8');sys.stderr.reconfigure(encoding='utf-8')
sys.path[:0]=[str(root/'.tts'),str(root/'.tts/third_party/Matcha-TTS')]
from cosyvoice.cli.cosyvoice import AutoModel
from audio_postprocess import normalize_clip,levels
out=root/'output/voice-delivery-audition'
expressive='--expressive' in sys.argv
prefix='expressive' if expressive else 'reference'
observations=json.loads((out/('expressive-reference-analysis.json' if expressive else 'reference-analysis.json')).read_text('utf-8'))
reference=root/'content/voices/sayo-source.wav'
before=hashlib.sha256((root/'src/audio-assets.json').read_bytes()).hexdigest()
torch.set_num_threads(4)
model=AutoModel(model_dir=str(root/'.models/Fun-CosyVoice3-0.5B-2512'),fp16=False)
base='You are a helpful assistant. 用同一个年轻成年女性的自然标准普通话说话，声调准确，字音完整。'
specs=[
 ('welcome','来了？开始吧。','Lái le? Kāishǐ ba.','You’re here? Let’s begin.','像见到熟悉的朋友，平常声音低而放松，含着笑，邀请时自然变得明亮一点。轻松亲切，有一点俏皮，不要刻意停顿。',9500),
 ('praise','不错嘛。','Bú cuò ma.','Not bad at all.','朋友做得比预想更好，有点惊喜地笑着夸他，语气明亮又带一点善意的打趣，最后轻松收住。',9501),
 ('teacher','认真一点。开始吧。','Rènzhēn yìdiǎn. Kāishǐ ba.','Focus a little. Let’s begin.','带着微笑提醒熟悉的朋友，语气温和从容，字音清楚，不要生气，也不要气声。',9502),
]
if expressive:
 specs=[
  ('welcome','来了？开始吧。','Lái le? Kāishǐ ba.','You’re here? Let’s begin.','像见到熟悉的朋友，带着笑懒懒地打招呼。第一句放松低一点，第二句开心明亮，尾音只延长一点，幽默亲切，不要叹气。',9600),
  ('surprise','诶？全对了？不错嘛。','Éi? Quán duì le? Bú cuò ma.','Huh? All correct? Not bad at all.','平常说话低而放松，突然发现朋友全答对了，惊喜地用明亮高音反问，随后带笑压低声音，假装淡定地夸他。有趣可爱，不要尖叫，不要唱歌。',9601),
  ('teacher','认真一点。开始吧。','Rènzhēn yìdiǎn. Kāishǐ ba.','Focus a little. Let’s begin.','笑着提醒熟悉的朋友，有一点淘气，提醒时从容，邀请时自然明亮一点。保持每个字准确，不要凶，不要拖长关键词。',9602),
  ('tones','声调呢？','Shēngdiào ne?','What about the tones?','像笑着发现朋友漏了一个小细节，轻轻逗他，反问时明亮一点，友好俏皮。每个字完整准确。',9603),
 ]
records=[]
for name,text,py,en,direction,seed in specs:
 instruction=base+direction+'<|endofprompt|>'
 random.seed(seed);np.random.seed(seed);torch.manual_seed(seed);torch.cuda.manual_seed_all(seed)
 chunks=list(model.inference_instruct2(text,instruction,str(reference),stream=False,speed=.98,text_frontend=False))
 y=torch.cat([c['tts_speech'].cpu() for c in chunks],dim=1).squeeze().numpy()
 assert np.isfinite(y).all() and np.max(np.abs(y))>.005
 active=np.flatnonzero(np.abs(y)>.005)
 y=y[max(0,active[0]-1920):min(len(y),active[-1]+1920)]
 assert .3<len(y)/24000<10
 y=librosa.resample(y,orig_sr=24000*2**(-2/12),target_sr=24000,res_type='soxr_hq')
 path=out/f'{prefix}-{name}.wav'
 sf.write(path,y,24000,subtype='PCM_16')
 stats=normalize_clip(path,out/'work')
 signal,rate=sf.read(path);sf.write(path,signal,rate,subtype='PCM_16')
 _,_,lufs,_=levels(path);assert abs(lufs+16)<=1
 records.append(dict(id=name,text=text,pinyin=py,meaning=en,file=path.name,instruction=instruction,seed=seed,speed=.98,pitchShift=-2,pitchMethod='resample',sha256=hashlib.sha256(path.read_bytes()).hexdigest(),**stats))
 print('GENERATED '+name,flush=True)
del model;torch.cuda.empty_cache()
recognizer=whisper.load_model('small',device='cuda',download_root=str(root/'.models/whisper'))
for clip in records:
 y,_=librosa.load(out/clip['file'],sr=16000)
 clip['screeningTranscript']=recognizer.transcribe(y,language='zh',temperature=0,beam_size=5,condition_on_previous_text=False)['text']
 print(clip['text'],clip['screeningTranscript'],flush=True)
receipt=dict(status='Audition only. Naturalness and tones need listening review.',reference='content/voices/sayo-source.wav',referenceSha256=hashlib.sha256(reference.read_bytes()).hexdigest(),analysisSourceSha256=observations['sourceSha256'],approach='Aggregate observations: lower relaxed passages and brighter, wider animated passages. No audio, embeddings or frame-by-frame pitch contours from the supplied recording were fed into synthesis.',clips=records)
(out/f'{prefix}-followup.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n','utf-8')
esc=html.escape
title='The funny side · new audition' if expressive else 'The calmer interview · new audition'
section='<section id="'+prefix+'-followup"><h2>'+title+'</h2><p>Lower relaxed delivery, brighter moments of surprise, then an easy finish. These new takes keep Sayo’s synthetic identity. The supplied recording informed broad delivery choices only. These are not approved pronunciation models.</p><div class="takes">'
for c in records:
 section+='<div><h3 lang="zh-CN">'+esc(c['text'])+'</h3><p>'+esc(c['pinyin'])+'</p><p>'+esc(c['meaning'])+'</p><audio controls preload="none" aria-label="'+prefix+' follow-up '+esc(c['text'])+'" src="'+esc(c['file'])+'"></audio></div>'
section+='</div></section>'
page=(out/'index.html').read_text('utf-8')
page=re.sub('<section id="'+prefix+'-followup">.*?</section>', '', page, flags=re.S)
page=page.replace('<h1>Smile first. Compare the depth.</h1>','<h1>Smile first. Compare the depth.</h1>'+section)
page=page.replace('The interview transcript was accessible, but its audio was not extracted; this is not a measured match to the video.', 'The initial six comparisons below predate the supplied audio files; the follow-ups above use aggregate observations from those recordings. No voice match is claimed.')
(out/'index.html').write_text(page,'utf-8')
assert hashlib.sha256((root/'src/audio-assets.json').read_bytes()).hexdigest()==before
print(f'DONE: {len(records)} reference-informed auditions, app voice unchanged.',flush=True)
