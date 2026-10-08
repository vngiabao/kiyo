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
$selectedUnits = switch ([int]$Batch) {
  37 { 's3-u41,s3-u42,s3-u43,s3-u44' }
  38 { 's3-u37,s3-u38,s3-u39,s3-u40' }
  39 { 's4-u01,s4-u02,s4-u03,s4-u04' }
  40 { 's4-u05,s4-u06,s4-u07,s4-u08' }
  41 { 's4-u09,s4-u10,s4-u11,s4-u12' }
  42 { 's5-u01,s5-u02,s5-u03,s5-u04' }
  43 { 's5-u05,s5-u06,s5-u07,s5-u08' }
  44 { 's5-u09,s5-u10,s5-u11,s5-u12' }
  45 { 's6-u01,s6-u02,s6-u03,s6-u04' }
  46 { 's6-u05,s6-u06,s6-u07,s6-u08' }
  47 { 's6-u09,s6-u10,s6-u11,s6-u12' }
  48 { 's3-u29,s3-u30,s3-u31,s3-u32' }
  49 { 's3-u33,s3-u34,s3-u35,s3-u36' }
  50 { 's3-u41,s3-u42,s3-u43,s3-u44' }
  51 { 's4-u01,s4-u02,s4-u03,s4-u04' }
  52 { 's4-u05,s4-u06,s4-u07,s4-u08' }
  53 { 's4-u09,s4-u10,s4-u11,s4-u12' }
  54 { 's3-u21,s3-u22,s3-u23,s3-u24' }
  55 { 's3-u25,s3-u26,s3-u27,s3-u28' }
  56 { 's3-u01,s3-u02,s3-u03,s3-u04' }
  57 { 's2-u29,s2-u30,s2-u31,s2-u32' }
}
$oldSelectedUnits = $env:COURSE_UNIT_IDS
try {
  if ($selectedUnits) { $env:COURSE_UNIT_IDS = $selectedUnits }
  Invoke-CourseGate 'browser' 'npx.cmd' @('playwright','test')
} finally {
  if ($null -eq $oldSelectedUnits) { Remove-Item Env:COURSE_UNIT_IDS -ErrorAction SilentlyContinue }
  else { $env:COURSE_UNIT_IDS = $oldSelectedUnits }
}
Invoke-CourseGate 'build' 'npm.cmd' @('run','build')
$oldAppUrl = $env:APP_URL
try {
  $env:APP_URL = $ProductionUrl
  Invoke-CourseGate 'production-browser' 'npx.cmd' @('playwright','test','--grep','waiting app update|installed production shell|installed HSK notebook')
} finally {
  if ($null -eq $oldAppUrl) { Remove-Item Env:APP_URL -ErrorAction SilentlyContinue } else { $env:APP_URL = $oldAppUrl }
}
$sourceFingerprint = (& npx.cmd tsx scripts/release-source-fingerprint.ts).Trim()
if ($LASTEXITCODE -ne 0 -or $sourceFingerprint -notmatch '^[a-f0-9]{64}$') { throw 'Could not stamp the tested source.' }
$gateResults[$gateResults.Count - 1]['sourceFingerprint'] = $sourceFingerprint
$gateResults | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath "$gatePrefix-receipt.json" -Encoding utf8
Write-Output "All batch $Batch gates passed. Native review is separate."
