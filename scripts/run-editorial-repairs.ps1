param([ValidateSet(48,49,50,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68)][int]$FirstBatch = 48, [ValidateSet(48,49,50,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68)][int]$LastBatch = 62)
$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath (Split-Path -Parent $PSScriptRoot)
$env:PYTHONIOENCODING = 'utf-8'
foreach ($batch in @(48,49,50,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68) | Where-Object { $_ -ge $FirstBatch -and $_ -le $LastBatch }) {
  $repair = '{0:00}' -f $(if ($batch -le 50) {$batch - 45} else {$batch - 48})
  $start = switch ($batch) { 48 {29} 49 {33} 50 {41} 54 {21} 55 {25} 56 {1} 57 {29} 58 {5} 59 {9} 60 {13} 61 {17} 63 {1} 64 {5} 65 {9} 66 {1} 67 {5} 68 {9} }
  $level = if ($batch -in @(57,62)) {2} elseif ($batch -in @(63,64,65)) {5} elseif ($batch -in @(66,67,68)) {6} else {3}
  $numbers = if ($batch -eq 62) { @(4,7,23,25) } else { $start..($start + 3) }
  & .voice-design-env/Scripts/python.exe "scripts/course-authoring/parity-repair-$repair.py" --publish
  if ($LASTEXITCODE -ne 0) { throw "Editorial source $repair could not publish." }
  & ./scripts/course-audio-gates.ps1 -Batch "$batch"
  if ($LASTEXITCODE -ne 0) { throw "Editorial batch $batch failed; no subsequent batch will change." }
  $receipt = Get-Content -LiteralPath "output/gates/batch-$batch-final-receipt.json" -Raw | ConvertFrom-Json
  if ($receipt.Count -ne 8 -or @($receipt | Where-Object { $_.exitCode -ne 0 }).Count) { throw 'Incomplete editorial acceptance receipt.' }
  & npx.cmd tsx scripts/coverage-report.ts --advanced --write
  if ($LASTEXITCODE -ne 0) { throw 'Editorial coverage report failed.' }
  $notes = @()
  foreach ($number in $numbers) {
    $id = 's{0}-u{1:00}' -f $level,$number
    $pack = Get-Content -LiteralPath "content/packs/$id.json" -Raw | ConvertFrom-Json
    $notes += "- $id`: $($pack.vocabulary.Count) existing word records; grammar: $(($pack.grammar | ForEach-Object { $_.pattern }) -join '; '). Applied fixes and native flags: $($pack.notes.Split([char]10)[-1])"
  }
  $entry = "`n## Editorial batch $batch accepted locally — $([DateTime]::UtcNow.ToString('yyyy-MM-dd HH:mm')) UTC`n`n$($notes -join "`n")`n- Existing unit, word and task IDs are preserved. Believable scenes and independent word examples replace coverage stuffing and policy/grammar analysis inside speech. Related later glossary dependencies gained definitions without changing their lines.`n- All eight strict gates passed: output/gates/batch-$batch-final-receipt.json. Changed audio was generated, screened, genuinely repaired and installed; dated unresolved exceptions remain unreviewed.`n- Native review remains pending. No automatic test establishes naturalness, accent certification or learner mastery. This receipt is local acceptance, not deployment.`n"
  Add-Content -LiteralPath prompts/research/course-log.md -Value $entry -Encoding utf8
}
