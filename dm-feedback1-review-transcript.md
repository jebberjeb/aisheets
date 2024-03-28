PromETL (2024-03-14 14:12 GMT+1) - Transcript
Attendees
Jeb Beich, Jeb Beich's Presentation, Philipp Meier, Philipp Meier's Presentation
Transcript
This editable transcript was computer generated and might contain errors. People can also change the text after it was created.
Jeb Beich: You're gonna guinea pig something for me if you don't mind. All right. check this out. I learned that you can do this while you can Picture and picture now. I can avoid the mint the mirror the infinite.
Philipp Meier: The two picture. Yeah. Yeah.
Jeb Beich: What is it called infant window mirror or something?
Philipp Meier: I don't know have this sign this is what it called like.
Jeb Beich: All right, let me
Philipp Meier: It interferes with the background detection, right? Because it's not face.
Jeb Beich: show you All I'm gonna run my AI sheet great this is a little AI process…
Philipp Meier: No, it's okay.
Jeb Beich: 
Philipp Meier: nice.
Jeb Beich: which Talks to the llm to give some feedback on the decision Matrix. It's connecting to the sheets.
Philipp Meier: Cool. yeah, …
Jeb Beich: It's like reading it and it's querying the element.
Philipp Meier: how hard is it to get access to Google sheet data with python because the deployment experience with the app script is kind of Complicated at new bank, right? I have that A&D Matrix template way can switch color scheme for a color blind people. and the script Works awesome, but you need to copy and paste it into Every DM and need to enable it so. Yeah. Okay.
Jeb Beich: I can definitely talk to you about that. And there's a way…
Jeb Beich: but let's do this first and…
Philipp Meier: Cool,…
Jeb Beich: then I have done it.
Philipp Meier: so it's tracking. Yeah.
Jeb Beich: All this is gonna be feedback only about criteria. And what I want you to do is I want you to tell…
Philipp Meier: Yeah.
Jeb Beich: what you think about I want you to give me your thoughts on the quality of this feedback. about criteria only…
Philipp Meier: Yeah.
Jeb Beich: because I've been looking into this. All right, let's go. so simplify criteria descriptions Some are explained with extensive details within the decision Matrix.
Philipp Meier: That's great. Yeah.
Jeb Beich: It would be beneficial to distill these into more concise statements. For example, for more elaborate explanations considered appendix or supplementary document. I don't really think that's great feedback.
00:35:00
Philipp Meier: Yeah. That's something to consider in general and…
Jeb Beich: That's kind of like me. I don't know. I'd rate that I
Philipp Meier: you're like, That's true, and maybe I could take that and Improved. Yeah, yeah.
Jeb Beich: yeah, but it's not particularly insightful or all right, next one clear ambiguous terminology terms like Good medium and bad or…
Philipp Meier: That's awesome advice.
Jeb Beich: subjective because lead to misinterpretation. Okay.
Philipp Meier: it might mean it's clear, but it's good to have that pointed out because sometimes you just lazy and…
Jeb Beich: It's limping.
Philipp Meier: that's not really something to quantify. What does it mean? This is Good,…
Jeb Beich: Yeah, it gets you to think a little more right?
Philipp Meier: right. Why is it good?
Jeb Beich: Yeah, why is it?
Philipp Meier: Right. It's missing the…
Philipp Meier: why right?
Jeb Beich: So I think of this as useful linting right here,…
Philipp Meier: Mmm Yeah mmm
Jeb Beich: it's not particularly profound, but it's something we do a lot and you uniformity and measurement is for consistency and how it comes or measured across different criteria. For instance use a consistent cost measurement across all the road and criteria. I don't know if I care about that too much.
Philipp Meier: guys rather General but yeah comparing apples to What do you say in English apples to?
Jeb Beich: Yeah, I don't know. oranges All…
Philipp Meier: Oranges, yeah for this apple to peaches.
Jeb Beich: let's specific criteria. All right. So here we go refinement overall performance is vaguely defined break it down in a specific criteria such as processing latency or…
Philipp Meier: Yeah.
Jeb Beich: in throughput.
Philipp Meier: Yeah. That's good.
Jeb Beich: I like this one. I think this is actually
Philipp Meier: And it's validated by my own comment. What is performance? what is like sea efficiency,…
Jeb Beich: yeah, right there. Yeah.
Philipp Meier: I don't know if that was the reason why that AI thought it's something but yeah, that would be a good feedback right in general when you see that in a criteria,…
Jeb Beich: Yeah, I would. Take it.
Philipp Meier: right? Yeah.
Jeb Beich: Efficiency could benefit from further breakdown into resource utilization efficiency and cost efficiency to provide a more. There you go.
Philipp Meier: Spot on right something to consider, right?
Jeb Beich: All right. The maintenance cost criteria should specify whether refers to financial cost time investment are both. I actually think that's good. When I do that all the time I miss that.
Philipp Meier: Yeah, yeah, and in this particular case, it's even more important as we talking about it. Doing something like having operational cost or…
Jeb Beich: Yeah.
Philipp Meier: Cloud cost being assigned to team a operational cost at least Handing up at reliability and maybe reassigning it to causing teams and…
Jeb Beich: interesting
Philipp Meier: So it points at one of the old core problems, right?
Jeb Beich: Let's check this out. This one is interesting.
Philipp Meier: Yeah. Yeah.
Jeb Beich: I'm not sure if this is particularly, right, but it's interesting. Operational ownership of pipelines and ownership of ingestion data set seem to overline with the overlap with alignment with overall governments and ownership strategy and data consider consolidating and that's interesting.
Philipp Meier: That's something good. Yeah, because the governance strategy says own data You own the processing?
Jeb Beich: interesting
Philipp Meier: Of it and…
Jeb Beich: Really? Really?
Philipp Meier: the Machinery cost, So yeah data governance or data strategy. This is pointed out somewhere in that she Would say…
Jeb Beich: Okay, okay.
Philipp Meier: if you earn the ingestion data set in your data, you also own the processing.
Philipp Meier: Which creates it including the ingestion pipelines?
Jeb Beich: So the scenario where?
Philipp Meier: So according to the data strategy. You should own the ingestion pipelines, Because data data strategy is from what I can tell focus on the data and the Ingress to the data, We currently also consider the egress are from ETL the fact that only prometl is feeding into the Pipelines.
Jeb Beich: 
Jeb Beich: Okay.
Philipp Meier: Right saying maybe all the consumer system should be owned by the owner of prometl. It's one of our arguments. So this is actually a good finding.
Jeb Beich: But you did talk about that here and…
Philipp Meier: Yeah.
Jeb Beich: you did like it as yellow. That's cool.
Jeb Beich: Okay, because it is slightly some of these Solutions deviate from that.
Philipp Meier: Yeah. it's a good advice to consider.
Jeb Beich: Nice.
Philipp Meier: Can you break that?
Jeb Beich: Yeah, can you refine it?
Philipp Meier: Break that down because It's kind of unclear. And that's General. These kind of findings are good because something like that happens when when you work on those criteria, Repetitively right and you figure something you added. And you would actually need to consolidate criteria, Because we maybe have touch aspects of it before you have a broad thing like ownership right plus minus good whatever and…
Jeb Beich: Yeah.
Philipp Meier: later down you realize ownership of Some subdomain of the problem right now. You have two overlapping criteria and you don't realize that while working it because that Matrix is so huge ready.
00:40:00
Jeb Beich: Interesting. Okay, let's go.
Philipp Meier: Yeah.
Jeb Beich: Let's keep going here…
Jeb Beich: because there's a little more and these are criterates.
Philipp Meier: I'm missing criter's good.
Jeb Beich: Yeah. Security so that's like isolation touch upon these conditions.
Philipp Meier: Yeah.
Jeb Beich: Most highlight important trade-offs between Solutions.
Philipp Meier: Yeah. it's a good point to consider in general.
Jeb Beich: I don't know. I mean, is it good?
Philipp Meier: The thing here is that particular case?
Jeb Beich: Is relevant here. Yeah.
Philipp Meier: I guess all of the solutions would have more or less The same answer and…
Jeb Beich: Yeah, I don't.
Philipp Meier: it comes back to the fact that all the data is initially sitting in the same storage. Anyways, in Prometheus. for example the separation of data based on ownership or…
Jeb Beich: Yeah, I don't think it's super relevant in this case.
Philipp Meier: ownership domain something you would typically do you do not want to mix data in the same data store if you don't need to But as they are. stored in one data Stone beginning We don't lose anything by using a single pipeline if that would be 15 systems with Data customer data business process technical things.
Jeb Beich: 
Philipp Meier: And we would start mixing them. That would be different. but we already have them in a global Prometheus instance right when you look at that from users contains.
Jeb Beich: Okay.
Philipp Meier: Cast not really customer related data, but say business data, right?
Jeb Beich: Good our customer data. I mean, I don't see any reason…
Philipp Meier: Yeah.
Jeb Beich: why because any app can log anything at once the Prometheus so,
Philipp Meier: Yeah, but we have that already. So this is in general a very good criteria to add.
Jeb Beich: Yeah. It's not relevant here.
Philipp Meier: In this case, it's not relevant because all of the solutions are yellow anyways,…
Jeb Beich: All right.
Philipp Meier: right already. Yeah.
Jeb Beich: Let's keep going on then. ability the term scalability EG or Boris could be clarified specific aspects like horizontal and…
Philipp Meier: Yeah.
Jeb Beich: vertical could provide deeper guards. I mean, I guess that's whatever it's okay.
Philipp Meier: That's good. It's missing contacts. Everybody working on that should have the context of oroboros. But yeah, it's good. Nevertheless not wrong.
Jeb Beich: Okay user experience. This is mentioned but can be expanded upon user operational complexity could be a valuable addition considering…
Philipp Meier: Mm-hmm
Jeb Beich: how different solutions might require different levels of Engagement from the teams involved.
Philipp Meier: I like the word user operational complexity. Or the term but there's something that aren't helpful…
Jeb Beich: Yeah. Clearer exactly…
Philipp Meier: because that's exactly what I wanted to point out, right? Yeah.
Jeb Beich: what you want to plan. Okay, and this one's …
Jeb Beich: 
Philipp Meier: That's a good finding right?
Philipp Meier: It's maybe yeah.
Jeb Beich: I'll show you the prompt I used but it's interesting that it came up with that. Okay, let's keep going because It's criteria structure avoid okay now structure now, we're gonna talk about structural.
Philipp Meier: Yeah, that's interesting.
Jeb Beich: Avoid nesting multiple aspects within a single Criterion. For example recovery after crash incident with promethial encompasses several potential evaluation metrics. Okay, but breaking complex criteria to simpler more Focus criteria can improve clarity.
Philipp Meier: Yeah.
Jeb Beich: I don't know that's decent general advice. I'm not sure that this Is really breakable though.
Philipp Meier: yeah, the thing is that It would be more helpful…
Jeb Beich: That is one thing right.
Philipp Meier: if it would list all the instances in the sheet where this happens right? Pretty sure that's not the only…
Jeb Beich: Yeah.
Philipp Meier: where we talk about two things. At the same time,…
Jeb Beich: Okay, that's great feedback. Thanks. I'm telling I think that's really great feedback.
Philipp Meier: right? Yeah.
Jeb Beich: And when I asked the AI to summarize your feedback on this later. I want that to be at the top of the list. Let's see if it doesn't.
Philipp Meier: But you asking AI to improve the prompt right? How can I improve the problem that maybe yeah.
Jeb Beich: Yeah. s***. that's it. I hadn't actually thought about that. I was gonna take my dude. I can't wait to do that.
Philipp Meier: What did we have if we have enough existing material now on prompt engineering so I can totally think that would be helpful, right?
Jeb Beich: my gosh, really?
Jeb Beich: Yeah. Yeah, I'm gonna take the prompt. I'm gonna tell I'm gonna give it your feedback and…
Philipp Meier: Yeah. Yeah.
Jeb Beich: I'm gonna ask it to improve the problem.
Philipp Meier: Yeah. …
Jeb Beich: I can't wait to do this, dude.
Philipp Meier: it sounds to me like my feeling is this is becoming weird mixture of a Star Trek Holodeck and…
Jeb Beich: All right.
Philipp Meier: Star Trek replicator right where they make me maybe a better replica. that's a philosophical question. Can you replicate the replicator?
Jeb Beich: You can confuse their eyebrows.
Philipp Meier: Can you ate a replicator in Star Trek?
Jeb Beich: No, that's a good question.
00:45:00
Jeb Beich: That's a good question.
Philipp Meier: I will ask AI about that…
Jeb Beich: Yeah, let's ask that.
Philipp Meier: because pretty sure in some using that group. This was discussed on the field down to the quantum physics level, right?
Jeb Beich: I mean that's sensitive.
Jeb Beich: All right. Let's keep going ensure. Each Criterion is directly relevant to the overarching goal of defining the cardinality and ingestion Pipelines. So make sure they're relevant some criteria seem to address broader organization operational issues. That although important May dilute to focus on selecting the optimal pipeline configuration. I don't know. You might want to think about it.
Philipp Meier: That it is something right this is basically also at the heart of our problem of one criteria is what's the best continentality for technical reasons for scale for scaling for isolation for? A cost efficiency and so on and we had identify the other question who's going to own that what is a completely operational question, right? This is a business…
Jeb Beich: Yeah. …
Philipp Meier: who pays for it question.
Jeb Beich: yeah. I'd be split apart.
Philipp Meier: So the interesting point is The Prompt extract basically that this is a main matter question of the seed,…
Jeb Beich: It did.
Philipp Meier: right? From…
Jeb Beich: Yeah.
Philipp Meier: how we practice the data,…
Jeb Beich: Yeah. I told the prompt A1.
Philipp Meier: right? Yeah.
Jeb Beich: Yeah, I told the prompt A1 Is the problem I told it about Solutions and I told it about criteria. It must have figured this.
Philipp Meier: Yeah, but yeah, and then it says you're talking about how to design it on which organizational level and you're talking about. How many do you want? And those are first of all independent concerns,…
Jeb Beich: Yeah. Yeah.
Philipp Meier: so the question is did the model. Come up with that as a conclusion from how we structured the data. right
Jeb Beich: I don't know.
Philipp Meier: which is not helpful because we took this advice to come up with the structure of the data or did that would have come up with that. Also if we had organized the decision Matrix differently,…
Jeb Beich: I told it that it should.
Philipp Meier: right? Yeah.
Jeb Beich: It should avoid criteria which broaden the scope of the problem.
Philipp Meier: Okay.
Jeb Beich: So maybe I'll show you.
Philipp Meier: Yeah. Yeah. So on the other hand is a little bit unspecific to saying what is mean some criteria. Please tell me which you're talking about, right? Yeah.
Jeb Beich: Okay, that's good feedback. Yeah, you'd like specific. So it says So this phrase some criteria seem to address. Our organization is you'd rather have it tell you exactly what criteria that it thinks that this applies to. All…
Philipp Meier: Yeah.
Jeb Beich: Let's keep going enhanced comparability for criteria like Cloud operational costs explicitly stated assumptions or provide formulas for cost calculations and that's good feedback. But whatever. Let's move past that where it depends is used in capital letters and quotes identifies specific factors or conditions that influence the outcome to guide decision making more effectively. I think that's good feedback. It'll help you like the criteria.
Philipp Meier: I mean one thing is Nothing so far is surprising, right? all is bad…
Jeb Beich: Okay, none of this is surprising to you.
Philipp Meier: if all is best practices or good like knowledge about that, but
Jeb Beich: linting stuff. This is all living.
Philipp Meier: Yeah, but having it pointed out is helpful as kind of a checklist or something to verify like what you said linting. It's like mmm
Jeb Beich: When you actually want this, would you want this list? I don't know. I think I would…
Philipp Meier: Yeah.
Jeb Beich: if I was gonna sit in front of stew with this decision Matrix in an you…
Philipp Meier: Yeah.
Jeb Beich: 
Jeb Beich: but if it's just me and you talking about it, I'm not sure because there's
Philipp Meier: I mean what one thing would be super helpful is could that kind of detect something like contradictions in The Matrix contradictions in criteria, hey in some line you talk about this is the most important criteria…
Jeb Beich: Yeah. Okay contradiction.
Philipp Meier: then further down you say this is what do you want right or you have solution Which does this right?
Jeb Beich: Okay, so That's another thing you would want. You don't criteria contradictions in the criteria. Okay?
Philipp Meier: So that would be awesome but this is again, llms cannot do reasoning but they can detect patterns of contradictions, right?
Jeb Beich: really surprised Okay, what about the okay, contradictions you would want to lose a question. I want to ask you.
Philipp Meier: I give you an example. We evaluate different cars,…
Jeb Beich: wait.
Philipp Meier: right and we say car a is great because it runs fast and how B is great because it also runs fast faster 80 miles per hour 90 miles per hour and we say solution C is the car and it's awesome because it's fuel efficient. There wouldn't be a contradiction but would be an inconsistency in the evaluation. right criteria kind of right if assume that those values would be in the same row like Performance,…
00:50:00
Jeb Beich: He didn't feel efficiency.
Jeb Beich: Yeah, yeah. Yeah.
Philipp Meier: right and you say fuel efficiency speed that's something what I think that could detect and say hey you're talking about the same thing,…
Jeb Beich: I see I see.
Philipp Meier: but you kind of switching topics.
Jeb Beich: Right. So use the value in the internal cells to actually figure out…
Philipp Meier: Yeah.
Jeb Beich: what you're talking about two separate criteria. Not the same thing.
Philipp Meier: and the summary that He overall that prompt gave us was I would say there was an A or a B+ right on the decision metric and…
Jeb Beich: B+. Okay.
Philipp Meier: Intuitively if I would say that decision Matrix, like ignoring the operating things like it depends or some, imprecision presentation language that's also an objective assessment. I would totally Once with an obviously bad decision Matrix, right? What happens with that problem, right?
Jeb Beich: Billy. I ran it on one of those first years a second.
Philipp Meier: Okay.
Jeb Beich: Here's what yeah, I considered your Matrix a good Matrix,…
Philipp Meier: Yeah, yeah.
Jeb Beich: and I think that it's interesting to get your feedback because That I got I believe much more useful output on a decision Matrix, which wasn't as thorough as yours.
Philipp Meier: I see. Okay. Yeah,…
Jeb Beich: I think yours is a really good example of sort…
Philipp Meier: yeah. I mean a little bit when you would say,…
Jeb Beich: where it's less useful. So there's
Philipp Meier: this is kind of like general advice a little bit reads to me when you have an assessment and in a school in school, right and the teacher needs to write something about your essay. It's A+ but they will not just say A Plus. Thank you. They will give you A+ and still will ride one page on. What you can improve right?
Jeb Beich: Reason, So the reason why I think that's good for you and you feel free to disagree with me here.
Philipp Meier: Yeah.
Jeb Beich: But this is my thought.
Philipp Meier: Yeah. Yeah.
Philipp Meier: What did you script say on that or the prompt say on that? Okay.
Philipp Meier: sure but it's interesting to see how it reacts because every tool you need to know where you can use it or not, right whether it's able to cut. But it yeah.
Philipp Meier: totally yeah, yeah.
Philipp Meier: totally yeah, yeah.
Jeb Beich: Right, you need to know who your customer is. Right? And I think you're a customer of this and…
Philipp Meier: The closure core team for sure will not and…
Jeb Beich: I think something like this would be useful and…
Philipp Meier: to avoid tragedies should not circulate their decision matrixes,…
Jeb Beich: this is a theory specifically because you are circulating this DM to other people so having it really dialed in a plus precise.
Philipp Meier: right just because it's not meant to and it's all the context is missing.
Jeb Beich: It's just making your own life easier.
Philipp Meier: It's awesome. If you send a TV team doing a show on…
Jeb Beich: When you talk to Florian or when you talk to now…
Philipp Meier: how close your court team is developing their magic sauce,…
Jeb Beich: if it was just me and you going back and forth. I don't think will be as useful. But …
Philipp Meier: right? Because it will add to the story of magic software Wizards,…
Jeb Beich: That's my theory. Is that maybe and Dinner circulating it. Yeah.
Philipp Meier: right and it's not like that.
Jeb Beich: Right, so there's different. Yeah.
Philipp Meier: wonder.
Philipp Meier: If I'm pretty sure that's good or possible with more specific problems, right regarding specific criteria in decision matrixes, is there some obviously in Clarity in language or that low high is typically not a very good criteria or answer to criteria maybe more concrete find criteria and evaluations where you think or where we should use something like an objective measurement or give me suggestions where we can replace something which is more categorical with something objective right High cost efficiency. that can mean everything right?
Philipp Meier: Maybe that's the thing. And I also think that everything that a problem like that will build is mostly a recommendation and a suggestion And only in few cases, it's something very concrete we say yeah, this is a spelling mistake, Yeah, but this film is still valuable. just to give you something like a virtual rubber ducky or something who's a little bit socratically mugging you right just for saying hey, technically you should not say medium high and…
00:55:00
Jeb Beich: Yes, absolutely.
Philipp Meier: low because what doesn't mean but then you would just Yeah,…
Jeb Beich: Yes. Absolutely agree with that.
Philipp Meier: that's true. Yeah, if it's overwhelming unexpectedly over bombings like you go to a doctor for checkout when the doctor is everything is okay, but
Jeb Beich: Yeah, this is about recommendations and suggestions.
Philipp Meier: This is one thing we found in the ultrasonic which we believe doesn't belong there.
Jeb Beich: Yeah.
Philipp Meier: It's like Yeah.
Jeb Beich: Yeah, and it's not a mugging if you ask for it either, that's the point is this is optional thing.
Philipp Meier: Yeah.
Jeb Beich: Yeah.
Philipp Meier: Yeah, yeah.
Jeb Beich: Good point good point Billy that the general so you gave me this analogy of the doctor the lawyer when you're being questioned,…
Philipp Meier: stop with it with the horrible stuff first, please and Yeah. What the dangerous stuff right start with the dangerous stuff like I mean,…
Jeb Beich: but now you're getting me the same analogy of visiting the doctor when you're getting advice on your decision Matrix.
Philipp Meier: I mean when you have an infection in your mouth something really horrible,…
Jeb Beich: And your point is that you for someone And maybe a fraction of this advice is helpful without all of it.
Philipp Meier: which needs to be taken care of right away. Maybe the doctor after sending that message to you and…
Jeb Beich: It could be overwhelming to get the big list of everything.
Philipp Meier: you're already okay**. Do I need some surgery and all that and…
Jeb Beich: That's cool.
Philipp Meier: maybe whatever maybe it's not the best time also…
Jeb Beich: Start with the horrible stuff first. Okay, and…
Philipp Meier: …
Jeb Beich: then ask them…
Philipp Meier: talk about General oral hygiene and…
Jeb Beich: if they want. more yeah.
Philipp Meier: flossing and what kind of toothbrush to use because you're already completely saturated with the information about you need a surgery, That's what I mean, right?
Philipp Meier: Okay, I'm the master of wrong examples, but you know what, I mean, right? Yeah.
Philipp Meier: Yeah.
Jeb Beich: Okay. All right. I'm not gonna
Philipp Meier: Totally totally but I'm totally loving your creativity and…
Jeb Beich: I changed no, they're good. I did I'm gonna show you something later.
Philipp Meier: applying AI to problems…
Jeb Beich: I'm taking your examples and actually started to keep track of them.
Philipp Meier: which is I think it's not a stretch. It's very very practical.
Jeb Beich: But listen, I'm gonna stop now and…
Philipp Meier: It's hard to make it efficient and…
Jeb Beich: I'm actually gonna show you the presentation I make afterwards.
Philipp Meier: and helpful sure now that I'm
Philipp Meier: At that we talk,…
Jeb Beich: I don't want to buy us any feedback right now based on showing you prompt. Thanks.
Philipp Meier: my wife is a physical therapist and she needs to ride those therapy reports. For example, she's barely paid for that. It's really not she's only writing them when the doctor asked for that and only because she knows that's important for the patient.
Jeb Beich: Someone is useful feedback,…
Philipp Meier: So the doctors can decide,…
Jeb Beich: right? Yeah.
Philipp Meier: what's the progress whether to continue PT or not, but she's really not paid for that. it's ridiculous like a one dollar fifty right for something…
Jeb Beich: that's
Philipp Meier: where you sit down for 15 minutes alone to fix the spelling mistake. So I told her hey, I will create you a template. We just take all the basic things like continue therapy patient compliance is low high or important things to know and…
Jeb Beich: You should. This is a place where?
Philipp Meier: whatever is the status, but that we talk about that. I'm like
Philipp Meier: You could do that…
Jeb Beich: Yeah. This is a good.
Philipp Meier: but actually doctors will be confused about that.
Jeb Beich: Yeah, it's a good place for that.
Philipp Meier: They don't want to have a mechanics report where they take off engine oil changed, But that could be input just to create a therapy report.
Jeb Beich: Mm-hmm
Philipp Meier: With a certain tone and sentiment you could also if there's low patient compliance you don't write to write that literally right? You want to write in a way that the doctor understands it but the patient is not offended right and stuff like that. It could totally imagine that would be useful. Yeah, that would be a way just to.
Jeb Beich: Yeah.
Philipp Meier: Save a lot of time you still had to do all the due diligence.
Jeb Beich: you can change the tone. Yeah.
Philipp Meier: You need to verify the report that there's no nonsense in it. But British you could use tax templates of course,…
Jeb Beich: right
Philipp Meier: but AI is able to create some pros with reads nicely right instead of somebody or…
Jeb Beich: You'll have a lot of fun doing that project. Yeah.
Philipp Meier: just taking off. mark
Philipp Meier: yeah.
01:00:00
Philipp Meier: totally Yeah, good. See you later mama.
Jeb Beich: totally and it has a lot of general knowledge and provides a lot of useful suggestions on. topics that are really well understood these types of things and you can tune it quite a bit in terms of what actual feedback you want I gotta go. Thanks, man. Thank you. All right.
Meeting ended after 01:00:09 👋

