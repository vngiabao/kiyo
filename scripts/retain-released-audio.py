"""Restore exact released clip URLs for cached clients, outside current coverage."""
import hashlib,json,re,subprocess
from datetime import date,timedelta
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
read=lambda p:json.loads(p.read_text('utf-8'))
sha=lambda data:hashlib.sha256(data).hexdigest()

def retain(root=ROOT,today=None,git=None,history=False):
    """history=True also keeps clips from every catalogue revision of the last 90 days,
    so a batch committed in several steps cannot strand an installed client."""
    root=Path(root).resolve()
    today=today or date.today()
    git=git or (lambda *args:subprocess.check_output(['git',*args],cwd=root))
    revision=git('rev-parse','HEAD').decode().strip()
    assert re.fullmatch('[a-f0-9]{40}',revision)
    revisions=[revision]
    if history:
        revisions+=[r for r in git('log','--since=90 days ago','--format=%H','--','src/audio-assets.json').decode().split() if r!=revision]
    current={url for voices in read(root/'src/audio-assets.json').values() for url in voices.values()}
    path=root/'content/voices/released-audio-compatibility.json'
    old=read(path) if path.exists() else dict(entries=[],expired=[])
    assert old.get('version',1)==1
    previous_rows=old.get('expired',[])+old['entries']
    assert len({r['file'] for r in previous_rows})==len(previous_rows),'Duplicate retention record'
    for record in previous_rows:
        assert re.fullmatch(r'public/audio-v2/[A-Za-z0-9_-]+\.mp3',record['file'])
        assert re.fullmatch('[a-f0-9]{40}',record['originCommit'])
        assert re.fullmatch('[a-f0-9]{64}',record['sha256'])
        assert re.fullmatch(r'\d{4}-\d{2}-\d{2}',record['retainThrough'])
        date.fromisoformat(record['retainThrough'])
    previous={r['file']:r for r in previous_rows}
    entries={file:r for file,r in previous.items() if date.fromisoformat(r['retainThrough'])>=today and '/'+file.removeprefix('public/') not in current}
    until=(today+timedelta(days=90)).isoformat()
    origins={}
    for rev in revisions:
        released=json.loads(git('show',rev+':src/audio-assets.json'))
        records=origins[rev]={r['file']:r for r in json.loads(git('show',rev+':content/voices/sayo-library-provenance.json'))['clips']}
        for voices in released.values():
            for url in voices.values():
                if url in current:continue
                file='public'+url
                # A later run cannot silently restart an expired retention window.
                if file in previous and date.fromisoformat(previous[file]['retainThrough'])<today:continue
                assert file in records,('Released clip lacks provenance',file,rev)
                entries.setdefault(file,dict(file=file,sha256=records[file]['sha256'],originCommit=rev,retainThrough=until))
    for file,record in entries.items():
        assert re.fullmatch(r'public/audio-v2/[A-Za-z0-9_-]+\.mp3',file),file
        assert re.fullmatch('[a-f0-9]{40}',record['originCommit'])
        assert re.fullmatch('[a-f0-9]{64}',record['sha256'])
        origin=record['originCommit']
        if origin not in origins:
            origins[origin]={r['file']:r for r in json.loads(git('show',origin+':content/voices/sayo-library-provenance.json'))['clips']}
        assert file in origins[origin] and origins[origin][file]['sha256']==record['sha256'],('Retention lacks committed proof',file)
        target=root/file
        assert target.resolve().parent==(root/'public/audio-v2').resolve()
        if not target.exists():
            archived=root/'output/audio-backup-before-approved-b/mp3'/target.name
            data=archived.read_bytes() if archived.exists() else git('show',record['originCommit']+':'+file)
            assert sha(data)==record['sha256'],('Retained clip differs from committed provenance',file)
            target.write_bytes(data)
        assert sha(target.read_bytes())==record['sha256'],file
    expired=[r for r in previous.values() if date.fromisoformat(r['retainThrough'])<today]
    ledger=dict(version=1,policy='Exact previously committed audio retained for 90 days for cached clients; excluded from current coverage and native-review claims.',entries=list(entries.values()),expired=expired)
    temp=path.with_suffix('.tmp');temp.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n','utf-8');temp.replace(path)
    print(f'Retained {len(entries)} previously released clips; exact committed hashes verified.')
    return ledger

if __name__=='__main__':retain(history=True)
