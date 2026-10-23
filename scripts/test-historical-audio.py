"""Earlier repairs require current voice, waveform and phonetic evidence."""
import hashlib,importlib.util,json,tempfile,unittest
from pathlib import Path
spec=importlib.util.spec_from_file_location('history',Path(__file__).with_name('select-historical-audio.py'))
history=importlib.util.module_from_spec(spec);spec.loader.exec_module(history)

class HistoricalRepairs(unittest.TestCase):
    def fixture(self,root,text='要，网页还没有跟着改。',py='Yào, wǎngyè hái méiyǒu gēn zhe gǎi.',heard='要網頁還沒有跟著改'):
        cache=root/'.cache/sayo-qwen-approved';cache.mkdir(parents=True)
        raw=cache/'raw.wav';raw.write_bytes(b'exact earlier waveform')
        raw_sha=history.sha(raw)
        entry=dict(id='a'*16,text=text,pinyin=py)
        recipe=dict(text=text,mood='clear',model=dict(repo='pinned'),profileSha256='voice',rosterSha256='roster',pipeline=1,take=3)
        token=hashlib.sha256(json.dumps(recipe,sort_keys=True,ensure_ascii=False).encode()).hexdigest()[:12]
        path=cache/f'{entry["id"]}-clear-{token}.json'
        path.write_text(json.dumps(dict(recipe,rawFile=raw.relative_to(root).as_posix(),rawSha256=raw_sha)),'utf-8')
        screen=dict(clips={raw_sha+':'+text:dict(transcript=heard,status='needs-review')})
        return entry,path,screen

    def run_check(self,root,args):return history.candidate(root,args[0],args[1],'voice','roster',args[2])

    def test_metadata_correction_recovers_the_exact_earlier_waveform(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder);args=self.fixture(root);result=self.run_check(root,args)
            self.assertEqual(result['take'],3)
            self.assertEqual(result['status'],'homophone-transcript')
            self.assertEqual(result['receipt'],args[1].relative_to(root).as_posix())
            args[0]['pinyin']=None
            self.assertIsNone(self.run_check(root,args))

    def test_a_wrong_tone_is_not_a_reusable_take(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder);self.assertIsNone(self.run_check(root,self.fixture(root,'把','bǎ','八')))

    def test_changed_waveform_or_voice_is_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder);args=self.fixture(root)
            (root/'.cache/sayo-qwen-approved/raw.wav').write_bytes(b'changed')
            self.assertIsNone(self.run_check(root,args))
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder);entry,path,screen=self.fixture(root)
            self.assertIsNone(history.candidate(root,entry,path,'different-voice','roster',screen))

    def test_a_changed_recipe_cannot_reuse_an_old_receipt_name(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder);args=self.fixture(root);row=history.read(args[1])
            row['take']=8;args[1].write_text(json.dumps(row),'utf-8')
            self.assertIsNone(self.run_check(root,args))

    def test_next_repair_stays_fresh_after_selecting_an_older_take(self):
        self.assertEqual(history.prepare.next_take('word-clear',{'word-clear':3},{'word-clear':5}),6)
        self.assertEqual(history.prepare.next_take('new-clear',{},{}),1)

if __name__=='__main__':unittest.main()
