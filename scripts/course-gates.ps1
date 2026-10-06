param(
  [Parameter(Mandatory = $true)][ValidatePattern('^[0-9]{2}$')][string]$Batch,
  [string]$ProductionUrl = 'http://127.0.0.1:4173'
)
$ErrorActionPreference = 'Stop'
$gateRoot = Split-Path -Parent $PSScriptRoot
Set-Location -LiteralPath $gateRoot
$gatePrefix = "output/gates/batch-$Batch-final"
$gateResults = [System.Collections.Generic.List[object]]::new()
function Invoke-CourseGate([string]$Name, [string]$Command, [string[]]$Arguments) {
  $started = [DateTime]::UtcNow
  & $Command @Arguments > "$gatePrefix-$Name.log" 2>&1
  $code = $LASTEXITCODE
  $gateResults.Add([ordered]@{ gate=$Name; exitCode=$code; startedAt=$started.ToString('o'); finishedAt=[DateTime]::UtcNow.ToString('o') })
  $gateResults | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath "$gatePrefix-receipt.json" -Encoding utf8
  if ($code -ne 0) { Get-Content -LiteralPath "$gatePrefix-$Name.log" -Tail 35; throw "Batch $Batch gate failed: $Name ($code)" }
  Write-Output "Passed: $Name"
}
Invoke-CourseGate 'packs' 'npm.cmd' @('run','packs')
Invoke-CourseGate 'types' 'npx.cmd' @('tsc','-b')
Invoke-CourseGate 'content' 'npm.cmd' @('run','validate:content')
Invoke-CourseGate 'unit' 'npm.cmd' @('test')
Invoke-CourseGate 'playback-review' 'npx.cmd' @('tsx','scripts/voice-task-review.ts')
Invoke-CourseGate 'browser' 'npx.cmd' @('playwright','test')
Invoke-CourseGate 'build' 'npm.cmd' @('run','build')
$oldAppUrl = $env:APP_URL
try {
  $env:APP_URL = $ProductionUrl
  Invoke-CourseGate 'production-browser' 'npx.cmd' @('playwright','test','--grep','waiting app update|installed production shell|installed HSK notebook')
} finally {
  if ($null -eq $oldAppUrl) { Remove-Item Env:APP_URL -ErrorAction SilentlyContinue } else { $env:APP_URL = $oldAppUrl }
}
Write-Output "All batch $Batch gates passed. Native review is separate."
