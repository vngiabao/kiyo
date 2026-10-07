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
  9='Checked time-versus-duration, message status, clarification and teasing targets. Corrected contextual 还 to huán when returning books and a pen, preserving hái for still/yet; exact tone delivery remains for native review. Replaced ambiguous syllabic interjections with clearly pronounceable language. Added distinct contexts and recognition glosses. Humour is not evidence of agreement.'
  10='Checked conditional weather, host rotation, map orientation and first-meeting chronology. Added genuine contexts for weather, teams, directions and age groups. A weather forecast is not treated as a confirmed outcome; map north is not equated with the direction the learner faces.'
  11='Checked relationship terms, distance and location references, favour requests, source readings and conjunction scope. Used 求朋友帮忙 rather than an unnatural request collocation. Added distinct contexts and actual glosses; no family or relationship practice is claimed universal.'
  12='Checked complaint causes, supported versus actual understanding, experience aspect and shared-room object references. Added distinct contexts and visible recognition glosses. A listening attempt is not marked comprehension and an experience is not a promised result.'
  13='Checked connective scope, hospital versus pharmacy references, causal reporting and inclusive versus exclusive boundaries. Added genuine contexts and source-specific readings of 得 and 长. Scope is explicit; no clinical advice or universal result is claimed.'
  14='Checked completed results, movement relative to the stated speaker, successive actions and distinctions between desire, obligation and certainty. Corrected classifier arithmetic and flour/称/倒 source readings. Added distinct contexts and actual room/furniture glosses. Recipe timings are fictional practice, not food-safety guarantees.'
  15='Checked surname address permission, non-question interrogatives, surprise intensity, and 可 versus 不易 conditions. Added second contexts and explicit recognition glosses. Later grammar retrieval remains separate from the owner instruction. No nickname implies age or a real family relationship.'
  16='Checked comparisons and proportions, attempt counts, urgency versus permission, and topic scope. Added actual contexts, contrastive examples and character glosses. A requested act is not recorded as a completed result.'
  17='Checked fractions and multiples against the stated denominator, approximate boundaries, result versus potential complements, and consequences versus purpose. Added genuine second contexts and visible glosses. Corrected arithmetic and kept uncertain outcomes conditional.'
  18='Checked direction relative to the speaker, temporal ordering, ongoing versus completed events, and 把 object/result requirements. Added distinct reading contexts and actual glosses. A promise or future action is not treated as completed evidence.'
  19='Checked priority and concession scope, cultural claims, apology versus excuse, and gift acceptance boundaries. Added genuine vocabulary contexts and recognition glosses. Fictional customs are not represented as universal Chinese practice.'
  20='Checked visual inference versus actual reports, comparative scope, causal ordering and concession. Added exact source readings, independent contexts and visible glosses. Retrieval examples do not certify learner mastery.'
  21='Checked four-character paired patterns, larger-topic predicates, 看起来/看上去 evidence, and elapsed time since an event. Differentiated 精神 noun versus adjective source records and 初 prefix use. Added literal second contexts and actual glosses. Fictional symptoms are language practice, not diagnosis.'
  22='Checked 越 comparisons, object/predicate complements, attributives, method versus purpose, and potential/event-count constructions. Corrected a malformed 发出 example, an unclear distractor and the new-character allocation. Kept 了 liǎo, 头 initial, 化 suffix and 信 verb source senses explicit.'
  23='Checked degree complements, emphatic negation, passive agent scope, corrective 是, simultaneous states, alternation and two-aspect framing. Corrected missing literal contexts and the 衣架 classifier. Preserved bèi back, suffix 性 and 极了 source records. Injuries and plant stories provide no clinical or agricultural advice.'
  24='Checked ordered actions, 并且 addition, 不仅 inclusion, exclusive alternatives, immediate sequence, approximation, advanced-state 都 and resigned concessions. Separated 调 diào from tiáo and both 为 wéi source senses. Added actual recognition glosses. Native review is specifically needed for 血 xiě versus xuè and colloquial concession delivery.'
  25='Checked X什么啊 pragmatics, indirect questions, degree and comparison, 把 and 被 focus. Added actual 演戏 character context, removed a traditional-character variant, and replaced an ambiguous 重 cloze with 推广 while preserving the 重 chóng introduction. Added all final retrieval slots. Completion means introduction, never level certification or assumed consent.'
}
if ($StartBatch -lt 8 -or $EndBatch -gt 25 -or $StartBatch -gt $EndBatch) { throw 'Only the self-reviewed sources 08 to 25 are available to this continuation.' }
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
  if ($batch -ge 15) { $first=1+4*($batch-15); $level=3; $units=@($first..($first+3) | ForEach-Object { 's3-u'+$_.ToString('00') }) }
  elseif ($batch -eq 14) { $level=2; $units=@('s2-u33','s2-u34') }
  else { $level=2; $first=9+4*($batch-8); $units=@($first..($first+3) | ForEach-Object { 's2-u'+$_.ToString('00') }) }
  & $python scripts/course-authoring/accept-batch.py $b @units --fixes $fixes[$batch]
  Require-Exit 'Acceptance receipt and protected-file check'
  & npx.cmd tsx scripts/coverage-report.ts --write > "output/gates/batch-$b-coverage.log" 2>&1
  Require-Exit 'Coverage audit'
  & git add -A > "output/gates/batch-$b-git-add.log" 2>&1
  Require-Exit 'Git stage'
  & git commit -q -m "Accept HSK$level batch $b with screened audio and context practice"
  Require-Exit 'Git commit'
  Write-Output "Accepted and committed batch ${b}: $($units -join ', ')."
}
Write-Output 'Requested course batches accepted. Exam-bank and final release gates are required before the level deployment.'
