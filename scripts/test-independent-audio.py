"""Independent recognition cannot rescue stale sources or changed pronunciations."""
import copy,hashlib,importlib.util,json,tempfile,unittest
from pathlib import Path
spec=importlib.util.spec_from_file_location('verify',Path(__file__).with_name('verify-independent-audio.py'))
verify=importlib.util.module_from_spec(spec);spec.loader.exec_module(verify)

class IndependentChecks(unittest.TestCase):
    def fixture(self,root,text='把',heard='把',status='text-match'):
        data=b'exact generated waveform';sha=hashlib.sha256(data).hexdigest()
        (root/'raw.wav').write_bytes(data)
        (root/'raw.json').write_text(json.dumps(dict(rawFile='raw.wav',rawSha256=sha,take=2)),'utf-8')
        plan=dict(jobs=[dict(text=text,mood='clear',receipt='raw.json')])
        primary=dict(clips={sha+':'+text:dict(text=text,transcript='other',status='needs-review',rawSha256=sha)})
        report=dict(model='Whisper large-v3',modelSha256='pinned',clips=[dict(text=text,receipt='raw.json',rawSha256=sha,transcript=heard,status=status)])
        return plan,primary,report,{text:dict(pinyin=None)}

    def run_check(self,root,args):return verify.verified_report(root,*args,'pinned')

    def test_exact_match_keeps_the_primary_failure_and_full_model_proof(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder);args=self.fixture(root)
            original=copy.deepcopy(args[1]);updated,accepted=self.run_check(root,args)
            self.assertEqual(args[1],original)
            self.assertEqual(len(accepted),1)
            result=next(iter(updated['clips'].values()))
            self.assertEqual(result['primaryScreen']['status'],'needs-review')
            self.assertEqual(result['independentVerification']['modelSha256'],'pinned')
            updated2,accepted2=self.run_check(root,(args[0],updated,args[2],args[3]))
            self.assertEqual(updated2,updated);self.assertEqual(accepted2,[])

    def test_wrong_tone_stays_unverified(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder);args=self.fixture(root,heard='八',status='needs-review')
            updated,accepted=self.run_check(root,args)
            self.assertEqual(accepted,[]);self.assertEqual(updated,args[1])

    def test_false_pass_label_cannot_override_the_screen(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder);args=self.fixture(root,heard='八')
            with self.assertRaises(AssertionError):self.run_check(root,args)

    def test_omitted_erhua_stays_unverified(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder);args=self.fixture(root,text='小孩儿',heard='小孩',status='needs-review')
            self.assertEqual(self.run_check(root,args)[1],[])

    def test_changed_waveform_rejects_the_whole_report(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder);args=self.fixture(root);(root/'raw.wav').write_bytes(b'changed')
            with self.assertRaises(AssertionError):self.run_check(root,args)

    def test_different_model_or_target_cannot_be_adopted(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder);args=self.fixture(root)
            args[2]['modelSha256']='other'
            with self.assertRaises(AssertionError):self.run_check(root,args)
            args[2]['modelSha256']='pinned';args[2]['clips'][0]['text']='八'
            with self.assertRaises(AssertionError):self.run_check(root,args)

if __name__=='__main__':unittest.main()
