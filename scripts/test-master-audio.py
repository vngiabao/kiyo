"""Exercise accepted-only installation without models or the real library."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent))
spec = importlib.util.spec_from_file_location('master', Path(__file__).with_name('master-audio-qwen.py'))
master = importlib.util.module_from_spec(spec)
spec.loader.exec_module(master)


class Installation(unittest.TestCase):
    def run_fixture(self, failed, deferred=None):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            cache = root / '.cache/sayo-qwen-approved'
            out = root / 'public/audio-v2'
            cache.mkdir(parents=True)
            out.mkdir(parents=True)
            (root / 'src').mkdir()
            voices = root / 'content/voices'
            (voices / 'approved-b-half').mkdir(parents=True)
            def put(path, value):
                path.write_text(json.dumps(value), 'utf-8')
            profile = voices / 'approved-b-half/profile.json'
            roster = voices / 'sayo-roster-staged.json'
            scripts = root / 'content/audio-scripts.json'
            put(profile, {'model': 'fixture', 'processing': {'resampleRatio': '1'}})
            put(roster, {'moods': []})
            put(root / 'src/audio-assets.json', {})
            entries = [{'id': 'a', 'text': '甲', 'moods': ['clear']},
                       {'id': 'b', 'text': '乙', 'moods': ['clear']}]
            entries.append({'id': 'joined', 'text': '甲乙', 'moods': ['clear'],
                            'parts': [{'text': '甲'}, {'text': '乙'}]})
            put(scripts, entries)
            if deferred:
                put(voices/'audio-deferred.json',dict(texts=deferred,entries=[dict(text=t,date='2026-10-06',reason='Fixture real repair failed',reviewed=False,repairRounds=1) for t in deferred]))
            jobs, clips = [], {}
            for i, text in enumerate(['甲', '乙']):
                wav = cache / f'{i}.wav'
                master.sf.write(wav, master.np.ones(2400 + i * 300) * .1, 24000)
                receipt = cache / f'{i}.json'
                record = dict(text=text, mood='clear', rawFile=wav.relative_to(root).as_posix(),
                              rawSha256=master.digest(wav), alreadyProcessed=True)
                put(receipt, record)
                jobs.append(dict(text=text, mood='clear', receipt=receipt.relative_to(root).as_posix()))
                clips[record['rawSha256'] + ':' + text] = {
                    'status': 'needs-review' if failed and text == '乙' else 'text-match'}
            plan = cache / 'plan.json'
            put(plan, dict(profileSha256=master.digest(profile), rosterSha256=master.digest(roster),
                           scriptsSha256=master.digest(scripts), jobs=jobs))
            put(cache / 'screening.json', dict(planSha256=master.digest(plan), clips=clips))
            def encode(audio, dest):
                # A tiny WAV container lets assembly read the fixture. Real encoding
                # and loudness are independently checked by the production gates.
                master.sf.write(dest, audio, 24000, format='WAV')
                return dict(file=dest.relative_to(root).as_posix(), sha256=master.digest(dest),
                            bytes=dest.stat().st_size, seconds=.1, sampleRate=24000, channels=1)
            code = 0
            with patch.multiple(master, ROOT=root, CACHE=cache, OUT=out), \
                 patch.object(master, 'encode', encode), \
                 patch.object(sys, 'argv', ['master', '--install']), \
                 contextlib.redirect_stdout(io.StringIO()), \
                 contextlib.redirect_stderr(io.StringIO()):
                # StringIO has no reconfigure; main owns real command-line streams.
                sys.stdout.reconfigure = lambda **kwargs: None
                sys.stderr.reconfigure = lambda **kwargs: None
                try:
                    master.main()
                except SystemExit as e:
                    code = e.code
            return code, master.read(root / 'src/audio-assets.json'), master.read(cache / 'provenance.json')

    def test_failure_installs_only_verified_audio_and_remains_failure(self):
        code, assets, provenance = self.run_fixture(True)
        self.assertEqual(code, 1)
        self.assertEqual(set(assets), {'甲'})
        self.assertEqual({r['text'] for r in provenance['unresolved']}, {'乙', '甲乙'})
        self.assertEqual({r['text'] for r in provenance['clips']}, {'甲'})

    def test_complete_screened_library_succeeds(self):
        code, assets, provenance = self.run_fixture(False)
        self.assertEqual(code, 0)
        self.assertEqual(set(assets), {'甲', '乙', '甲乙'})
        self.assertEqual(provenance['unresolved'], [])

    def test_documented_exception_does_not_install_unverified_speech(self):
        code, assets, provenance = self.run_fixture(True, ['乙'])
        self.assertEqual(code, 0)
        self.assertEqual(set(assets), {'甲'})
        self.assertEqual({r['text'] for r in provenance['deferred']}, {'乙', '甲乙'})
        self.assertEqual({r['text'] for r in provenance['clips']}, {'甲'})

    def test_unrelated_exception_cannot_hide_a_missing_take(self):
        code, _, _ = self.run_fixture(True, ['甲'])
        self.assertEqual(code, 1)


if __name__ == '__main__':
    unittest.main()
