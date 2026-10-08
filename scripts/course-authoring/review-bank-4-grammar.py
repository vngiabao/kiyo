"""Explicit translations and rationales for the HSK4 grammar-practice draft."""
import re
from pathlib import Path
p=Path(__file__).with_name('exam-bank-4.py')
s=p.read_text(encoding='utf-8')
edits={
2:'''We only send the photo if she agrees.|Keep the condition before the 才 response.
Although the rain is heavy, we still arrive on time.|Keep the concessive clause and its result together.
She put the book back in its original place.|The passive object comes before 被, the agent and the action.
I wrote the ending time clearly.|把 introduces the object before the verb and result.
She is going; she'll just arrive a little later.|不是不去 negates refusal, followed by the limited qualification.''',
3:'''Although the rain is heavy, we still arrive on time.|虽然 introduces the concessive clause here.
We only share the photo if she agrees.|才 completes the 只有 condition.
I returned the materials to their original place.|把 introduces the object before 放回.
He can both sing and write lyrics.|既…又 links the two abilities.
We confirm the place, then enrol.|然后 sequences the second action.''',
6:'''Since you haven't received a reply, check first.|Keep the 既然 reason before the 就 consequence.
Whoever arrives first should go inside and sit.|无论谁 pairs with the unconditional 都 response.
If she hasn't agreed, don't send the photo.|Preserve the negative condition and the instruction.
She put the letter into her bag.|Keep the object 把信 before the action 收进包里.
We confirm the venue before enrolling.|先…再 gives the required order.''',
7:'''Since you haven't received a reply, check first.|就 follows the given 既然 reason.
Whoever arrives first should go inside and sit.|都 completes the 无论 construction.
If she hasn't agreed, don't send the photo.|就 introduces the result of this condition.
She can sing and also write.|也 adds the second ability after 不仅.
Write the ending time clearly to avoid people missing their bus.|避免 introduces the outcome to prevent.''',
10:'''Although the time was short, we still explained it clearly.|Keep the concessive clause and 仍然 result intact.
I do want to take part; today just doesn't work.|The double negative is followed by a specific qualification.
Listen to the whole sentence before judging its meaning.|先…再 orders listening before interpretation.
This is only a pilot; long-term continuation hasn't been decided.|Keep the current pilot separate from a future decision.
She wants to talk and catch her bus.|既…也 connects both wishes.''',
11:'''Although the time was short, we still explained it clearly.|仍然 preserves the result despite the concession.
She wants to talk and catch her bus.|既…也 connects both wishes.
Not every laugh means agreement.|都 falls within the partial negation, so agreement is not universal.
Listen to the whole sentence before judging its meaning.|先…再 establishes the order.
According to the record, twelve people stayed.|从…来看 identifies the basis for the statement.'''
}
regions=list(re.finditer(r"'''(.*?)'''",s,re.S))
for idx,edit in edits.items():
    rows=[r.split('|') for r in regions[idx].group(1).strip().splitlines()]
    replacements=[r.split('|') for r in edit.splitlines()]
    assert len(rows)==len(replacements)==5
    for row,values in zip(rows,replacements):
        row[1],row[-1]=values
    regions[idx]=(*regions[idx].span(1),'\n'+'\n'.join('|'.join(r) for r in rows)+'\n')
for region in reversed(regions):
    if isinstance(region,tuple):
        start,end,new=region;s=s[:start]+new+s[end:]
for old,new in {'Becauseof.':'Because of.','Inorderto.':'In order to.','In orderto.':'In order to.','Soastoavoid.':'To avoid.','Mistakenlythink.':'Mistakenly think.'}.items():s=s.replace(old,new)
p.write_text(s,encoding='utf-8')
print('Applied 30 explicit grammar-item editorial edits.')
