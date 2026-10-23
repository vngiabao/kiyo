"""A written synthesis cue cannot silently change a teaching target's sounds."""
import importlib.util
from pathlib import Path
import unittest

spec=importlib.util.spec_from_file_location('prepare',Path(__file__).with_name('prepare-audio-gap-repair.py'))
prepare=importlib.util.module_from_spec(spec)
spec.loader.exec_module(prepare)

class PronunciationCues(unittest.TestCase):
    def test_exact_toned_homophones_and_pauses_are_allowed(self):
        self.assertEqual(prepare.checked_cue('把','靶','bǎ'),'靶')
        self.assertEqual(prepare.checked_cue('方面','方。面','fāng miàn'),'方。面')
        self.assertEqual(prepare.checked_cue('同一','铜。衣','tóng yī'),'铜。衣')
        self.assertEqual(prepare.checked_cue('借电话。','界电话。','Jiè diànhuà.'),'界电话。')
        self.assertEqual(prepare.checked_cue('早一点借电话。','早一点界电话。','Zǎo yìdiǎn jiè diànhuà.'),'早一点界电话。')
        self.assertEqual(prepare.checked_cue('二两米饭。','二魉米饭。','èr liǎng mǐ fàn'),'二魉米饭。')
        self.assertEqual(prepare.checked_cue('那件','呐件','nà jiàn'),'呐件')

    def test_a_changed_tone_or_syllable_is_rejected(self):
        for text,cue,py in [('把','八','bǎ'),('补写','补谢','bǔ xiě'),('油','有','yóu'),('两','粮','liǎng')]:
            with self.assertRaises(AssertionError):prepare.checked_cue(text,cue,py)

    def test_erhua_and_neutral_endings_cannot_be_omitted(self):
        for text,cue,py in [('小孩儿','小孩',None),('着','这','zhe')]:
            with self.assertRaises(AssertionError):prepare.checked_cue(text,cue,py)

    def test_ambiguous_authored_reading_needs_a_separate_recipe(self):
        with self.assertRaises(AssertionError):prepare.checked_cue('应','英','yìng')

    def test_extra_english_or_digits_are_not_silently_ignored(self):
        for cue in ['靶 hello','靶123']:
            with self.assertRaises(AssertionError):prepare.checked_cue('把',cue,'bǎ')

if __name__=='__main__':unittest.main()
