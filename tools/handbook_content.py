"""Contenido del manual metodológico (en inglés). Lo usa tools/handbook.py."""

P = "assets/photos/"

# Cada capítulo: (clave, etiqueta, título, foto, posición, texto de apertura, html del cuerpo)

def box(title, body, kind="tip"):
    return f'<aside class="box {kind}"><p class="box-t">{title}</p>{body}</aside>'

def checks(items):
    return '<ul class="chk">' + "".join(f"<li><span class='cb'></span><span>{i}</span></li>" for i in items) + "</ul>"

def bullets(items):
    return "<ul class='bul'>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

def lines(n=4, label=""):
    l = f"<p class='fl'>{label}</p>" if label else ""
    return l + "<div class='lines'>" + "<i></i>" * n + "</div>"

def field(label, w="100%"):
    return f"<div class='field' style='width:{w}'><span>{label}</span><i></i></div>"

def table(head, rows, cls=""):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f"<table class='tb {cls}'><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table>"

# ------------------------------------------------------------------ front matter

ABOUT = f"""
<p class="lead">Eurolibrary was an Erasmus+ project that took young people across five countries to build a living library made of people. Between June and November 2025, five mobilities by train, on foot, by bike, by ferry and by campervan brought together participants from Bulgaria, Greece, the Netherlands, Portugal and Spain. In each one, they ran Human Libraries with local communities, in town squares, on islands, in cafés and in schools.</p>
<p>This handbook is the project's legacy for the people who come next: youth workers, teachers, librarians, community organisers and young people who want to run a Human Library of their own. It brings together what the method is, what we learned by running twenty of them, and a set of ready to use materials.</p>
<div class="stats">
  <div><b>5</b><span>mobilities in 5 countries</span></div>
  <div><b>20</b><span>Human Library events</span></div>
  <div><b>125</b><span>Human Books in the catalogue</span></div>
  <div><b>120+</b><span>young participants</span></div>
</div>
<h2>How to use this handbook</h2>
<p>You do not need to read it from start to finish. Choose the way in that suits you.</p>
{table(["If you want to", "Start with"], [
  ["Understand what a Human Library is", "Part 1, chapters 1 to 4"],
  ["Plan your first event from scratch", "Part 2, chapters 5 to 9, then the checklist in Annex A1"],
  ["Run the day itself", "Part 3, chapters 10 and 11, and the run sheet in Annex A2"],
  ["Evaluate and share what happened", "Part 4, chapters 12 to 14"],
  ["Copy forms, scripts and templates", "The annexes, A1 to A17: print them or adapt them"],
])}
<p class="small">Every annex page is designed to be copied. Adapt the wording to your language, your audience and your venue, and have your own organisation review the consent texts before you use them.</p>
<h2>The Eurolibrary partnership</h2>
<p>Eurolibrary was coordinated by Asociación Xeración (Spain), together with AltVenturers, De Kracht van Sport (the Netherlands), The Future Now Association (Bulgaria) and GAIA Alentejo (Portugal). It was funded by the Erasmus+ programme of the European Union.</p>
"""

# ------------------------------------------------------------------ PART 1

CH1 = f"""
<h2>The idea in one minute</h2>
<p>A Human Library works like an ordinary library, with one difference: the books are people. A reader chooses a title from a catalogue, and the librarian introduces them to the person behind it. For about twenty minutes they talk, one to one or in a very small group. Then the book goes back to the shelf.</p>
<p>The people who volunteer as books share a part of their life that others often judge or misunderstand: migration, a mental health challenge, a disability, an unusual job or a life choice that raises eyebrows. Readers come with curiosity, ask honest questions and listen. Nobody has to agree. The aim is to understand.</p>
{box("In one sentence", "<p>A Human Library is a safe, structured space where people who would not normally meet can have an honest conversation, so that a real person replaces a stereotype.</p>", "key")}
<h2>Where it comes from</h2>
<p>The first Human Library took place in 2000 at a music festival in Denmark, promoted by an association working against discrimination. Festival goers could sit down between concerts with people who were usually labelled by others. The idea spread. In 2003 the Council of Europe backed the method, and Human Libraries have since been organised on every continent. The Human Library Organisation, which grew from that first event, shares guidance at humanlibrary.org.</p>
<h2>What it is for</h2>
{bullets([
 "<b>Reducing prejudice.</b> Research on contact between groups, which began with the psychologist Gordon Allport in the 1950s, suggests that meaningful, respectful contact can change attitudes. A Human Library creates that kind of contact in a short time.",
 "<b>Building empathy.</b> Hearing a person's story in the first person is different from reading about a group.",
 "<b>Giving a voice.</b> Books decide what to share, and being heard is empowering.",
 "<b>Training listening.</b> Readers practise asking without judging, and books telling without persuading.",
])}
<h2>What it is not</h2>
{table(["A Human Library is not", "Because"], [
  ["A debate", "Books do not defend a position or try to convince anyone. They share their own story."],
  ["A lecture or a panel", "Conversations are one to one, or at most two readers per book, so they stay personal."],
  ["Therapy or counselling", "Books choose what to share and are never expected to disclose more than they want. Nobody is treated."],
  ["A performance or a zoo", "Books are guests with rights, not exhibits. Readers are not spectators."],
])}
"""

CH2 = f"""
<h2>Five roles</h2>
<p>Every Human Library is built by people in five roles. In a small event one person can combine two roles, but a book should never also be the librarian during the same loan.</p>
<div class="roles">
 <div class="role"><i>1</i><h3>Books</h3><p>People who share a part of their story. They write a short review for the catalogue, speak in the first person and keep the right to decline any question or end a loan at any moment. They do not need to be experts or to represent a whole group: they speak only for themselves.</p></div>
 <div class="role"><i>2</i><h3>Readers</h3><p>Members of the public who borrow a book. They register, accept the rules, listen with curiosity and ask honest, respectful questions. A reader can borrow several books during the event.</p></div>
 <div class="role"><i>3</i><h3>Librarians</h3><p>The organisers and masters of ceremonies. They build the spaces, welcome readers, explain the rules, hand out the catalogue, introduce reader and book, time each loan, keep the loan record and look after everyone's comfort.</p></div>
 <div class="role"><i>4</i><h3>Dictionaries</h3><p>Interpreters for loans where book and reader do not share a language, or where one of them is deaf. They keep the conversation flowing and do not add opinions.</p></div>
 <div class="role"><i>5</i><h3>Promoters</h3><p>The team that invites people in. In a public space nobody is guaranteed to walk by, so promoters explain the idea in a playful way: flash mobs, free hugs, paper arrows or human arrows. They can also run activities for children while parents read.</p></div>
</div>
{box("Rule of thumb for team size", "<p>Plan at least six books for a small library, so readers have a real choice. Keep one librarian for every three or four books, with one person on reception, and one or two promoters if the venue is in a public place. In Eurolibrary, groups of around twenty five participants split into books, librarians and promoters, and swapped roles between events.</p>", "tip")}
<h2>Three spaces</h2>
<p>A reader walks through three spaces in order.</p>
{{FLOORPLAN}}
{table(["Space", "What it is for", "What it needs"], [
  ["Reception", "Welcome, rules, registration and the catalogue.", "A desk, the printed catalogue and a QR code, a sign in sheet and pens, the rules on a poster."],
  ["Bookshelf", "Where books wait between loans, away from the readers.", "Chairs, water and snacks, a quiet corner, out of earshot of the reading tables."],
  ["Reading space", "Where loans happen.", "Tables for two or three people, armchairs or chairs, paper tablecloths for notes, coffee and snacks, a timer."],
])}
"""

CH3 = f"""
<p class="lead">From the moment a reader arrives to the moment the book goes back to the shelf, every loan follows the same eight steps. Keeping the sequence predictable is what makes the unpredictable part, the conversation, feel safe.</p>
{table(["", "Step", "What happens", "Who"], [
  ["1", "Welcome", "The reader arrives at reception. The librarian greets them and explains the rules. The reader registers and accepts them.", "Librarian"],
  ["2", "Browse", "The reader receives the catalogue: every book with a title and a short review. They choose the story they want to read.", "Reader"],
  ["3", "Call the book", "The librarian goes to the bookshelf and tells the book that a reader is waiting.", "Librarian"],
  ["4", "Introduce", "The librarian introduces book and reader and walks them to a free table in the reading space.", "Librarian"],
  ["5", "Read", "The conversation begins. The book sets the boundaries and the reader asks honest questions. No more than two readers per book.", "Book, reader"],
  ["6", "Time is up", "The librarian signals when the loan is over. The conversation can end earlier. The length is fully customisable.", "Librarian"],
  ["7", "Return", "The reader thanks the book. Book and reader become available again. The reader can ask for a new loan.", "Reader"],
  ["8", "Feedback", "The librarian asks for a short evaluation and, with consent, a contact for the next events. The loan is noted.", "Librarian"],
], "steps")}
<h2>How long should a loan last?</h2>
<p>Around twenty to thirty minutes works well, and a loan should never go over thirty. It is long enough for a real conversation and short enough for a book to give several loans without getting tired. Decide the length before the event and let the librarians keep time. A conversation can always end earlier.</p>
{{TIMELINE}}
<h2>The six rules of the library</h2>
{table(["Rule", "In practice"], [
  ["Timed loans", "Around 20 to 30 minutes, never more than 30. It can end earlier."],
  ["Register first", "Readers sign in at reception, receive the instructions and accept them explicitly."],
  ["Your own story", "Books speak from the &quot;I&quot;. No generalisations, no apologies and no attempt to convince."],
  ["The right to say no", "A book can skip any question and end the loan if the conversation goes somewhere unwanted."],
  ["Two readers at most", "To keep it a conversation and not a lecture, no more than two readers per book at once."],
  ["Return it with care", "Readers hand the book back as they found it: treated with courtesy, kindness and confidentiality."],
], "rules")}
"""

CH4 = f"""
<p class="lead">The method works because people feel safe. Safety is not a side note, it is the job of the whole team. This chapter sets out the principles we followed and the practical steps behind them.</p>
<h2>Five principles</h2>
<div class="cols2">
 <div><h3>1. Voluntary and informed</h3><p>Nobody is pushed to be a book. Volunteers know what the event involves, what readers may ask and what they can refuse, before they say yes.</p></div>
 <div><h3>2. Control belongs to the book</h3><p>Books decide what to tell, what to skip and when to stop. Nobody has to justify a no.</p></div>
 <div><h3>3. Respect and confidentiality</h3><p>What is said in the reading space stays there. Photos, recordings and notes need explicit permission.</p></div>
 <div><h3>4. Care before, during and after</h3><p>Preparation, a librarian within sight, and a debrief afterwards: care does not end when the loan does.</p></div>
</div>
<h2>Looking after books</h2>
{bullets([
 "<b>Choose a story you can tell calmly.</b> Pick a part of your life that you have already processed enough to share. You do not need to tell everything.",
 "<b>Decide your limits in advance.</b> Write down topics you will not discuss and a phrase to use when a question is too much, such as &quot;I would rather not go there.&quot;",
 "<b>Practise with peers.</b> Telling the story aloud before the event, and hearing questions, removes most surprises.",
 "<b>Rest between loans.</b> Plan breaks and let books skip a round. Several emotional conversations in a row are tiring.",
 "<b>Debrief.</b> Offer a short conversation after the event, or small reflection groups. In Eurolibrary we formed international groups of four or five participants, a kind of project family, as people to turn to.",
])}
{box("If a story stirs up strong emotions", "<p>Pause the loan, thank the reader, and take the book to the quiet corner. Offer water and company, not advice. Remind them that they can stop for the day. Know in advance who can help and how to reach local support services if needed. A Human Library is not therapy, and organisers are not expected to act as counsellors.</p>", "care")}
<h2>Looking after readers</h2>
<p>Readers also take a risk: they might hear something that challenges them or that touches their own experience. Explain the rules clearly, remind them that they can end the loan too, and tell them where the quiet corner is. Ask them to leave their arguments at the door: curiosity is welcome, debate is not.</p>
<h2>Working with schools and young people</h2>
{bullets([
 "Agree the format with teachers beforehand, and confirm who is responsible for the students at every moment.",
 "Check national and school rules on consent. As a safe practice, ask parents or guardians for permission before photographing or recording anyone under 18.",
 "Keep groups small. Make sure that a librarian and a teacher are always within sight of the reading tables.",
 "Prepare books for the age of the audience, and agree in advance on topics that need extra care.",
])}
<h2>Data, photos and recordings</h2>
<p>This is general guidance, not legal advice. Check the rules that apply in your country and with your organisation.</p>
{bullets([
 "<b>Ask for consent and say why.</b> Explain what you will do with photos, recordings or contact details, and let people say no.",
 "<b>Collect only what you need.</b> An email address is enough to send a newsletter. Do not collect more.",
 "<b>Keep it safe and delete it.</b> Store the data securely, share it only with those who need it and delete it when it has served its purpose.",
 "<b>Never record a loan without both people's agreement.</b> Books can withdraw their consent later.",
])}
<h2>Inclusion and accessibility</h2>
{bullets([
 "Choose a venue with step free access, accessible toilets and good acoustics, and tell readers about it in advance.",
 "Offer a quiet area, and avoid very loud music.",
 "Arrange sign language interpreters or dictionaries where needed, and write the catalogue in plain language.",
 "Be careful with the words you use. Ask people how they want to be described, and avoid terms that label them.",
])}
"""

# ------------------------------------------------------------------ PART 2

CH5 = f"""
<p class="lead">Before you book a venue, decide what you want the Human Library to do and what format fits that aim. A clear purpose makes every later choice easier.</p>
<h2>Start with the purpose</h2>
<p>Answer four questions in a short planning meeting, and write the answers on one page.</p>
{table(["Question", "Example answer"], [
  ["Why are we doing this?", "To challenge prejudice about migration among young people in our town."],
  ["Who are the readers?", "Secondary school students and visitors to the town square."],
  ["Who are the books?", "Young people who have experienced migration, and who want to share their story."],
  ["What would success look like?", "Readers say they learned something new, and books feel proud and respected."],
])}
<h2>Choose a format</h2>
{table(["Format", "Best for", "Watch out for"], [
  ["Public space event", "Reaching people who would not normally attend: squares, parks, markets, festivals.", "Weather, noise and low turnout. You need promoters and a plan B."],
  ["School session", "Young audiences and curriculum links. Students are a captive but curious audience.", "Safeguarding and consent. Agree everything with teachers beforehand."],
  ["Library, cultural centre or café", "A calm, indoor setting with a built in audience.", "It can attract the already convinced. Invite new audiences on purpose."],
  ["Travelling library", "Taking the method on the road, as Eurolibrary did by train, on foot, by bike, by ferry and by campervan.", "Logistics are demanding. Keep the number of stops realistic."],
  ["Online or hybrid", "People who cannot travel. Loans take place in a video call.", "Less warmth, and security risks. Use a private link and a waiting room."],
])}
<h2>Set a timeline</h2>
<p>Allow at least six to eight weeks for a first event. The plan we used in each mobility, and a checklist version, are in chapter 9 and Annex A1. Work backwards from the event date and give every task an owner.</p>
{box("A realistic scale for a first library", "<p>Six to ten books, two to four hours of opening, one librarian for every three or four books, and one venue you already know. You can grow later. A small, well run library is better than a big chaotic one.</p>", "tip")}
<h2>Think about the budget</h2>
<p>A Human Library is inexpensive, but it is not free. Annex A16 lists typical cost lines. The main items are the venue (often free if you partner with a school or a library), printing, refreshments, signs and badges, promotion, interpretation and insurance, if required.</p>
"""

CH6 = f"""
<p class="lead">The venue shapes the atmosphere more than anything else. Readers need to feel welcome, and books need to feel protected.</p>
<h2>What to look for</h2>
{table(["Criterion", "Why it matters"], [
  ["Footfall", "In public spaces, you need people already walking by. Squares, markets, cafés and station concourses work well."],
  ["Shelter", "A roof or an indoor fallback protects you from rain, wind and heat. In Eurolibrary, rain and strong wind moved events more than once."],
  ["Acoustics and privacy", "Tables need enough distance to avoid overhearing, and the bookshelf must be out of earshot. Avoid venues with loud music."],
  ["Accessibility", "Step free access, toilets and clear signage. Tell people about it in advance."],
  ["Space for three zones", "Reception, bookshelf and reading space, with a clear route from one to the next."],
  ["Permissions", "Ask the venue owner or the municipality early. Check rules on noise, furniture, food and signs."],
])}
<h2>Setting up the three zones</h2>
{bullets([
 "<b>Reception at the entrance.</b> Visible from the street. A banner or roll up, the rules poster and the catalogue go here.",
 "<b>Bookshelf away from the tables.</b> A calm corner with chairs, water and snacks, ideally behind a screen or a wall.",
 "<b>Reading tables spread out.</b> Small tables for two or three, paper tablecloths for notes, and a number on each table so the librarian can find every loan.",
])}
<h2>A plan B for every venue</h2>
<p>Know what you will do if it rains, if the venue closes early or if almost nobody comes, and share the plan with the team. Annex A15 has a risk matrix.</p>
{box("From our events", "<p>We ran Human Libraries on trains and ferries, in squares, cafés, museums and school courtyards. The best venues were where people were already stopping: a shaded square in the evening, a café terrace, a school break. The hardest were exposed squares in strong wind.</p>", "euro")}
"""

CH7 = f"""
<p class="lead">The books are the heart of the library. Recruit them with care, prepare them well and keep them safe, and the rest of the event will take care of itself.</p>
<h2>Who can be a book?</h2>
<p>Anyone who is willing to tell a part of their story honestly and who has the emotional space to do it. Books are often people who are labelled or stereotyped, but they can also be people who have simply lived through something others rarely hear about. They do not need to be public speakers or to represent a group.</p>
<p>In Eurolibrary the books were the young participants themselves, chosen around the theme of each mobility: entrepreneurship in Bulgaria, mental health in Spain, a healthy lifestyle in the Netherlands, migration in Greece and sustainability in Portugal. Catalogues ranged from stories of overcoming anxiety to rebuilding a life in a new country, launching a first business or finding identity through sport.</p>
<h2>Recruit</h2>
{bullets([
 "Publish a call for books (Annex A3) through your organisation, social media and trusted partners.",
 "Invite directly. Many people say yes when asked personally and told what is involved.",
 "Aim for diversity of experience, background and age, so that readers have a real choice.",
 "Talk to every volunteer before accepting. Check motivation and readiness, and explain the rules.",
])}
<h2>Prepare: a two hour training</h2>
<p>A short training before the event makes books more confident. Annex A6 contains a full agenda. The core of it is:</p>
{table(["Block", "Aim"], [
  ["Welcome and expectations (15 min)", "Create trust, explain the method and answer questions."],
  ["The rules and the right to say no (15 min)", "Practise phrases to decline a question or end a loan."],
  ["Find your story (30 min)", "Choose a part of your life to share, in pairs."],
  ["Tell it and hear questions (40 min)", "Practise a five minute version and receive three honest questions."],
  ["Write the review (15 min)", "Draft the title and the short review for the catalogue."],
  ["Close and care (5 min)", "Explain the debrief and how to reach the team."],
])}
<h2>Structure a story</h2>
<p>A story told in the first person, with a simple shape, is easier to hear and to tell. A useful structure has four parts.</p>
<div class="cols2 s4">
 <div><h3>1. Before</h3><p>Where you started, and what people assumed about you.</p></div>
 <div><h3>2. The turning point</h3><p>The moment, or the choice, that changed something.</p></div>
 <div><h3>3. What happened</h3><p>What was hard, what helped and what you did.</p></div>
 <div><h3>4. What I learned</h3><p>What you would tell your younger self, or someone in the same situation.</p></div>
</div>
<h2>Write the review</h2>
<p>Every book has a title and a short review, between 50 and 150 words: the equivalent of the back cover of a book. It is the appetizer that readers skim before deciding. A good review answers these questions:</p>
{bullets([
 "How do you define yourself, and what do others say about you?",
 "Which part of your life or work do you want to talk about?",
 "Which challenges have you had to overcome, at school, at work or in your relationships?",
 "What is something surprising you have done that others might find interesting?",
])}
<p>Combine the answers into a few sentences that invite readers to know more. Use the worksheet in Annex A5.</p>
<h2>Build the catalogue</h2>
{bullets([
 "One entry per book, with a title and the review. Avoid labels that turn people into categories.",
 "Collect the entries a week before the event, as Eurolibrary did, and check them with each book.",
 "Provide a digital version with a QR code and a few printed copies. Keep the same order in both.",
 "Update the catalogue during the event if a book is unavailable. Annex A7 shows a layout.",
])}
"""

CH8 = f"""
<p class="lead">A great set of books is not enough: you also need a team that runs the library calmly and readers who come through the door.</p>
<h2>Prepare the librarians and the dictionaries</h2>
<p>Librarians are the hosts of the event. Brief them on the rules, the flow of a loan (chapter 3) and how to handle difficult moments (chapter 10). Practise a complete loan from reception to feedback, with someone playing a reader who asks a tricky question. Annex A8 gives a welcome script. Dictionaries should receive the catalogue early, so that they can prepare vocabulary.</p>
<h2>Recruit readers</h2>
<p>The most challenging task in a Human Library is to bring in enough readers. A few things help:</p>
{bullets([
 "<b>Go where people are.</b> A square, a school break, a market, a cultural festival.",
 "<b>Partner with someone who has an audience.</b> A school, a library, a youth centre or a local association can invite their members.",
 "<b>Invite personally.</b> People who are asked in person are much more likely to come than people who see a poster.",
 "<b>Promote on the day.</b> The most effective promotion is the one done at the moment of the event, by promoters who explain the idea.",
])}
<h2>Promotion that works</h2>
{table(["Channel", "Tips"], [
  ["Posters and leaflets", "Short, bright, with the place and the time, and a QR code to the catalogue. Put them where your readers already are."],
  ["Social media", "Announce a week ahead and the day before. Show faces of books who agreed to be shown, and quote a title from the catalogue."],
  ["Local media and partners", "Send a short press note to local papers, radio and municipality newsletters. Ask partners to share it."],
  ["On the day", "Promoters invite passers by. Paper arrows, signs, a roll up banner and free hugs bring people in."],
])}
{box("Playful promotion", "<p>Promotion has to be original, attractive and fun. Examples that work: flash mobs, free hugs, paper arrows or human arrows pointing to the library, a poster with a question, face painting for children while parents read, and a chalk sign on the pavement.</p>", "tip")}
<h2>Welcoming the readers</h2>
<p>Readers often arrive nervous: they are not sure what they will be asked to do. A friendly librarian, a clear explanation of the rules and a first book recommendation can turn hesitation into curiosity. Offer a few titles that match their interests, and tell them they can change their mind.</p>
<h2>Activities for the people who are not reading</h2>
<p>In a long event, not everybody is reading or being read at the same time. Plan something for the rest: games with children, promotion, short videos, a reflection corner or a wall where readers can leave a message. In Eurolibrary, participants who were not books ran games, invited passers by and filmed short clips, so that everybody had a role.</p>
"""

CH9 = f"""
<p class="lead">This chapter describes the model we followed in each of the five Eurolibrary mobilities. You can use it as it is for a multi day exchange, or take parts of it for a single event.</p>
<h2>Preparation timeline</h2>
{table(["When", "What", "Who"], [
  ["3 weeks before", "<b>Full group meeting</b> (60 to 90 minutes). Ice breakers, the project, the Human Library method and its roles, the programme and logistics. Break out into national teams and agree the date of their meeting.", "Host organisation"],
  ["2 weeks before", "<b>National group meeting</b> (1 to 2 hours, online or in person). A deeper dive into the method, ethics and storytelling structure. Help each participant choose a story and set emotional boundaries. Share drafts and give peer feedback.", "Sending organisations"],
  ["1 week before", "<b>Story submission.</b> Each organisation collects titles and short descriptions. The host compiles the catalogue, digital with a QR code and a few printed copies.", "Host and sending organisations"],
])}
<h2>During the mobility</h2>
{table(["Day", "Focus", "Details"], [
  ["Day 1", "Ice breaking and team building", "Name games, movement games, value based activities and trust building. The group co-creates agreements: respect, confidentiality, punctuality and support. Small international groups of four or five form the project family. An overview of the week."],
  ["Days 2 to 5", "The core of the project", "At least four Human Libraries, in squares, schools, libraries, community centres or other public spaces, organised with local venues and partners. Podcast recordings, social media and audiovisual support run in parallel."],
  ["Day 6", "Reflection, evaluation and closing", "Collective reflection, a brief presentation of Youthpass, feedback forms, ideas for the next mobility. The team checks the attendance lists and the recordings."],
])}
<h2>Five mobilities, five settings</h2>
{table(["Chapter", "Where and how", "Theme"], [
  ["The Balkan Express", "Bulgaria, 23 to 30 June 2025. More than 500 km by train.", "Entrepreneurship"],
  ["Buen Camino", "Spain, 26 July to 2 August 2025. On foot, more than 20 km a day.", "Mental health"],
  ["The Dutch Way", "The Netherlands, 1 to 8 September 2025. More than 150 km by bike.", "Healthy lifestyle"],
  ["Waves of Hope", "Greece, 2 to 9 October 2025. Ferries across three Cycladic islands.", "Migration"],
  ["Green on Wheels", "Portugal, 2 to 9 November 2025. A campervan road trip.", "Sustainability"],
])}
{box("What we would repeat", bullets(["Starting with ice breakers and group agreements before the first library.", "Closing the catalogue a week before the event.", "Letting participants rotate between book, librarian and promoter.", "Choosing venues where people already gather, and partnering with local schools."]), "euro")}
{box("What we would change", bullets(["Plan fewer moves and more rest. In Greece participants suggested fewer island changes or more time to recover.", "Keep a plan B for weather, especially for squares and bike or ferry routes.", "Brief local partners earlier on what readers will experience."]), "tip")}
"""

# ------------------------------------------------------------------ PART 3

CH10 = f"""
<p class="lead">The day has arrived. This chapter gives you a run of show, the roles during the event and a short guide to the moments that usually go wrong.</p>
<h2>A run of show for a three hour library</h2>
{table(["Time", "What happens"], [
  ["T minus 3 hours", "Set up the three zones, decorate, start promotion around the venue. Last meeting of the team."],
  ["T minus 1 hour", "Books arrive and meet the librarians. Catalogue check. Briefing: roles, signals and the plan B."],
  ["T minus 15 min", "Reception opens. Promoters take their places. Books settle on the bookshelf."],
  ["T plus 0", "The library opens. The librarian says a short welcome to the first readers."],
  ["Every 20 to 30 min", "A new round of loans. Books rest between rounds."],
  ["T plus 90 min", "Short break. Water, snacks, a quick check on how books feel."],
  ["T plus 2 h 30", "Last call for loans. Remind readers to leave a feedback form."],
  ["T plus 3 h", "Close. Thank everybody. Short debrief with books and librarians."],
  ["After", "Tidy up, collect forms and the loan record, and thank the venue."],
])}
<h2>Roles during the event</h2>
{table(["Role", "Main tasks on the day"], [
  ["Reception librarian", "Greets readers, explains rules, hands out the catalogue and the sign in sheet, shows the route."],
  ["Floor librarian", "Calls the book, introduces, times the loan, watches the reading tables."],
  ["Book guardian", "Stays on the bookshelf, welcomes books back, offers water and a quiet moment."],
  ["Promoter", "Invites passers by, hands out leaflets, answers questions and guides people to reception."],
  ["Dictionary", "Stays near the reception and steps in when a language is needed."],
  ["Photographer", "Takes photos only of those who agreed. Respects the reading tables."],
])}
<h2>When things go wrong</h2>
{table(["Situation", "What to do"], [
  ["Few readers arrive", "Send promoters out, move the reception closer to the street, use personal invitations. Do not rush readers."],
  ["Too many readers at once", "Create a queue with a number, offer a quick conversation with the librarian while they wait, and open a second reception if possible."],
  ["A reader asks something too personal", "The book can decline. The librarian steps in, thanks the reader and offers another book."],
  ["A reader starts to argue or to preach", "The librarian ends the loan politely and reminds the reader that the aim is to listen. Escort them out if needed."],
  ["A book becomes emotional", "Pause, offer water and the quiet corner. Do not push them to continue. Call the book guardian."],
  ["Rain, wind or heat", "Move to plan B. Cover the bookshelf first. Keep paper catalogues dry."],
  ["Noise", "Move tables away from the noise, use a quieter room, or shorten loans."],
  ["Technical problems", "Keep paper copies of the catalogue and the rules."],
])}
"""

CH11 = f"""
<p class="lead">Small, concrete tools make a big difference. In this chapter, you will find activities to build the group, a way to run a debrief and prompts for readers.</p>
<h2>Ice breakers for the team</h2>
{table(["Activity", "How it works", "Time"], [
  ["Name and gesture", "In a circle, each person says their name and does a gesture. The group repeats it.", "10 min"],
  ["Four corners", "Corners of the room stand for four answers to a question such as &quot;What kind of traveller are you?&quot;. People move and chat with their corner.", "15 min"],
  ["Common ground", "In pairs, find three things you share that are not obvious. Share them with the group.", "15 min"],
  ["Stand if", "The facilitator reads statements. People stand if they agree. Silence, then a short reflection.", "15 min"],
  ["Story circles", "In groups of four, each person tells a one minute story on a prompt. Others only listen.", "20 min"],
  ["Trust walk", "In pairs, one person leads the other, eyes closed, around the venue. Swap. Talk about trust.", "20 min"],
])}
<h2>Group agreements</h2>
<p>Start every mobility or training by agreeing the rules of the group together. Write them on a poster and keep them visible. Annex A9 gives a template. We always included respect, confidentiality, punctuality and support.</p>
<h2>Reflection groups</h2>
<p>Form small, mixed groups of four or five on the first day and keep them for the whole project. They meet each evening for twenty minutes. Rotate who guides the conversation, and keep the same simple questions.</p>
{box("Questions for a daily reflection group", bullets(["What did I see, hear or feel today?", "What surprised me?", "What was hard, and what helped?", "What do I want to remember, and what do I want to let go?", "What do I need tomorrow?"]), "tip")}
<h2>Debrief with the books</h2>
<p>After every event, give books ten to fifteen minutes with a librarian. Ask what it felt like and whether anything needs follow up.</p>
{bullets([
 "How was the experience for you?",
 "Is there a conversation you want to talk about?",
 "How did you feel when you said no, or when you wanted to say no?",
 "What would help you next time?",
])}
<h2>Prompts for readers</h2>
<p>Some readers do not know what to ask. Share a short card at the reception with open questions that help:</p>
{bullets([
 "What would you like people to know about you?",
 "What was the hardest moment, and what helped?",
 "What do people usually assume about you? What is the reality?",
 "What did you learn from this experience?",
 "What would you tell someone who is going through the same?",
])}
"""

# ------------------------------------------------------------------ PART 4

CH12 = f"""
<p class="lead">A Human Library changes minds quietly. Give yourself a way to see it, to improve and to show funders, partners and the community what happened.</p>
<h2>Decide what to measure</h2>
{table(["Aspect", "What to ask", "How"], [
  ["Participation", "How many loans, readers and books took part?", "The loan record (Annex A11) and the sign in sheet."],
  ["Reader experience", "Did readers learn something new? Did their view change?", "A short reader form (Annex A12)."],
  ["Book experience", "Did books feel safe, heard and respected?", "A debrief and a short form (Annex A13)."],
  ["Organisation", "What worked, what to change?", "A team reflection at the end of the event."],
  ["Reach", "Who heard about it?", "Social media views, local press, newsletter sign ups."],
])}
<h2>Collect simply</h2>
{bullets([
 "Keep forms short, five to seven questions, and let people answer on paper or with a QR code.",
 "Ask for consent before collecting emails, and say what you will do with them.",
 "Count what you can: loans per book, loans per hour, readers per event.",
 "Collect short quotes, with permission and signed with a first name, to illustrate the findings.",
])}
<h2>Analyse and report</h2>
<p>Do not wait. Within a week, enter the data in a simple spreadsheet, read the open answers together and note three things that worked and three to change. Share the results with your team, your partners and the books. A short one page summary is enough for a first report. Annex A12 includes a short set of questions you can adapt.</p>
{box("From our results", "<p>Participants in the Eurolibrary mobilities rated the experience between 4.2 and 5.0 out of 5 in the feedback forms. They highlighted the Human Libraries as their favourite activity, and the friendship and the sense of being listened to. They also asked for more time to rest between moves. These figures are aggregated from participant forms in each chapter, and show direction rather than a rigorous evaluation.</p>", "euro")}
<h2>Close the loop</h2>
{bullets([
 "Thank books, readers, venues and partners in person and online.",
 "Share photos, videos and podcasts with readers who agreed to receive them.",
 "Show readers what changed because of their feedback.",
 "Invite readers and books to the next event.",
])}
"""

CH13 = f"""
<p class="lead">A Human Library lasts a few hours, but the stories can last longer. Eurolibrary recorded participants' stories as a podcast series, People of EU, so that they could reach people who could not attend.</p>
<h2>Why record</h2>
<p>A recorded story reaches people beyond the venue and gives books a lasting voice, in their own words.</p>
<h2>What you need</h2>
{bullets([
 "A quiet room with soft furnishings. Avoid echo, traffic and air conditioning noise.",
 "A decent microphone and headphones (a smartphone with a clip on microphone is enough to start), and a person who handles the technology so that the speaker can focus on the story.",
 "Slots of fifteen to twenty minutes per story, with a sign up sheet.",
 "A written consent form, signed before the recording (Annex A14).",
])}
<h2>Record with care</h2>
{bullets([
 "Give speakers the questions in advance, and let them change or skip any of them.",
 "Do not force a dramatic story. Short and honest is better than long and rehearsed.",
 "Let people listen to the recording and ask for changes before it is published.",
 "Agree on how they want to be named: first name, a nickname or anonymous.",
])}
<h2>Edit and publish</h2>
<p>Keep the edit light: remove long pauses and noise, and keep the speaker's voice. Add a clear title and a short description, a single sentence about what the story is about. Publish on the platforms your audience uses, and tell books when and where it is available. The People of EU series is available on Spotify, and can be embedded on a website.</p>
{box("A format that worked", "<p>Each People of EU episode is a short story of three to ten minutes, told by the person who lived it, with a short title and a one sentence description beginning &quot;A story about&quot;.</p>", "euro")}
"""

CH14 = f"""
<p class="lead">Some of what we learned fits on a page. Here is what we would tell ourselves before the first Human Library, and answers to the questions organisers ask most often.</p>
<h2>Ten lessons</h2>
<ol class="num">
 <li><b>Start small and do it well.</b> Six books and one librarian per three or four books is enough for a good first event.</li>
 <li><b>Prepare the books.</b> Time spent on stories, limits and reviews pays off during the event.</li>
 <li><b>Make safety visible.</b> Rules on a poster, a librarian within sight, and a quiet corner.</li>
 <li><b>Build the group first.</b> Ice breakers and agreements on the first day made every Human Library better.</li>
 <li><b>Go where people already are.</b> Squares at the right time, schools at break time, a café terrace.</li>
 <li><b>Promote on the day.</b> Posters help, but a promoter who explains the idea fills the library.</li>
 <li><b>Give everyone a role.</b> Books, librarians, promoters, filmmakers: nobody should feel like a spectator.</li>
 <li><b>Have a plan B.</b> Weather and noise are the usual suspects.</li>
 <li><b>Rest.</b> Books and librarians need breaks and a debrief.</li>
 <li><b>Follow up.</b> Thank, share and show what changed.</li>
</ol>
<h2>Frequently asked questions</h2>
<div class="faqs">
 <div><h3>Do I have to belong to a minority to be a book?</h3><p>No. Books are people with a story to share, often because they are labelled or stereotyped, but also because they have lived something others rarely hear. What matters is that they are willing to speak honestly about their own experience.</p></div>
 <div><h3>How many books do we need?</h3><p>At least six for a small library, so readers have a real choice. With more books, each one has time to rest between loans.</p></div>
 <div><h3>What if nobody comes?</h3><p>Send promoters out, move reception closer to the street, invite people personally and be patient. A few good loans are better than many rushed ones.</p></div>
 <div><h3>Can we run it in a school?</h3><p>Yes. Eurolibrary held sessions in local schools, where students heard stories straight from the people who lived them. Agree the format with the teachers, keep groups small and always keep a librarian nearby.</p></div>
 <div><h3>What about languages?</h3><p>Choose a shared language for the event. If a book and a reader do not share one, or one of them is deaf, bring in a dictionary.</p></div>
 <div><h3>Can we record or photograph?</h3><p>Only with the consent of everyone who appears or speaks. Never record a loan without both people's agreement.</p></div>
 <div><h3>Can we use the name Human Library?</h3><p>The Human Library Organisation shares resources and guidance at humanlibrary.org. Check their advice on how to present your event before you announce it.</p></div>
</div>
"""

# ------------------------------------------------------------------ ANNEXES (materials)

def annex(code, title, intro, body):
    return code, title, intro, body

A = []

A.append(annex("A1", "Planning checklist", "Use it as a master list. Give each task an owner and a date.", f"""
{table(["When", "Task", "Owner", "Done"], [
  ["3 weeks before", "Full group meeting with ice breakers, the method and the logistics", "", "&#9744;"],
  ["3 weeks before", "Choose venues and ask permission", "", "&#9744;"],
  ["3 weeks before", "Decide whether events are open or by invitation", "", "&#9744;"],
  ["2 weeks before", "Team meetings: ethics, storytelling structure, boundaries", "", "&#9744;"],
  ["2 weeks before", "Form working groups: books, librarians, promoters, dictionaries", "", "&#9744;"],
  ["1 week before", "Collect titles and short reviews; compile the catalogue", "", "&#9744;"],
  ["1 week before", "Print catalogue, signs, posters, badges; prepare the QR code", "", "&#9744;"],
  ["1 week before", "Train books and librarians", "", "&#9744;"],
  ["Day before", "Promote online and in mailing lists; run a general trial", "", "&#9744;"],
  ["Day before", "Gather materials; organise snacks and drinks", "", "&#9744;"],
  ["3 hours before", "Set up the three spaces; start promotion; last team meeting", "", "&#9744;"],
  ["3 hours before", "Check consent for photos and for collecting emails", "", "&#9744;"],
  ["During", "Register readers, time loans, keep the loan record, rest the books", "", "&#9744;"],
  ["After", "Thank everyone; collect feedback; share photos and podcasts", "", "&#9744;"],
  ["After", "Write down what worked and what to change", "", "&#9744;"],
], "plan")}
"""))

A.append(annex("A2", "Event run sheet", "Print one per event and keep it at reception.", f"""
<div class="grid2">{field("Event")}{field("Date")}{field("Venue")}{field("Opening hours")}{field("Lead librarian")}{field("Phone")}</div>
{table(["Time", "What", "Who", "Notes"], [["", "Set up the three zones", "", ""], ["", "Books arrive and are briefed", "", ""], ["", "Reception opens", "", ""], ["", "Round 1 of loans", "", ""], ["", "Round 2 of loans", "", ""], ["", "Break", "", ""], ["", "Round 3 of loans", "", ""], ["", "Last call", "", ""], ["", "Close and debrief", "", ""]], "plan")}
<h3>Plan B</h3>{lines(3)}
<h3>Emergency contacts</h3>{lines(2)}
"""))

A.append(annex("A3", "Call for books", "A text you can copy into an email, a poster or a social media post.", f"""
<div class="paper"><h3>Do you have a story to tell?</h3>
<p>We are organising a Human Library on [date] in [place]. In a Human Library, people are the books, and visitors borrow them for a conversation of about twenty minutes. We are looking for [number] people who are willing to share a part of their life that others often judge or misunderstand.</p>
<p>You do not need to be a speaker. You decide what you share, and you can say no to any question and stop a conversation at any time. We will train you, help you write a short review and be with you throughout.</p>
<p><b>What we offer:</b> training, support, a debrief afterwards, and a space to be listened to.<br><b>What we ask:</b> an honest conversation about your own experience, and about two hours of your time on [date].</p>
<p><b>To join:</b> write to [email] before [date] with a few lines about the story you would like to share.</p></div>
<h3>Tips</h3>{bullets(["Name the theme, if the library has one.", "Say what is involved and what is not expected.", "Make clear that participation is voluntary and confidential.", "Invite directly the people you think may be interested."])}
"""))

A.append(annex("A4", "Book profile form", "For books to fill in before they are accepted. Keep it confidential.", f"""
<div class="grid2">{field("First name")}{field("Contact (email or phone)")}</div>
{field("Title of the story, if you have one")}
{lines(1, "In a few lines, what would you like to share?")}{lines(3)}
{lines(1, "Is there anything you would not like to talk about?")}{lines(2)}
{lines(1, "Is there anything you need to feel comfortable (language, quiet breaks, accessibility)?")}{lines(2)}
<h3>I confirm that</h3>
{checks(["I take part voluntarily and understand that I can say no to any question and stop a conversation at any time.", "I will share only my own story, in the first person.", "I have read and understood the rules of the library."])}
<div class="grid2">{field("Signature")}{field("Date")}</div>
"""))

A.append(annex("A5", "Book review worksheet", "Write the title and a review between 50 and 150 words. Keep it short and honest.", f"""
{field("Working title")}
<h3>Think about it</h3>
{lines(1, "How do you define yourself? What do others say about you?")}{lines(2)}
{lines(1, "Which part of your life or work do you want to talk about?")}{lines(2)}
{lines(1, "Which challenges have you had to overcome?")}{lines(2)}
{lines(1, "What is something surprising you have done?")}{lines(2)}
<h3>Your review (50 to 150 words)</h3>{lines(7)}
<p class="small">Check: it speaks in the first person, it makes people curious, it does not give away the whole story, it does not blame anybody and it does not label you.</p>
"""))

A.append(annex("A6", "Training agenda for books", "A two hour session to run one to two weeks before the event.", f"""
{table(["Time", "Activity", "Method", "Materials"], [
  ["0:00", "Welcome and expectations", "Circle, name and one word for how you feel", "Flipchart"],
  ["0:15", "The method and the rules", "Short presentation, questions", "Rules poster"],
  ["0:30", "The right to say no", "Practise phrases in pairs: &quot;I would rather not go there.&quot;", "Cards with phrases"],
  ["0:45", "Find your story", "In pairs, choose a part of your life using the questions of Annex A5", "Worksheet A5"],
  ["1:00", "Tell it, hear questions", "Trios: five minute story, three honest questions, feedback", "Timer"],
  ["1:40", "Write the review", "Individual writing, then read aloud to a partner", "Worksheet A5"],
  ["1:55", "Close and care", "How to reach the team, the debrief, the quiet corner", "Contacts"],
], "plan")}
<h3>Facilitator notes</h3>
{bullets(["Make clear that nobody has to tell a story they are not ready to tell.", "Give people the option to join in silence, or to pass.", "Watch the energy: shorten the exercises if the group is tired.", "Close with a round: one thing I take with me."])}
"""))

A.append(annex("A7", "Catalogue template", "One entry per book. Replace the placeholder text with each book's title and review.", f"""
<div class="cat">
 <div class="cat-e"><span class="no">1</span><h4>Title of the book</h4><p>A short review of 50 to 150 words in the first person, written by the book. It invites readers to learn more without telling the whole story.</p><p class="tags">Language: English &middot; Available: all day</p></div>
 <div class="cat-e"><span class="no">2</span><h4>Title of the book</h4><p>A short review of 50 to 150 words in the first person, written by the book. It invites readers to learn more without telling the whole story.</p><p class="tags">Language: English &middot; Available: from 11:00</p></div>
 <div class="cat-e"><span class="no">3</span><h4>Title of the book</h4><p>A short review of 50 to 150 words in the first person, written by the book. It invites readers to learn more without telling the whole story.</p><p class="tags">Language: English and [language] &middot; Available: all day</p></div>
</div>
<h3>Catalogue checklist</h3>
{checks(["Each entry has a title and a review approved by the book.", "No labels or categories that reduce a person to a group.", "The same order in the printed and the digital versions.", "A QR code on every printed copy.", "A note at the top with the rules of the library.", "A way to mark books that are not available."])}
"""))

A.append(annex("A8", "Librarian welcome script", "Read it, adapt it and say it in your own words.", f"""
<div class="paper"><h3>Welcome to the Human Library</h3>
<p>Hello, and welcome. In this library, the books are people. Each one has a title and a short description in this catalogue. You choose a book, and you borrow it for a conversation of about twenty minutes.</p>
<p><b>The rules are simple.</b> You can ask honest questions, and the book decides what to answer. A book can skip any question and end the loan at any time. Please listen with curiosity, without judgement. What is said at the table stays at the table. We ask you not to take photos or recordings of the conversation. We will tell you when your time is up.</p>
<p>Would you like to register here? Then have a look at the catalogue, and tell me which story you would like to read. If you are not sure, I will be glad to help you choose.</p></div>
<h3>Introducing a book and a reader</h3>
<div class="paper"><p>[Reader's first name], this is [Book's first name], who shares the story "[Title]". [Book], this is [Reader], who would like to hear your story. You have about twenty minutes. I will let you know when there are five minutes left. If you need anything, wave to me.</p></div>
<h3>When time is up</h3>
<div class="paper"><p>I am sorry to interrupt, but your time is up. [Reader], would you like to thank [Book]? [Book], thank you. Please come to reception to tell us how it was, or choose another book.</p></div>
"""))

A.append(annex("A9", "Group agreements", "Co create them with the group on the first day. Write them on a poster and keep them visible.", f"""
<div class="paper poster"><h3>Our agreements</h3>
<ol class="num">
<li><b>Respect.</b> We listen to each other without interrupting or judging.</li>
<li><b>Confidentiality.</b> What is shared here stays here, unless the person says otherwise.</li>
<li><b>Punctuality.</b> We start and finish on time. Our time is a gift to the group.</li>
<li><b>Support.</b> We look after each other and ask for help when we need it.</li>
<li><b>The right to pass.</b> Everyone can say no, or take a break, without explaining.</li>
<li><b>Curiosity.</b> We ask questions to understand, not to prove somebody wrong.</li>
</ol></div>
<h3>Our own agreements</h3>{lines(5)}
<h3>How to use them</h3>
{bullets(["Read them aloud on the first day and ask whether anyone wants to add something.", "Ask everyone to say yes in their own way: a word, a nod or a signature.", "Return to them when the group is tired or when tensions arise.", "Keep them on the wall of the venue during events."])}
"""))

A.append(annex("A10", "Reader registration card", "Print one per reader, or turn it into a QR form.", f"""
<div class="paper"><h3>Welcome to the Human Library</h3>
<p>Please read the rules and sign below to borrow a book.</p>
{checks(["I will listen with curiosity and respect.", "I understand that a book can decline any question and end the loan.", "I will not record, photograph or share what I hear without permission.", "What is said at the table stays at the table.", "I will return the book with courtesy and kindness."])}
<div class="grid2">{field("First name")}{field("Signature")}</div>
<p class="small">Optional: I would like to receive news of future events at this email address. I agree that it will be used only for this purpose, and I can withdraw my consent at any time.</p>
{field("Email")}
</div>
<h3>Keep the cards</h3><p>Store the cards securely, share them only with the team and delete them after the event, unless people agreed to be contacted.</p>
"""))

A.append(annex("A11", "Loan record sheet", "Keep one at reception. It helps you balance the loans and report.", f"""
{table(["Time", "Book", "Reader(s)", "Table", "Length (min)", "Notes"], [["", "", "", "", "", ""]] * 14, "plan rec")}
<p class="small">At the end of the day: total loans ______ &nbsp; readers ______ &nbsp; books ______ &nbsp; most borrowed ______</p>
"""))

A.append(annex("A12", "Reader feedback form", "Keep it short. Five to seven questions are enough.", f"""
<div class="paper">
<h3>Tell us about your conversation</h3>
<p>1. How did you find the experience?&nbsp;&nbsp; &#9734; &#9734; &#9734; &#9734; &#9734;</p>
<p>2. Did you learn something new? &nbsp;&nbsp; &#9744; A lot &nbsp; &#9744; Some &nbsp; &#9744; Not really</p>
<p>3. Has your view of something changed? &nbsp;&nbsp; &#9744; Yes &nbsp; &#9744; A little &nbsp; &#9744; No</p>
<p>4. Did you feel respected and safe? &nbsp;&nbsp; &#9744; Yes &nbsp; &#9744; Mostly &nbsp; &#9744; No</p>
{lines(1, "5. What will you remember from your conversation?")}{lines(2)}
{lines(1, "6. What would you change?")}{lines(2)}
<p>7. Would you come to another Human Library? &nbsp;&nbsp; &#9744; Yes &nbsp; &#9744; Maybe &nbsp; &#9744; No</p>
<p class="small">May we quote you? &#9744; Yes, with my first name &nbsp; &#9744; Yes, anonymously &nbsp; &#9744; No</p></div>
<h3>Reading the answers</h3>{bullets(["Count the answers to the closed questions and report them as simple percentages.", "Read the open answers together as a team and choose three quotes.", "Do not publish a quote without permission.", "Write down what you will change for the next event."])}
"""))

A.append(annex("A13", "Book debrief form", "Offer it at the end of the event, with a short conversation.", f"""
<div class="paper">
<h3>How was it for you?</h3>
<p>1. How do you feel after the event?&nbsp;&nbsp; &#9744; Great &nbsp; &#9744; Good &nbsp; &#9744; Tired &nbsp; &#9744; Mixed &nbsp; &#9744; Not well</p>
<p>2. Did you feel safe and respected? &nbsp;&nbsp; &#9744; Always &nbsp; &#9744; Mostly &nbsp; &#9744; Sometimes &nbsp; &#9744; No</p>
<p>3. Did you use your right to say no? &nbsp;&nbsp; &#9744; Yes &nbsp; &#9744; No &nbsp; &#9744; I wanted to but did not</p>
{lines(1, "4. Is there a conversation you would like to talk about?")}{lines(2)}
{lines(1, "5. What helped you? What would help next time?")}{lines(2)}
{lines(1, "6. Would you like follow up from the team?")}{lines(2)}
</div>
<h3>For the librarian</h3>{bullets(["Thank the book and acknowledge their courage.", "Ask how they are. Listen, without fixing.", "If someone is distressed, do not leave them alone, and offer to put them in touch with a support service.", "Note anything that needs to change, and share it with the team."])}
"""))

A.append(annex("A14", "Consent templates", "Starting points for you to adapt. Have your organisation or a legal adviser review them for your country.", f"""
<div class="paper"><h3>Consent for photos and video</h3>
<p>I agree that [organisation] may take photos and videos of me at [event] on [date], and use them for [purposes, for example the project website, social media and reports]. I understand that I can withdraw my consent at any time by writing to [email], and that the material will then be removed from future use.</p>
<div class="grid2">{field("Name")}{field("Signature")}</div>
<p class="small">For people under 18, a parent or guardian must also sign: ____________________</p></div>
<div class="paper"><h3>Consent for audio recording and publication</h3>
<p>I agree to record my story for [project]. I understand that I can listen to the recording and ask for changes before it is published, that I can choose how I am named, and that I can withdraw my consent by writing to [email].</p>
<p>I would like to be named: &#9744; with my first name &nbsp; &#9744; with a nickname: __________ &nbsp; &#9744; anonymously</p>
<div class="grid2">{field("Name")}{field("Signature")}</div></div>
<div class="paper"><h3>Consent for contact details</h3>
<p>I agree that [organisation] may use my email address to send me news about [project] and invitations to events. It will not share it with others, and I can unsubscribe at any time.</p>
{field("Email")}</div>
"""))

A.append(annex("A15", "Risk and contingency matrix", "Complete it with your team before the event and share it.", f"""
{table(["Risk", "Likelihood", "Impact", "What we do"], [
  ["Rain, wind or heat", "", "", ""],
  ["Few or no readers", "", "", ""],
  ["Too many readers at once", "", "", ""],
  ["A book is overwhelmed", "", "", ""],
  ["A reader behaves badly", "", "", ""],
  ["A book cancels at the last moment", "", "", ""],
  ["Noise or an interruption", "", "", ""],
  ["Technical failure", "", "", ""],
  ["A language barrier", "", "", ""],
  ["", "", "", ""],
], "plan risk")}
<p class="small">Rate likelihood and impact from 1 (low) to 3 (high). Plan a response for every risk with a total of 4 or more.</p>
"""))

A.append(annex("A16", "Budget checklist", "Typical cost lines for a first Human Library. Many can be free with the right partner.", f"""
{table(["Item", "Notes", "Estimate"], [
  ["Venue", "Often free with a school, library or municipality", ""],
  ["Printing", "Catalogue, posters, leaflets, forms, badges", ""],
  ["Signs and banner", "Roll up, paper arrows, table numbers", ""],
  ["Refreshments", "Coffee, water, snacks for books, librarians and readers", ""],
  ["Furniture and decoration", "Paper tablecloths, flipcharts, markers, balloons", ""],
  ["Promotion", "Online ads are optional. Posters and personal invitations work best", ""],
  ["Interpretation", "Dictionaries, sign language", ""],
  ["Audio and video", "Microphone, headphones, storage", ""],
  ["Insurance and permits", "If required by the venue or the municipality", ""],
  ["Thank you gifts", "Small tokens for books and partners", ""],
  ["Contingency", "Ten percent of the total", ""],
], "plan")}
"""))

A.append(annex("A17", "Promotion kit", "Texts you can adapt for posters, social media and press.", f"""
<div class="paper"><h3>Poster text</h3><p><b>Borrow a person, not a book.</b><br>Human Library &middot; [date] &middot; [time] &middot; [place]<br>Free. No booking. Twenty minutes of honest conversation.<br>[logo, QR code]</p></div>
<div class="paper"><h3>Social media post</h3><p>What happens when you truly listen to someone's story? On [date], [place] opens a Human Library: people are the books, and you can borrow one for a conversation. Come with curiosity, leave with a new perspective. Free for everyone. #HumanLibrary #Eurolibrary</p></div>
<div class="paper"><h3>Press note, first lines</h3><p>[Organisation] will open a Human Library on [date] in [place], where visitors can borrow a person for a twenty minute conversation. Volunteers will share personal stories about [theme], with the aim of challenging prejudice and building empathy. The event is free and open to everyone.</p></div>
<h3>Hashtags and tags</h3><p>Use a short event hashtag and tag your partners. Add the Erasmus+ and EU funding acknowledgements if your event is funded by the programme.</p>
"""))

RESOURCES = f"""
<p class="lead">Where to learn more, and where to find the people who can help.</p>
<h2>The method</h2>
{table(["Resource", "What it offers"], [
  ["humanlibrary.org", "The Human Library Organisation: history of the method, guidance for organisers and a network. Check their advice on use of the name."],
  ["Council of Europe, &quot;Don't judge a book by its cover! The Living Library organiser's guide&quot;", "A detailed guide to organising a Living Library, published by the Council of Europe in the 2000s. Check the Council of Europe website for the latest edition."],
])}
<h2>Erasmus+ and youth work</h2>
{table(["Resource", "What it offers"], [
  ["Erasmus+ Programme Guide and the European Commission's Erasmus+ website", "Funding rules and priorities for projects like Eurolibrary."],
  ["Youthpass", "The recognition tool for learning in Erasmus+ projects. Participants of Eurolibrary were introduced to it on the last day."],
])}
<h2>Eurolibrary</h2>
{table(["Resource", "What it offers"], [
  ["eurolibrary.eu", "The five mobilities, photos, results and this handbook."],
  ["People of EU, on Spotify", "The podcast of stories recorded in the project."],
  ["Instagram: @eurolibrary", "Photos and videos from the five mobilities."],
])}
<h2>Glossary</h2>
{table(["Term", "Meaning"], [
  ["Book", "A person who shares a part of their story with a reader."],
  ["Reader", "A member of the public who borrows a book."],
  ["Librarian", "An organiser who welcomes readers, introduces books and keeps time."],
  ["Dictionary", "An interpreter who helps book and reader communicate."],
  ["Promoter", "A volunteer who invites people into the library."],
  ["Catalogue", "The list of books with a title and a short review."],
  ["Reflection group", "A small, stable group that meets to reflect on the experience."],
])}
"""


# ------------------------------------------------------------------ cierres de capítulo (ideas clave, citas y fotos)

def take(items):
    return box("Key ideas", bullets(items), "key")


def quote(text, name):
    return f'<blockquote class="q"><p>&ldquo;{text}&rdquo;</p><cite>{name}, participant</cite></blockquote>'


def photos(files, cls=""):
    return '<div class="photos ' + cls + '">' + "".join(
        f'<div style="background-image:url(\'@PH@{f}\')"></div>' for f in files) + "</div>"


CH1 += quote("People deserve to be heard.", "Óscar") + take([
    "A Human Library is a structured space for conversation where people are the books.",
    "Loans are short, voluntary and safe: the book decides what to share.",
    "The aim is to understand, not to agree or to convince.",
    "It works in squares, schools, libraries, cafés and even on the road.",
]) + photos(["human-library-table.jpg", "spain-hl-talk.jpg"])

CH2 += take([
    "Five roles: books, readers, librarians, dictionaries and promoters.",
    "Three spaces, in this order: reception, bookshelf and reading space.",
    "Start with at least six books and one librarian for every three or four books.",
])

CH3 += take([
    "Eight steps, always in the same order, from welcome to feedback.",
    "Twenty to thirty minutes, never more than thirty.",
    "The six rules go on a poster at reception.",
]) + photos(["spain-hl-conversation.jpg", "greece-lunch.jpg"])

CH4 += take([
    "Participation is voluntary and informed, and control stays with the book.",
    "Prepare, supervise and debrief: care does not stop when the loan does.",
    "Ask for consent for photos, recordings and contact details, and keep data to a minimum.",
    "Plan accessibility and the safety of young people from the start.",
])

CH5 += take([
    "Define the purpose and the audience before choosing a format.",
    "Start small: six to ten books, a few hours and a venue you know.",
    "Work backwards from the date and give every task an owner.",
]) + photos(["portugal-van.jpg", "netherlands-cyclists.jpg"])

CH6 += take([
    "Choose places where people already stop, with shelter and a plan B.",
    "Three zones with a clear route, and a bookshelf out of earshot.",
    "Check accessibility and permissions early.",
]) + photos(["greece-lunch.jpg", "netherlands-dinner.jpg"])

CH7 += quote("Hearing so many stories of overcoming big issues was very inspiring!", "Alessandro") + take([
    "Anyone willing to tell a part of their story honestly can be a book.",
    "A two hour training builds confidence: limits, the right to say no and a short practice.",
    "Every book has a title and a review of 50 to 150 words, checked with the book.",
    "Close the catalogue a week before the event.",
])

CH8 += quote("A powerful human experience of connection, growth, and shared vulnerability.", "Beatriz") + take([
    "Brief and rehearse the librarians with a full practice loan.",
    "Invite personally, and promote on the day: promoters fill the library.",
    "Give everyone a role, including people who are not reading.",
]) + photos(["greece-school-group.jpg", "greece-circle-dance.jpg"])

CH9 += photos(["bulgaria-sofia.jpg", "spain-obradoiro-group.jpg", "netherlands-ferry.jpg", "greece-sifnos.jpg", "portugal-van.jpg"], "five") + take([
    "Three weeks, two weeks, one week: whole group, national teams, catalogue.",
    "Day one is for the group, days two to five for the libraries, day six for reflection.",
    "Weather, rest and early briefing of partners were our main lessons.",
])

CH10 += take([
    "Set up three hours before, brief the team one hour before, open on time.",
    "Time every loan, let books rest and keep a record.",
    "Have an answer ready for the usual problems: weather, noise, a difficult reader.",
])

CH11 += quote("It was a fun, dynamic trip focussed on connection.", "Rashel") + take([
    "Build the group first, with ice breakers and shared agreements.",
    "Meet each day in small reflection groups.",
    "Always debrief with the books after an event.",
])

CH12 += take([
    "Decide what to measure before the event, and keep forms short.",
    "Count loans, collect quotes with permission and read the open answers as a team.",
    "Thank, share and show what changed because of the feedback.",
]) + photos(["greece-ferry-circle.jpg", "spain-hug.jpg"])

CH14 += quote("The friendship lasted and the connection we had has been unbelievable.", "Christian") + photos(["greece-ios-group.jpg", "netherlands-grass.jpg"])
