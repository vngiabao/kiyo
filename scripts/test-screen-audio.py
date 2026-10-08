"""Contextual de comparison cannot accept ground dì or different speech."""
import importlib.util
from pathlib import Path
import unittest

spec=importlib.util.spec_from_file_location('screen',Path(__file__).with_name('screen-audio-qwen.py'))
screen=importlib.util.module_from_spec(spec)
spec.loader.exec_module(screen)

class ContextualReading(unittest.TestCase):
    def test_year_transcription_preserves_the_authored_date(self):
        self.assertEqual(screen.transcript_status('二零二六年十月六日，星期二。','2026年10月6日 星期二'),'text-match')
        self.assertEqual(screen.transcript_status('二零二六年十月六日，星期二。','2025年10月6日 星期二'),'needs-review')
        self.assertEqual(screen.transcript_status('二千零二十六个学生。','2026个学生'),'needs-review')
        self.assertEqual(screen.transcript_status('二零二六年十月六日。','2026年10月7日'),'needs-review')

    def test_adverbial_de_is_a_spoken_homophone(self):
        self.assertEqual(screen.transcript_status('我认真地读课文。','我认真的读课文','wǒ rèn zhēn de dú kè wén'),'homophone-transcript')
        self.assertEqual(screen.transcript_status('认真的学生认真地读课文。','认真的学生认真的读课文','rèn zhēn de xué sheng rèn zhēn de dú kè wén'),'homophone-transcript')

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
