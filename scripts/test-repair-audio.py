"""Parallel file reads preserve exact-source and complete-screen requirements."""
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('repair', Path(__file__).with_name('repair-audio.py'))
repair = importlib.util.module_from_spec(spec)
spec.loader.exec_module(repair)

class CheckedSources(unittest.TestCase):
    def fixture(self, root):
        jobs, screen = [], {'clips': {}}
        for i in range(20):
            text = str(i)
            data = f'source {i}'.encode()
            digest = hashlib.sha256(data).hexdigest()
            (root / f'{i}.wav').write_bytes(data)
            record = dict(rawFile=f'{i}.wav', rawSha256=digest)
            (root / f'{i}.json').write_text(json.dumps(record), 'utf-8')
            jobs.append(dict(receipt=f'{i}.json', text=text))
            screen['clips'][digest + ':' + text] = dict(status='needs-review' if i % 2 else 'text-match')
        return jobs, screen

    def test_every_source_keeps_its_order_and_exact_screen_status(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            jobs, screen = self.fixture(root)
            rows = list(repair.checked_rows(root, jobs, screen))
            self.assertEqual([job for job, _, _ in rows], jobs)
            self.assertEqual([s['status'] for _, _, s in rows],
                             ['needs-review' if i % 2 else 'text-match' for i in range(20)])

    def test_any_changed_waveform_fails_the_check(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            jobs, screen = self.fixture(root)
            (root / '13.wav').write_bytes(b'changed')
            with self.assertRaises(AssertionError):
                list(repair.checked_rows(root, jobs, screen))

    def test_any_missing_screen_result_fails_the_check(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            jobs, screen = self.fixture(root)
            screen['clips'].pop(next(iter(screen['clips'])))
            with self.assertRaises(KeyError):
                list(repair.checked_rows(root, jobs, screen))

    def test_any_missing_receipt_fails_the_check(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            jobs, screen = self.fixture(root)
            (root / '18.json').unlink()
            with self.assertRaises(FileNotFoundError):
                list(repair.checked_rows(root, jobs, screen))

if __name__ == '__main__':
    unittest.main()
