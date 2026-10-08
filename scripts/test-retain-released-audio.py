"""Test release restoration without touching the app, Git history or models."""
import importlib.util,json,tempfile,unittest
from datetime import date
from pathlib import Path

spec=importlib.util.spec_from_file_location('retention',Path(__file__).with_name('retain-released-audio.py'))
retention=importlib.util.module_from_spec(spec);spec.loader.exec_module(retention)

class ReleasedAudio(unittest.TestCase):
    def fixture(self,root,archived=None):
        file='public/audio-v2/old.mp3';data=b'ID3 exact released audio'
        for folder in ('src','content/voices','public/audio-v2'):(root/folder).mkdir(parents=True)
        (root/'src/audio-assets.json').write_text('{}','utf-8')
        if archived is not None:
            folder=root/'output/audio-backup-before-approved-b/mp3';folder.mkdir(parents=True)
            (folder/'old.mp3').write_bytes(archived)
        def git(*args):
            if args==('rev-parse','HEAD'):return b'a'*40
            if args==('show','a'*40+':src/audio-assets.json'):return json.dumps({'old':{'clear':'/audio-v2/old.mp3'}}).encode()
            if args==('show','a'*40+':content/voices/sayo-library-provenance.json'):return json.dumps({'clips':[dict(file=file,sha256=retention.sha(data))]}).encode()
            if args==('show','a'*40+':'+file):return data
            raise AssertionError(args)
        return file,data,git

    def test_restores_exact_committed_bytes(self):
        with tempfile.TemporaryDirectory(prefix='kiyo-retention-test-') as folder:
            root=Path(folder);file,data,git=self.fixture(root)
            ledger=retention.retain(root,date(2026,10,8),git)
            self.assertEqual((root/file).read_bytes(),data)
            self.assertEqual(ledger['entries'][0]['retainThrough'],'2027-01-06')
            self.assertEqual(json.loads((root/'src/audio-assets.json').read_text()),{})

    def test_archive_must_match_committed_proof(self):
        with tempfile.TemporaryDirectory(prefix='kiyo-retention-test-') as folder:
            root=Path(folder);file,data,git=self.fixture(root,b'tampered')
            with self.assertRaises(AssertionError):retention.retain(root,date(2026,10,8),git)
            self.assertFalse((root/file).exists())

    def test_does_not_renew_expiry(self):
        with tempfile.TemporaryDirectory(prefix='kiyo-retention-test-') as folder:
            root=Path(folder);file,data,git=self.fixture(root)
            retention.retain(root,date(2026,10,8),git)
            for today in (date(2027,1,7),date(2027,1,8)):
                ledger=retention.retain(root,today,git)
                self.assertEqual(ledger['entries'],[])
                self.assertEqual(len(ledger['expired']),1)

    def test_drops_retention_when_clip_is_active_again(self):
        with tempfile.TemporaryDirectory(prefix='kiyo-retention-test-') as folder:
            root=Path(folder);file,data,git=self.fixture(root)
            retention.retain(root,date(2026,10,8),git)
            (root/'src/audio-assets.json').write_text(json.dumps({'old':{'clear':'/audio-v2/old.mp3'}}),'utf-8')
            self.assertEqual(retention.retain(root,date(2026,10,9),git)['entries'],[])

if __name__=='__main__':unittest.main()
