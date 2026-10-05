"""Six original synthetic voice directions. Audition only; never locks a voice."""
import os
os.environ['HF_HUB_OFFLINE'] = '1'
os.environ['TOKENIZERS_PARALLELISM'] = 'false'
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
root = Path(__file__).resolve().parent.parent
sys.path[:0] = [str(root/'.tts'), str(root/'.tts/third_party/Matcha-TTS')]
import numpy as np
import soundfile as sf
import torch
import pyloudnorm as pyln
from cosyvoice.cli.cosyvoice import AutoModel

out = root/'output/voice-compare/base'
out.mkdir(exist_ok=True)
reference = root/'output/voice-compare/synthetic-reference-solid-v4.wav'
script = '来了？开始吧。今天先学十个字，一个一个来。声调要准——妈、麻、马、骂。……不错嘛。再来一次——你，可以的！'
directions = [
    ('01','Cool & husky','Low, relaxed, slightly rough; the most restrained option.','请用低沉、略带沙哑、有点慵懒的年轻女声说，声音厚实，句尾轻轻下沉。',.96),
    ('02','Solid & dry','Fuller presence, clipped endings, straight-faced humor.','请用浑厚结实的低音女声说，冷静自信，咬字干脆，面无表情地开玩笑，声音不甜。',.98),
    ('03','Sharp & cheeky','Assertive attacks, teasing confidence, punchy rhythm.','请用有力量、略带沙哑的年轻女声说，态度自信又调皮，重音锐利，干脆俏皮，带着坏笑。',1.0),
    ('04','Dark & gritty','More chest weight and rasp on emphatic words.','请用低沉浑厚、沙哑有力量的女声说，胸腔共鸣强，重音带着粗粝感，个性强烈，发音清楚。',.97),
    ('05','Quiet → power','Intimate opening, sudden strong finish, then composure.','请用低沉沙哑的女声说，前半句低声冷静，最后的你可以的突然充满力量地爆发，反差强烈，发音清楚。',1.0),
    ('06','Maximum edge','The strongest grit and theatrical energy to compare.','请用极具爆发力、沙哑粗粝、低沉浑厚的年轻女声说，像摇滚舞台上的台词，态度凶悍又带一点幽默，咬字锐利清楚。',1.02),
]
previews = [
    ('clear','妈，麻，马，骂。你好。','用清晰、标准、平稳的普通话，语速稍慢，每个声调都很准确，声音低沉干净。',.96),
    ('cool','来了？开始吧。声调呢？','用冷静、低沉、略带沙哑、有点慵懒的语气说，句尾轻轻下沉。',.97),
    ('intense','太棒了！升级了！','用突然爆发、充满力量、带点沙哑和狠劲、干脆有力的语气说，重音加强，发音清楚。',1.03),
    ('growl','不错嘛。再来一次——你，可以的！','前半句低声冷静，关键词突然用沙哑有力的嗓音爆发出来，然后马上恢复冷淡。',1.0),
    ('whisper','还记得吗？今天够了。','贴近耳边、气声很重、几乎是悄悄话的语气说。',.96),
    ('soft','没关系，再试试。','用轻柔、温和、有点害羞但真诚的语气小声说。',.97),
    ('deadpan','又断了。不错嘛。','用面无表情、平淡、带一点冷幽默的语气说。',1.0),
    ('playful','你想吃米饭还是面？','用轻松、带点笑意、自然随意的语气说。',1.02),
    ('cool-accent','来了？开始吧。声调呢？','用冷静低沉的语气说，带一点日本人说中文的口音，但声调要能听清楚。',.97),
]
if not torch.cuda.is_available():
    raise RuntimeError('CUDA is required.')
torch.set_num_threads(4)
model_dir = root/'.models/Fun-CosyVoice3-0.5B-2512'
model = AutoModel(model_dir=str(model_dir), fp16=False)

def synth(target,text,prompt,ref,speed,seed):
    instruction='You are a helpful assistant. '+prompt+'<|endofprompt|>'
    if not target.exists():
        torch.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
        parts=list(model.inference_instruct2(text,instruction,str(ref),stream=False,speed=speed,text_frontend=False))
        audio=torch.cat([part['tts_speech'].cpu() for part in parts],dim=1).squeeze().numpy()
        if not np.isfinite(audio).all() or np.max(np.abs(audio))<.005:
            raise ValueError(f'Invalid signal: {target}')
        nz=np.flatnonzero(np.abs(audio)>.005);pad=int(.08*model.sample_rate)
        audio=audio[max(0,nz[0]-pad):min(len(audio),nz[-1]+pad)]
        seconds=len(audio)/model.sample_rate
        if not .3<seconds<min(28,max(9,len(text)*.85)):
            raise ValueError(f'Suspicious duration {seconds}: {target}')
        meter=pyln.Meter(model.sample_rate,block_size=min(.4,seconds/2))
        audio=pyln.normalize.loudness(audio,meter.integrated_loudness(audio),-16)
        audio*=min(1,.98/np.max(np.abs(audio)))
        sf.write(str(target),audio,model.sample_rate,subtype='PCM_16')
    info=sf.info(str(target))
    print(f'READY {target.name} {info.duration:.2f}s',flush=True)
    return {'file':target.name,'text':text,'instruction':instruction,'speed':speed,'seed':seed,'pitchShift':0,'seconds':info.duration,'reference':str(ref.relative_to(root)),'referenceSha256':hashlib.sha256(ref.read_bytes()).hexdigest(),'sha256':hashlib.sha256(target.read_bytes()).hexdigest()}

items=[]
for i,(id,name,description,prompt,speed) in enumerate(directions):
    base=out/f'{id}-base.wav'
    base_record=synth(base,script,prompt,reference,speed,3000+i)
    takes=[]
    for j,(mood,text,instruction,rate) in enumerate(previews):
        takes.append({'mood':mood,**synth(out/f'{id}-{mood}.wav',text,instruction,base,rate,4100+j)})
    items.append({'id':id,'name':name,'description':description,'base':base_record,'previews':takes})
    (out/'candidates.json').write_text(json.dumps({'generatedAt':datetime.now(timezone.utc).isoformat(),'model':json.loads((model_dir/'revision.json').read_text()),'format':'mono PCM16 WAV, 24000 Hz','loudness':'target -16 LUFS with peak cap at 0.98','codeRevision':'074ca6dc9e80a2f424f1f74b48bdd7d3fea531cc','status':'Unapproved synthetic directions. No candidate selected; accent, timbre and tones need listening review.','candidates':items},ensure_ascii=False,indent=2),'utf-8')
print('Six candidates, each with nine mood previews. No voice selected or installed.',flush=True)
