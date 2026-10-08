param([ValidateRange(51,53)][int]$FirstBatch = 51, [ValidateRange(51,53)][int]$LastBatch = 53)
$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath (Split-Path -Parent $PSScriptRoot)
$env:PYTHONIOENCODING = 'utf-8'
foreach ($batch in $FirstBatch..$LastBatch) {
  $start = 1 + 4 * ($batch - 51)
  if ($batch -eq 51) {
    & .voice-design-env/Scripts/python.exe scripts/course-authoring/install-early-character-repairs.py
    if ($LASTEXITCODE -ne 0) { throw 'Early character pronunciation repair could not install.' }
    & .voice-design-env/Scripts/python.exe scripts/course-authoring/exam-bank-4.py --publish
    if ($LASTEXITCODE -ne 0) { throw 'Reviewed bank correction could not publish.' }
  }
  foreach ($number in $start..($start + 3)) {
    & .voice-design-env/Scripts/python.exe scripts/course-authoring/install-character-retrofit.py $number
    if ($LASTEXITCODE -ne 0) { throw 'Character retrofit failed; no subsequent unit will change.' }
  }
  & ./scripts/course-audio-gates.ps1 -Batch "$batch"
  if ($LASTEXITCODE -ne 0) { throw "Character batch $batch failed." }
  $receipt = Get-Content -LiteralPath "output/gates/batch-$batch-final-receipt.json" -Raw | ConvertFrom-Json
  if ($receipt.Count -ne 8 -or @($receipt | Where-Object { $_.exitCode -ne 0 }).Count) { throw 'Incomplete character batch receipt.' }
  & npx.cmd tsx scripts/coverage-report.ts --advanced --write
  if ($LASTEXITCODE -ne 0) { throw 'Character coverage report failed.' }
  $entry = "`n## Character batch $batch accepted locally — $([DateTime]::UtcNow.ToString('yyyy-MM-dd HH:mm')) UTC`n`n- s4-u$('{0:00}' -f $start)–s4-u$('{0:00}' -f ($start + 3)): explicit authored glyph meanings, official contextual readings and connected taught words added. Existing unit, vocabulary, task and lesson IDs and all other content were preserved.`n- Self-review: character readings must match both the official glyph entry and the shown word; incompatible polyphonic contexts are excluded from that reading's coverage. Stroke counts use the existing stroke data. Usage notes do not invent etymology.`n- All eight strict checks passed: output/gates/batch-$batch-final-receipt.json. New audio followed the same generation, screening, repair and dated unreviewed fallback policy.`n- Native review pending for all new recognition definitions and recorded contextual tones. These entries are recognition instruction, not new dedicated character lessons or learner mastery.`n"
  Add-Content -LiteralPath prompts/research/course-log.md -Value $entry -Encoding utf8
}
