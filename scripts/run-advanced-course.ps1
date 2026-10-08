param([int]$FirstBatch = 41, [int]$LastBatch = 47)
$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath (Split-Path -Parent $PSScriptRoot)
$env:PYTHONIOENCODING = 'utf-8'
$python = '.voice-design-env/Scripts/python.exe'
foreach ($batch in $FirstBatch..$LastBatch) {
  if ($batch -lt 41 -or $batch -gt 47) { throw 'Advanced course batches are 41 through 47.' }
  $level = if ($batch -eq 41) { 4 } elseif ($batch -le 44) { 5 } else { 6 }
  $start = if ($batch -eq 41) { 9 } elseif ($level -eq 5) { 1 + 4 * ($batch - 42) } else { 1 + 4 * ($batch - 45) }
  # Validate the unpublished bank before adding it to this level's audio batch.
  if ($start -eq 1) {
    & $python "scripts/course-authoring/exam-bank-$level.py"
    if ($LASTEXITCODE -ne 0) { throw "Could not serialize level $level bank." }
    & npx.cmd tsx scripts/check-exam-draft.ts ".cache/course-authoring/hsk-$level-bank.hsk.json"
    if ($LASTEXITCODE -ne 0) { throw "Level $level bank has not passed its strict validator." }
    & $python "scripts/course-authoring/exam-bank-$level.py" --publish
    if ($LASTEXITCODE -ne 0) { throw "Could not publish level $level bank." }
  }
  foreach ($unit in $start..($start + 3)) {
    $source = 'scripts/course-authoring/advanced-{0}-{1:00}.py' -f $level, $unit
    & $python $source --publish
    if ($LASTEXITCODE -ne 0) { throw "Could not publish $source" }
  }
  & $python scripts/course-authoring/advanced-grammar-evidence.py
  if ($LASTEXITCODE -ne 0) { throw "Manual grammar evidence installation failed." }
  $batchId = '{0:00}' -f $batch
  & ./scripts/course-audio-gates.ps1 -Batch $batchId
  if ($LASTEXITCODE -ne 0) { throw "Batch $batchId failed; no following batch will publish." }
  $receipt = Get-Content -LiteralPath "output/gates/batch-$batchId-final-receipt.json" -Raw | ConvertFrom-Json
  if ($receipt.Count -ne 8 -or @($receipt | Where-Object { $_.exitCode -ne 0 }).Count) {
    throw "Batch $batchId has an incomplete acceptance receipt."
  }
  & npx.cmd tsx scripts/coverage-report.ts --advanced --write
  if ($LASTEXITCODE -ne 0) { throw "Batch $batchId coverage report failed." }
  # Log only after the complete receipt exists. Author notes retain native flags.
  $units = @()
  $families = @()
  foreach ($unit in $start..($start + 3)) {
    $id = 's{0}-u{1:00}' -f $level, $unit
    $pack = Get-Content -LiteralPath "content/packs/$id.json" -Raw | ConvertFrom-Json
    $units += "$id ($($pack.vocabulary.Count) word records)"
    $families += "$id`: $(($pack.grammar | ForEach-Object { $_.pattern }) -join '; ')"
  }
  $entry = @"

## Advanced batch $batchId accepted locally — $([DateTime]::UtcNow.ToString('yyyy-MM-dd HH:mm')) UTC

- Units: $($units -join ', '). Word records include retrieval; they are not all new distinct source entries.
- Grammar cards actually present: $($families -join ' | '). Manual source-family crosswalk remains separate.
- Self-review and applied content fixes: recorded in each pack's notes and its authored source. Readability/pinyin problems were repaired before publication; no non-audio gate was relaxed.
- All eight receipt checks passed: packs/pinyin/readability, types, content/audio, unit tests, playback review, development browser tests, build, and production offline browser tests. Receipt: output/gates/batch-$batchId-final-receipt.json.
- Sayo takes were generated, screened and genuinely repaired; unresolved takes are dated unreviewed exceptions under the owner's audio-only policy. Device speech is not labelled Sayo.
- Native review remains pending for every newly authored line, with particular flags in each pack's notes. No synthetic check certifies natural tone or learner mastery.
- Acceptance is local. A commit, push or deployment must be reported separately after it actually succeeds.
"@
  Add-Content -LiteralPath prompts/research/course-log.md -Value $entry -Encoding utf8
  Write-Output "Accepted advanced batch $batchId."
}
