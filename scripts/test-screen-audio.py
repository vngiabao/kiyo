"""Contextual de comparison cannot accept ground dì or different speech."""
import importlib.util
from pathlib import Path
import unittest
import contextlib
import io
import json
import sys
import tempfile
from unittest.mock import patch

spec=importlib.util.spec_from_file_location('screen',Path(__file__).with_name('screen-audio-qwen.py'))
screen=importlib.util.module_from_spec(spec)
spec.loader.exec_module(screen)

class ContextualReading(unittest.TestCase):
    def test_numeric_two_can_spell_an_exact_aligned_authored_liang(self):
        self.assertEqual(screen.transcript_status('两点到两点十五分。','2点到2点15分'),'text-match')
        self.assertEqual(screen.transcript_status('第二组有两个人。','第2组有2个人'),'text-match')
        self.assertEqual(screen.transcript_status('两百人等两分钟。','200人等2分钟'),'needs-review')

    def test_liang_does_not_allow_a_changed_value_or_explicit_er(self):
        for heard in ['3点到2点15分','二点到两点十五分','12点到2点15分','2.0点到2点15分','-2点到2点15分']:
            self.assertEqual(screen.transcript_status('两点到两点十五分。',heard),'needs-review')

    def test_snapshot_checks_every_present_source_and_leaves_unfinished_jobs_pending(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder)
            jobs=[]
            for i in range(20):
                data=f'waveform {i}'.encode()
                raw=root/f'{i}.wav'
                raw.write_bytes(data)
                record=dict(rawFile=raw.name,rawSha256=screen.digest(raw))
                (root/f'{i}.json').write_text(json.dumps(record),'utf-8')
                jobs.append(dict(receipt=f'{i}.json'))
            (root/'7.json').unlink()
            result=screen.verified_receipts(root,jobs)
            self.assertEqual(list(result),[f'{i}.json' for i in range(20) if i!=7])
            (root/'16.wav').write_bytes(b'changed')
            with self.assertRaises(AssertionError):
                screen.verified_receipts(root,jobs)

    def test_snapshot_rejects_a_missing_recorded_waveform(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder)
            (root/'receipt.json').write_text(json.dumps(dict(rawFile='missing.wav',rawSha256='0'*64)),'utf-8')
            with self.assertRaises(FileNotFoundError):
                screen.verified_receipts(root,[dict(receipt='receipt.json')])

    def test_failed_repeat_preserves_completed_carrier_evidence_and_terminates(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder)
            cache=root/'.cache/sayo-qwen-approved'
            cache.mkdir(parents=True)
            (root/'content').mkdir()
            def put(path, value):
                path.write_text(json.dumps(value,ensure_ascii=False),'utf-8')
            raw=cache/'word.wav'
            carrier=cache/'carrier.wav'
            screen.sf.write(raw,screen.np.ones(12000)*.1,24000)
            screen.sf.write(carrier,screen.np.ones(24000)*.1,24000)
            receipt=cache/'word.json'
            record=dict(text='后',mood='clear',rawFile=raw.relative_to(root).as_posix(),
                        rawSha256=screen.digest(raw),carrierFile=carrier.relative_to(root).as_posix(),
                        carrierSha256=screen.digest(carrier))
            put(receipt,record)
            put(cache/'plan.json',dict(jobs=[dict(text='后',mood='clear',receipt=receipt.relative_to(root).as_posix())]))
            put(root/'content/audio-scripts.json',[dict(text='后',pinyin='hòu')])
            calls=[]
            class Model:
                def transcribe(self,*args,**kwargs):
                    calls.append(kwargs)
                    return dict(text='好')
            actual_read=screen.read
            receipt_reads=[]
            def counted_read(path):
                if path==receipt:receipt_reads.append(path)
                return actual_read(path)
            output=io.StringIO()
            output.reconfigure=lambda **kwargs:None
            with patch.multiple(screen,ROOT=root,CACHE=cache), \
                 patch.object(screen,'read',side_effect=counted_read), \
                 patch.object(screen.whisper,'load_model',return_value=Model()), \
                 patch.object(sys,'argv',['screen','--device','cpu','--repeat-short','--carrier']), \
                 contextlib.redirect_stdout(output):
                screen.main()
            report=actual_read(cache/'screening.json')
            result=report['clips'][record['rawSha256']+':后']
            self.assertEqual(result['status'],'needs-review')
            self.assertIn('carrierTranscript',result)
            self.assertIn('repeatedTranscript',result)
            self.assertEqual(len(calls),3) # original, carrier and repeat; each exactly once
            self.assertEqual(len(receipt_reads),3) # one verified snapshot per pass
            self.assertEqual(report['unreviewed'],1)

    def test_traditional_aspect_spelling_needs_the_authored_reading(self):
        self.assertEqual(screen.transcript_status('他拿着书。','他拿著書','Tā ná zhe shū'),'homophone-transcript')
        self.assertEqual(screen.transcript_status('她拿着书。','他拿著書','Tā ná zhe shū'),'homophone-transcript')
        self.assertEqual(screen.transcript_status('他拿着书。','他拿著書','Tā ná zhù shū'),'needs-review')
        self.assertEqual(screen.transcript_status('他拿着书。','他拿書','Tā ná zhe shū'),'needs-review')
        self.assertEqual(screen.transcript_status('他拿着书。','他拿著筆','Tā ná zhe shū'),'needs-review')
        self.assertEqual(screen.transcript_status('著作','着作','zhù zuò'),'needs-review')

    def test_integer_percent_notation_is_the_same_spoken_number(self):
        self.assertEqual(screen.transcript_status('百分之二十到百分之三十，增加十个百分点。','20%到30%增加10个百分点。'),'text-match')
        self.assertEqual(screen.transcript_status('比例提高到百分之四十五。','比例提高到45％。'),'text-match')

    def test_wrong_percent_and_percentage_points_stay_distinct(self):
        self.assertEqual(screen.transcript_status('百分之二十到百分之三十。','20%到35%'),'needs-review')
        self.assertEqual(screen.transcript_status('增加十个百分点。','增加10%'),'needs-review')
        self.assertEqual(screen.transcript_status('百分之二十。','0.2%'),'needs-review')
        self.assertEqual(screen.transcript_status('百分之二十。','-20%'),'needs-review')
        self.assertEqual(screen.transcript_status('百分之二十。','120%'),'needs-review')

    def test_year_transcription_preserves_the_authored_date(self):
        self.assertEqual(screen.transcript_status('二零二六年十月六日，星期二。','2026年10月6日 星期二'),'text-match')
        self.assertEqual(screen.transcript_status('二零二六年十月六日，星期二。','2025年10月6日 星期二'),'needs-review')
        self.assertEqual(screen.transcript_status('二千零二十六个学生。','2026个学生'),'needs-review')
        self.assertEqual(screen.transcript_status('二零二六年十月六日。','2026年10月7日'),'needs-review')

    def test_adverbial_de_is_a_spoken_homophone(self):
        self.assertEqual(screen.transcript_status('我认真地读课文。','我认真的读课文','wǒ rèn zhēn de dú kè wén'),'homophone-transcript')
        self.assertEqual(screen.transcript_status('认真的学生认真地读课文。','认真的学生认真的读课文','rèn zhēn de xué sheng rèn zhēn de dú kè wén'),'homophone-transcript')
        self.assertEqual(screen.transcript_status('有条件地继续试周四。','有条件的继续是周四','Yǒu tiáojiàn de jìxù shì Zhōusì.'),'homophone-transcript')
        self.assertEqual(screen.transcript_status('她认真地读课文。','他认真的读课文','Tā rènzhēn de dú kèwén.'),'homophone-transcript')
        self.assertEqual(screen.transcript_status('有条件地继续试周四。','有条件的继续时周四','Yǒu tiáojiàn de jìxù shì Zhōusì.'),'needs-review')

    def test_wrong_ground_and_missing_syllables_still_fail(self):
        self.assertEqual(screen.transcript_status('地上','的上','dì shang'),'needs-review')
        self.assertEqual(screen.transcript_status('我认真地读课文。','我认真读课文','wǒ rèn zhēn de dú kè wén'),'needs-review')
        self.assertEqual(screen.transcript_status('认真地读。','认真的读','rèn zhēn dì dú'),'needs-review')
        self.assertEqual(screen.transcript_status('认真地读。','认真的赌','rèn zhēn de dú'),'needs-review')
        self.assertEqual(screen.transcript_status('小孩儿','小孩','xiǎo háir'),'needs-review')

    def test_word_spaced_neutral_complement_de(self):
        self.assertEqual(screen.transcript_status('他说得很好。','他说的很好','Tā shuō de hěnhǎo'),'homophone-transcript')
        self.assertEqual(screen.transcript_status('她笑得很大声。','她笑的很大声','Tā xiào de hěn dàshēng'),'homophone-transcript')
        self.assertEqual(screen.transcript_status('我认真地读课文。','我认真的读课文','Wǒ rènzhēn de dú kèwén'),'homophone-transcript')

    def test_dei_de_and_other_changed_words_still_fail(self):
        self.assertEqual(screen.transcript_status('我得早点走。','我的早点走','wǒ děi zǎodiǎn zǒu'),'needs-review')
        self.assertEqual(screen.transcript_status('我得早点走。','我的早点走','wǒ de zǎodiǎn zǒu'),'needs-review')
        self.assertEqual(screen.transcript_status('得到三分。','的到三分','dé dào sān fēn'),'needs-review')
        self.assertEqual(screen.transcript_status('得到三分。','的到三分','de dào sān fēn'),'needs-review')
        self.assertEqual(screen.transcript_status('他说得很好。','他说很好','Tā shuō de hěnhǎo'),'needs-review')
        self.assertEqual(screen.transcript_status('他说得很好。','他说的很高','Tā shuō de hěnhǎo'),'needs-review')
        self.assertEqual(screen.transcript_status('认真地读。','认真的赌','rènzhēn de dú'),'needs-review')

if __name__=='__main__':unittest.main()
