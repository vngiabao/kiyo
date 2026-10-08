"""Manually reviewed card-to-source-family evidence, installed cards only.

Multi-form families stay partial unless every listed form is explicitly taught.
No sentence occurrence, question-bank item or lexical match counts as a card.
"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
# Source family index, status, card IDs, the precise instruction inspected.
MAPPING={
4:[
(1,'introduced','01-01','Modal děi contrasted with complement de.'),
(2,'introduced','01-02','Informal 人家, referent and ambiguity.'),
(9,'introduced','02-01','却 and expectation-disconfirming predicates.'),
(10,'introduced','01-03 08-02','未必 as possibility, contrasted with definite negation.'),
(11,'partial','02-04','似乎 is explained; 几乎 has no owned card here.'),
(12,'partial','01-04 02-02 02-04 04-04 08-04','的确、反而、究竟、竟然 are instructed; the entire printed family is not complete.'),
(14,'introduced','02-03','对于 introduces the target of a view, with register comparison.'),
(16,'introduced','03-04','替 introduces acting for another person.'),
(17,'introduced','07-01','根据 as an evidential basis, contrasted with 按照 following instructions.'),
(20,'partial','03-01 04-01 04-04','Several listed conjunctions are instructed; other forms remain.'),
(38,'partial','05-02','Disposal with a result/location is taught; not all three printed structures.'),
(43,'introduced','04-01 05-03','不是…而是 distinguishes the rejected and asserted claims.'),
(46,'introduced','12-01','于是 introduces the resulting next action; 因此 comparison.'),
(50,'introduced','03-03','否则 warns what happens without the stated action.'),
(52,'introduced','09-02','万一 introduces a contingency, not an established fact.'),
(53,'introduced','03-02','不管…都 invariance across named conditions.'),
(54,'introduced','03-02','无论…都 contrasted with conditional rather than universal claims.'),
(55,'introduced','03-01','既然 known reason and 就 proposed consequence.'),
(57,'introduced','10-03','哪怕…也 extreme condition while preserving the result.'),
(64,'introduced','10-01 12-04','Double negation does not remove the following qualification.'),
(66,'introduced','04-02','连…都 emphasizes an unexpected member of a set.'),
],
5:[
(8,'partial','01-01 01-02 01-03 11-01 11-02 11-03','毕竟、明明、倒是、居然、可 explained; printed family has further forms.'),
(9,'introduced','03-01 12-01','随着 connects a change and its accompanying development.'),
(12,'introduced','10-05','凭 makes the evidential basis explicit; one item need not establish a broad claim.'),
(13,'introduced','10-05','依据 introduces evidence, contrasted with unsupported assertion.'),
(15,'partial','07-04 08-02','一旦、从而 taught; 加上 and 完了 remain unowned.'),
(29,'introduced','07-01 09-01','拿…来说 draws a situated example into discussion.'),
(30,'introduced','06-03','A的A，B的B distributes different actions across people.'),
(31,'introduced','02-04 09-03','在…看来 marks a viewpoint, not an uncontested fact.'),
(34,'partial','05-03 07-05','Onset 讨论起来 and continuation 下去; all printed complement senses are not exhausted.'),
(37,'partial','02-03 06-05','得 plus an explanatory clause taught; not all printed phrase classes.'),
(43,'partial','12-05','跟…相比 taught; quantitative comparative pattern still unowned.'),
(44,'introduced','08-04','或是 coordinates alternatives, with clause structure.'),
(45,'introduced','01-04 07-03 09-02 10-04','尽管 accepted fact contrasted with hypothetical 即使.'),
(46,'introduced','07-04','一旦…就 trigger and response.'),
(48,'introduced','08-01','除非…才 frames the required exceptional condition.'),
(49,'introduced','05-02','除非…否则 distinguishes the exception and default consequence.'),
(51,'introduced','10-02','即使…也 hypothetical concession.'),
(52,'introduced','05-04 06-04','为的是 states purpose, not a guaranteed result.'),
(53,'introduced','07-02','以便 written purpose/result-enabling register.'),
(54,'introduced','10-03','没有…就没有 necessary dependence, not a promise of success.'),
(55,'introduced','02-02 04-03','再…也 concession at an extreme degree.'),
(58,'introduced','11-03','Emphatic 可 and its conversational tone.'),
(59,'introduced','06-01','怎么…也/都不 strong rejection across alternatives.'),
(64,'partial','02-01 06-02','X归X concession taught; paired Y归Y structure not exhaustively contrasted.'),
(67,'introduced','11-04','真有你的 can praise or tease; relationship/context matters.'),
(68,'introduced','11-05','X什么X rejects the proposed action; potentially blunt register.'),
],
6:[
(4,'partial','04-06 12-03','番 instruction only; 声 and 趟 are not owned by these cards.'),
(7,'introduced','05-02 12-04','一时、时时、早晚 distinctions and literal vs sooner/later.'),
(8,'introduced','06-02','便 links completion of a condition to the next action.'),
(10,'introduced','05-01 12-01','仿佛 gives an appearance/comparison, not a literal identity.'),
(13,'introduced','07-02','沿着 path, contrasted with 至 endpoint.'),
(15,'introduced','02-03 06-05 08-02 10-06','至于 changes the topic or restricts a different issue.'),
(16,'introduced','06-01','因 introduces the reason; 而 links the result.'),
(17,'introduced','05-06 06-04','除/除了 exception scope.'),
(18,'introduced','03-01 08-01','据 states an information source; 截至 time boundary kept separate.'),
(20,'partial','02-01 09-06 10-05','若 is taught; 不料 and colloquial 可 not covered as this family.'),
(22,'partial','02-06','罢了 restricts scope; 啦、嘛 still lack instruction.'),
(24,'introduced','03-06 05-03 07-03','或A或B written alternatives.'),
(28,'introduced','01-04','那倒也是 concedes a point without erasing the first concern.'),
(29,'introduced','03-05','就是说/这就是说 reformulates the previous information.'),
(34,'introduced','07-05','A一+classifier，B一+classifier distribution.'),
(36,'introduced','04-05','为了…而 frames motivation for an action.'),
(38,'partial','01-06','平静下来/想起来 taught; wider printed state-complement forms remain.'),
(40,'introduced','06-03 07-04','Passive 被…给… with result and register.'),
(41,'introduced','03-03 04-04 12-02','时而…时而 alternation.'),
(44,'introduced','01-03 03-02','不但没有…反而 contrary result rather than a mere addition.'),
(45,'introduced','05-04','不是…还/还是 confirmation question and added observation.'),
(46,'introduced','03-04','连…都…更 establishes an emphatic comparison.'),
(47,'introduced','02-04','要么…要么 alternatives with an appropriate shared scope.'),
(48,'introduced','01-01','虽…但/却 concessive contrast.'),
(50,'introduced','02-02 10-01','凡是…都 applies to all members satisfying the condition.'),
(51,'introduced','01-02 06-06 07-06','就算…也 hypothetical concession.'),
(56,'introduced','01-05','X就X吧 qualified acceptance; can sound reluctant.'),
(57,'introduced','04-01','X是X acknowledges a fact while making a separate point.'),
(61,'introduced','04-02','早不…晚不… complains about timing; not literal universal negation.'),
(63,'introduced','04-03','放着X不Y highlights a neglected available choice.'),
(64,'introduced','05-05','X来X去 identifies what remains across repeated attempts.'),
]}

cards={g['id'] for f in (ROOT/'content/packs').glob('s*-u*.json') for g in json.loads(f.read_text('utf-8')).get('grammar',[])}
# Six has two derivational families before the word classes and four idiom
# families before 那倒也是. Use the actual printed positions, not query order
# guessed from a shortened list. These positions were checked against all 67 rows.
six_positions={4:5,7:8,8:9,10:11,13:14,15:16,16:17,17:18,18:19,
               20:21,22:23,24:25,28:32,29:33,34:35,36:37,38:39,
               40:41,41:42,44:45,45:46,46:47,47:48,48:49,50:51,
               51:52,56:57,57:58,61:62,63:64,64:65}
MAPPING[6]=[(six_positions[index],status,short,note) for index,status,short,note in MAPPING[6]]
inventory=json.loads((ROOT/'prompts/research/gf2021-advanced-inventory.json').read_text('utf-8'))
path=ROOT/'prompts/research/grammar-crosswalk.json'
data=json.loads(path.read_text('utf-8'))
existing={r['code']:r for r in data['evidence']}
for level,entries in MAPPING.items():
    for index,status,short,note in entries:
        code=['','','','','四','五','六'][level]+f'{index:02}'
        all_ids=[f's{level}-u{u}-g{g}' for u,g in (s.split('-') for s in short.split())]
        installed=[i for i in all_ids if i in cards]
        if not installed:continue
        existing[code]=dict(code=code,cards=installed,
            status=status if len(installed)==len(all_ids) else 'partial',
            note=f"Source family: {inventory['levels'][str(level)]['grammar'][index-1][5]}. "+note+' Explicit AI-assisted cards inspected; native review pending. Introduction is not mastery.')
data['evidence']=list(existing.values())
path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n','utf-8')
print('Installed manual advanced grammar evidence; uninstalled cards excluded.')
