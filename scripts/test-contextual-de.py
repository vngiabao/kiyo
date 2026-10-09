import sys,unittest
sys.path.insert(0,'scripts/course-authoring')
from contextual_de import correct, reading

class ContextualDe(unittest.TestCase):
    def test_reviewed_recording_complement(self):
        text='店里的笑声录得特别清楚。'
        self.assertEqual(correct(text,'diàn lǐ de xiào shēng lù dé tè bié qīng chǔ.'),'diàn lǐ de xiào shēng lù de tè bié qīng chǔ.')
        unknown='录得这个。'
        self.assertIsNone(reading(unknown,unknown.index('得')))
    def test_reviewed_separate_comparison_obligation(self):
        text='要评价它，得另外安排一次比较。'
        self.assertEqual(correct(text,'yào píng jià tā, de lìng wài ān pái yī cì bǐ jiào.'),'yào píng jià tā, děi lìng wài ān pái yī cì bǐ jiào.')
        unknown='得另外一个东西。'
        self.assertIsNone(reading(unknown,unknown.index('得')))
        self.assertEqual(correct('得到另外一个东西。','dé dào lìng wài yī gè dōng xi.'),'dé dào lìng wài yī gè dōng xi.')
    def test_distinct_uses(self):
        self.assertEqual(correct('我得走了，她说得很清楚，也得到了答复。','wǒ dé zǒu le, tā shuō dé hěn qīng chǔ, yě dé dào le dá fù.'),'wǒ děi zǒu le, tā shuō de hěn qīng chǔ, yě dé dào le dá fù.')
    def test_preserves_other_authored_readings(self):
        self.assertEqual(correct('一号房间我得再问，小孩儿说得清楚。','yāo hào fáng jiān wǒ dé zài wèn, xiǎo háir shuō dé qīng chǔ.'),'yāo hào fáng jiān wǒ děi zài wèn, xiǎo háir shuō de qīng chǔ.')
    def test_bound_forms_and_citations(self):
        self.assertEqual(correct('舍不得，只得走。','shě bu dé, zhǐ dé zǒu.'),'shě bu de, zhǐ dé zǒu.')
        for citation in ['de','dé','děi']:self.assertEqual(correct('得',citation),citation)
    def test_alignment_is_required(self):
        with self.assertRaises(ValueError):correct('她说得好。','tā de hǎo.')
    def test_potential_is_not_obtaining(self):
        self.assertEqual(correct('找得到书，才得到答案。','zhǎo dé dào shū, cái dé dào dá àn.'),'zhǎo de dào shū, cái dé dào dá àn.')
        self.assertEqual(correct('说得出口，看得出来，再得出结论。','shuō dé chū kǒu, kàn dé chū lái, zài dé chū jié lùn.'),'shuō de chū kǒu, kàn de chū lái, zài dé chū jié lùn.')
    def test_score_and_complement_citation(self):
        self.assertEqual(correct('她得了三分，高兴得想跳起来，箱子也拿得动。','tā dé le sān fēn, gāo xìng dé xiǎng tiào qǐ lái, xiāng zi yě ná dé dòng.'),'tā dé le sān fēn, gāo xìng de xiǎng tiào qǐ lái, xiāng zi yě ná de dòng.')
        self.assertEqual(correct('得很','dé hěn'),'de hěn')

if __name__=='__main__':unittest.main()
