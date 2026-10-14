#!/usr/bin/env python3
"""Genera las páginas estáticas de Eurolibrary.

Uso:
  python3 tools/build.py                 escribe las páginas en la raíz del repo
  python3 tools/build.py --inline DIR    escribe una copia con el CSS incrustado en DIR
                                         (para publicarla como artefacto, con enlaces .html)

Las páginas de la raíz usan URLs limpias (/about) gracias a "cleanUrls" en vercel.json.
"""
import html
import os
import re
import urllib.parse
import sys

import podcast_all  # noqa: E402

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
        hero="photos/spain-hero.jpg", hero_alt="Three walkers with backpacks on a country road in Galicia",
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
            ("26 to 27 July", "Pontedeume", "A lovely medieval town to get ready, mind and legs, before the first steps away from the Atlantic.", "photos/spain-group-street.jpg", "The group sitting together on a street in Pontedeume"),
            ("28 July", "Betanzos", "Said by many to serve the best tortilla in the world. Tasted with locals while celebrating the first public event in its stone streets.", "photos/spain-hl-talk.jpg", "Two people in conversation during a Human Library in a town square"),
            ("29 July", "Ordes", "A modern town halfway along the route, and the place to rest, reflect and recharge for the final kilometres.", "photos/spain-church.jpg", "A stone chapel with a bell tower in the Galician countryside"),
            ("30 July", "Sigüeiro", "The last stop before Santiago, with parks, forest and a river, and friendly locals keen to listen to the stories.", "photos/spain-picnic.jpg", "Three walkers resting and smiling on the roadside"),
            ("31 July to 2 August", "Santiago de Compostela", "The magical city hosted the last and most important part of the trip: time to digest everything collected along the Way.", "photos/spain-obradoiro-group.jpg", "Pilgrims hugging in front of Santiago cathedral"),
        ],
        side=None,
        gallery_h="Photos from the road",
        gallery_p="From the first kilometres to the Obradoiro square. Tap a photo to see it larger.",
        gallery_link=("View the full album", "https://photos.app.goo.gl/FBvjyPFJJKJQ9BHe8"),
        gallery=[
            ("photos/spain-viewpoint.jpg", "A walker standing on a rock above a Galician landscape", "50% 50%"),
            ("photos/spain-landscape.jpg", "A river valley under a cloudy sky seen from the Way", "50% 50%"),
            ("photos/spain-town.jpg", "A Galician town of white glazed balconies on a hill", "50% 50%"),
            ("photos/spain-hl-table.jpg", "A volunteer at the Human Library registration table", "50% 30%"),
            ("photos/spain-hl-conversation.jpg", "A reader and a human book talking during a Human Library", "30% 40%"),
            ("photos/spain-human-library-setup.jpg", "A Human Library table under a blue tent in a town square", "50% 50%"),
            ("photos/spain-landscape-2.jpg", "Rolling green hills under a wide sky", "50% 50%"),
            ("photos/spain-selfie.jpg", "A smiling walker in a sun hat taking a selfie on the road", "50% 50%"),
            ("photos/spain-walkers-women.jpg", "Three walkers coming down a village street", "50% 50%"),
            ("photos/spain-walkers-hands.jpg", "Walkers raising their arms on a tree lined road", "50% 50%"),
            ("photos/spain-hostel-group.jpg", "The group resting together on a sofa after a day of walking", "50% 50%"),
            ("photos/spain-walkers-path.jpg", "Walkers with backpacks on a path between fields", "50% 50%"),
            ("photos/spain-hug.jpg", "Two pilgrims hugging in front of Santiago cathedral", "50% 66%"),
            ("photos/spain-santiago-arrival.jpg", "The group arriving in the Obradoiro square", "50% 50%"),
            ("photos/spain-cathedral.jpg", "The facade of Santiago cathedral seen from below", "50% 22%"),
        ],
    ),
    "netherlands": dict(
        file="netherlands.html", no=3, name="The Dutch Way", country="The Netherlands",
        mode="by bike", mode_short="By bike", dates="1 to 8 September 2025", topic="Healthy lifestyle",
        hero="photos/netherlands-hero.jpg", hero_alt="The whole group gathered around a table, smiling at the camera",
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
            ("1 September", "Leeuwarden", "Historic canals, bold street art and Frisian pride. Open skies, cosy cafés and a creative, down to earth vibe.", "photos/netherlands-leeuwarden.jpg", "Participants posing together on a street in a Dutch town", "50% 55%"),
            ("1 to 3 September", "Sint Annaparochie", "A quiet village with big stories: poetic landscapes, local pride and the roots of Rembrandt's love story. Calm meets curiosity.", "photos/netherlands-annaparochie.jpg", "Participants crouching and smiling on a grass dike", "50% 45%"),
            ("3 to 5 September", "Terschelling", "Where sea meets sky: windswept beaches, endless bike paths and a rhythm made of nature, freedom and inspiration.", "photos/netherlands-ferry.jpg", "Two participants laughing on the deck of a ferry", "85% 40%"),
            ("5 to 8 September", "Goingarijp", "Tucked between lakes and meadows, a place to slow down and discover Friesland on the water. A hidden gem for nature and sailing lovers.", "photos/netherlands-sailors.jpg", "Participants laughing in life jackets on a sailing boat", "50% 80%"),
        ],
        side=("photos/netherlands-cyclists-smiling.jpg", "Three participants smiling on their bikes"),
        gallery_h="Photos from the ride",
        gallery_p="Bikes, ferries, sailboats and long dinners. Tap a photo to see it larger.",
        gallery_link=("View the full album", "https://photos.app.goo.gl/QfrxSffqHgeStmjM6"),
        gallery_portrait=True,
        gallery=[
            ("photos/netherlands-cyclists-pair.jpg", "Two participants smiling as they cycle along a country path", "50% 50%"),
            ("photos/netherlands-cyclists.jpg", "Cyclists riding side by side in the Frisian countryside", "50% 50%"),
            ("photos/netherlands-tandem.jpg", "Two participants on a tandem bike on the deck of a ferry", "50% 50%"),
            ("photos/netherlands-ferry-hug.jpg", "Two participants hugging in a ferry corridor", "50% 50%"),
            ("photos/netherlands-boat-chat.jpg", "Participants chatting on a boat under a cloudy sky", "50% 50%"),
            ("photos/netherlands-sailing.jpg", "Participants sailing together on a Frisian lake", "50% 50%"),
            ("photos/netherlands-sailboat.jpg", "A white sailboat with a blue striped hull on a lake", "50% 50%"),
            ("photos/netherlands-dinner.jpg", "A long candlelit dinner table", "50% 50%"),
            ("photos/netherlands-cooks.jpg", "Two cooks in aprons smiling at the camera", "50% 50%"),
            ("photos/netherlands-apron.jpg", "Two participants in aprons asking for silence", "50% 50%"),
            ("photos/netherlands-table.jpg", "Participants talking around a table", "50% 50%"),
            ("photos/netherlands-talk.jpg", "Two participants in conversation on the grass", "50% 50%"),
            ("photos/netherlands-grass.jpg", "Three participants laughing together on the grass", "50% 50%"),
            ("photos/netherlands-fierljeppen.jpg", "A participant pole vaulting over a canal", "50% 50%"),
            ("photos/netherlands-couple.jpg", "Two participants smiling and hugging", "50% 50%"),
        ],
    ),
    "greece": dict(
        file="greece.html", no=4, name="Waves of Hope", country="Greece",
        mode="by ferry", mode_short="By ferry", dates="2 to 9 October 2025", topic="Migration",
        hero="photos/greece-hero.jpg", hero_alt="The whole group gathered on the ferry deck with the sea behind them",
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
            ("2 October", "Piraeus, Athens", "A night in a hotel close to the port, then an early start to catch the ferry to Ios.", "photos/greece-piraeus.jpg", "Participants with backpacks boarding the ferry at the port of Piraeus", "50% 40%"),
            ("3 to 5 October", "Ios", "After an eight hour ferry, the first island. The group got to know each other, introduced the project and ran the first Human Library.", "photos/greece-ios.jpg", "The group on a hilltop above the whitewashed town of Ios", "50% 60%"),
            ("5 to 7 October", "Folegandros", "Time to prepare and visit a local school, and to organise the second Human Library in the Chora, the main square.", "photos/greece-folegandros.jpg", "Participants gathered in the Chora of Folegandros for the Human Library", "50% 60%"),
            ("7 to 8 October", "Sifnos", "A three hour ferry ride to share stories on board, then a second school visit and the last local event.", "photos/greece-sifnos.jpg", "Participants by the turquoise sea in Sifnos", "50% 55%"),
            ("8 to 9 October", "Piraeus, Athens", "The last ferry from Sifnos brought the group back to the port and the same accommodation as the first night. 9 October was departures day.", "photos/greece-return.jpg", "Participants waiting with their luggage at the port", "50% 50%"),
        ],
        side=("photos/greece-side.jpg", "Participants smiling together on the ferry deck"),
        gallery_h="Photos from the islands",
        gallery_p="Ferries, whitewashed squares, school courtyards and sunsets. Tap a photo to see it larger.",
        gallery_link=("View the full album", "https://photos.app.goo.gl/DerMeM1c22HKJRPC6"),
        gallery=[
            ("photos/greece-ferry-circle.jpg", "Participants sitting in a circle on the ferry", "50% 50%"),
            ("photos/greece-ferry-hug.jpg", "A group hug on the ferry", "50% 50%"),
            ("photos/greece-ferry-joy.jpg", "Participants laughing in a huddle on board", "50% 50%"),
            ("photos/greece-sunset-group.jpg", "The group posing at sunset with a green dinosaur plush", "50% 50%"),
            ("photos/greece-performance.jpg", "Participants performing in front of an audience", "50% 50%"),
            ("photos/greece-ios-group.jpg", "A group photo on the hill above Ios", "50% 50%"),
            ("photos/greece-hillside.jpg", "Participants gathered on a hillside in Folegandros", "50% 50%"),
            ("photos/greece-lunch.jpg", "A long outdoor lunch in a village square", "50% 50%"),
            ("photos/greece-red-room.jpg", "A conversation circle in a room with red curtains", "50% 50%"),
            ("photos/greece-school-banners.jpg", "Participants standing by the Eurolibrary banners at a school", "50% 50%"),
            ("photos/greece-mountain-road.jpg", "The whole group on a mountain road", "50% 50%"),
            ("photos/greece-circle-dance.jpg", "Students and participants dancing in a circle", "50% 50%"),
            ("photos/greece-school-group.jpg", "A big group photo with the students of Sifnos", "50% 50%"),
            ("photos/greece-harbour.jpg", "Two participants chatting by the harbour with a cat", "50% 50%"),
            ("photos/greece-cats-sea.jpg", "Participants relaxing by the sea in Sifnos", "50% 50%"),
        ],
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
        stats=BASE + [("4.2 of 5", "Average rating from 9 participant responses"),
                      ("4 of 5", "Survey respondents who picked a Human Library as their favourite activity")],
        note="Ratings and favourite activity come from two participant feedback forms.",
        worked=["The Human Library on the train, which participants singled out as a highlight.",
                "The mix of backgrounds and professions in the group, and the sense of connection it created.",
                "Singing and dancing together in Varna, and a last trip to the beach."],
        learned=["A heat wave made the programme tough. Participants suggested later start times for events, more breaks and more water and snacks.",
                 "They also asked for more time in each city and at the start to get to know each other's stories, and for a larger travel allowance for people coming from far away."],
        quotes=[("Inspiring.", "Gui"), ("A powerful human experience of connection, growth, and shared vulnerability.", "Beatriz"), ("It was a fun, dynamic trip focussed on connection.", "Rashel")],
    ),
    "spain": dict(
        stats=BASE + [("125", "Human Books in the catalogue"), ("4.7 of 5", "Average rating from 3 participant responses")],
        note="Ratings come from the participant feedback form.",
        worked=["A shared catalogue of personal stories on mental health, built by participants before the walk and used to prepare each Human Library.",
                "The stories shared along the Way, and friendships that lasted long after the walk."],
        learned=["Participants would have liked more days on the Camino."],
        quotes=[("Hearing so many stories of overcoming big issues was very inspiring!", "Alessandro"),
                ("People deserve to be heard.", "Óscar"),
                ("The friendship lasted and the connection we had has been unbelievable.", "Christian")],
    ),
    "netherlands": dict(
        stats=BASE + [("5.0 of 5", "Average rating from 4 participant responses")],
        note="Ratings come from the participant feedback form.",
        worked=["Four public events held along the whole route through Friesland.",
                "The rides through the landscape, the sailing, the ferry and the evenings together."],
        learned=["Rain and wind complicated the logistics. The team found alternatives that kept participants safe and the events impactful.",
                 "Participants asked for better food and a larger travel allowance, and suggested announcing public events in advance so more people stop to listen."],
        quotes=[("That I can do more than I think I am capable of, and that my body is stronger than I thought.", "Inés"),
                ("I will remember the ferry adventure and the nights dancing.", "Javier")],
    ),
    "greece": dict(
        stats=BASE + [("5.0 of 5", "Average rating from 5 participant responses")],
        note="Ratings come from the participant feedback form.",
        worked=["Human Library events held in unusual places, including on board a ferry, and in local schools.",
                "Organising the events together, talking to locals and exploring each island, with a group that felt like a family."],
        learned=["Visiting several islands in one week left little time to rest. Participants suggested fewer moves or more days."],
        quotes=[("I've learned that every story is unique and valuable, and that instead of looking for differences, we should try to see what we have in common.", "Estefanía"),
                ("We really became like a family and felt really safe sharing our stories together.", "Victoria")],
    ),
    "portugal": dict(
        stats=BASE + [("5.0 of 5", "Average rating from 3 participant responses")],
        note="Ratings come from the participant feedback form.",
        worked=["Four Human Library events spread along a campervan route across the south of Portugal.",
                "A surfing day and cooking in the van kitchen for 25 people, which participants remembered as highlights."],
        learned=["Sanitary logistics on the road, mainly bathrooms, were the main thing to improve, and participants said they were manageable."],
        quotes=[("Traveling light and having a place to sleep is all we need sometimes.", "David"),
                ("Surfing day, deep talks, funny moments in the van.", "Raquel")],
    ),
}

HL_HOW = ("How does it work? Readers choose a book from the catalogue and borrow it for a timed conversation. "
          "Respect comes first, books decide what they share, and nobody has to agree. The point is to understand.")
HL_INTRO = {
    "bulgaria": "Picture a library where the books are young entrepreneurs. You pick a title, sit down for a timed conversation and hear how someone built something from nothing, including the setbacks nobody posts about. On the Balkan Express that library never stayed in one place. It opened in city squares and parks, and even on a moving train between cities.",
    "spain": "In this library every book is a story about mental health. Participants wrote a title and a short summary for a shared catalogue, and readers chose who to borrow. Along the English Way the library opened in town squares, where strangers sat down on a bench and listened to experiences that are rarely said out loud.",
    "netherlands": "Healthy living is easier to talk about when you are doing it. Cycling across Friesland, the books were coaches, creators and people finding their own balance, and the readers were locals who stopped to ask honest questions about movement, food, rest and connection. Rain and wind forced some changes, and the team found alternatives so the events still went ahead.",
    "greece": "Here the books were stories of migration, and the library travelled by ferry. It opened on Cycladic islands, in a village square and in local schools, where students heard these stories straight from the people who lived them. It even set up on board a ferry.",
    "portugal": "A campervan became a travelling library about living lightly and caring for the planet. Across the south of Portugal, four stops each opened a Human Library where readers borrowed stories about eco friendly, minimalist lifestyles and asked how those choices work in everyday life.",
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


SITE = "https://eurolibrary.eu"
# clave de página: (ruta pública, foto de cabecera usada para la imagen social)
SOCIAL = {
    "home": ("/", "about-classroom"),
    "about": ("/about", "about-banner"),
    "hl": ("/human-library", "human-library-talk"),
    "podcast": ("/podcast", "podcast"),
    "bulgaria": ("/bulgaria", "bulgaria-hero"),
    "spain": ("/spain", "spain-hero"),
    "netherlands": ("/netherlands", "netherlands-hero"),
    "greece": ("/greece", "greece-hero"),
    "portugal": ("/portugal", "portugal-hero"),
}


def head(title, desc, key):
    path, img = SOCIAL[key]
    url, image = SITE + path, f"{SITE}/assets/social/{key}.jpg"
    return f"""<meta charset="utf-8">
<script>document.documentElement.classList.add('js')</script>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Eurolibrary">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="twitter:image" content="{image}">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="icon" href="assets/favicon-32.png" type="image/png" sizes="32x32">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
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
    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="menu"><span>Menu</span><span class="mt-ico" aria-hidden="true"><i></i><i></i></span></button>
    <ul id="menu">
      <li><a href="index.html"{cur("home")}>Home</a></li>
      <li class="dd">
        <a href="index.html#destinations"{mob_active}>Mobilities</a>
        <div class="dd-menu" id="dd-menu">
          <a class="mob-only" href="index.html#destinations">All mobilities</a>
{mob}
        </div>
      </li>
      <li><a href="human-library.html"{cur("hl")}>Human library</a></li>
      <li><a href="about.html"{cur("about")}>About</a></li>
      <li><a class="icon-link" href="https://www.instagram.com/eurolibrary" target="_blank" rel="noopener" aria-label="Eurolibrary on Instagram"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4.2"/><circle cx="17.3" cy="6.7" r="0.6" fill="currentColor"/></svg><span class="icon-label">Instagram</span></a></li>
      <li><a class="btn btn-dark" href="podcast.html"{cur("podcast")}>Podcast</a></li>
    </ul>
  </div>
</header>"""


def footer():
    links = "".join(
        f'<li><a href="{f}">{t}</a></li>' for f, t in [
            ("index.html", "Home"), ("about.html", "About"), ("human-library.html", "Human library"),
            ("podcast.html", "Podcast"), ("about.html#contact", "Contact")] + [(CH[k]["file"], CH[k]["name"]) for k in CHAPTERS])
    return f"""<footer>
  <div class="wrap">
    <img class="eu" src="assets/eu-funded-blue.png" alt="Funded by the European Union">
    <div class="meta">
      <ul class="links">{links}</ul>
      <p class="partners-line">Coordinated by <a href="https://xeracion.org">Asociación Xeración</a>, with <a href="https://altventurers.com/">AltVenturers</a>, <a href="https://www.dekrachtvansport.nl/">De Kracht van Sport</a>, <a href="https://tfn-bg.com/">The Future Now Association</a> and <a href="https://gaiaalentejo.wordpress.com/english/">GAIA Alentejo</a>.</p>
      <p>{e(EU_DISCLAIMER)}</p>
    </div>
    <p class="copy">Copyright © 2026 Eurolibrary</p>
  </div>
</footer>"""


SCRIPT = """<script>
  var nav=document.getElementById('nav'),t=nav.querySelector('.menu-toggle'),mq=matchMedia('(max-width: 960px)');
  function setMenu(o){nav.classList.toggle('open',o);t.setAttribute('aria-expanded',o);document.body.classList.toggle('menu-open',o)}
  t.addEventListener('click',function(){setMenu(!nav.classList.contains('open'))});
  nav.addEventListener('click',function(e){if(e.target===nav)setMenu(false)});
  document.addEventListener('keydown',function(e){if(e.key==='Escape'&&nav.classList.contains('open')){setMenu(false);t.focus()}});
  [].forEach.call(nav.querySelectorAll('#menu a'),function(a){a.addEventListener('click',function(e){
    var dd=a.parentNode.classList.contains('dd')&&a.parentNode.firstElementChild===a;
    if(dd&&mq.matches){e.preventDefault();var o=a.parentNode.classList.toggle('exp');a.setAttribute('aria-expanded',o);return}
    if(mq.matches)setMenu(false);
  })});
  var ddl=nav.querySelector('.dd>a');
  if(ddl){ddl.setAttribute('aria-haspopup','true');ddl.setAttribute('aria-expanded','false');if(ddl.hasAttribute('aria-current')){ddl.parentNode.classList.add('exp');ddl.setAttribute('aria-expanded','true')}}
  (mq.addEventListener?mq.addEventListener.bind(mq,'change'):mq.addListener.bind(mq))(function(e){if(!e.matches)setMenu(false)});
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
  (function(){
    var car=document.querySelector('[data-carousel]');
    if(!car)return;
    var track=car.querySelector('.carousel-track'),prev=car.querySelector('.prev'),next=car.querySelector('.next');
    function upd(){prev.disabled=track.scrollLeft<=2;next.disabled=track.scrollLeft+track.clientWidth>=track.scrollWidth-2}
    function step(d){track.scrollBy({left:d*Math.max(track.clientWidth*0.8,260),behavior:'smooth'})}
    prev.addEventListener('click',function(){step(-1)});
    next.addEventListener('click',function(){step(1)});
    track.addEventListener('scroll',upd,{passive:true});
    window.addEventListener('resize',upd);
    track.addEventListener('keydown',function(e){if(e.key==='ArrowRight'){e.preventDefault();step(1)}if(e.key==='ArrowLeft'){e.preventDefault();step(-1)}});
    upd();
    var lb=document.getElementById('lightbox'),btns=[].slice.call(car.querySelectorAll('[data-lightbox]'));
    var img=lb.querySelector('.lb-fig img'),cap=lb.querySelector('figcaption'),cur=0,opener=null;
    var ctrls=[lb.querySelector('.lb-close'),lb.querySelector('.lb-prev'),lb.querySelector('.lb-next')];
    function show(i){
      cur=(i+btns.length)%btns.length;
      var im=btns[cur].querySelector('img');
      img.src=im.currentSrc||im.src;img.alt=im.alt;
      cap.textContent=(cur+1)+' / '+btns.length;
    }
    function open(i){opener=btns[i];show(i);lb.hidden=false;document.body.style.overflow='hidden';ctrls[0].focus()}
    function close(){lb.hidden=true;document.body.style.overflow='';if(opener)opener.focus()}
    btns.forEach(function(b,i){b.addEventListener('click',function(){open(i)})});
    ctrls[0].addEventListener('click',close);
    ctrls[1].addEventListener('click',function(){show(cur-1)});
    ctrls[2].addEventListener('click',function(){show(cur+1)});
    lb.addEventListener('click',function(e){if(e.target===lb||e.target.classList.contains('lb-fig'))close()});
    document.addEventListener('keydown',function(e){
      if(lb.hidden)return;
      if(e.key==='Escape')close();
      else if(e.key==='ArrowLeft')show(cur-1);
      else if(e.key==='ArrowRight')show(cur+1);
      else if(e.key==='Tab'){
        var i=ctrls.indexOf(document.activeElement);
        e.preventDefault();
        ctrls[(i+(e.shiftKey?-1:1)+ctrls.length)%ctrls.length].focus();
      }
    });
    var x0=null;
    lb.addEventListener('touchstart',function(e){x0=e.touches[0].clientX},{passive:true});
    lb.addEventListener('touchend',function(e){
      if(x0===null)return;
      var dx=e.changedTouches[0].clientX-x0;x0=null;
      if(Math.abs(dx)>50)show(cur+(dx<0?1:-1));
    });
  })();
</script>"""


def page(active, title, desc, body):
    return f"""<!doctype html>
<html lang="en">
<head>
{head(title, desc, active)}
</head>
<body>
<div class="sp" aria-hidden="true"></div>

{nav(active)}

<main>
{body}
</main>

{footer()}

{SCRIPT}
{FX}
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
            <a class="btn btn-ghost card-btn" href="{c['file']}">Check the details</a>
          </div>
        </article>""")
    body = f"""  <div class="hero">
    <div class="wrap">
      <h1 class="display h1">5 countries, 5 topics,<br>5 ways to move.</h1>
      <p class="lead">This Erasmus+ project took young people across Europe by train, on foot, by bike, by ferry and by campervan, and turned their stories into a living library. The trip is over. The stories keep going.</p>
      <div class="cta">
        <a class="btn btn-primary" href="#destinations">Explore the five chapters</a>
        <a class="btn btn-ghost" href="human-library.html">See how the Human Library works</a>
      </div>
      <p class="note">All five mobilities are completed and applications are closed. This site is the project record. <a href="about.html#results" style="text-decoration:underline">See the results</a>.</p>

      <div class="ticket-row" aria-label="The five chapters at a glance">
{tickets}
      </div>
    </div>
  </div>

  <section>
    <div class="wrap concept">
      <div>
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
      <div class="pod-teaser">
        <img src="assets/podcast/show.jpg" alt="People of EU podcast cover" width="200" height="200" loading="lazy">
        <div>
          <h2 class="display h2">Prefer to listen?</h2>
          <p class="lead">People of EU is our podcast: short personal stories from across Europe, told by the people who lived them. Press play on any episode without leaving the site.</p>
          <a class="btn btn-primary" href="podcast.html">Listen to the podcast</a>
        </div>
      </div>
    </div>
  </section>

  <section style="padding-top:0">
    <div class="wrap">
      <div class="join">
        <h2 class="display h2">Want to know more?</h2>
        <p class="lead">Reviewing the project, curious about our method or thinking about a collaboration? We are happy to talk.</p>
        <a class="btn btn-primary" href="about.html#contact">Get in touch</a>
      </div>
    </div>
  </section>

  <section class="leitmotiv">
    <div class="wrap">
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
        <h1 class="display h1">Plenty of Erasmus+ projects. None quite like this one.</h1>
        <p class="lead">Eurolibrary bridges cultural gaps by putting young people face to face with the communities they travel through. The result is more understanding, more empathy and lasting relationships, plus real tools to push back against discrimination and promote inclusion.</p>
      </div>
      <div class="polaroid"><img src="assets/photos/about-banner.jpg" alt="Two participants with a Eurolibrary roll up banner" style="aspect-ratio:3/3.6"></div>
    </div>
  </div>

  <section style="padding-top:32px">
    <div class="wrap">
      <div class="section-head" style="margin-bottom:32px">
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

  <section id="results" style="padding-top:0">
    <div class="wrap">
      <div class="section-head" style="margin-bottom:32px">
        <h2 class="display h2">Five chapters, in numbers</h2>
        <p class="lead muted">Figures taken from the project reports. Digital figures are as reported in October 2025, six months after the Instagram account launched.</p>
      </div>
      <div class="results-grid">
        {stats_block([("5", "Mobilities in five countries"), ("125", "Young participants, 25 per mobility"), ("20", "Human Library events, 4 per country"), ("20 to 30", "Readers per event, on average"), ("600,000+", "Video views across platforms"), ("20,000+", "Accounts reached on Instagram"), ("1,000+", "Organic followers, with no paid promotion"), ("3,000+", "Likes, comments, shares and saves"), ("200+", "Registrations of interest in the project")])}
      </div>
      <p class="lead" style="max-width:760px;margin:32px auto 0;text-align:center">Behind the numbers: more than 75 posts and reels, including over 50 short videos, plus several hours of interviews and footage that fed our podcast and videos. Participants also left written feedback that points to high satisfaction and personal growth.</p>
    </div>
  </section>

  <section style="padding-top:0">
    <div class="wrap">
      <div class="section-head" style="margin-bottom:32px">
        <h2 class="display h2">The project at a glance</h2>
      </div>
      <div class="facts-list">
        <div><small>Programme</small><strong>Erasmus+, European Youth Together</strong></div>
        <div><small>Project number</small><strong>101186721</strong></div>
        <div><small>Coordinator</small><strong>Asociación Xeración, Spain</strong></div>
        <div><small>Partners</small><strong>Five NGOs from Bulgaria, Greece, the Netherlands, Portugal and Spain</strong></div>
        <div><small>Mobilities</small><strong>Five chapters, June to November 2025</strong></div>
        <div><small>Dissemination lead</small><strong>AltVenturers, Greece</strong></div>
      </div>
    </div>
  </section>

  <section id="partners" style="padding-top:0">
    <div class="wrap">
      <div class="section-head" style="margin-bottom:32px">
        <h2 class="display h2">Five NGOs, one living library</h2>
        <p class="lead muted">Eurolibrary is coordinated by Asociación Xeración and carried out together with four partner organisations.</p>
      </div>
      <ul class="partners">
        <li class="lead-partner"><span class="tag">Coordinator</span><h3 class="display h3">Asociación Xeración</h3><p>Spain</p><a class="btn btn-ghost" href="https://xeracion.org">Visit website</a></li>
        <li><span class="tag">Partner</span><h3 class="display h3">AltVenturers</h3><p>Greece</p><a class="btn btn-ghost" href="https://altventurers.com/">Visit website</a></li>
        <li><span class="tag">Partner</span><h3 class="display h3">De Kracht van Sport</h3><p>The Netherlands</p><a class="btn btn-ghost" href="https://www.dekrachtvansport.nl/">Visit website</a></li>
        <li><span class="tag">Partner</span><h3 class="display h3">The Future Now Association</h3><p>Bulgaria</p><a class="btn btn-ghost" href="https://tfn-bg.com/">Visit website</a></li>
        <li><span class="tag">Partner</span><h3 class="display h3">GAIA Alentejo</h3><p>Portugal</p><a class="btn btn-ghost" href="https://gaiaalentejo.wordpress.com/english/">Visit website</a></li>
      </ul>
    </div>
  </section>

  <section style="padding-top:0">
    <div class="wrap">
      <div class="section-head">
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
        <h2 class="display h2">See the five chapters</h2>
        <p class="lead">Five countries, five topics and five ways to move. Pick a chapter and follow the route.</p>
        <a class="btn btn-primary" href="index.html#destinations">Explore the chapters</a>
      </div>
    </div>
  </section>""" + contact_section()
    return page("about", "About Eurolibrary",
                "The story of Eurolibrary: an Erasmus+ partnership of five NGOs that connects young people and communities through personal stories. Get in touch with the team here.", body)


def chapter(k):
    c = CH[k]
    order = CHAPTERS
    i = order.index(k)
    prev = CH[order[i - 1]] if i > 0 else None
    nxt = CH[order[i + 1]] if i < len(order) - 1 else None
    intro = "".join(f"<p>{e(p)}</p>" for p in c["intro"])
    facts = "".join(f'<div class="fact"><small>{e(a)}</small><strong>{e(b)}</strong></div>' for a, b in c["facts"])
    stops = []
    for date, name, desc, img, alt, *rest in c["stops"]:
        pos = f' style="object-position:{rest[0]}"' if rest else ""
        im = f'<img src="assets/{img}" alt="{e(alt)}" loading="lazy"{pos}>' if img else ""
        cls = "stop-card has-img" if img else "stop-card"
        stops.append(f"""        <li class="stop"><div class="{cls}">
          <div class="stop-body"><time>{e(date)}</time><h3 class="display h3">{e(name)}</h3><p>{e(desc)}</p></div>
          {im}
        </div></li>""")
    r = RESULTS[k]
    ncols = len(r["stats"])
    ccls = "counters four" if ncols == 4 else ("counters" if ncols == 3 else "counters two")
    lists = ""
    if r["worked"]:
        lists += '<div><h3 class="display h3">What worked</h3><ul class="checklist">' + "".join(f"<li>{e(x)}</li>" for x in r["worked"]) + "</ul></div>"
    if r["learned"]:
        lists += '<div><h3 class="display h3">What we learned</h3><ul class="checklist learn">' + "".join(f"<li>{e(x)}</li>" for x in r["learned"]) + "</ul></div>"
    quotes = "".join(f"<figure><blockquote>{e(q)}</blockquote><figcaption>{e(n)}, participant</figcaption></figure>" for q, n in r["quotes"])
    if quotes:
        quotes = f'<div class="quotes" style="--n:{len(r["quotes"])}">{quotes}<small>Participants, in their own words.</small></div>'
    note = f'<p class="form-note" style="text-align:center;margin-top:12px">{e(r["note"])}</p>' if r["note"] else ""
    two = f'<div class="two-col" style="margin-top:32px">{lists}</div>' if lists else ""
    results_section = f"""  <section id="results" style="padding-top:0">
    <div class="wrap">
      <div class="section-head" style="margin-bottom:32px">
        <h2 class="display h2">What this chapter delivered</h2>
      </div>
      <div class="{ccls}" style="margin:0">{stats_block(r["stats"])}</div>
      {note}
      {two}
      {quotes}
    </div>
  </section>"""
    gallery_section = ""
    if c.get("gallery"):
        slides = "".join(
            f'<figure class="slide"><button type="button" class="slide-btn" data-lightbox aria-label="Open photo: {e(alt)}">'
            f'<img src="assets/{u}" alt="{e(alt)}" loading="lazy" style="object-position:{pos}"></button></figure>'
            for u, alt, pos in c["gallery"])
        album = ""
        if c.get("gallery_link"):
            album = f'<p class="car-album"><a class="btn btn-dark" href="{c["gallery_link"][1]}" target="_blank" rel="noopener">{e(c["gallery_link"][0])}<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17L17 7M9 7h8v8"/></svg></a></p>'
        chev_l = '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 5l-7 7 7 7"/></svg>'
        chev_r = '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 5l7 7-7 7"/></svg>'
        gallery_section = f"""  <section id="photos" style="padding-top:0">
    <div class="wrap">
      <div class="section-head" style="margin-bottom:32px">
        <h2 class="display h2">{e(c['gallery_h'])}</h2>
        <p class="lead muted">{e(c['gallery_p'])}</p>
      </div>
      <div class="carousel{" portrait" if c.get("gallery_portrait") else ""}" data-carousel role="region" aria-roledescription="carousel" aria-label="{e(c['gallery_h'])}">
        <div class="carousel-track" tabindex="0">{slides}</div>
        <button type="button" class="car-btn prev" aria-label="Previous photos">{chev_l}</button>
        <button type="button" class="car-btn next" aria-label="Next photos">{chev_r}</button>
      </div>
      {album}
    </div>
    <div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="Photo viewer" hidden>
      <button type="button" class="lb-close" aria-label="Close photo viewer">{chr(215)}</button>
      <button type="button" class="lb-nav lb-prev" aria-label="Previous photo">{chev_l}</button>
      <figure class="lb-fig"><img alt=""><figcaption></figcaption></figure>
      <button type="button" class="lb-nav lb-next" aria-label="Next photo">{chev_r}</button>
    </div>
  </section>
"""
    if c["side"]:
        idea_block = f'''<div class="wrap two-col idea">
      <div>
        <h2 class="display h2">{e(c['tagline'])}</h2>
        {intro}
      </div>
      <div class="polaroid alt side"><img src="assets/{c["side"][0]}" alt="{e(c["side"][1])}" loading="lazy"></div>
    </div>'''
    else:
        idea_block = f'''<div class="wrap narrow">
      <h2 class="display h2">{e(c['tagline'])}</h2>
      {intro}
    </div>'''
    arrow_l = '<span class="arrow"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 12H5M11 6l-6 6 6 6"/></svg></span>'
    arrow_r = '<span class="arrow"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span>'
    pager = '<div class="pager">'
    pager += (f'<a class="prev" href="{prev["file"]}">{arrow_l}<span class="txt"><small>Previous chapter</small><strong>{e(prev["name"])}</strong></span></a>' if prev else "<span></span>")
    pager += (f'<a class="next" href="{nxt["file"]}"><span class="txt"><small>Next chapter</small><strong>{e(nxt["name"])}</strong></span>{arrow_r}</a>' if nxt else "<span></span>")
    pager += "</div>"
    body = f"""  <div class="page-hero split">
    <div class="wrap">
      <div>
        <span class="status-pill">Chapter {c['no']} of 5</span>
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
    {idea_block}
  </section>

  <section style="padding-top:0">
    <div class="wrap">
      <div class="section-head" style="margin-bottom:32px">
        <h2 class="display h2">{e(c['route_h'])}</h2>
        <p class="lead muted">{e(c['route_p'])}</p>
      </div>
      <ol class="timeline">
{chr(10).join(stops)}
      </ol>
    </div>
  </section>

{gallery_section}
{results_section}
  <section style="padding-top:0">
    <div class="wrap">
      <div class="join">
        <h2 class="display h2">A library where the books are people</h2>
        <p class="lead hl-text">{e(HL_INTRO[k])}</p>
        <p class="hl-text">{e(HL_HOW)}</p>
        <a class="btn btn-primary" href="human-library.html">See how the Human Library works</a>
      </div>
    </div>
  </section>

  <section style="padding-top:0">
    <div class="wrap">{pager}</div>
  </section>"""
    return page(k, f"{c['name']}, {c['country']}",
                f"{c['name']}: {c['subtitle']} in {c['country']}, {c['dates']}.", body)


HL_ROLES = [
    ("book", "Book", "A person who shares a part of their life",
     "A book is a person who, for some reason, is labelled or stereotyped by society and who chooses to tell their own story honestly. Books speak in the first person, without generalising and without trying to convince anyone. Each one writes a short review for the catalogue.",
     "A book always keeps the right to skip a question or to end a loan."),
    ("reader", "Reader", "A curious member of the public",
     "Readers register at reception, accept the rules and borrow one or more books. They come to listen and to ask honest, respectful questions, not to debate.",
     "Come curious and leave the arguments at the door."),
    ("librarian", "Librarian", "The organiser and master of ceremonies",
     "Librarians build the spaces, welcome readers, explain the rules and hand out the catalogue. They introduce each reader to a book, time every loan, keep count of who was borrowed and make sure everybody feels comfortable.",
     "Keep an eye on the reading space without listening in."),
    ("dictionary", "Dictionary", "An interpreter for the conversation",
     "When a book and a reader do not share a language, or when one of them is deaf, an interpreter joins the loan. In the Human Library they are called dictionaries.",
     "If your audience is multilingual, line up your dictionaries early."),
    ("promoter", "Promoter", "The people who bring readers in",
     "In a public space nobody is guaranteed to walk in. Promoters invite passers by and explain the idea in an original and playful way. They also keep children busy, for example with face painting, while their parents read.",
     "Flash mobs, free hugs and paper arrows pointing the way all work."),
]

HL_SPACES = [
    ("Reception", "Where readers arrive",
     "An info desk staffed by at least one librarian. Readers register, accept the rules and receive the up to date catalogue."),
    ("Bookshelf", "Where books wait",
     "A calm, separate corner where books relax between loans until a librarian calls them. Keep it out of earshot of the reading space."),
    ("Reading space", "Where loans happen",
     "Tables or armchairs, coffee and snacks to invite dialogue, and paper tablecloths for notes and doodles."),
]

HL_RULES = [
    ("Timed loans", "A loan lasts around 20 to 30 minutes, and never more than 30. It can end earlier."),
    ("Register first", "Readers sign in at reception, receive the instructions and accept them explicitly."),
    ("Your own story", "Books speak from the \"I\". No generalisations, no apologies and no attempt to convince."),
    ("The right to say no", "A book can skip any question and end the loan if the conversation goes somewhere unwanted."),
    ("Two readers at most", "To keep it a conversation and not a lecture, no more than two readers per book at once."),
    ("Return it with care", "Readers hand the book back as they found it: treated with courtesy, kindness and confidentiality."),
]

HL_STEPS = [
    ("Welcome", "A reader arrives at reception. The librarian greets them, explains the rules and asks them to register and accept them."),
    ("Browse", "The reader gets the catalogue: every book with a title and a short review. They choose the story they want to read."),
    ("Call the book", "The librarian goes to the bookshelf and tells the book that a reader is waiting."),
    ("Introduce", "The librarian introduces book and reader and walks them to a free table in the reading space."),
    ("Read", "The conversation begins. The book sets the boundaries and the reader asks honest questions. No more than two readers per book."),
    ("Time is up", "The librarian signals when the loan is over. The conversation can end earlier, and the time is fully customisable."),
    ("Return", "The reader thanks the book. Book and reader become available again, and the reader can ask for a new loan."),
    ("Feedback", "The librarian asks for a short evaluation and, with consent, a contact for the next events. Every loan is noted."),
]

HL_PLAN = [
    ("weeks3", "Three weeks before", [
        "Hold a full group meeting of 60 to 90 minutes: ice breakers, the project, the method, its roles and principles.",
        "Agree the date of each team meeting before the call ends.",
        "Choose the venues and ask permission: squares, schools, libraries, community centres or other public spaces.",
        "Decide whether each event is open to the public or by invitation."]),
    ("weeks2", "Two weeks before", [
        "Go deeper into the method with each team: ethics, storytelling structure, and the roles of books and readers.",
        "Help each participant choose their story and decide their emotional boundaries.",
        "Share draft stories and give each other peer feedback.",
        "Form the working groups: books, librarians, promoters and dictionaries."]),
    ("week1", "One week before", [
        "Collect every book's title and short review.",
        "Compile the catalogue, with at least six books for a small library.",
        "Prepare a digital version with a QR code and a few printed copies.",
        "Prepare signs, posters, leaflets and badges or T-shirts for each role.",
        "Run a short training for books and librarians."]),
    ("daybefore", "The day before", [
        "Promote the event online, in mailing lists and on social media.",
        "Gather all the materials in one place.",
        "Do a general trial: act out a whole loan from reception to feedback.",
        "Organise snacks and drinks for the reading space."]),
    ("hours3", "Three hours before", [
        "Set up the three spaces: reception, bookshelf and reading space.",
        "Start the promotion around the venue.",
        "Hold a last team meeting to agree roles, timings and signals.",
        "Check the consent you need for photos and for collecting emails."]),
    ("during", "During the library", [
        "Run reception: registration, rules and catalogue.",
        "Time every loan and note who borrowed which book.",
        "Let books rest between loans.",
        "Keep activities going for people who are not reading: games for children, promotion, short videos."]),
    ("after", "After the library", [
        "Thank books, readers and the venue.",
        "Gather feedback from participants and readers.",
        "Share photos, videos and podcasts with readers who agreed to receive them.",
        "Write down what worked and what to change next time."]),
]

HL_MATERIALS = ["Coloured paper and flipcharts", "Markers, pens, scissors and tape", "Badges or T-shirts for each role",
                "Tables and chairs", "Paper tablecloths to write on", "Printed catalogue and a QR code",
                "Signs, posters or a roll up banner", "Snacks, coffee and water", "A timer", "A sign in sheet"]

HL_FAQ = [
    ("Do I have to belong to a minority to be a book?",
     "No. Books are people with a story to share, often because they are labelled or stereotyped, but also because they have lived something others rarely hear. What matters is that they are willing to speak honestly about their own experience."),
    ("How long should a loan last?",
     "Around 20 to 30 minutes works well, and it should never go over 30. A conversation can always end earlier. Fix the duration before the event and let the librarians keep time."),
    ("How many books do we need?",
     "A small library needs at least six, so readers have a real choice. With more books, each one gets time to rest between loans."),
    ("Can we run one in a school?",
     "Yes. Eurolibrary held sessions in local schools, where students heard stories straight from the people who lived them. Agree the format with the teachers beforehand, keep groups small and make sure a librarian is always nearby."),
    ("What if a reader asks something too personal?",
     "The book can decline to answer or end the loan at any time, and does not have to explain why. The librarian can step in and offer the reader another book."),
    ("What about languages?",
     "Choose a shared language for the event. If a book and a reader do not share one, or one of them is deaf, bring in a dictionary to interpret."),
    ("Can we take photos or recordings?",
     "Only with the consent of everyone who appears or speaks. Ask for it at registration, and do not collect readers' emails without their agreement."),
    ("Where do we start?",
     "The Human Library Organisation, which started the method, shares resources and guidance at humanlibrary.org. Check their advice on how to present your event before you announce it."),
]

HL_SCRIPT = r"""
<script>
(function(){
  var root=document.documentElement;root.classList.add('js');
  function $(s,c){return (c||document).querySelector(s)}
  function $$(s,c){return [].slice.call((c||document).querySelectorAll(s))}

  /* table of contents with scroll spy */
  var links=$$('.toc a'),secs=$$('.g-sec');
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){
      if(e.isIntersecting){links.forEach(function(a){a.classList.toggle('on',a.getAttribute('href')==='#'+e.target.id)})}
    })},{rootMargin:'-20% 0px -70% 0px'});
    secs.forEach(function(s){io.observe(s)});
  }

  /* roles tabs */
  var tabs=$$('.role-tab'),panels=$$('.role-panel');
  function showRole(id){
    tabs.forEach(function(t){var on=t.dataset.role===id;t.setAttribute('aria-selected',on);t.tabIndex=on?0:-1});
    panels.forEach(function(p){p.hidden=p.dataset.role!==id});
  }
  tabs.forEach(function(t,i){
    t.addEventListener('click',function(){showRole(t.dataset.role)});
    t.addEventListener('keydown',function(e){
      var k=e.key==='ArrowRight'?1:e.key==='ArrowLeft'?-1:0;if(!k)return;
      var n=tabs[(i+k+tabs.length)%tabs.length];n.focus();showRole(n.dataset.role);e.preventDefault();
    });
  });
  if(tabs.length)showRole(tabs[0].dataset.role);

  /* loan stepper */
  var steps=$$('.step-btn'),detail=$('#step-detail'),cur=0;
  function goStep(i){
    cur=Math.max(0,Math.min(steps.length-1,i));
    steps.forEach(function(b,j){b.classList.toggle('on',j===cur);b.classList.toggle('done',j<cur);b.setAttribute('aria-current',j===cur?'step':'false')});
    detail.querySelector('h3').textContent=steps[cur].dataset.title;
    detail.querySelector('p').textContent=steps[cur].dataset.text;
    detail.querySelector('.count').textContent='Step '+(cur+1)+' of '+steps.length;
    $('#step-prev').disabled=cur===0;$('#step-next').disabled=cur===steps.length-1;
  }
  steps.forEach(function(b,i){b.addEventListener('click',function(){goStep(i)})});
  if(steps.length){$('#step-prev').addEventListener('click',function(){goStep(cur-1)});$('#step-next').addEventListener('click',function(){goStep(cur+1)});goStep(0)}

  /* loan timer */
  var tEl=$('#timer-time'),tMsg=$('#timer-msg'),total=20*60,left=total,tick=null;
  function fmt(s){var m=Math.floor(s/60),r=s%60;return (m<10?'0':'')+m+':'+(r<10?'0':'')+r}
  function paint(){tEl.textContent=fmt(left)}
  function stop(){if(tick){clearInterval(tick);tick=null}$('#timer-go').textContent='Start'}
  $$('.t-pre').forEach(function(b){b.addEventListener('click',function(){
    stop();total=+b.dataset.min*60;left=total;tMsg.textContent='';$('#timer').classList.remove('over');
    $$('.t-pre').forEach(function(x){x.setAttribute('aria-pressed',x===b)});paint();
  })});
  if(tEl){
    $('#timer-go').addEventListener('click',function(){
      if(tick){stop();return}
      if(left<=0){left=total;$('#timer').classList.remove('over');tMsg.textContent=''}
      this.textContent='Pause';
      tick=setInterval(function(){
        left--;paint();
        if(left===60)tMsg.textContent='One minute left.';
        if(left<=0){stop();tMsg.textContent='Time is up. Thank the book and return it to the shelf.';$('#timer').classList.add('over')}
      },1000);
    });
    $('#timer-reset').addEventListener('click',function(){stop();left=total;tMsg.textContent='';$('#timer').classList.remove('over');paint()});
    paint();
  }

  /* planning checklist */
  var KEY='eurolibrary-hl-checklist',boxes=$$('.cl input[type=checkbox]'),saved={};
  try{saved=JSON.parse(localStorage.getItem(KEY)||'{}')}catch(e){}
  function progress(){
    var n=boxes.filter(function(b){return b.checked}).length;
    $('#cl-done').textContent=n;$('#cl-bar').style.width=(100*n/boxes.length)+'%';
    $('#cl-bar').parentNode.setAttribute('aria-valuenow',n);
    $$('.cl-group').forEach(function(g){
      var all=$$('input',g),c=all.filter(function(b){return b.checked}).length;
      $('.cl-count',g).textContent=c+'/'+all.length;g.classList.toggle('complete',c===all.length);
    });
  }
  boxes.forEach(function(b){
    if(saved[b.id])b.checked=true;
    b.addEventListener('change',function(){
      saved[b.id]=b.checked;try{localStorage.setItem(KEY,JSON.stringify(saved))}catch(e){}progress();
    });
  });
  var rs=$('#cl-reset');if(rs)rs.addEventListener('click',function(){
    boxes.forEach(function(b){b.checked=false});saved={};try{localStorage.removeItem(KEY)}catch(e){}progress();
  });
  var pr=$('#cl-print');if(pr)pr.addEventListener('click',function(){window.print()});
  progress();

  /* review builder */
  var ta=$('#rev-text'),wc=$('#rev-count'),wb=$('#rev-bar'),wm=$('#rev-msg');
  if(ta){
    function count(){
      var w=(ta.value.trim().match(/\S+/g)||[]).length;
      wc.textContent=w;wb.style.width=Math.min(100,100*w/150)+'%';
      var st=w===0?'':w<50?'A little short. Aim for at least 50 words.':w<=150?'Just right.':'A bit long. Trim it to 150 words or fewer.';
      wm.textContent=st;wb.parentNode.className='meter '+(w===0?'':w<50?'low':w<=150?'ok':'high');
    }
    ta.addEventListener('input',count);count();
    $('#rev-copy').addEventListener('click',function(){
      var b=this;
      function done(){b.textContent='Copied';setTimeout(function(){b.textContent='Copy review'},1600)}
      if(navigator.clipboard)navigator.clipboard.writeText(ta.value).then(done,function(){ta.select();document.execCommand('copy');done()});
      else{ta.select();document.execCommand('copy');done()}
    });
  }
})();
</script>"""


def human_library():
    toc = [("what", "What it is"), ("roles", "Roles and spaces"), ("loan", "How a loan works"),
           ("organise", "Organise yours"), ("books", "Write a book"), ("safe", "Keep it safe"),
           ("impact", "Measure the impact"), ("eurolibrary", "In Eurolibrary"), ("faq", "Questions")]
    toc_html = "".join(f'<li><a href="#{i}">{e(t)}</a></li>' for i, t in toc)
    rules = "".join(f'<li class="rule"><i>{n}</i><h3 class="display h3">{e(t)}</h3><p>{e(p)}</p></li>'
                    for n, (t, p) in enumerate(HL_RULES, 1))
    role_tabs = "".join(
        f'<button class="role-tab" type="button" role="tab" data-role="{i}" aria-selected="false" id="tab-{i}" aria-controls="panel-{i}">{e(n)}</button>'
        for i, n, *_ in HL_ROLES)
    role_panels = "".join(
        f'<div class="role-panel" role="tabpanel" id="panel-{i}" aria-labelledby="tab-{i}" data-role="{i}"><p class="role-kicker">{e(k)}</p><p class="role-text">{e(t)}</p><p class="role-tip"><strong>Tip.</strong> {e(tip)}</p></div>'
        for i, n, k, t, tip in HL_ROLES)
    spaces = '<span class="zone-arrow" aria-hidden="true">&rarr;</span>'.join(
        f'<div class="zone"><span class="zone-no">{n}</span><h3 class="display h3">{e(t)}</h3><p class="zone-k">{e(k)}</p><p>{e(d)}</p></div>'
        for n, (t, k, d) in enumerate(HL_SPACES, 1))
    step_btns = "".join(
        f'<li><button class="step-btn" type="button" data-title="{e(t)}" data-text="{e(d)}"><span class="step-n">{n}</span><span>{e(t)}</span></button></li>'
        for n, (t, d) in enumerate(HL_STEPS, 1))
    total_items = sum(len(items) for _, _, items in HL_PLAN)
    plan = "".join(
        f'<fieldset class="cl-group"><legend><span>{e(t)}</span><span class="cl-count">0/{len(items)}</span></legend>'
        + "".join(f'<label class="cl-item"><input type="checkbox" id="cl-{g}-{n}"><span>{e(x)}</span></label>' for n, x in enumerate(items))
        + "</fieldset>" for g, t, items in HL_PLAN)
    materials = "".join(f"<li>{e(m)}</li>" for m in HL_MATERIALS)
    faq = "".join(f"<details class=\"faq\"><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in HL_FAQ)
    body = f"""  <div class="page-hero split">
    <div class="wrap">
      <div>
        <h1 class="display h1">The Human Library guide</h1>
        <p class="lead">What a Human Library is, why it works and how to organise one, step by step. We learned it by running twenty of them across five countries, and we wrote down everything we would have liked to know on day one.</p>
        <div class="cta">
          <a class="btn btn-primary" href="#organise">Start planning</a>
          <a class="btn btn-ghost" href="assets/downloads/eurolibrary-human-library-handbook.pdf" download>Download the handbook (PDF)</a>
        </div>
      </div>
      <div class="polaroid"><img src="assets/photos/human-library-talk.jpg" alt="Two people talking during a Human Library"></div>
    </div>
  </div>

  <section class="handbook" id="handbook" style="padding-bottom:0">
    <div class="wrap">
      <div class="hb-card">
        <div class="book"><img src="assets/downloads/handbook-cover.jpg" alt="Cover of The Human Library handbook" width="300" height="424" loading="lazy"></div>
        <div>
          <h2 class="display h2">The full handbook</h2>
          <p class="lead">Everything on this page and much more, in a 50 page methodological handbook for organisers: the method, the preparation, the day itself, and seventeen ready to print templates, from the call for books to the consent forms.</p>
          <ul class="hb-facts"><li><b>14</b> chapters</li><li><b>17</b> templates</li><li><b>50</b> pages, A4</li></ul>
          <p><a class="btn btn-primary" href="assets/downloads/eurolibrary-human-library-handbook.pdf" download>Download the handbook (PDF)</a></p>
        </div>
      </div>
    </div>
  </section>

  <div class="wrap guide">
    <aside class="toc" aria-label="Guide contents">
      <p class="toc-h">In this guide</p>
      <ol>{toc_html}</ol>
    </aside>

    <div class="guide-body">

      <section class="g-sec" id="what">
        <h2 class="display h2">You borrow a person, not a book</h2>
        <p class="lead">You walk into a library. Instead of borrowing a book, you borrow a person. They tell you a story, their story: raw, real and often misunderstood.</p>
        <p>The Human Library is a method that creates a safe space for dialogue between people who would not normally meet. It uses the metaphor of a library: the books are people, the readers are the public, and a loan is a conversation. It challenges prejudice by replacing assumptions with a real person, and asks nothing of readers except that they listen.</p>
        <div class="two-col g-two">
          <div>
            <h3 class="display h3">Where it comes from</h3>
            <p>The first Human Library took place in 2000 at a music festival in Denmark, promoted by an anti discrimination association. Festival goers could sit down between concerts with people who were usually labelled by others, and the idea spread. In 2003 the Council of Europe backed the method, and Human Libraries have since been organised on every continent.</p>
          </div>
          <div>
            <h3 class="display h3">What it is for</h3>
            <ul class="checklist" aria-label="What the Human Library is for">
              <li>Building empathy between strangers.</li>
              <li>Breaking stereotypes through contact and dialogue.</li>
              <li>Giving people a voice about their own experience.</li>
              <li>Practising listening without assumptions.</li>
            </ul>
          </div>
        </div>
        <p class="quote">"It is not about agreeing. It is about understanding."</p>
        <h3 class="display h3" style="margin-top:40px">The rules of the library</h3>
        <p class="muted" style="margin-bottom:20px">They are close to the rules of a real library, and they keep everyone safe.</p>
        <ul class="rules" aria-label="The rules of the library">{rules}</ul>
      </section>

      <section class="g-sec" id="roles">
        <h2 class="display h2">Roles and spaces</h2>
        <p class="lead">Every Human Library needs five roles and three spaces. Pick a role to see what it does.</p>
        <div class="roles">
          <div class="role-tabs" role="tablist" aria-label="Roles">{role_tabs}</div>
          <div class="role-panels">{role_panels}</div>
        </div>
        <h3 class="display h3" style="margin-top:48px">Three spaces</h3>
        <p class="muted" style="margin-bottom:20px">A reader walks through them in order.</p>
        <div class="zones">{spaces}</div>
      </section>

      <section class="g-sec" id="loan">
        <h2 class="display h2">How a loan works</h2>
        <p class="lead">From the moment a reader arrives to the moment the book goes back on the shelf. Click through the eight steps.</p>
        <div class="stepper">
          <ol class="step-list">{step_btns}</ol>
          <div class="step-detail" id="step-detail" aria-live="polite">
            <p class="count">Step 1 of {len(HL_STEPS)}</p>
            <h3 class="display h3">Welcome</h3>
            <p>{e(HL_STEPS[0][1])}</p>
            <div class="step-nav">
              <button class="btn btn-ghost" type="button" id="step-prev">Previous</button>
              <button class="btn btn-dark" type="button" id="step-next">Next step</button>
            </div>
          </div>
        </div>
        <div class="timer" id="timer">
          <div>
            <h3 class="display h3">Loan timer</h3>
            <p>Librarians keep the time. Pick a length and press start.</p>
            <div class="t-pres" role="group" aria-label="Loan length">
              <button class="chip t-pre" type="button" data-min="15" aria-pressed="false">15 min</button>
              <button class="chip t-pre" type="button" data-min="20" aria-pressed="true">20 min</button>
              <button class="chip t-pre" type="button" data-min="30" aria-pressed="false">30 min</button>
            </div>
          </div>
          <div class="t-face">
            <p class="t-time" id="timer-time" aria-live="off">20:00</p>
            <p class="t-msg" id="timer-msg" role="status"></p>
            <div class="t-btns"><button class="btn btn-primary" type="button" id="timer-go">Start</button><button class="btn btn-ghost" type="button" id="timer-reset">Reset</button></div>
          </div>
        </div>
      </section>

      <section class="g-sec" id="organise">
        <h2 class="display h2">Organise yours</h2>
        <p class="lead">A checklist built from how we prepared each Eurolibrary mobility. Tick things off as you go: your progress stays in this browser.</p>
        <div class="cl-bar-wrap">
          <div class="meter-row"><p><strong id="cl-done">0</strong> of {total_items} done</p>
            <div class="cl-actions"><a class="chip" href="assets/downloads/eurolibrary-human-library-checklist.pdf" download>Download PDF</a><button class="chip" type="button" id="cl-print">Print</button><button class="chip" type="button" id="cl-reset">Reset</button></div></div>
          <div class="meter" role="progressbar" aria-label="Checklist progress" aria-valuemin="0" aria-valuemax="{total_items}" aria-valuenow="0"><span id="cl-bar"></span></div>
        </div>
        <div class="cl">{plan}</div>
        <div class="two-col g-two" style="margin-top:40px">
          <div>
            <h3 class="display h3">Where and when</h3>
            <p>Choose a place where people already walk by: a square, a school, a library, a community centre or a café. Indoors is safer if the weather is unpredictable. An event can be open to the public or by invitation. Plan about two hours of loans, and start setting up at least three hours before.</p>
          </div>
          <div>
            <h3 class="display h3">What you need</h3>
            <ul class="checklist small materials" aria-label="Materials">{materials}</ul>
          </div>
        </div>
        <figure class="g-fig"><img src="assets/photos/spain-human-library-setup.jpg" alt="A Human Library table under a blue tent in a town square" loading="lazy"><figcaption class="sr">A Human Library set up in a town square</figcaption></figure>
      </section>

      <section class="g-sec" id="books">
        <h2 class="display h2">Write a book</h2>
        <p class="lead">Every book has a title and a short review, like the back cover of a real book. It is the appetizer that helps readers choose.</p>
        <div class="two-col g-two">
          <div>
            <h3 class="display h3">Find your story</h3>
            <p>You do not need a dramatic story, just one you are happy to share. Choose a part of your life, not all of it, and decide in advance what you will not talk about.</p>
            <ul class="checklist small" aria-label="Questions to find your story">
              <li>How do you define yourself, and what do others say about you?</li>
              <li>Which part of your life or work do you want to talk about?</li>
              <li>Which challenges have you overcome, at school, at work or with others?</li>
              <li>What have you done that might surprise people?</li>
            </ul>
          </div>
          <div class="builder">
            <h3 class="display h3">Review builder</h3>
            <p class="muted">Write your review below. Aim for 50 to 150 words.</p>
            <label class="sr" for="rev-text">Your review</label>
            <textarea id="rev-text" rows="8" placeholder="Start with how others see you, then show what they do not see."></textarea>
            <div class="meter-row"><p><strong id="rev-count">0</strong> words</p><p class="rev-msg" id="rev-msg" role="status"></p></div>
            <div class="meter" aria-hidden="true"><span id="rev-bar"></span></div>
            <button class="btn btn-dark" type="button" id="rev-copy" style="margin-top:16px">Copy review</button>
          </div>
        </div>
      </section>

      <section class="g-sec" id="safe">
        <h2 class="display h2">Keep it safe</h2>
        <p class="lead">The method works because people feel safe. Safety is not a side note, it is the job.</p>
        <div class="grid-3">
          <div class="pillar"><h3 class="display h3">Agree the ground rules</h3><p>Co create group agreements before anything else: respect, confidentiality, punctuality and support. What is said in the reading space stays there.</p></div>
          <div class="pillar"><h3 class="display h3">Know your limits</h3><p>Books choose what to share and what to keep. Practise the story with peers first, and agree what you will do if a question goes too far.</p></div>
          <div class="pillar"><h3 class="display h3">Look after each other</h3><p>Form small reflection groups of four or five, a kind of project family. They are the people you can go to when a story stirs something up.</p></div>
        </div>
        <ul class="checklist" style="margin-top:28px" aria-label="Safety practices">
          <li>Keep a librarian within sight of every reading table.</li>
          <li>Give books a quiet place to rest and to talk after a hard loan.</li>
          <li>Ask for consent before taking photos or recordings, and before collecting contact details.</li>
        </ul>
      </section>

      <section class="g-sec" id="impact">
        <h2 class="display h2">Measure the impact</h2>
        <p class="lead">A Human Library changes minds quietly, so give yourself a way to see it.</p>
        <div class="grid-3">
          <div class="pillar"><i>During</i><h3 class="display h3">Keep count</h3><p>Note each loan and which book it was. It shows which stories reach people and when books need a rest.</p></div>
          <div class="pillar"><i>With readers</i><h3 class="display h3">Ask and keep in touch</h3><p>Ask for a short evaluation. With explicit consent, collect an email so readers can follow the project and receive videos and podcasts afterwards.</p></div>
          <div class="pillar"><i>With the team</i><h3 class="display h3">Reflect and improve</h3><p>Use the last day for reflection and feedback forms. Write down what to change next time.</p></div>
        </div>
      </section>

      <section class="g-sec" id="eurolibrary">
        <h2 class="display h2">In Eurolibrary</h2>
        <p class="lead">Each of the five mobilities ran at least four Human Libraries, on trains, ferries, in squares, in museums, in cafés and in local schools.</p>
        <div class="counters four" style="margin:32px 0 0">
          {stats_block([("20", "Human Library events, 4 per chapter"), ("20 to 30", "Readers per event, on average"), ("125", "Human Books in the catalogue"), ("5", "Countries represented")])}
        </div>
        <div class="grid-3" style="margin-top:32px">
          <div class="pillar"><h3 class="display h3">Prepared together</h3><p>A full group meeting three weeks before, team meetings two weeks before and the catalogue closed a week ahead, with a title and a teaser for every story.</p></div>
          <div class="pillar"><h3 class="display h3">Built on the first day</h3><p>Ice breakers, group agreements and small reflection groups came first. The Human Libraries filled days two to five.</p></div>
          <div class="pillar"><h3 class="display h3">Always something to do</h3><p>While some participants were books, others ran games, promoted the event and filmed short videos, so everybody had a role.</p></div>
        </div>
        <div class="photo-row" style="margin-top:32px"><figure><img src="assets/photos/greece-red-room.jpg" alt="A conversation circle in a room with red curtains" loading="lazy"></figure>
        <figure><img src="assets/photos/human-library-table.jpg" alt="An information table with leaflets and a small globe" loading="lazy"></figure></div>
        <p style="margin-top:24px"><a class="btn btn-ghost" href="index.html#destinations">See the five chapters</a></p>
      </section>

      <section class="g-sec" id="faq">
        <h2 class="display h2">Questions we are often asked</h2>
        <div class="faqs">{faq}</div>
      </section>

    </div>
  </div>

  <section style="padding-top:0">
    <div class="wrap">
      <div class="join">
        <h2 class="display h2">Ready to open your own library?</h2>
        <p class="lead">Start with the checklist, or tell us what you are planning. We are glad to help.</p>
        <p class="cta-row"><a class="btn btn-primary" href="#organise">Open the checklist</a> <a class="btn btn-ghost on-dark" href="about.html#contact">Get in touch</a></p>
      </div>
    </div>
  </section>
{HL_SCRIPT}"""
    return page("hl", "The Human Library guide",
                "A guide to the Human Library method: what it is, the roles and rules, how a loan works and how to organise your own, with a checklist and tools.", body)


PODCAST_ID = "1WtlYaA3IX5eSzW3NonMTU"
PODCAST_URL = f"https://open.spotify.com/show/{PODCAST_ID}"
# Los episodios (título, fecha, descripción, audio y portada) salen de tools/podcast_all.py,
# que genera tools/podcast_sync.py a partir del feed RSS del programa.
POD_TAGS = [("identity", "Identity and belonging"), ("journeys", "Journeys and borders"),
            ("health", "Health and mind"), ("sport", "Sport"), ("nature", "Nature"), ("work", "Work and ideas")]
# Enlaces directos a Spotify de los episodios que se conocen. El resto enlaza a la búsqueda del título.
SPOTIFY_IDS = {'From tulips to olive trees': '5xO0poKtNFYFQ6DRtZzGmY', 'Full, but not filled': '0kMWU6A3GgwhhdLj7ysnvX', 'Between Two Worlds': '1p7TkWes3AkyiLXRescwIO', 'Chasing Freedom on Two Skis': '0evcFH79CgbJOB2PxcLxys', 'All the tales we used to believe': '6iTZlIDDHCW8uR3iL4nXXp', 'You Reap What You Sow: How I Learned That My Roots Travel Faster Than I Do': '4cXsiThBOhcTzTlrSg7gjj', 'Choosing health': '2DCAEEvRbYIy6ldo9GsNar', 'Rails of Passion': '3OwqtjcKreaMUZtWw62yew', 'How I run a whole country': '7kcuASm3aD98r9RrwjXvAe', 'Finding the right path': '3hyixc1eXaRiIMIiZ6T6sT', 'Born Twice, Growing Once': '5L7CXLOYxV95n5DdnjaDLs', 'Two Hours to a Dream': '62H28nz67jZsZiEKrQ3sB6', 'I work on an educational game about circular economy': '6MwcV8OLYqVzdWQg2wDqpj'}
# Temas revisados a mano. Los demás se asignan por palabras clave en el título y la descripción.
POD_TAGS_CURATED = {'From tulips to olive trees': ['identity', 'journeys'], 'Full, but not filled': ['health'], 'Between Two Worlds': ['identity', 'journeys'], 'Chasing Freedom on Two Skis': ['sport', 'identity'], 'All the tales we used to believe': ['nature'], 'You Reap What You Sow: How I Learned That My Roots Travel Faster Than I Do': ['nature', 'journeys'], 'Choosing health': ['health'], 'Rails of Passion': ['work'], 'How I run a whole country': ['sport'], 'Finding the right path': ['health', 'identity'], 'Born Twice, Growing Once': ['journeys'], 'Two Hours to a Dream': ['sport', 'journeys'], 'I work on an educational game about circular economy': ['work', 'nature'], 'Home is where I park It': ['journeys', 'identity'], 'A Tale of Two Cities': ['work'], 'Stopping, losing, learning': ['health'], 'Appreciate the small things': ['health'], 'The quest to bring life back to life': ['journeys', 'identity'], 'Brewing change from the kitchen': ['health'], 'The book': ['health', 'sport'], 'Where Im standing': ['journeys', 'identity'], 'How one „Yes“ changed my life': ['identity'], 'She who asks too many questions': ['identity', 'work'], 'A girl with a dream': ['identity'], 'Neither from here nor from there': ['identity', 'journeys'], "No Man's Home": ['health']}
POD_KEYWORDS = {
    "identity": ["identity", "belong", "who i am", "roots", "culture", "tradition", "self", "myself", "queer", "gender", "language", "third culture", "authentic"],
    "journeys": ["migrat", "border", "refugee", "war", "abroad", "country", "countries", "immigr", "expat", "homeland", "moving", "moved", "journey", "travel", "pilgrim", "road", "greece", "return", "far from home", "new country"],
    "health": ["health", "body", "mental", "anxiety", "depress", "therapy", "eating", "food", "burnout", "panic", "fear", "trauma", "healing", "mind", "addiction", "smok", "cancer", "pain", "wellbeing", "stress", "balance", "taboo", "breath", "darkness", "self acceptance"],
    "sport": ["sport", " run", "running", "ski", "football", "marathon", "cycl", "bike", "climb", "hik", "mountain", "swim", "surf", "muscle", "training", "pedal", "peak", "judo", "athlet", "trek"],
    "nature": ["nature", "eco", "green", "recycl", "waste", "environment", "climate", "sustainab", "planet", "garden", "tree", "wild", "animal", "forest", "ocean", "plastic", "vegan", "zero waste", "biology"],
    "work": ["business", "entrepreneur", "startup", "career", "professional", "company", "game", "technolog", "design", "social enterprise", "educator", "volunteer", "project", "innovation", "leader", "calling", "work", "studies", "job", "create", "crafting"],
}


def pod_tags(ep):
    if ep["title"] in POD_TAGS_CURATED:
        return POD_TAGS_CURATED[ep["title"]]
    hay = " " + (ep["title"] + " " + ep["text"]).lower() + " "
    scores = [(sum(hay.count(w) for w in ws), k) for k, ws in POD_KEYWORDS.items()]
    scores = [x for x in sorted(scores, reverse=True) if x[0] > 0][:2]
    return [k for _, k in scores]


def pod_date(iso):
    import datetime
    d = datetime.date.fromisoformat(iso)
    return f"{d.day} {d.strftime('%B')} {d.year}"


def podcast():
    tag_name = dict(POD_TAGS)
    chips = '<button class="chip" type="button" data-tag="all" aria-pressed="true">All episodes</button>' + "".join(
        f'<button class="chip" type="button" data-tag="{k}" aria-pressed="false">{e(v)}</button>' for k, v in POD_TAGS)
    eps = podcast_all.ALL
    cards = []
    for i, x in enumerate(eps):
        tg = pod_tags(x)
        sid = SPOTIFY_IDS.get(x["title"])
        spot = (f"https://open.spotify.com/episode/{sid}" if sid
                else "https://open.spotify.com/search/" + urllib.parse.quote(x["title"]))
        spot_l = "Open in Spotify" if sid else "Find on Spotify"
        no = f'<span class="ep-no">Ep. {x["no"]}</span>' if x.get("no") else ""
        search = (x["title"] + " " + x["text"] + " " + " ".join(tag_name[t] for t in tg)).lower()
        tagline = "".join(f"<span>{e(tag_name[t])}</span>" for t in tg)
        cards.append(f"""        <article class="ep" id="ep-{x['cover'][:8]}" data-i="{i}" data-date="{x['date']}" data-tags="{' '.join(tg)}" data-audio="{e(x['audio'])}" data-search="{e(search)}">
          <div class="ep-main">
            <img src="assets/podcast/ep/{x['cover']}" alt="" width="112" height="112" loading="lazy">
            <div class="ep-body">
              <p class="ep-meta">{no}{e(pod_date(x['date']))} · {x['secs'] // 60} min</p>
              <h3 class="display h3">{e(x['title'])}</h3>
              <p>{e(x['text'])}</p>
              <p class="ep-tags">{tagline}</p>
            </div>
          </div>
          <div class="ep-actions">
            <button class="btn btn-dark ep-play" type="button" aria-expanded="false">Play here</button>
            <a class="ep-link" href="{spot}" target="_blank" rel="noopener">{spot_l}</a>
          </div>
          <div class="ep-embed" hidden></div>
        </article>""")
    cards = "\n".join(cards)
    n = len(eps)
    body = f"""  <div class="page-hero split">
    <div class="wrap">
      <div>
        <h1 class="display h1">People of EU, the podcast</h1>
        <p class="lead">What happens when you truly listen to someone's story? Real voices, real journeys and real experiences from across Europe, told by the people who lived them. No headlines, no stereotypes. Just human stories.</p>
        <div class="cta">
          <a class="btn btn-primary" href="#player">Press play</a>
          <a class="btn btn-ghost" href="#episodes">Browse the episodes</a>
        </div>
      </div>
      <div class="polaroid"><img src="assets/podcast/show.jpg" alt="People of EU podcast cover: an orange cassette tape and the words 100 stories worth sharing from all over Europe" style="aspect-ratio:1/1"></div>
    </div>
  </div>

  <section id="player" style="padding-top:32px">
    <div class="wrap">
      <div class="pod-player">
        <div class="pod-copy">
          <h2 class="display h2">Listen to the whole series</h2>
          <p>The Human Library puts stories in people's mouths. This podcast carries them further. Each episode is a short personal story, from overcoming anxiety to starting over in a new country, choosing a sustainable life or finding identity through sport.</p>
          <ul class="pod-facts">
            <li><strong>{n}</strong> episodes</li>
            <li><strong>Feb to May</strong> 2026</li>
            <li><strong>Short</strong> personal stories</li>
          </ul>
        </div>
        <div class="pod-embed" id="show-embed">
          <button class="pod-load" type="button" data-src="https://open.spotify.com/embed/show/{PODCAST_ID}?utm_source=generator">
            <img src="assets/podcast/show.jpg" alt="" width="96" height="96">
            <span class="display">Load the Spotify player</span>
            <small>Content is loaded from Spotify, which may set cookies.</small>
          </button>
        </div>
      </div>
    </div>
  </section>

  <section id="episodes" style="padding-top:0">
    <div class="wrap">
      <div class="section-head" style="margin-bottom:32px">
        <h2 class="display h2">Pick a story</h2>
        <p class="lead muted">All {n} episodes. Filter by theme, search by word or let us choose for you. Press play and the episode opens right here.</p>
      </div>
      <div class="pod-tools">
        <div class="chips" role="group" aria-label="Filter by theme">{chips}</div>
        <div class="pod-find">
          <label class="sr" for="pod-search">Search episodes</label>
          <input id="pod-search" type="search" placeholder="Search episodes" autocomplete="off">
          <label class="sr" for="pod-sort">Sort</label>
          <select id="pod-sort"><option value="new">Newest first</option><option value="old">Oldest first</option></select>
          <button class="btn btn-primary" type="button" id="pod-random">Surprise me</button>
        </div>
      </div>
      <p class="pod-count" id="pod-count" aria-live="polite">Showing {n} of {n} episodes</p>
      <div class="ep-grid" id="ep-grid">
{cards}
      </div>
      <p class="pod-empty" id="pod-empty" hidden>No episode matches that search. Try another word or clear the filters.</p>
      <p class="pod-more"><button class="btn btn-ghost" type="button" id="pod-more">Show more stories</button></p>
    </div>
  </section>

  <section style="padding-top:0">
    <div class="wrap">
      <div class="join">
        <h2 class="display h2">Keep listening</h2>
        <p class="lead">Follow People of EU on Spotify so the next story finds you, or meet the method that inspired it.</p>
        <p class="cta-row"><a class="btn btn-primary" href="{PODCAST_URL}" target="_blank" rel="noopener">Follow on Spotify</a> <a class="btn btn-ghost on-dark" href="human-library.html">Explore the Human Library</a></p>
      </div>
    </div>
  </section>
""" + POD_SCRIPT
    return page("podcast", "People of EU, the podcast",
                "Short personal stories from across Europe, told by the people who lived them. Listen to every episode of People of EU, the Eurolibrary podcast, right here.", body)


POD_SCRIPT = r"""<script>
(function(){
  var grid=document.getElementById('ep-grid'),cards=[].slice.call(grid.querySelectorAll('.ep')),
      chips=[].slice.call(document.querySelectorAll('#episodes .chip')),q=document.getElementById('pod-search'),
      sortSel=document.getElementById('pod-sort'),count=document.getElementById('pod-count'),empty=document.getElementById('pod-empty'),
      more=document.getElementById('pod-more'),tag='all',limit=12,PAGE=12,cur=null;
  function fmt(s){s=Math.floor(s||0);var m=Math.floor(s/60),r=s%60;return m+':'+(r<10?'0':'')+r}
  /* reproductor de audio propio */
  function closeP(c){
    var b=c.querySelector('.ep-play'),h=c.querySelector('.ep-embed'),a=c._audio;
    if(a){a.pause();a.removeAttribute('src');a.load();c._audio=null}
    c.classList.remove('playing');b.textContent='Play here';b.setAttribute('aria-expanded','false');h.hidden=true;h.replaceChildren();
  }
  function build(c){
    var h=c.querySelector('.ep-embed'),a=new Audio();a.preload='none';a.src=c.dataset.audio;c._audio=a;
    var ui=document.createElement('div');ui.className='ap';
    ui.innerHTML='<button type="button" class="ap-b" aria-label="Play"></button><input type="range" class="ap-r" min="0" max="1000" value="0" aria-label="Seek"><span class="ap-t">0:00</span><button type="button" class="ap-s" aria-label="Playback speed">1x</button><p class="ap-e" role="alert" hidden>The audio could not be loaded. Open the episode on Spotify instead.</p>';
    h.appendChild(ui);
    var b=ui.querySelector('.ap-b'),r=ui.querySelector('.ap-r'),t=ui.querySelector('.ap-t'),sp=ui.querySelector('.ap-s'),er=ui.querySelector('.ap-e'),drag=false,speeds=[1,1.25,1.5,2],si=0;
    function paint(){var d=a.duration||0;if(!drag&&d)r.value=1000*a.currentTime/d;t.textContent=fmt(a.currentTime)+' / '+(d?fmt(d):'...');ui.classList.toggle('on',!a.paused)}
    b.addEventListener('click',function(){if(a.paused){var p=a.play();if(p&&p.catch)p.catch(function(){er.hidden=false})}else a.pause()});
    a.addEventListener('play',function(){b.setAttribute('aria-label','Pause');paint()});
    a.addEventListener('pause',function(){b.setAttribute('aria-label','Play');paint()});
    a.addEventListener('timeupdate',paint);a.addEventListener('loadedmetadata',paint);a.addEventListener('ended',paint);
    a.addEventListener('error',function(){er.hidden=false});
    r.addEventListener('input',function(){drag=true;if(a.duration)t.textContent=fmt(a.duration*r.value/1000)+' / '+fmt(a.duration)});
    r.addEventListener('change',function(){if(a.duration)a.currentTime=a.duration*r.value/1000;drag=false});
    sp.addEventListener('click',function(){si=(si+1)%speeds.length;a.playbackRate=speeds[si];sp.textContent=speeds[si]+'x'});
    var p=a.play();if(p&&p.catch)p.catch(function(){});
  }
  function play(c){
    if(c.classList.contains('playing')){closeP(c);cur=null;return}
    if(cur&&cur!==c)closeP(cur);
    var b=c.querySelector('.ep-play'),h=c.querySelector('.ep-embed');
    c.classList.add('playing');b.textContent='Close player';b.setAttribute('aria-expanded','true');h.hidden=false;build(c);cur=c;
  }
  cards.forEach(function(c){c.querySelector('.ep-play').addEventListener('click',function(){play(c)})});
  /* filtros, orden y paginación */
  function match(c){var t=q.value.trim().toLowerCase();return(tag==='all'||c.dataset.tags.split(' ').indexOf(tag)>-1)&&(!t||c.dataset.search.indexOf(t)>-1)}
  function apply(){
    var old=sortSel.value==='old',list=cards.slice().sort(function(a,b){return old?(a.dataset.date<b.dataset.date?-1:a.dataset.date>b.dataset.date?1:b.dataset.i-a.dataset.i):(a.dataset.i-b.dataset.i)});
    var shown=0,total=0;
    list.forEach(function(c){grid.appendChild(c);var ok=match(c);if(ok)total++;var vis=ok&&shown<limit;if(vis)shown++;c.hidden=!vis;if(!vis&&c===cur){closeP(c);cur=null}});
    count.textContent='Showing '+shown+' of '+total+' episodes';empty.hidden=total>0;more.hidden=shown>=total;
  }
  chips.forEach(function(b){b.addEventListener('click',function(){tag=b.dataset.tag;limit=PAGE;chips.forEach(function(x){x.setAttribute('aria-pressed',x===b)});apply()})});
  q.addEventListener('input',function(){limit=PAGE;apply()});
  sortSel.addEventListener('change',function(){limit=PAGE;apply()});
  more.addEventListener('click',function(){limit+=PAGE;apply()});
  document.getElementById('pod-random').addEventListener('click',function(){
    tag='all';chips.forEach(function(x){x.setAttribute('aria-pressed',x.dataset.tag==='all')});q.value='';
    var c=cards[Math.floor(Math.random()*cards.length)];
    sortSel.value='new';
    var pos=cards.slice().sort(function(a,b){return a.dataset.i-b.dataset.i}).indexOf(c);
    if(pos>=limit)limit=pos+1;apply();
    c.scrollIntoView({behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth',block:'center'});
    c.classList.add('pulse');setTimeout(function(){c.classList.remove('pulse')},1800);
    if(!c.classList.contains('playing'))play(c);
  });
  var load=document.querySelector('.pod-load');
  if(load)load.addEventListener('click',function(){
    var h=document.getElementById('show-embed'),f=document.createElement('iframe');
    f.src=load.dataset.src;f.width='100%';f.height='352';f.loading='lazy';
    f.setAttribute('allow','autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture');
    f.setAttribute('title','Spotify player');f.style.border='0';f.style.borderRadius='12px';h.replaceChildren(f);h.classList.add('live');
  });
  apply();
})();
</script>"""


def contact_section():
    return f"""

  <section id="contact" style="padding-top:0">
    <div class="wrap">
      <div class="section-head" style="margin-bottom:32px">
        <h2 class="display h2">Get in touch</h2>
        <p class="lead muted">Reviewing the project, curious about the method or up for a collaboration? Write to us and we will get back to you.</p>
      </div>
      <div class="two-col">
        <form class="contact" id="contact-form" novalidate>
          <div class="field"><label for="f-name">First name</label><input id="f-name" name="name" type="text" autocomplete="given-name" required></div>
          <div class="field"><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email" required></div>
          <div class="field"><label for="f-msg">Message</label><textarea id="f-msg" name="message" required></textarea></div>
          <div><button class="btn btn-primary" type="submit">Send message</button></div>
          <p class="form-note" id="form-status" role="status"></p>
        </form>
        <div>
          <h3 class="display h3">Write to us directly</h3>
          <p>The project is completed, but the team still answers questions about the method, the results and possible collaborations.</p>
          <div class="email-line"><code>{EMAIL}</code><button class="btn btn-ghost" type="button" id="copy-email">Copy address</button></div>
        </div>
      </div>
    </div>
  </section>"""


PAGES = {"index.html": home, "about.html": about, "human-library.html": human_library, "podcast.html": podcast}
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


FX = """<script>
(function(){
  var calm=matchMedia('(prefers-reduced-motion: reduce)').matches;
  /* barra de progreso de lectura */
  var sp=document.querySelector('.sp');
  if(sp&&!calm){
    var tick=false;
    function prog(){var h=document.documentElement.scrollHeight-innerHeight;sp.style.setProperty('--p',h>0?Math.min(1,scrollY/h):0);tick=false}
    addEventListener('scroll',function(){if(!tick){tick=true;requestAnimationFrame(prog)}},{passive:true});prog();
  }
  if(calm||!('IntersectionObserver' in window))return;
  /* aparición al hacer scroll */
  var sel='.section-head,.card,.ticket,.pillar,.fact,.stop,.counter,.polaroid,.join,.ep,.hb-card,.photo-row figure,.carousel,.rule,.role,.zone,.cl-group,.faq,.pod-player,.pager>*,.grid-3>*,.quotes blockquote,.voices>*,.two-col>*,.timeline-years li,.pod-tools,.builder,.stepper,.timer';
  var els=[].slice.call(document.querySelectorAll('main '+sel.split(',').join(',main '))).filter(function(el){
    return !el.closest('.hero,.page-hero')&&!el.closest('.rv');
  });
  var io=new IntersectionObserver(function(es){es.forEach(function(e){
    if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}
  })},{threshold:.12,rootMargin:'0px 0px -6% 0px'});
  els.forEach(function(el){
    var sib=[].slice.call(el.parentNode.children).filter(function(c){return els.indexOf(c)>-1});
    el.style.setProperty('--d',Math.min(sib.indexOf(el),5)*80+'ms');
    el.classList.add('rv');io.observe(el);
  });
  /* las imágenes con carga diferida aparecen con un fundido */
  [].slice.call(document.querySelectorAll('main img[loading="lazy"]')).forEach(function(im){
    if(im.complete&&im.naturalWidth)return;
    im.classList.add('fd');
    var ok=function(){im.classList.add('ld')};
    im.addEventListener('load',ok);im.addEventListener('error',ok);
  });
})();
</script>"""


def clean_links(doc):
    """Quita .html de los enlaces internos. Vercel los sirve con cleanUrls (vercel.json)."""
    def repl(m):
        name, frag = m.group(1), m.group(2) or ""
        return 'href="/' + ("" if name == "index" else name) + frag + '"'
    return re.sub(r'href="([a-z][a-z-]*)\.html(#[^"]*)?"', repl, doc)


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
            doc = clean_links(doc)
        with open(os.path.join(out, name), "w", encoding="utf8") as f:
            f.write(doc)
        print("escrito", os.path.join(out, name))


if __name__ == "__main__":
    main()
