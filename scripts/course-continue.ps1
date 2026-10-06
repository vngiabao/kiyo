param(
  [Parameter(Mandatory=$true)][int]$StartBatch,
  [Parameter(Mandatory=$true)][int]$EndBatch,
  [switch]$WaitForFirstBatch
)
$ErrorActionPreference='Stop'
Set-Location -LiteralPath (Split-Path -Parent $PSScriptRoot)
$env:PYTHONIOENCODING='utf-8'
$python='.voice-design-env/Scripts/python.exe'
$fixes=@{
  8='Checked recipient order, counters, venue temperature versus impression, and portion estimates. Added distinct vocabulary contexts with visible glosses; no universal allergy or portion claim. Calendar and comparative retrieval remain separate from current assessment.'
  9='Checked time-versus-duration, message status, clarification and teasing targets. Replaced ambiguous syllabic interjections with clearly pronounceable language. Added distinct contexts and recognition glosses. Humour is not evidence of agreement.'
  10='Checked conditional weather, host rotation, map orientation and first-meeting chronology. Added genuine contexts for weather, teams, directions and age groups. A weather forecast is not treated as a confirmed outcome; map north is not equated with the direction the learner faces.'
  11='Checked relationship terms, distance and location references, favour requests, source readings and conjunction scope. Used 求朋友帮忙 rather than an unnatural request collocation. Added distinct contexts and actual glosses; no family or relationship practice is claimed universal.'
  12='Checked complaint causes, supported versus actual understanding, experience aspect and shared-room object references. Added distinct contexts and visible recognition glosses. A listening attempt is not marked comprehension and an experience is not a promised result.'
  13='Checked connective scope, hospital versus pharmacy references, causal reporting and inclusive versus exclusive boundaries. Added genuine contexts and source-specific readings of 得 and 长. Scope is explicit; no clinical advice or universal result is claimed.'
  14='Checked completed results, movement relative to the stated speaker, successive actions and distinctions between desire, obligation and certainty. Corrected classifier arithmetic and flour/称/倒 source readings. Added distinct contexts and actual room/furniture glosses. Recipe timings are fictional practice, not food-safety guarantees.'
}
if ($StartBatch -lt 8 -or $EndBatch -gt 14 -or $StartBatch -gt $EndBatch) { throw 'Only the self-reviewed HSK2 sources 08 to 14 are available to this continuation.' }
function Require-Exit([string]$Step) { if ($LASTEXITCODE -ne 0) { throw "$Step failed ($LASTEXITCODE)" } }
for ($batch=$StartBatch; $batch -le $EndBatch; $batch++) {
  $b=$batch.ToString('00')
  if ($WaitForFirstBatch -and $batch -eq $StartBatch) {
    $receipt="output/gates/batch-$b-final-receipt.json"
    while ($true) {
      if (Test-Path -LiteralPath $receipt) {
        $rows=Get-Content -LiteralPath $receipt -Raw -Encoding utf8 | ConvertFrom-Json
        if (@($rows | Where-Object { $_.exitCode -ne 0 }).Count) { throw "Batch $b has a failed gate; repair it before continuing." }
        if (@($rows).Count -eq 8) { break }
      }
      Start-Sleep -Seconds 10
    }
  } else {
    & $python "scripts/course-authoring/batch-$b.py" > "output/gates/batch-$b-serialize.log" 2>&1
    Require-Exit 'Editorial serialization'
    & npm.cmd run packs > "output/gates/batch-$b-preflight.log" 2>&1
    Require-Exit 'Unchanged pack preflight'
    & ./scripts/course-audio-gates.ps1 -Batch $b
    Require-Exit 'Audio and acceptance gates'
  }
  if ($batch -eq 14) { $units=@('s2-u33','s2-u34') }
  else { $first=9+4*($batch-8); $units=@($first..($first+3) | ForEach-Object { 's2-u'+$_.ToString('00') }) }
  & $python scripts/course-authoring/accept-batch.py $b @units --fixes $fixes[$batch]
  Require-Exit 'Acceptance receipt and protected-file check'
  & npx.cmd tsx scripts/coverage-report.ts --write > "output/gates/batch-$b-coverage.log" 2>&1
  Require-Exit 'Coverage audit'
  & git add -A > "output/gates/batch-$b-git-add.log" 2>&1
  Require-Exit 'Git stage'
  & git commit -q -m "Accept HSK2 batch $b with screened audio and context practice"
  Require-Exit 'Git commit'
  Write-Output "Accepted and committed batch ${b}: $($units -join ', ')."
}
Write-Output 'HSK2 course batches accepted. Exam-bank and final release gates are required before the level deployment.'
