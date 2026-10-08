param([ValidateSet('characters','level5','level6','editorial')][string]$From = 'characters')
$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath (Split-Path -Parent $PSScriptRoot)
function Require-Batch([int]$Batch) {
  $receipt = Get-Content -LiteralPath "output/gates/batch-$Batch-final-receipt.json" -Raw | ConvertFrom-Json
  if ($receipt.Count -ne 8 -or @($receipt | Where-Object { $_.exitCode -ne 0 }).Count) {
    throw "Batch $Batch is not accepted."
  }
}
Require-Batch 41
if ($From -eq 'characters') {
  & ./scripts/run-character-retrofit.ps1
  & ./scripts/release-advanced-level.ps1 -Level 4
}
if ($From -in 'characters','level5') {
  & ./scripts/run-advanced-course.ps1 -FirstBatch 42 -LastBatch 44
  & ./scripts/release-advanced-level.ps1 -Level 5
}
if ($From -in 'characters','level5','level6') {
  & ./scripts/run-advanced-course.ps1 -FirstBatch 45 -LastBatch 47
  & ./scripts/release-advanced-level.ps1 -Level 6
}
& ./scripts/run-editorial-repairs.ps1
& ./scripts/release-advanced-level.ps1 -Level 6
Write-Output 'All queued course, character and editorial batches released. Live-site verification remains separate.'
