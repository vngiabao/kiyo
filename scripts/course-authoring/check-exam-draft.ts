import fs from 'node:fs';
import { verifiedBankText, type HskBankPack } from '../../src/hsk-pack';
import type { HskWord } from '../../src/packs';
const words = JSON.parse(fs.readFileSync('content/hsk/levels.json', 'utf8')).words as Record<string, HskWord>;
const pack = JSON.parse(fs.readFileSync(process.argv[2], 'utf8')) as HskBankPack;
for (const q of pack.items) {
  for (const [text, py] of [[q.sentence,q.py],[q.prompt,q.promptPy!],...q.choices.map(c=>[c.zh,c.py]),...(q.segments??[]).map(c=>[c.zh,c.py])]) {
    if (!verifiedBankText(text,py,words,pack.level)) console.log(JSON.stringify({id:q.id,text,py}));
  }
}
