param([Parameter(Mandatory=$true)][ValidateSet(4,5,6)][int]$Level)
$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath (Split-Path -Parent $PSScriptRoot)
$repo = (Get-Location).Path
$prefix = "output/gates/advanced-$Level-release"
function Require-Exit([string]$Step) {
  if ($LASTEXITCODE -ne 0) { throw "$Step failed ($LASTEXITCODE)" }
}
# These already-authored changes clarify reading timelines and question support.
# Accept their changed audio before shipping HSK 5, not in a later release.
if ($Level -eq 5) {
  & ./scripts/run-editorial-repairs.ps1 -FirstBatch 63 -LastBatch 63
  Require-Exit 'HSK 5 connected-reading editorial acceptance'
}
$batches = switch ($Level) { 4 {39,40,41,51,52,53} 5 {42,43,44} 6 {45,46,47} }
foreach ($batch in $batches) {
  $receipt = Get-Content -LiteralPath "output/gates/batch-$batch-final-receipt.json" -Raw | ConvertFrom-Json
  if ($receipt.Count -ne 8 -or @($receipt | Where-Object { $_.exitCode -ne 0 }).Count) {
    throw "Batch $batch has no complete passing receipt."
  }
}
if (@(Get-ChildItem -LiteralPath content/packs -Filter "s$Level-u*.json" -File).Count -ne 12) {
  throw "Level $Level does not have its twelve selected media/social core units."
}
$latest = Get-ChildItem output/gates -Filter 'batch-*-final-receipt.json' | ForEach-Object {
  $checks = Get-Content -LiteralPath $_.FullName -Raw | ConvertFrom-Json
  if ($checks.Count -eq 8 -and -not @($checks | Where-Object { $_.exitCode -ne 0 }).Count -and $checks[-1].sourceFingerprint) { $checks[-1] }
} | Sort-Object finishedAt -Descending | Select-Object -First 1
$currentFingerprint = (& npx.cmd tsx scripts/release-source-fingerprint.ts).Trim()
Require-Exit 'Read current source fingerprint'
if (-not $latest -or $latest.sourceFingerprint -ne $currentFingerprint) {
  throw 'Source changed since the latest complete checks; run all gates before releasing.'
}
& npx.cmd tsx scripts/coverage-report.ts --advanced --write > "$prefix-coverage.log" 2>&1
Require-Exit 'Coverage report'
& .voice-design-env/Scripts/python.exe scripts/course-authoring/native-review-report.py > "$prefix-native.log" 2>&1
Require-Exit 'Native review flags'
& git add -A > "$prefix-stage.log" 2>&1
Require-Exit 'Stage source and app assets'
$staged = @(& git diff --cached --name-only)
Require-Exit 'Read staged files'
if ($staged | Where-Object { $_ -match '(^|/)(\.env(\.|$)|\.models/|\.cache/|node_modules/|\.voice-design-env/)' -and $_ -ne '.env.example' }) {
  throw 'A credential or local runtime path was staged; inspect before committing.'
}
if ($staged.Count) {
  & git commit -q -m "Add HSK $Level media and social core with screened Sayo audio and practice bank"
  Require-Exit 'Commit accepted release'
}
$revision = (& git rev-parse HEAD).Trim()
Require-Exit 'Read committed revision'
$archive = Join-Path ([IO.Path]::GetTempPath()) "kiyo-advanced-$Level-$($revision.Substring(0,12))-clean.zip"
$cleanRoot = Join-Path ([IO.Path]::GetTempPath()) "kiyo-clean-$($revision.Substring(0,12))"
if (Test-Path -LiteralPath $cleanRoot) { throw 'Clean verification directory exists; preserve it and inspect.' }
& git archive --format=zip -o $archive HEAD
Require-Exit 'Archive committed checkout'
Expand-Archive -LiteralPath $archive -DestinationPath $cleanRoot
# Existing public build settings only; the ignored file never enters Git.
Copy-Item -LiteralPath .env.local -Destination (Join-Path $cleanRoot '.env.local')
Push-Location -LiteralPath $cleanRoot
try {
  & npm.cmd ci > "$repo/$prefix-clean-ci.log" 2>&1
  Require-Exit 'Clean dependency installation from the existing lockfile'
  & npm.cmd run build > "$repo/$prefix-clean-build.log" 2>&1
  Require-Exit 'Clean checkout production build'
} finally { Pop-Location }
if (@(& git ls-files --others --exclude-standard).Count) { throw 'Untracked production/source files remain; inspect before release.' }
$env:GIT_TERMINAL_PROMPT = '0'
& git -c credential.interactive=false push origin main > "$prefix-push.log" 2>&1
Require-Exit 'Push accepted checkout'
& npx.cmd wrangler deploy > "$prefix-deploy.log" 2>&1
Require-Exit 'Deploy accepted checkout'
$entry = "`n- Advanced HSK $Level selected media/social core release: committed $revision; clean checkout npm ci and build passed; pushed to origin/main and deployed. Live browser verification remains separate. Full vocabulary inventory and independent native review are not claimed."
Add-Content -LiteralPath prompts/research/course-log.md -Value $entry -Encoding utf8
Write-Output "Released HSK $Level selected core at $revision."
Get-Content -LiteralPath "$prefix-deploy.log" -Tail 8
