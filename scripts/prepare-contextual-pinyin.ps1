$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath (Split-Path -Parent $PSScriptRoot)
$env:PYTHONIOENCODING = 'utf-8'
$python = '.voice-design-env/Scripts/python.exe'
function Invoke-Preparation([string]$Command, [string[]]$Arguments) {
  & $Command @Arguments
  if ($LASTEXITCODE -ne 0) { throw "Contextual pinyin preparation failed: $Command $Arguments" }
}
Invoke-Preparation $python @('scripts/test-contextual-de.py')
Invoke-Preparation $python @('scripts/course-authoring/parity-repair-16.py','--publish')
Invoke-Preparation $python @('scripts/course-authoring/repair-de-pinyin.py','--write')
Invoke-Preparation 'npm.cmd' @('run','packs')
Invoke-Preparation 'npx.cmd' @('tsx','scripts/audio-manifest.ts')
# Two dates and an awkward expression change three paragraphs; pinyin preserves
# the Chinese in every other line.
# Replan and screen the new recordings with the original approved voice recipe.
Invoke-Preparation $python @('scripts/generate-audio-qwen.py','--batch','4')
Invoke-Preparation $python @('scripts/screen-audio-qwen.py','--repeat-short','--carrier')
Invoke-Preparation $python @('scripts/repair-audio.py','retry')
Invoke-Preparation $python @('scripts/generate-audio-qwen.py','--batch','4')
Invoke-Preparation $python @('scripts/screen-audio-qwen.py','--repeat-short','--carrier')
Invoke-Preparation $python @('scripts/repair-audio.py','defer')
Invoke-Preparation $python @('scripts/master-audio-qwen.py','--install')
Invoke-Preparation $python @('scripts/retain-released-audio.py')
Invoke-Preparation $python @('scripts/review-approved-audio.py')
Write-Output 'Contextual pinyin, two reading dates and one expression corrected; screened audio provenance refreshed. Native tone review remains pending.'
