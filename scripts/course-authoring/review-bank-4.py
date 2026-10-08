"""Applied editorial corrections to the authored HSK4 source, before publication."""
import re
from pathlib import Path

path=Path(__file__).with_name('exam-bank-4.py')
s=path.read_text(encoding='utf-8')
for old,new in {
    '不说法不相反，所以无限大。':'不相反，所以无限大。',
    '停止这个开玩笑。':'停止这样说。',
    '把开玩笑说得更久。':'继续这样开玩笑。',
    '真实说奖提前。':'真的说朋友来得早。',
    '被说那句已不存在。':'那句已经不存在。',
    '建议得到喜欢，安排还没确认。':'喜欢这个建议，安排还没确认。',
    '二楼借书借书的地方':'二楼借书的地方',
    '参与者可以参加的人数是多少？':'可以参加活动的人有多少？',
    '通知说参与者二十个座位，工作的人另外有位置。现场四名工作的人，不算进这二十人。':'通知说可以参加活动的人有二十个，工作的人另外有位置。现场四名工作的人，不算进这二十人。',
    '任什么时候间都进。':'什么时候都能进。',
    '那张多了不太平的地方。':'那张纸没有以前那么平了。',
    '不全一样，有不太平的地方。':'不全一样，有张纸不平了。',
    '时间虽然很短我们仍然说清楚了':'虽然时间我们很短仍然说清楚了',
    '|不但|Unless.':'|不但|Not only.',
}.items():
    s=s.replace(old,new)

# Each row is sentence translation, four choice glosses, and key rationale.
# These are explicit edits, not generated translations or inferred answers.
blocks=[
'''Text 1: I can help on Saturday, but I have to leave at three. Text 2: We start moving the tables at four.|The moving time doesn't work.|They've agreed to move the tables.|They can stay until five.|Both texts give the same time.|Leaving at three cannot cover a task that starts at four.
She likes most of the film, but not the ending. She would recommend it, with no spoilers.|She mostly likes it, with reservations about the ending.|She dislikes every part.|She hasn't seen it.|She wants the ending revealed immediately.|Her criticism is limited to the ending.
He planned to take two classes, but their times clash. This time he enrolled only in Wednesday speaking.|Wednesday speaking.|Both classes.|Only reading.|Neither class.|Distinguish his earlier plan from his actual enrolment.
She likes the coat, but it's a little big. She'll try a smaller size before deciding.|No, she still needs to try it.|Yes, calling it nice means she bought it.|Yes, the assistant has paid.|No, she dislikes every coat.|Trying an item does not establish a purchase.
Text 1: The song says the window stays open. Text 2: The notice says the room closes at nine.|Nine, as stated in the notice.|Forever, as in the lyric.|There is no closing time.|It starts at nine tomorrow.|The practical notice supplies the event's closing time.
Two meals cost 35 yuan each and a tea costs 10. All three friends agree to split the whole bill equally.|80 yuan.|70 yuan.|45 yuan.|90 yuan.|The total is 35 + 35 + 10 = 80 yuan.
She misses the second discussion to catch a bus. She liked the first part and might return if the timing works.|To catch a bus.|She finds all the discussions boring.|The next event is cancelled.|She doesn't know anyone.|The text explicitly gives her travel plans as the reason.
A friend may come on Friday if work finishes early. The organiser keeps the name unconfirmed.|Unconfirmed.|Already arrived.|A permanent refusal.|Already paid.|A possible visit has not been confirmed.
Text 1: I like this quiet room. Text 2: It's too small for twenty people.|Not necessarily; it can be quiet and small.|Yes; liking it means twenty people fit.|Yes; a small room cannot be quiet.|No; therefore it is infinitely large.|The two descriptions concern different properties.
She asks whether the materials can be shared. The answer is that they still need to ask the author, so they haven't sent them.|They still need to ask the author.|Everything has already been sent.|She proved that all the content is wrong.|Everyone has explicitly refused.|The stated reason is the outstanding permission.''',
'''I'm at the shop. Take your time. Don't buy my ticket yet; my friend may already have bought it. Wait for her reply.|Wait for the friend's reply.|Buy another ticket immediately.|Announce that the event is cancelled.|Give away every ticket.|The speaker explicitly asks them to wait before buying.
The heavy rain didn't cancel our meeting. We moved it from the park to a café, still at two.|The place.|The time.|The friend's name.|The meeting has been cancelled.|Only the location changes.
Don't misunderstand: I want to help, but I'm only free after six. If it ends at five, I can't help today.|No; they're free too late.|Yes; they can start at four.|Yes; they've already arrived.|Yes; arriving after it ends counts as taking part.|Being free after six does not overlap an event ending at five.
It was a joke, but if you didn't find it funny, I'll stop. You don't have to laugh.|Stop saying it.|Require the other person to laugh.|Ban the other person from coming.|Keep making the joke.|The speaker offers to stop, without demanding a laugh.
I'm asking about this enrolment, not previous study. She studied writing before; this time she enrolled only in speaking.|Speaking.|Writing.|Both speaking and writing.|Only listening to songs.|The question concerns this enrolment.
It used to open at nine. The new notice says nine thirty. Arriving at nine may mean waiting, not that it's closed all day.|Nine thirty.|Nine.|Ten thirty.|It won't open today.|The new notice changes the opening time to nine thirty.
You don't need to tell me everything at once. Start with why the place changed; the other details can wait.|The reason for changing the place.|Everyone's names.|Every price on the menu.|The song's final line.|The listener states the requested priority.
I'm not saying the film is bad. I didn't understand why the sister left the letter on the table. Did you see that part?|To understand that part.|To prove the whole film is bad.|To buy a coat immediately.|To cancel every film.|The speaker asks about the meaning of a particular scene.
Just save me some water. Don't order food for me yet. I ate a little on the way and will decide when I arrive.|Water.|Two meals.|Absolutely nothing.|A return ticket.|Water is specifically requested; food is postponed.
Did you say Thursday or Friday? It's too noisy and I didn't catch it. I haven't agreed to come on both evenings.|They didn't hear which day.|They've agreed to both evenings.|They dislike every sound.|The event has already ended.|This is a request to repair a hearing gap.''',
'''Text 1: Reply before Friday to keep the seat. Text 2: She replies on Saturday morning.|No; her reply is too late.|Yes; she's replied early.|Yes; Saturday is Thursday.|No; she never replied.|She did reply, but after the deadline.
The front of the phone stand holds twelve kilograms. The back becomes unstable above ten. An eleven-kilogram device needs both sides stable.|No; the back is unstable.|Yes; the front being strong enough is sufficient.|Yes; both sides hold twelve.|No; the device weighs only five.|Eleven exceeds the back's stated capacity.
One group wants to sort the materials before discussing them; the other wants to do both together. Both want to finish before Friday.|To finish before Friday.|They must work simultaneously.|They must split the tasks into two separate sessions.|They've already finished.|Their goal agrees even though their methods differ.
The two o'clock bus is cancelled. Staff announce a replacement at 15:10, and she sends her friend the new time.|The new departure time.|The original bus still leaves at two.|There are no buses at all.|She's already home early.|The message communicates the replacement departure.
She declines Saturday's birthday gathering and suggests dinner at seven on Tuesday. Her friend agrees to the time; the place isn't settled.|Dinner at seven on Tuesday.|Attendance at Saturday's party.|The restaurant's name.|Breakfast on Wednesday.|Only the proposed Tuesday time is confirmed.
Her friend is twenty minutes late. She says, 'Really early!' and then says she's joking and hopes they'll come earlier next time.|An ironic reminder about being late.|A sincere compliment about arriving early.|An announcement that there was no arrangement.|A claim that the friend never came.|The explicit joke and late arrival establish the irony.
Text 1: If the weather is good, we'll go. Text 2: Today it rained, so we didn't go.|No; the good-weather condition wasn't met.|Yes; the condition means they go every day.|Yes; not going proves the weather was good.|No; neither text mentions weather.|Rain does not satisfy the stated good-weather condition.
She wants an evening course, but her finishing time at work varies. She asks about catching up on missed classes before deciding.|To see whether the course fits her schedule.|She's already decided not to study.|She wants to cancel all work.|The course has no teacher.|Her question helps her make a decision that is still pending.
In the final scene she puts an unopened letter in her bag. One friend thinks she's afraid to read it; another thinks she's saving it for later. The film doesn't give a reason.|The letter wasn't opened.|She's definitely afraid to read it.|She definitely wants no contact.|The letter's contents are public.|The action is visible; the motive remains unspecified.
She sent the changed time but hasn't received a reply. To avoid a wasted trip, she phones to check.|To check that the friend knows and responds.|To prove that no message was written.|She's already received agreement.|The event is completely over.|Sending a message alone does not establish acceptance.''',
'''Don't use the old entrance today. The new entrance is on the east side, away from the old parking area. I'll send you a photo.|The new entrance on the east side.|The old parking entrance.|The station to the north.|The door at home.|The directions explicitly identify the new entrance.
I said that one sentence was well written, not that the whole article needs no revision. The second paragraph still repeats itself.|Repetition in the second paragraph.|The praised sentence no longer exists.|Everyone's names.|The enrolment time.|The praise concerns one sentence; a separate problem remains.
Wednesday's trial class is free. Friday's full course costs 1,200 yuan, with books bought separately. Taking the trial doesn't enrol you in the full course.|No; books are bought separately.|Every book is included.|It pays for books but no classes.|Both classes are free.|The fee expressly excludes the books.
He did do the work, but didn't test the two sides separately as requested. Let's clarify the method and do it again.|The testing method doesn't meet the requirement.|He did nothing at all.|Both sides have already been tested separately.|No testing is needed.|The problem is how the work was done, not whether any work happened.
She wants to sit quietly alone for a while; she's not angry with anyone. You can say, 'Call me if you need anything,' without continually asking.|Leave a way to contact you when needed.|Keep asking whose fault it is.|Make her speak immediately.|Announce that you'll never contact her again.|This respects her request while keeping help available.
The performance begins at six. Equipment checks start at five thirty. Helpers should come for the checks.|Five thirty.|Six thirty.|Seven.|After the performance.|Helpers need to arrive before the performance starts.
I like the suggestion, but we still need to ask whether the venue can arrange it. We can't announce a definite start next week yet.|The suggestion is liked; arrangements remain unconfirmed.|It definitely starts next week.|Everything is cancelled.|The venue has already agreed.|A positive opinion is not confirmed scheduling.
Review for ten minutes every day from today. One seventy-minute session doesn't count as reviewing on all seven days.|Ten minutes every day.|Seventy minutes today counts as seven days.|Only one day next week.|Only remember names each time.|The instruction includes daily frequency, not just a total duration.
The friend smiled and said, 'Don't make me speak first.' He explained that he wanted to listen first and add something later.|Listen first, then contribute.|He hasn't come at all.|He only handles payment.|He wants everyone else to leave.|His preferred way of participating is explicitly stated.
Don't look only at the low price. The first shop charges eighteen yuan before transport. The second charges twenty-three including delivery. We need the total cost.|The transport charge.|The owner's name.|The door's colour.|The song's final part.|The missing charge prevents a full cost comparison.''',
'''Text 1: The evening event uses only the first floor. Text 2: The upstairs book-lending service still closes at six.|No; lending still closes at six.|Yes; lights mean every service is open.|Yes; the second floor is always open.|Yes; the second text gives no time.|An evening event does not extend the lending service's stated hours.
The novel says he sat for a long time without opening the door. Fear and waiting are possible readings; the next part explains why.|He didn't open the door.|The reason is already explicit.|There is no next part.|He's definitely waiting for his sister.|Only the action is established in this part.
She proposed a four-week trial, continuing only if it works. A friend reposted this as 'already open forever,' and she asked for a correction.|The claim that it's already permanently open.|The fact that there's a four-week trial.|The condition for continuing.|Every time in the message.|The repost wrongly removes the trial period and condition.
Singing may extend a syllable for the music. Class separately practises spoken pronunciation; sounding like the song doesn't prove every spoken syllable is accurate.|Know what each practice is training.|Sounding like the song proves all spoken sounds are correct.|Singing must be forbidden.|Music is grammar.|Musical performance and spoken pronunciation are different practice goals.
Text 1: I want to meet on Sunday, but the morning doesn't work. Text 2: She suggests two on Sunday afternoon, and the other person agrees.|Two on Sunday afternoon.|Two on Sunday morning.|Saturday afternoon.|No agreement was made.|The accepted proposal explicitly says Sunday afternoon.
The notice allows twenty participants, with separate places for staff. Four staff members don't count towards those twenty.|Twenty.|Sixteen.|Twenty-four.|Four.|The participant allowance excludes staff.
She reads the rain in the lyric as waiting; her friend reads it as sound. Both point to lines in the song, without claiming that it describes that day's weather.|Discussing interpretations of the lyric.|Reporting actual rainfall that day.|Confirming the weather in every city.|Proving the author's identity.|They discuss the song's meaning, not a weather report.
The organiser invites anyone who wants to add something. Some people only listen. The rules don't require everyone to speak.|No; listening alone is allowed.|Yes; everyone has to speak.|Yes; listening means leaving.|Yes; they have no seats.|The stated participation rule permits listening.
Text 1: An interview says the event helps people after work. Text 2: The notice requires registration, and no direct entry when it's full.|No; registration is still required.|Yes; they may enter at any time.|Yes; even a full event has unlimited entry.|No; every person is banned.|A benefit described in an interview does not remove registration rules.
The older sister watches the younger sister's bag. Later, the younger sister takes the letter away. In 'she watches the bag', 'she' refers to the older sister.|The older sister.|The younger sister.|Both of them.|The author.|The text explicitly supplies the pronoun's referent.''',
'''You're here? Don't rush onto the stage; have some water. It's okay to be nervous. You can pause and continue without pretending you remember everything.|Pause, then continue.|Drink no water.|Go fast the whole time.|Send everyone away.|The speaker explicitly permits pausing.
'The light is still on' is a lyric, not the venue notice. Pack at nine thirty and close at ten. Don't leave all the closing work to others just to sing more.|Pack things away.|Start a second performance.|Arrange all-night opening.|Announce there is no work.|The stated closing arrangements require packing first.
You said, 'It's good, but too far.' That's still considering, not agreement, so I won't buy your ticket yet.|Still considering.|Already agreed.|Already arrived.|Doesn't know the location.|The stated reservation leaves the decision pending.
Not every laugh means agreement. I liked the joke, but helping on Saturday still depends on my schedule.|No; the timing still needs checking.|Yes; laughing means agreement.|Yes; the work is already done.|Yes; Saturday is already over.|Enjoying the joke does not confirm help with a separate task.
Let her finish. You can add something, but don't drown out her final sentence or we'll have to ask again.|Wait for her to finish, then add something.|Both speak louder at once.|Never speak.|Leave immediately.|Finishing one turn prevents the final words from being missed.
Leaving now doesn't mean I won't come again. Getting home late doesn't work today; I'd still join another event at an earlier time.|Staying very late today.|Every future meeting.|Every friend.|Every song.|The refusal concerns today's late finish, not all future attendance.
The lyric leaves the next page for a future meeting, but doesn't name a day next week. Making a real plan still requires checking everyone's time.|No; no date is stated.|Yes; a ticket has already been bought.|Yes; the lyric is an event notice.|Yes; everyone is free.|The lyrical image doesn't set an actual date.
There are five pages. The bag has pages one, two, three and five; page four was found in the corridor. Returning it completes the set, but that page is no longer flat.|Not completely; one page is no longer flat.|Everything is identical.|No pages have been found.|There are only five identical pages.|Finding the whole set doesn't restore every page's physical condition.
When I say 'hard to say', I mean I don't know yet, not that it definitely won't happen. Wait for their reply; don't turn my answer into certainty.|Not yet.|It definitely won't happen.|It definitely will happen.|Everyone has already been told.|An uncertain answer is neither a definite yes nor a definite no.
Replay the second half of her sentence. I heard 'it's not bad' but missed the rest. Don't give her complete opinion for her.|To hear the missing second half.|To prove everything was understood.|All the meaning is already known.|Only to speed up the song.|The listener identifies a specific part they didn't hear.'''
]
regions=list(re.finditer(r"'''(.*?)'''",s,re.S))
assert len(regions)==12
for idx,translations in zip([0,1,4,5,8,9],blocks):
    rows=[r.split('|') for r in regions[idx].group(1).strip().splitlines()]
    edits=[r.split('|') for r in translations.strip().splitlines()]
    assert len(rows)==len(edits)==10
    for row,edit in zip(rows,edits):
        assert len(row)==12 and len(edit)==6
        for col,value in zip([1,4,6,8,10,11],edit): row[col]=value
    start,end=regions[idx].span(1)
    regions[idx]= (start,end,'\n'+'\n'.join('|'.join(r) for r in rows)+'\n')
for region in reversed(regions):
    if isinstance(region,tuple):
        start,end,new=region
        s=s[:start]+new+s[end:]
path.write_text(s,encoding='utf-8')
print('Applied 60 explicit translation/choice/key edits and Chinese one-key repairs.')
