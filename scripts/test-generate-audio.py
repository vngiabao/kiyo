"""Cached synthesis must never reuse changed or missing waveforms."""
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('generate', Path(__file__).with_name('generate-audio-qwen.py'))
generate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(generate)

class CachedSources(unittest.TestCase):
    def fixture(self, root):
        jobs = []
        for i in range(20):
            data = f'waveform {i}'.encode()
            (root / f'{i}.wav').write_bytes(data)
            receipt = root / f'{i}.json'
            receipt.write_text(json.dumps(dict(rawFile=f'{i}.wav', rawSha256=hashlib.sha256(data).hexdigest())), 'utf-8')
            jobs.append(dict(receipt=receipt))
        return jobs

    def test_missing_receipts_are_pending_in_the_original_order(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            jobs = self.fixture(root)
            jobs[3]['receipt'].unlink()
            jobs[17]['receipt'].unlink()
            self.assertEqual(generate.cached_jobs(jobs, root), [i not in (3, 17) for i in range(20)])

    def test_changed_waveform_blocks_reuse(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            jobs = self.fixture(root)
            (root / '13.wav').write_bytes(b'changed')
            with self.assertRaises(AssertionError):
                generate.cached_jobs(jobs, root)

    def test_missing_waveform_blocks_reuse(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            jobs = self.fixture(root)
            (root / '8.wav').unlink()
            with self.assertRaises(FileNotFoundError):
                generate.cached_jobs(jobs, root)

if __name__ == '__main__':
    unittest.main()
