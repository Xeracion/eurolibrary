#!/usr/bin/env python3
"""Genera las páginas estáticas de Eurolibrary.

Uso:
  python3 tools/build.py                 escribe las páginas en la raíz del repo
  python3 tools/build.py --inline DIR    escribe una copia con el CSS incrustado en DIR
                                         (para publicarla como artefacto)
"""
import html
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TYPEFORM = "https://xeracion.typeform.com/go2eurolibrary"
EMAIL = "info@xeracion.org"

CHAPTERS = [
    "bulgaria", "spain", "netherlands", "greece", "portugal",
]

# ---------------------------------------------------------------- contenido

CH = {
    "bulgaria": dict(
        file="bulgaria.html", no=1, name="The Balkan Express", country="Bulgaria",
        mode="by train", mode_short="Train", dates="23 to 30 June 2025", topic="Entrepreneurship",
        hero="photos/bulgaria-hero.jpg", hero_alt="A blue regional train on the tracks",
        subtitle="A journey by train through stories and startups",
        tagline="Like an Interrail, but for entrepreneurs.",
        intro=[
            "We crossed Bulgaria by rail with young entrepreneurs who wanted to share what it takes to build something of their own. Along the way they told their stories to local people in four Human Libraries.",
        ],
        profile_h="Young entrepreneurs",
        profile=[
            "Freelancers, brand builders, owners of social media businesses, people who had just wrapped up a startup idea and were asking themselves what comes next. All of them ready to share a train adventure with like minded peers from all over Europe.",
        ],
        criteria=[
            "Aged between 18 and 30",
            "Fluent English, minimum B2",
            "Enough stamina for a non stop programme on the go",
            "Legal resident in Bulgaria, Greece, the Netherlands, Portugal or Spain",
        ],
        facts=[("Dates", "23 to 30 June 2025"), ("Travel", "More than 500 km by train"),
               ("Topic", "Entrepreneurship"), ("Format", "4 Human Libraries")],
        route_h="Corner to corner of the country",
        route_p="More than 500 km by train with the international Eurolibrary team, with stops in four cities.",
        stops=[
            ("23 to 24 June", "Sofia", "Roman history, Orthodox churches and edgy street art, with mountain views and a young, lively energy.", "photos/bulgaria-sofia.jpg", "Panorama of Sofia at sunset"),
            ("25 June", "Plovdiv", "Europe's oldest continuously inhabited city, where ancient Roman theatres meet colourful creative quarters.", "photos/bulgaria-plovdiv.jpg", "A cobbled street in Plovdiv"),
            ("26 June", "Stara Zagora", "Modern and green with ancient roots: Roman ruins, the Neolithic Museum and the quiet charm of central Bulgaria.", "photos/bulgaria-stara-zagora.jpg", "View over Stara Zagora"),
            ("27 to 29 June", "Varna", "The pearl of the Black Sea, with golden beaches, Roman baths and lively nights. Summer, culture and sea in one place.", "photos/bulgaria-varna.jpg", "The beach at Varna"),
        ],
        side=None,
    ),
    "spain": dict(
        file="spain.html", no=2, name="Buen Camino", country="Spain",
        mode="on foot", mode_short="On foot", dates="26 July to 2 August 2025", topic="Mental health",
        hero="photos/spain-hero.jpg", hero_alt="A Camino de Santiago waymarker with a yellow arrow",
        subtitle="An intense journey about mental health",
        tagline="A pilgrimage to the inner self.",
        intro=[
            "We walked the English Way of the Camino de Santiago, an ancient pathway to Santiago, to talk about mental health with the people of Spain. Participants shared their personal stories in four Human Libraries along the route.",
        ],
        profile_h="Young people connected with mental health",
        profile=[
            "People who had experienced or overcome anxiety, depression, burnout, trauma or other mental health challenges, and who were ready to speak up and connect through storytelling.",
            "The only requirement on the inside: walk, share and listen with an open heart.",
        ],
        criteria=[
            "Aged between 18 and 30",
            "Fluent English, minimum B2",
            "Enough stamina to walk more than 20 km a day",
            "Legal resident in Bulgaria, Greece, the Netherlands, Portugal or Spain",
        ],
        facts=[("Dates", "26 July to 2 August 2025"), ("Travel", "On foot, 20+ km a day"),
               ("Topic", "Mental health"), ("Format", "4 Human Libraries")],
        route_h="Five stops on the English Way",
        route_p="From the Atlantic coast to Santiago de Compostela, one stage at a time.",
        stops=[
            ("26 to 27 July", "Pontedeume", "A lovely medieval town to get ready, mind and legs, before the first steps away from the Atlantic.", "photos/spain-pontedeume.jpg", "A street in Pontedeume"),
            ("28 July", "Betanzos", "Said by many to serve the best tortilla in the world. Tasted with locals while celebrating the first public event in its stone streets.", "photos/spain-betanzos.jpg", "Church and square in Betanzos"),
            ("29 July", "Ordes", "A modern town halfway along the route, and the place to rest, reflect and recharge for the final kilometres.", "photos/spain-ordes.jpg", "Town hall of Ordes"),
            ("30 July", "Sigüeiro", "The last stop before Santiago, with parks, forest and a river, and friendly locals keen to listen to the stories.", "photos/spain-sigueiro.jpg", "A stone bridge near Sigüeiro"),
            ("31 July to 2 August", "Santiago de Compostela", "The magical city hosted the last and most important part of the trip: time to digest everything collected along the Way.", "photos/spain-santiago.jpg", "A scallop shell hanging from a backpack"),
        ],
        side=None,
    ),
    "netherlands": dict(
        file="netherlands.html", no=3, name="The Dutch Way", country="The Netherlands",
        mode="by bike", mode_short="By bike", dates="1 to 8 September 2025", topic="Healthy lifestyle",
        hero="photos/netherlands-hero.jpg", hero_alt="A group of cyclists on a path in the Netherlands",
        subtitle="A journey by bike through stories about a healthy lifestyle",
        tagline="Pedal through Friesland, inspire with your lifestyle.",
        intro=[
            "We cycled across the northern Dutch landscapes with young people who love healthy living. Some had built a wellness brand, some promoted mental wellbeing, some coached others, and some were simply passionate about living in balance.",
            "Four unique events let them tell their stories, meet local communities and show what healthy living can mean: movement, nutrition, rest and connection.",
        ],
        profile_h="Young cyclists",
        profile=[
            "People passionate about a healthy lifestyle, physically, mentally and socially: lifestyle coaches, wellness creators, yoga teachers, recipe makers, or people on their own way to feeling fit, strong and well.",
            "A chance to meet like minded people from across Europe, swap experiences, get inspired and recharge, all while moving through nature.",
        ],
        criteria=[
            "Aged between 18 and 30",
            "Fluent English, minimum B2",
            "Enough stamina for a non stop programme on the go",
            "Legal resident in Bulgaria, Greece, the Netherlands, Portugal or Spain",
        ],
        facts=[("Dates", "1 to 8 September 2025"), ("Travel", "More than 150 km by bike"),
               ("Topic", "Healthy lifestyle"), ("Format", "4 public events")],
        route_h="Across the whole province",
        route_p="More than 150 km by bike through Friesland with the international Eurolibrary team.",
        stops=[
            ("1 September", "Leeuwarden", "Historic canals, bold street art and Frisian pride. Open skies, cosy cafés and a creative, down to earth vibe.", "photos/netherlands-leeuwarden.jpg", "A canal in Leeuwarden"),
            ("1 to 3 September", "Sint Annaparochie", "A quiet village with big stories: poetic landscapes, local pride and the roots of Rembrandt's love story. Calm meets curiosity.", "photos/netherlands-annaparochie.jpg", "A boat on a canal near Sint Annaparochie"),
            ("3 to 5 September", "Terschelling", "Where sea meets sky: windswept beaches, endless bike paths and a rhythm made of nature, freedom and inspiration.", "photos/netherlands-terschelling.jpg", "The island of Terschelling"),
            ("5 to 8 September", "Goingarijp", "Tucked between lakes and meadows, a place to slow down and discover Friesland on the water. A hidden gem for nature and sailing lovers.", "photos/netherlands-goingarijp.jpg", "Aerial view of Goingarijp"),
        ],
        side=("photos/netherlands-bike.jpg", "A cycling path along a lake in Friesland"),
    ),
    "greece": dict(
        file="greece.html", no=4, name="Waves of Hope", country="Greece",
        mode="by ferry", mode_short="By ferry", dates="2 to 9 October 2025", topic="Migration",
        hero="photos/greece-hero.jpg", hero_alt="A ferry sailing past a Cycladic island",
        subtitle="A journey by ferry through stories about migration",
        tagline="No borders. Just islands.",
        intro=[
            "We hopped between three Cycladic islands, sharing our stories with local islanders and, above all, with local school students.",
            "Four Human Library events gave participants the chance to talk with strangers, meet local communities and inspire others with their life stories about migration.",
        ],
        profile_h="Young people connected with migration",
        profile=[
            "People who had lived through migration, by choice, necessity or circumstance. Those who had crossed borders, left home behind or built a life in a new place.",
            "An invitation to speak up and connect through storytelling, to change places often, and to share and listen with an open heart.",
        ],
        criteria=[
            "Aged between 18 and 30",
            "Fluent English, minimum B2",
            "Able to pack light: just a backpack, because accommodation changed constantly",
            "Legal resident in Bulgaria, Greece, the Netherlands, Portugal or Spain",
        ],
        facts=[("Dates", "2 to 9 October 2025"), ("Travel", "Ferries across 3 Cycladic islands"),
               ("Topic", "Migration"), ("Format", "4 Human Libraries, with local schools")],
        route_h="Island hopping, step by step",
        route_p="The project closed where it began, in the port of Piraeus.",
        stops=[
            ("2 October", "Piraeus, Athens", "A night in a hotel close to the port, then an early start to catch the ferry to Ios.", "photos/greece-piraeus.jpg", "The port of Piraeus"),
            ("3 to 5 October", "Ios", "After an eight hour ferry, the first island. The group got to know each other, introduced the project and ran the first Human Library.", "photos/greece-ios.jpg", "A Cycladic island coast at dusk"),
            ("5 to 7 October", "Folegandros", "Time to prepare and visit a local school, and to organise the second Human Library in the Chora, the main square.", "photos/greece-folegandros.jpg", "Whitewashed steps on a Greek island"),
            ("7 to 8 October", "Sifnos", "A three hour ferry ride to share stories on board, then a second school visit and the last local event.", "photos/greece-sifnos.jpg", "A blue domed church in the Cyclades"),
            ("8 to 9 October", "Piraeus, Athens", "The last ferry from Sifnos brought the group back to the port and the same accommodation as the first night. 9 October was departures day.", "photos/greece-window.jpg", "A window opening onto the sea"),
        ],
        side=None,
    ),
    "portugal": dict(
        file="portugal.html", no=5, name="Green on Wheels", country="Portugal",
        mode="by campervan", mode_short="By campervan", dates="2 to 9 November 2025", topic="Sustainability",
        hero="photos/portugal-hero.jpg", hero_alt="Campervans driving along the coast of southern Portugal",
        subtitle="A journey by campervan through stories about eco friendly lifestyles",
        tagline="Vanlife for environmentally friendly lifestyles.",
        intro=[
            "We took a campervan road trip through the south of Portugal. Four stops, four Human Library events, and one big theme: stories about protecting the environment and living in an eco friendly, minimalist way.",
        ],
        profile_h="Young people connected to eco friendly lifestyles",
        profile=[
            "People who live with appreciation and concern for nature and the environment, and for whom ecology is a present topic in everyday life.",
            "An invitation to speak up, share, inspire and connect with others through storytelling.",
        ],
        criteria=[
            "Aged between 18 and 30",
            "Fluent English, minimum B2",
            "Enough stamina for six intense days on the road",
            "Legal resident in Bulgaria, Greece, the Netherlands, Portugal or Spain",
        ],
        facts=[("Dates", "2 to 9 November 2025"), ("Travel", "Campervan road trip"),
               ("Topic", "Sustainability and eco living"), ("Format", "4 Human Libraries")],
        route_h="From Faro to the west coast and back",
        route_p="A route across the south of Portugal, from the Algarve shore inland and up the southwest coast.",
        stops=[
            ("2 to 3 November", "Faro", "A youth hostel in the city centre to get to know each other and prepare for the road, plus the first Human Library as the trip hit the road.", "photos/portugal-faro.jpg", "The marina in Faro at dusk"),
            ("4 to 5 November", "Santa Clara a Velha", "From the south coast inland, to a culturally rich village with beautiful landscapes. The first night on the road and the second Human Library.", "photos/portugal-santa-clara.jpg", "View over Santa Clara a Velha"),
            ("5 to 6 November", "Odemira", "The southwest shore, a visit to an agroecological project and the third event.", "photos/portugal-odemira.jpg", "A beach near Odemira"),
            ("6 to 7 November", "São Luís", "A lively village where social and ecological projects are growing, and the setting for the final event and a celebration of the journey.", "photos/portugal-sao-luis.jpg", "Hills around São Luís"),
            ("8 to 9 November", "Faro", "The project finished where it started, with time to reflect on and celebrate the whole experience.", None, ""),
        ],
        side=("photos/portugal-van.jpg", "A person looking out of a vintage campervan"),
    ),
}

# Resultados verificados en los informes del proyecto (informe interno de noviembre 2025,
# informe de diseminación de octubre 2025, hoja de valoración de Bulgaria y catálogo de Spain).
BASE = [("25", "Young participants"), ("4", "Human Library events")]
RESULTS = {
    "bulgaria": dict(
        stats=BASE + [("4.0 of 5", "Average project rating in the participant survey"),
                      ("4 of 5", "Respondents who picked a Human Library as their favourite activity")],
        note="Survey based on 5 responses.",
        worked=["The Human Library on the train, which participants singled out as a highlight.",
                "The mix of backgrounds and professions in the group, and the sense of connection it created."],
        learned=["A heat wave made the programme tough. Participants suggested later start times for events, more breaks and more water and snacks.",
                 "They also asked for more time at the start to get to know each other's stories before organising events together."],
        quotes=["Inspiring.", "A powerful human experience of connection, growth, and shared vulnerability."],
    ),
    "spain": dict(
        stats=BASE + [("22", "Human Books in the catalogue"), ("5", "Countries represented in the catalogue")],
        note="",
        worked=["A shared catalogue of personal stories on mental health, built by participants before the walk and used to prepare each Human Library."],
        learned=[],
        quotes=[],
    ),
    "netherlands": dict(
        stats=BASE,
        note="",
        worked=["Four public events held along the whole route through Friesland."],
        learned=["Rain and wind complicated the logistics. The team found alternatives that kept participants safe and the events impactful."],
        quotes=[],
    ),
    "greece": dict(
        stats=BASE,
        note="",
        worked=["Human Library events held in unusual places, including on board a ferry, and in local schools."],
        learned=[],
        quotes=[],
    ),
    "portugal": dict(
        stats=BASE,
        note="",
        worked=["Four Human Library events spread along a campervan route across the south of Portugal."],
        learned=[],
        quotes=[],
    ),
}

NAV_MOB = [
    ("bulgaria", "Balkan Express, Bulgaria"),
    ("spain", "Buen Camino, Spain"),
    ("netherlands", "The Dutch Way, Netherlands"),
    ("greece", "Waves of Hope, Greece"),
    ("portugal", "Green on Wheels, Portugal"),
]

EU_DISCLAIMER = ("Funded by the European Union. Views and opinions expressed are however those of the author(s) only "
                 "and do not necessarily reflect those of the European Union or the European Education and Culture "
                 "Executive Agency (EACEA). Neither the European Union nor EACEA can be held responsible for them.")

# ---------------------------------------------------------------- plantillas


def e(s):
    return html.escape(s, quote=True)


def head(title, desc):
    return f"""<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<!--CSS-->"""


def nav(active):
    def cur(k):
        return ' aria-current="page"' if k == active else ""
    mob = "\n".join(
        f'          <a href="{CH[k]["file"]}"{cur(k)}>{e(t)}</a>' for k, t in NAV_MOB)
    mob_active = ' aria-current="page"' if active in CHAPTERS else ""
    return f"""<header class="nav" id="nav">
  <div class="wrap">
    <a href="index.html" aria-label="Eurolibrary home"><img src="assets/logo-ink.svg" alt="Eurolibrary"></a>
    <button class="menu-toggle" aria-expanded="false" aria-controls="menu">Menu</button>
    <ul id="menu">
      <li><a href="index.html"{cur("home")}>Home</a></li>
      <li><a href="about.html"{cur("about")}>About</a></li>
      <li class="dd">
        <a href="index.html#destinations"{mob_active}>Mobilities</a>
        <div class="dd-menu">
{mob}
        </div>
      </li>
      <li><a href="human-library.html"{cur("hl")}>Human library</a></li>
      <li><a class="btn btn-dark" href="contact.html"{cur("contact")}>Contact</a></li>
    </ul>
  </div>
</header>"""


def footer():
    links = "".join(
        f'<li><a href="{f}">{t}</a></li>' for f, t in [
            ("index.html", "Home"), ("about.html", "About"), ("human-library.html", "Human library"),
            ("contact.html", "Contact")] + [(CH[k]["file"], CH[k]["name"]) for k in CHAPTERS])
    return f"""<footer>
  <div class="wrap">
    <img class="eu" src="assets/eu-funded.png" alt="Funded by the European Union" style="background:var(--ink);padding:8px 12px;border-radius:8px">
    <div class="meta">
      <ul class="links">{links}</ul>
      <p>{e(EU_DISCLAIMER)}</p>
    </div>
    <p class="copy">Copyright © 2026 Eurolibrary. Project completed in 2025.</p>
  </div>
</footer>"""


SCRIPT = """<script>
  var nav=document.getElementById('nav'),t=nav.querySelector('.menu-toggle');
  t.addEventListener('click',function(){var o=nav.classList.toggle('open');t.setAttribute('aria-expanded',o)});
  if(!matchMedia('(prefers-reduced-motion: reduce)').matches&&'IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){
      if(!e.isIntersecting)return;io.unobserve(e.target);
      var el=e.target,to=+el.dataset.to,p=el.dataset.prefix||'',x=el.dataset.suffix||'',s=performance.now();
      (function f(n){var k=Math.min((n-s)/1500,1);el.textContent=p+Math.round(to*k).toLocaleString('en-GB')+x;if(k<1)requestAnimationFrame(f)})(s);
    })},{threshold:.6});
    document.querySelectorAll('[data-to]').forEach(function(el){io.observe(el)});
  }
  var form=document.getElementById('contact-form');
  if(form){
    form.addEventListener('submit',function(ev){
      ev.preventDefault();
      var n=document.getElementById('f-name').value.trim(),m=document.getElementById('f-email').value.trim(),b=document.getElementById('f-msg').value.trim();
      var body=encodeURIComponent(b+'\\n\\n'+n+(m?' ('+m+')':''));
      var note=document.getElementById('form-status');
      note.textContent='Your email app should open with the message ready. If it does not, write to """ + EMAIL + """.';
      window.location.href='mailto:""" + EMAIL + """?subject='+encodeURIComponent('Message from the Eurolibrary website')+'&body='+body;
    });
    var cp=document.getElementById('copy-email');
    if(cp){cp.addEventListener('click',function(){
      var done=function(){cp.textContent='Copied'};
      if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText('""" + EMAIL + """').then(done,function(){});}
    })}
  }
</script>"""


def page(active, title, desc, body):
    return f"""<!doctype html>
<html lang="en">
<head>
{head(title, desc)}
</head>
<body>

{nav(active)}

<main>
{body}
</main>

{footer()}

{SCRIPT}
</body>
</html>
"""


def counters(items):
    out = []
    for to, prefix, suffix, label in items:
        shown = f"{prefix}{to:,}{suffix}"
        out.append(
            f'<div class="counter"><b data-to="{to}" data-prefix="{prefix}" data-suffix="{suffix}">{shown}</b><span>{e(label)}</span></div>')
    return "\n        ".join(out)


def stats_block(items, cls="counters four"):
    return "".join(
        f'<div class="counter"><b>{e(v)}</b><span>{e(l)}</span></div>' for v, l in items)


# ---------------------------------------------------------------- páginas


def home():
    tickets = "\n".join(
        f'        <a class="ticket" href="{CH[k]["file"]}"><small>Chapter {CH[k]["no"]}, {CH[k]["mode"]}</small><strong>{e(CH[k]["country"])}</strong></a>'
        for k in CHAPTERS)
    summaries = {
        "bulgaria": "More than 500 km by rail with young entrepreneurs and changemakers, who told their stories in four Human Libraries.",
        "spain": "Walking the English Way of the Camino de Santiago to talk about mental health, with four Human Libraries along the route.",
        "netherlands": "More than 150 km by bike across Friesland to share personal stories about healthy living in four public events.",
        "greece": "Three Cycladic islands by ferry, with Human Library events for local communities and school students, all around migration.",
        "portugal": "A campervan road trip across the south of Portugal, with four Human Library events about sustainability and eco living.",
    }
    cards = []
    for k in CHAPTERS:
        c = CH[k]
        cards.append(f"""        <article class="card">
          <figure><img src="assets/{c['hero']}" alt="{e(c['hero_alt'])}" width="1000" height="838"><span class="no">Chapter {c['no']}</span></figure>
          <div class="body">
            <span class="country">{e(c['country'])}, {c['mode']}</span>
            <h3 class="display h3">{e(c['name'])}</h3>
            <span class="dates">{c['dates']}</span>
            <p>{summaries[k]}</p>
            <span class="tag">{c['topic']}</span>
            <div class="status"><span>Completed</span><a href="{c['file']}">Read the chapter</a></div>
          </div>
        </article>""")
    body = f"""  <div class="hero">
    <div class="wrap">
      <span class="eyebrow">An Erasmus+ project, completed in 2025</span>
      <h1 class="display h1">5 countries, 5 topics,<br>5 ways to move.</h1>
      <p class="lead">We took young people across Europe by train, on foot, by bike, by ferry and by campervan, and turned their stories into a living library. The trip is over. The stories keep going.</p>
      <div class="cta">
        <a class="btn btn-primary" href="#destinations">Explore the five chapters</a>
        <a class="btn btn-ghost" href="human-library.html">See how the Human Library works</a>
      </div>
      <p class="note">All five mobilities are completed and applications are closed. This site is the project record.</p>

      <div class="ticket-row" aria-label="The five chapters at a glance">
{tickets}
      </div>
    </div>
  </div>

  <section>
    <div class="wrap concept">
      <div>
        <span class="eyebrow">A journey beyond borders</span>
        <h2 class="display h2">The concept</h2>
        <p class="lead">At Eurolibrary we bet on two things: a story can <strong>change a life</strong>, and a journey can <strong>unite a continent</strong>. So we travelled green across the EU to build a <strong>living library</strong> made of people, not books.</p>
        <ul class="voices">
          <li><span>01</span>Real voices.</li>
          <li><span>02</span>Real experiences.</li>
          <li><span>03</span>Real connections.</li>
        </ul>
      </div>
      <div class="stack" aria-hidden="true">
        <img src="assets/photos/spain-hero.jpg" alt="">
        <img src="assets/photos/netherlands-hero.jpg" alt="">
        <img src="assets/photos/greece-hero.jpg" alt="">
      </div>
    </div>
  </section>

  <section id="destinations" style="padding-top:0">
    <div class="wrap">
      <div class="section-head">
        <span class="eyebrow">The five chapters</span>
        <h2 class="display h2">Five chapters, five ways to travel</h2>
        <p class="lead muted">Each mobility paired one green way of moving with one topic that matters to young Europeans. Here is what each chapter was about.</p>
      </div>
      <div class="cards">
{chr(10).join(cards)}
      </div>
    </div>
  </section>

  <section style="padding-top:0">
    <div class="wrap">
      <div class="join">
        <span class="eyebrow">Listen, share, inspire</span>
        <h2 class="display h2">Want to know more?</h2>
        <p class="lead">Reviewing the project, curious about our method or thinking about a collaboration? We are happy to talk.</p>
        <a class="btn btn-primary" href="contact.html">Get in touch</a>
      </div>
    </div>
  </section>

  <section class="leitmotiv">
    <div class="wrap">
      <span class="eyebrow">Our leitmotiv</span>
      <h2 class="display h2">This was never just a project. It was an adventure and a celebration of empathy, sustainability and European identity.</h2>

      <div class="counters">
        {counters([(5, "", "", "Mobilities"), (120, "+", "", "Participants"), (150, "+", "", "Videos, podcasts and reels")])}
      </div>

      <div class="pillars">
        <div class="pillar">
          <i>01</i>
          <h3 class="display h3">Discovering Europe the wild way</h3>
          <p>Five corners of the continent, five intense travelling exchanges. Each one used a different kind of green travel to bring our stories to local communities.</p>
        </div>
        <div class="pillar">
          <i>02</i>
          <h3 class="display h3">The most international group</h3>
          <p>Every trip brought together young people from five countries who had a lot to say about Europe's biggest challenges.</p>
        </div>
        <div class="pillar">
          <i>03</i>
          <h3 class="display h3">Cool content</h3>
          <p>We documented everything on the way in short clips on our socials, and our participants' stories found a home in our podcast.</p>
        </div>
      </div>
    </div>
  </section>"""
    return page("home", "Eurolibrary home",
                "An Erasmus+ project that took young people across five countries to build a living library made of people.", body)


def about():
    body = f"""  <div class="page-hero split">
    <div class="wrap">
      <div>
        <span class="eyebrow">Mobility and stories, since 2022</span>
        <h1 class="display h1">Plenty of Erasmus+ projects. None quite like this one.</h1>
        <p class="lead">Eurolibrary bridges cultural gaps by putting young people face to face with the communities they travel through. The result is more understanding, more empathy and lasting relationships, plus real tools to push back against discrimination and promote inclusion.</p>
      </div>
      <div class="polaroid"><img src="assets/photos/about-banner.jpg" alt="Two participants with a Eurolibrary roll up banner" style="aspect-ratio:3/3.6"></div>
    </div>
  </div>

  <section style="padding-top:32px">
    <div class="wrap">
      <div class="section-head" style="margin-bottom:32px">
        <span class="eyebrow">Our commitment to cultural connection</span>
        <h2 class="display h2">What the earlier editions delivered</h2>
        <p class="lead muted">Figures from the Spain edition in 2022 and the Greece edition in 2023.</p>
      </div>
      <div class="counters four" style="margin:0">
        {counters([(2, "", "", "Successful projects"), (50, "+", "", "Participants"), (1500, "+", " km", "Around Greece and Spain"), (98, "", "%", "Participant satisfaction")])}
      </div>
    </div>
  </section>

  <section>
    <div class="wrap two-col">
      <div>
        <span class="eyebrow">Our story</span>
        <h2 class="display h2">How Eurolibrary evolved</h2>
        <p class="lead">Eurolibrary was born in 2021 from an Erasmus+ partnership between NGOs from Spain, Portugal, Bulgaria, the Netherlands and Greece.</p>
        <p>We started with one question: how do we get young Europeans to engage with each other in a meaningful way? The answer grew into a platform for cultural exchange and community connection, with a real impact on participants' lives.</p>
      </div>
      <div class="photo-row"><figure><img src="assets/photos/about-classroom.jpg" alt="A participant presenting to a class of students"></figure>
        <figure><img src="assets/photos/human-library-talk.jpg" alt="Two people talking during a Human Library"></figure></div>
    </div>
  </section>

  <section style="padding-top:0">
    <div class="wrap">
      <div class="section-head" style="margin-bottom:32px">
        <span class="eyebrow">Where we came from</span>
        <h2 class="display h2">Our editions so far</h2>
      </div>
      <ul class="timeline-years">
        <li><b>2021</b><span>Eurolibrary is founded through an Erasmus+ partnership of five NGOs.</span></li>
        <li><b>2022</b><span>First edition, in Spain, in October.</span></li>
        <li><b>2023</b><span>Second edition, in Greece, in October.</span></li>
        <li><b>2025</b><span>Five chapters in five countries, from June to November.</span></li>
      </ul>
    </div>
  </section>

  <section style="padding-top:0">
    <div class="wrap">
      <div class="section-head">
        <span class="eyebrow">Why it matters</span>
        <h2 class="display h2">How the project connects with Erasmus+ priorities</h2>
        <p class="lead muted">Four ideas run through every chapter.</p>
      </div>
      <div class="grid-4">
        <div class="pillar"><h3 class="display h3">Inclusion and diversity</h3><p>The Human Library gives a voice to marginalised and underrepresented young people, and brings together participants from five countries.</p></div>
        <div class="pillar"><h3 class="display h3">Green mobility</h3><p>Train, feet, bikes, ferries and a shared campervan. How we travelled was part of the message.</p></div>
        <div class="pillar"><h3 class="display h3">Civic engagement</h3><p>Public events in local communities and schools, where young people start conversations that challenge prejudice.</p></div>
        <div class="pillar"><h3 class="display h3">Digital storytelling</h3><p>More than 150 videos, podcasts and reels carried the stories beyond the places we visited.</p></div>
      </div>
    </div>
  </section>

  <section style="padding-top:0">
    <div class="wrap">
      <div class="join">
        <span class="eyebrow">Listen, share, inspire</span>
        <h2 class="display h2">See the five chapters</h2>
        <p class="lead">Five countries, five topics and five ways to move. Pick a chapter and follow the route.</p>
        <a class="btn btn-primary" href="index.html#destinations">Explore the chapters</a>
      </div>
    </div>
  </section>"""
    return page("about", "About Eurolibrary",
                "The story of Eurolibrary: an Erasmus+ partnership of five NGOs that connects young people and communities through personal stories.", body)


def chapter(k):
    c = CH[k]
    order = CHAPTERS
    i = order.index(k)
    prev = CH[order[i - 1]] if i > 0 else None
    nxt = CH[order[i + 1]] if i < len(order) - 1 else None
    intro = "".join(f"<p>{e(p)}</p>" for p in c["intro"])
    profile = "".join(f"<p>{e(p)}</p>" for p in c["profile"])
    facts = "".join(f'<div class="fact"><small>{e(a)}</small><strong>{e(b)}</strong></div>' for a, b in c["facts"])
    crit = "".join(f"<li>{e(x)}</li>" for x in c["criteria"])
    stops = []
    for date, name, desc, img, alt in c["stops"]:
        im = f'<img src="assets/{img}" alt="{e(alt)}" loading="lazy">' if img else ""
        cls = "stop-card has-img" if img else "stop-card"
        stops.append(f"""        <li class="stop"><div class="{cls}">
          <div class="stop-body"><time>{e(date)}</time><h3 class="display h3">{e(name)}</h3><p>{e(desc)}</p></div>
          {im}
        </div></li>""")
    r = RESULTS[k]
    ncols = len(r["stats"])
    ccls = "counters four" if ncols == 4 else "counters two"
    lists = ""
    if r["worked"]:
        lists += '<div><h3 class="display h3">What worked</h3><ul class="checklist">' + "".join(f"<li>{e(x)}</li>" for x in r["worked"]) + "</ul></div>"
    if r["learned"]:
        lists += '<div><h3 class="display h3">What we learned</h3><ul class="checklist learn">' + "".join(f"<li>{e(x)}</li>" for x in r["learned"]) + "</ul></div>"
    quotes = "".join(f"<blockquote>{e(q)}</blockquote>" for q in r["quotes"])
    if quotes:
        quotes = f'<div class="quotes">{quotes}<small>Participants, in one sentence.</small></div>'
    note = f'<p class="form-note" style="text-align:center;margin-top:12px">{e(r["note"])}</p>' if r["note"] else ""
    two = f'<div class="two-col" style="margin-top:32px">{lists}</div>' if lists else ""
    results_section = f"""  <section id="results" style="padding-top:0">
    <div class="wrap">
      <div class="section-head" style="margin-bottom:32px">
        <span class="eyebrow">Results</span>
        <h2 class="display h2">What this chapter delivered</h2>
      </div>
      <div class="{ccls}" style="margin:0">{stats_block(r["stats"])}</div>
      {note}
      {two}
      {quotes}
    </div>
  </section>"""
    side = ""
    if c["side"]:
        side = f'<div class="polaroid alt" style="margin-top:24px"><img src="assets/{c["side"][0]}" alt="{e(c["side"][1])}" loading="lazy"></div>'
    pager = '<div class="pager">'
    pager += (f'<a href="{prev["file"]}"><small>Previous chapter</small><strong>{e(prev["name"])}</strong></a>' if prev else "<span></span>")
    pager += (f'<a class="next" href="{nxt["file"]}"><small>Next chapter</small><strong>{e(nxt["name"])}</strong></a>' if nxt else "<span></span>")
    pager += "</div>"
    body = f"""  <div class="page-hero split">
    <div class="wrap">
      <div>
        <span class="status-pill">Chapter {c['no']} of 5, completed</span>
        <h1 class="display h1">{e(c['name'])}</h1>
        <p class="tagline">{e(c['tagline'])}</p>
        <p class="lead">{e(c['subtitle'])}, {e(c['country'])}.</p>
      </div>
      <div class="polaroid"><img src="assets/{c['hero']}" alt="{e(c['hero_alt'])}"></div>
    </div>
  </div>

  <section style="padding-top:0;padding-bottom:0">
    <div class="wrap"><div class="facts">{facts}</div></div>
  </section>

  <section>
    <div class="wrap two-col">
      <div>
        <span class="eyebrow">The idea</span>
        <h2 class="display h2">{e(c['tagline'])}</h2>
        {intro}
        {side}
      </div>
      <div>
        <span class="eyebrow">Who we were looking for</span>
        <h2 class="display h2">{e(c['profile_h'])}</h2>
        {profile}
        <ul class="checklist" aria-label="Participation criteria">{crit}</ul>
      </div>
    </div>
  </section>

  <section style="padding-top:0">
    <div class="wrap">
      <div class="section-head" style="margin-bottom:32px">
        <span class="eyebrow">The journey</span>
        <h2 class="display h2">{e(c['route_h'])}</h2>
        <p class="lead muted">{e(c['route_p'])}</p>
      </div>
      <ol class="timeline">
{chr(10).join(stops)}
      </ol>
    </div>
  </section>

{results_section}
  <section style="padding-top:0">
    <div class="wrap">
      <div class="join">
        <span class="eyebrow">What was covered</span>
        <h2 class="display h2">Everything on the road</h2>
        <p class="lead">Tickets, accommodation and meals were covered by the project. Some restrictions applied. This chapter is completed and applications are closed.</p>
        <a class="btn btn-primary" href="human-library.html">See how the Human Library works</a>
      </div>
    </div>
  </section>

  <section style="padding-top:0">
    <div class="wrap">{pager}</div>
  </section>"""
    return page(k, f"{c['name']}, {c['country']}",
                f"{c['name']}: {c['subtitle']} in {c['country']}, {c['dates']}.", body)


def human_library():
    body = f"""  <div class="page-hero split">
    <div class="wrap">
      <div>
        <span class="eyebrow">Our method</span>
        <h1 class="display h1">What is a Human Library?</h1>
        <p class="lead">In Eurolibrary, the Human Library is the engine of every mobility. Participants were trained to share personal stories about mental health, eco living, migration, healthy lifestyles and entrepreneurship, and shared them with local communities across Europe in a safe, respectful space.</p>
      </div>
      <div class="polaroid"><img src="assets/photos/human-library-talk.jpg" alt="Two people talking during a Human Library"></div>
    </div>
  </div>

  <section>
    <div class="wrap two-col">
      <div>
        <span class="eyebrow">Imagine this</span>
        <h2 class="display h2">You borrow a person, not a book</h2>
        <p class="lead">You walk into a library. Instead of borrowing a book, you borrow a person. They tell you a story, their story: raw, real and often misunderstood.</p>
        <p>Welcome to the Human Library, where people are the books and every conversation is a chance to question bias, break stereotypes and build connection.</p>
      </div>
      <div>
        <p>The Human Library is an innovative, interactive method that promotes dialogue, reduces prejudice and builds understanding. Participants "borrow" Human Books, people who share personal stories of overcoming adversity, embracing diversity or living unique experiences.</p>
        <p>These one to one or small group conversations challenge stereotypes and make room for authentic, empathetic exchange.</p>
        <ul class="checklist" aria-label="Results of the Human Library events">
          <li>Communities gain insight into the experiences of marginalised or underrepresented young people.</li>
          <li>Locals become "readers" and talk in real time with a diverse group of young "books".</li>
          <li>Participants build confidence, empathy and storytelling skills.</li>
        </ul>
      </div>
    </div>
  </section>

  <section style="padding-top:0">
    <div class="wrap">
      <p class="quote">"It is not about agreeing. It is about understanding."</p>
    </div>
  </section>

  <section style="padding-top:0">
    <div class="wrap">
      <div class="section-head" style="margin-bottom:32px">
        <span class="eyebrow">Why a Human Library</span>
        <h2 class="display h2">Five reasons we use it</h2>
      </div>
      <div class="grid-4 grid-5">
        <div class="pillar"><h3 class="display h3" style="font-size:22px">Challenge prejudice</h3><p>Through personal storytelling.</p></div>
        <div class="pillar"><h3 class="display h3" style="font-size:22px">Stay true</h3><p>Inspire young people to hold on to their values and question social norms.</p></div>
        <div class="pillar"><h3 class="display h3" style="font-size:22px">Honest dialogue</h3><p>Create safe spaces to talk openly.</p></div>
        <div class="pillar"><h3 class="display h3" style="font-size:22px">Real listening</h3><p>Help us listen without assumptions.</p></div>
        <div class="pillar"><h3 class="display h3" style="font-size:22px">Connection</h3><p>Bring together people from different cultures, experiences and walks of life.</p></div>
      </div>
    </div>
  </section>

  <section style="padding-top:0">
    <div class="wrap">
      <div class="section-head" style="margin-bottom:32px">
        <span class="eyebrow">Format</span>
        <h2 class="display h2">How a session works</h2>
        <p class="lead muted">We ran four Human Library events in each of the five chapters.</p>
      </div>
      <div class="steps">
        <div class="pillar"><i>Catalogue</i><h3 class="display h3">Pick a title</h3><p>A list of human books, each with a title that represents their story and a short summary.</p></div>
        <div class="pillar"><i>Borrowing</i><h3 class="display h3">Borrow a book</h3><p>Readers choose a book from the catalogue and borrow them for a timed conversation.</p></div>
        <div class="pillar"><i>Rules</i><h3 class="display h3">Respect first</h3><p>Mutual respect, open mindedness and confidentiality. Readers are encouraged to ask honest questions, and books can share or withhold details as they wish.</p></div>
      </div>
    </div>
  </section>

  <section style="padding-top:0">
    <div class="wrap">
      <div class="photo-row"><figure><img src="assets/photos/human-library-talk.jpg" alt="A reader and a human book talking in a park"></figure>
      <figure><img src="assets/photos/human-library-table.jpg" alt="An information table with leaflets and a small globe"></figure></div>
    </div>
  </section>

  <section style="padding-top:0">
    <div class="wrap">
      <div class="join">
        <span class="eyebrow">Listen, share, inspire</span>
        <h2 class="display h2">Where we used it</h2>
        <p class="lead">From Bulgarian trains to Greek islands, in town squares and in schools.</p>
        <a class="btn btn-primary" href="index.html#destinations">See the five chapters</a>
      </div>
    </div>
  </section>"""
    return page("hl", "Human Library method",
                "How Eurolibrary uses the Human Library method to challenge prejudice and connect young people with local communities.", body)


def contact():
    body = f"""  <div class="page-hero">
    <div class="wrap">
      <span class="eyebrow">Get in touch</span>
      <h1 class="display h1">Reach out to the Eurolibrary team</h1>
      <p class="lead">Reviewing the project, curious about the method or up for a collaboration? Write to us and we will get back to you.</p>
    </div>
  </div>

  <section style="padding-top:32px">
    <div class="wrap two-col">
      <form class="contact" id="contact-form" novalidate>
        <div class="field"><label for="f-name">First name</label><input id="f-name" name="name" type="text" autocomplete="given-name" required></div>
        <div class="field"><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email" required></div>
        <div class="field"><label for="f-msg">Message</label><textarea id="f-msg" name="message" required></textarea></div>
        <div><button class="btn btn-primary" type="submit">Send message</button></div>
        <p class="form-note" id="form-status" role="status"></p>
      </form>
      <div>
        <span class="eyebrow">Prefer email?</span>
        <h2 class="display h2">Write to us directly</h2>
        <p>The project is completed, but the team still answers questions about the method, the results and possible collaborations.</p>
        <div class="email-line"><code>{EMAIL}</code><button class="btn btn-ghost" type="button" id="copy-email">Copy address</button></div>
      </div>
    </div>
  </section>"""
    return page("contact", "Contact Eurolibrary",
                "Get in touch with the Eurolibrary team about the project, the method or a collaboration.", body)


PAGES = {"index.html": home, "about.html": about, "human-library.html": human_library, "contact.html": contact}
for _k in CHAPTERS:
    PAGES[CH[_k]["file"]] = (lambda k=_k: chapter(k))


# ---------------------------------------------------------------- salida


def strip_wrapper(doc):
    """Deja solo el contenido que espera el esqueleto de artefactos."""
    doc = re.sub(r"<!doctype html>\s*<html[^>]*>\s*<head>\s*", "", doc, flags=re.I)
    doc = re.sub(r'<meta charset[^>]*>\n|<meta name="viewport"[^>]*>\n', "", doc)
    doc = re.sub(r"\s*</head>\s*<body>\s*", "\n", doc)
    doc = re.sub(r"\s*</body>\s*</html>\s*$", "\n", doc)
    return doc


def main():
    inline = None
    if "--inline" in sys.argv:
        inline = sys.argv[sys.argv.index("--inline") + 1]
    css = open(os.path.join(ROOT, "css", "site.css"), encoding="utf8").read()
    out = inline or ROOT
    os.makedirs(out, exist_ok=True)
    for name, fn in PAGES.items():
        doc = fn()
        if inline:
            doc = doc.replace("<!--CSS-->", "<style>\n" + css + "</style>")
            if name == "index.html":
                doc = strip_wrapper(doc)
                doc = re.sub(r"<title>.*?</title>", "<title>Eurolibrary rediseño</title>", doc, count=1)
        else:
            doc = doc.replace("<!--CSS-->", '<link rel="stylesheet" href="css/site.css">')
        with open(os.path.join(out, name), "w", encoding="utf8") as f:
            f.write(doc)
        print("escrito", os.path.join(out, name))


if __name__ == "__main__":
    main()
