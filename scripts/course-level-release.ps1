param([Parameter(Mandatory=$true)][ValidateSet(2,3)][int]$Level)
$ErrorActionPreference='Stop'
Set-Location -LiteralPath (Split-Path -Parent $PSScriptRoot)
$env:PYTHONIOENCODING='utf-8'
$python='.voice-design-env/Scripts/python.exe'
$gateBatch=if ($Level -eq 2) {'26'} else {'27'}
$prefix="output/gates/level-$Level-release"
function Require-Exit([string]$Step) { if ($LASTEXITCODE -ne 0) { throw "$Step failed ($LASTEXITCODE)" } }
$expected=if ($Level -eq 2) {34} else {44}
$units=@(Get-ChildItem "content/packs/s$Level-u*.json" -File)
if ($units.Count -ne $expected) { throw "HSK$Level has $($units.Count) units, expected $expected" }
$courseLog=Get-Content prompts/research/course-log.md -Raw -Encoding utf8
foreach ($unit in $units) { if (!$courseLog.Contains($unit.BaseName)) { throw "$($unit.BaseName) has no acceptance log" } }
if ($Level -eq 2) {
  # Apply the later self-review correction before compiling the release manifest.
  # IDs and existing records remain stable; regenerate the changed speech only.
  & $python scripts/course-authoring/batch-09.py > "$prefix-editorial-correction.log" 2>&1
  Require-Exit 'Reserialize the reviewed safety wording with unchanged unit IDs'
}
if ($Level -eq 3) {
  & $python scripts/course-authoring/batch-07.py > "$prefix-coverage-correction.log" 2>&1
  Require-Exit 'Align the temporal adverbial entry with its explicit source classification'
  & $python scripts/course-authoring/batch-15.py > "$prefix-sense-correction.log" 2>&1
  Require-Exit 'Teach the cautious-guess adverb sense of 怕 with unchanged unit IDs'
}
& $python "scripts/course-authoring/exam-bank-$Level.py" --install > "$prefix-bank.log" 2>&1
Require-Exit 'Exam-bank serialization'
& npm.cmd run packs > "$prefix-bank-preflight.log" 2>&1
Require-Exit 'Compile and validate the new exam bank before its audio manifest'
& ./scripts/course-audio-gates.ps1 -Batch $gateBatch
Require-Exit 'Exam-bank audio and full level gates'
if ($Level -eq 2) {
  Add-Content -LiteralPath prompts/research/course-log.md -Encoding utf8 -Value '- HSK 2 release self-review correction: replaced the awkward 先看安全 with 先注意安全 in s2-u13, added the recognition gloss, updated English, regenerated the changed speech and reading assembly, and passed all eight release gates. Existing unit/item IDs are preserved; native review remains pending.'
}
& npx.cmd tsx scripts/coverage-report.ts --write > "$prefix-coverage.log" 2>&1
Require-Exit 'Coverage audit'
& $python scripts/course-authoring/native-review-report.py > "$prefix-native.log" 2>&1
Require-Exit 'Exact native-review flags'
& git add -A > "$prefix-stage.log" 2>&1
Require-Exit 'Stage release'
& git commit -q -m "Complete HSK$Level course and rotating exam bank with screened Sayo audio"
Require-Exit 'Commit release'
$revision=(& git rev-parse HEAD).Trim()
Require-Exit 'Read revision'
$cleanRoot=Join-Path (Get-Location) ".cache/clean-hsk$Level-$($revision.Substring(0,8))"
$archive=Join-Path (Get-Location) "$prefix-clean.zip"
if (Test-Path -LiteralPath $cleanRoot) { throw 'Clean verification directory already exists; do not overwrite it' }
& git archive --format=zip -o $archive HEAD
Require-Exit 'Archive committed source'
Expand-Archive -LiteralPath $archive -DestinationPath $cleanRoot
Copy-Item -LiteralPath '.env.local' -Destination (Join-Path $cleanRoot '.env.local')
Push-Location -LiteralPath $cleanRoot
try {
  & npm.cmd ci > "$archive-ci.log" 2>&1
  Require-Exit 'Clean npm ci'
  & npm.cmd run build > "$archive-build.log" 2>&1
  Require-Exit 'Clean production build'
} finally { Pop-Location }
$untracked=@(& git ls-files --others --exclude-standard)
if ($untracked.Count) { throw 'Untracked files remain before deployment; inspect them' }
& git push origin main > "$prefix-push.log" 2>&1
Require-Exit 'Push committed release'
& npx.cmd wrangler deploy > "$prefix-deploy.log" 2>&1
Require-Exit 'Deploy accepted level'
Write-Output "HSK$Level committed, clean-checkout build passed, pushed and deployed: $revision. Live browser checks remain separate."
Get-Content -LiteralPath "$prefix-deploy.log" -Tail 8
