param([Parameter(Mandatory=$true)][ValidatePattern('^[0-9]{2}$')][string]$Batch)
$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath (Split-Path -Parent $PSScriptRoot)
$env:PYTHONIOENCODING = 'utf-8'
$prefix = "output/gates/batch-$Batch"
function Invoke-AudioStep([string]$Name, [string]$Command, [string[]]$Arguments) {
  & $Command @Arguments > "$prefix-$Name.log" 2>&1
  if ($LASTEXITCODE -ne 0) {
    Get-Content -LiteralPath "$prefix-$Name.log" -Tail 25
    throw "Batch $Batch audio step failed: $Name"
  }
  Write-Output "Passed: $Name"
}
$python = '.voice-design-env/Scripts/python.exe'
Invoke-AudioStep 'manifest' 'npx.cmd' @('tsx','scripts/audio-manifest.ts')
Invoke-AudioStep 'generate' $python @('scripts/generate-audio-qwen.py','--batch','8')
Invoke-AudioStep 'screen' $python @('scripts/screen-audio-qwen.py','--repeat-short','--carrier')
Invoke-AudioStep 'repair' $python @('scripts/repair-audio.py','retry')
Invoke-AudioStep 'regenerate' $python @('scripts/generate-audio-qwen.py','--batch','8')
Invoke-AudioStep 'rescreen' $python @('scripts/screen-audio-qwen.py','--repeat-short','--carrier')
Invoke-AudioStep 'defer' $python @('scripts/repair-audio.py','defer')
Invoke-AudioStep 'master' $python @('scripts/master-audio-qwen.py','--install')
Invoke-AudioStep 'review' $python @('scripts/review-approved-audio.py')
& ./scripts/course-gates.ps1 -Batch $Batch
if ($LASTEXITCODE -ne 0) { throw "Batch $Batch gates failed" }
