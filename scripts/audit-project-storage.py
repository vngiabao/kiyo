import heapq
import json
import os
from pathlib import Path

root = Path.cwd()
results = {}
for folder in [root, root.parent / 'Japanese']:
    totals = {}
    detail = {}
    largest = []
    errors = []
    stack = [(str(folder), ())]
    directories = 0
    while stack:
        current, parts = stack.pop()
        try:
            with os.scandir(current) as entries:
                for entry in entries:
                    if entry.is_symlink() or getattr(entry.stat(follow_symlinks=False), 'st_reparse_tag', 0) in (0xA0000003, 0xA000000C):
                        continue
                    relative = parts + (entry.name,)
                    if entry.is_dir(follow_symlinks=False):
                        directories += 1
                        stack.append((entry.path, relative))
                    elif entry.is_file(follow_symlinks=False):
                        size = entry.stat(follow_symlinks=False).st_size
                        key = parts[0] if parts else '(root files)'
                        row = totals.setdefault(key, {'bytes': 0, 'files': 0})
                        row['bytes'] += size
                        row['files'] += 1
                        key2 = '/'.join(parts[:2]) if parts else '(root files)'
                        row2 = detail.setdefault(key2, {'bytes': 0, 'files': 0})
                        row2['bytes'] += size
                        row2['files'] += 1
                        item = (size, '/'.join(relative))
                        if len(largest) < 15:
                            heapq.heappush(largest, item)
                        elif size > largest[0][0]:
                            heapq.heapreplace(largest, item)
        except OSError as exc:
            errors.append({'path': current, 'error': str(exc)})
    results[folder.name] = {
        'bytes': sum(v['bytes'] for v in totals.values()),
        'files': sum(v['files'] for v in totals.values()),
        'directories': directories,
        'top': dict(sorted(totals.items(), key=lambda r: r[1]['bytes'], reverse=True)),
        'detail': dict(sorted(detail.items(), key=lambda r: r[1]['bytes'], reverse=True)),
        'largest': sorted(largest, reverse=True),
        'errors': errors,
    }
    print(folder.name, 'scan complete', flush=True)
Path('output/folder-size-audit-current.json').write_text(json.dumps(results, indent=2), encoding='utf8')
for name, data in results.items():
    print(name, round(data['bytes'] / 2**30, 3), 'GiB', data['files'], 'files;', len(data['errors']), 'errors')
    for key, value in list(data['top'].items())[:15]:
        print(f"  {key}: {value['bytes']/2**30:.3f} GiB ({value['files']} files)")
