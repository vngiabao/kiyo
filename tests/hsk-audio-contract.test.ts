import { expect, it } from 'vitest';
import { hskItems, hskSpeech, hskStudyWords } from '../src/hsk-model';
import { collectAudioScripts } from '../scripts/audio-manifest';
import { voiceKey } from '../src/sayo-voice';

it('retains every playable exam sentence and each study-word pronunciation', () => {
  const scripts = collectAudioScripts();
  const index = new Map(scripts.map((s) => [voiceKey(s.text), s]));
  for (const item of hskItems) {
    // HskExam listening and Results, plus Hsk study examples, use sentence.
    expect(index.get(voiceKey(item.sentence))?.moods, item.id).toContain('clear');
    for (const choice of hskStudyWords([item]))
      expect(index.get(voiceKey(hskSpeech(choice.zh)))?.moods, item.id).toContain('clear');
  }
  expect(scripts.some((s) => s.kinds.includes('hsk-question'))).toBe(false);
  expect(scripts.some((s) => s.kinds.includes('hsk-ordering-part'))).toBe(false);
  expect(scripts.filter((s) => s.kinds.some((k) => k.startsWith('hsk-')))
    .some((s) => s.text.includes('___'))).toBe(false);
});

it('study vocabulary preserves legacy words while excluding unplayed distractors', () => {
  const choice = (zh: string) => ({ zh, py: 'test', en: zh });
  expect(hskStudyWords([
    { choices: [choice('是')] },
    { format: 'cloze', choices: [choice('还是'), choice('是')] },
    { format: 'ordering', choices: [choice('八我点半到')] },
    { format: 'reading', choices: [choice('A wrong interpretation')] },
    { format: 'listening', choices: [choice('Another wrong interpretation')] },
  ]).map((c) => c.zh)).toEqual(['是', '还是']);
});
