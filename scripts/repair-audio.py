"""Retry unresolved speech once, or record the owner's dated device-speech exception.

Never marks a failed take reviewed or installs it. The mastering/catalog gates
still validate every non-deferred file and source hash.
"""
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
read = lambda p: json.loads(p.read_text('utf-8'))
write = lambda p, data: p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', 'utf-8')

def checked_rows(root, jobs, screen):
    """Check every immutable source; overlap independent Windows file reads only."""
    def verify(job):
        receipt = read(root / job['receipt'])
        source = root / receipt['rawFile']
        assert hashlib.sha256(source.read_bytes()).hexdigest() == receipt['rawSha256']
        result = screen['clips'][receipt['rawSha256'] + ':' + job['text']]
        return job, receipt, result
    with ThreadPoolExecutor(max_workers=8) as pool:
        yield from pool.map(verify, jobs)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['retry', 'defer'])
    args = parser.parse_args()
    cache = ROOT / '.cache/sayo-qwen-approved'
    plan_path = cache / 'plan.json'
    plan, screen = read(plan_path), read(cache / 'screening.json')
    assert screen['planSha256'] == hashlib.sha256(plan_path.read_bytes()).hexdigest(), 'Stale screening plan'
    grouped = {}
    for job, receipt, result in checked_rows(ROOT, plan['jobs'], screen):
        grouped.setdefault(job['text'], []).append((job, receipt, result))
    failed = {text: rows for text, rows in grouped.items() if all(r['status'] == 'needs-review' for _, _, r in rows)}
    retry_path = ROOT / 'content/voices/approved-b-half/retries.json'
    context_path = ROOT / 'content/voices/approved-b-half/pronunciation-contexts.json'
    retries, contexts = read(retry_path), read(context_path)
    if args.action == 'retry':
        count = 0
        for text, rows in failed.items():
            job, receipt, _ = next((row for row in rows if row[0]['mood'] == 'clear'), rows[0])
            if receipt.get('take', 0) >= 1:
                continue
            token = Path(job['receipt']).name.split('-'+job['mood']+'-')[0] + '-'+job['mood']
            retries[token] = 1
            # Reference delivery changes, but the same approved fixed speaker identity remains.
            contexts[token] = dict(synthesisText=text, extract='whole', promptMode='speaker-only',
                sampling=dict(temperature=.65, subtalker_temperature=.65),
                reason='One real pronunciation repair under the owner-approved reading-first policy.')
            count += 1
        write(retry_path, retries)
        write(context_path, contexts)
        print('Repair jobs queued:', count)
        return
    path = ROOT / 'content/voices/audio-deferred.json'
    policy = read(path)
    entries = {entry['text']: entry for entry in policy.get('entries', [])}
    for text, rows in failed.items():
        repaired = [(job, receipt, result) for job, receipt, result in rows if receipt.get('take', 0) >= 1]
        assert repaired, 'A real repair is required before deferral: ' + text
        entries[text] = dict(text=text, date=datetime.now(timezone.utc).date().isoformat(),
            reason='No accepted take after a real pronunciation repair; automatic transcripts require native listening review.',
            reviewed=False, repairRounds=max(r.get('take', 0) for _, r, _ in repaired),
            evidence=[dict(receipt=job['receipt'], rawSha256=r['rawSha256'], transcript=s.get('transcript'), status=s['status'])
                for job, r, s in repaired])
    # Remove an exception as soon as any exact-text take passes the existing screen.
    entries = {text: entry for text, entry in entries.items() if text in failed}
    policy.update(texts=list(entries), entries=list(entries.values()),
        policy='Owner approved directly: one real repair, then dated device-speech deferral. All non-audio gates remain strict.')
    write(path, policy)
    print('Documented deferred texts:', len(entries))

if __name__ == '__main__':
    main()
