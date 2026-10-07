param([switch]$WaitForHsk2Course)
$ErrorActionPreference='Stop'
Set-Location -LiteralPath (Split-Path -Parent $PSScriptRoot)
if ($WaitForHsk2Course) {
  while ($true) {
    $lastSubject=(& git log -1 --format=%s)
    if ($lastSubject -eq 'Accept HSK2 batch 14 with screened audio and context practice') { break }
    Start-Sleep -Seconds 10
  }
}
& ./scripts/course-level-release.ps1 -Level 2
if ($LASTEXITCODE -ne 0) { throw 'HSK2 release failed; inspect its receipts before continuing' }
& ./scripts/course-continue.ps1 -StartBatch 15 -EndBatch 25
if ($LASTEXITCODE -ne 0) { throw 'HSK3 batch failed; inspect its receipts before continuing' }
& ./scripts/course-level-release.ps1 -Level 3
if ($LASTEXITCODE -ne 0) { throw 'HSK3 release failed; inspect its receipts before reporting completion' }
Write-Output 'All requested course batches and level deployments completed. Read the final receipts and perform live checks before reporting.'
