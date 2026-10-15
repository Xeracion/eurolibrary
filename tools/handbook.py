#!/usr/bin/env python3
"""Genera assets/downloads/eurolibrary-human-library-handbook.pdf (manual metodológico, A4).

Uso: python3 tools/handbook.py [--html]   (--html deja también el HTML para depurar)
Necesita Chromium (variable CHROMIUM o /opt/pw-browsers/chromium) y pdftotext (poppler).
El texto está en tools/handbook_content.py y los estilos del sitio en css/site.css."""
import os
import re
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import handbook_content as C  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "downloads", "eurolibrary-human-library-handbook.pdf")
FONTS = os.path.join(ROOT, "tools", "fonts")
PH = f"file://{ROOT}/assets/photos/"
EU_DISCLAIMER = ("Funded by the European Union. Views and opinions expressed are however those of the author(s) only "
                 "and do not necessarily reflect those of the European Union or the European Education and Culture "
                 "Executive Agency (EACEA). Neither the European Union nor EACEA can be held responsible for them.")

CHAPTERS = [
    # (no, parte, título, foto, posición, cuerpo)
    (1, "Part 1 · Understand", "What is a Human Library?", "human-library-talk.jpg", "50% 50%", C.CH1),
    (2, "Part 1 · Understand", "Roles and spaces", "spain-human-library-setup.jpg", "50% 60%", C.CH2),
    (3, "Part 1 · Understand", "How a loan works", "spain-hl-talk.jpg", "50% 45%", C.CH3),
    (4, "Part 1 · Understand", "Safety, ethics and inclusion", "greece-school-banners.jpg", "50% 50%", C.CH4),
    (5, "Part 2 · Prepare", "Plan your Human Library", "greece-ferry-circle.jpg", "50% 50%", C.CH5),
    (6, "Part 2 · Prepare", "Choose and set up the venue", "about-classroom.jpg", "50% 50%", C.CH6),
    (7, "Part 2 · Prepare", "Recruit and prepare the books", "spain-hl-conversation.jpg", "50% 40%", C.CH7),
    (8, "Part 2 · Prepare", "Build the team and bring in readers", "greece-circle-dance.jpg", "50% 45%", C.CH8),
    (9, "Part 2 · Prepare", "The Eurolibrary model", "greece-ios-group.jpg", "50% 60%", C.CH9),
    (10, "Part 3 · Run", "Run the day", "greece-performance.jpg", "50% 50%", C.CH10),
    (11, "Part 3 · Run", "Facilitation toolkit", "greece-red-room.jpg", "50% 50%", C.CH11),
    (12, "Part 4 · Evaluate and share", "Evaluate and report", "spain-hostel-group.jpg", "50% 50%", C.CH12),
    (13, "Part 4 · Evaluate and share", "From the library to a podcast", "about-banner.jpg", "50% 30%", C.CH13),
    (14, "Part 4 · Evaluate and share", "Lessons learned and FAQ", "spain-obradoiro-group.jpg", "50% 60%", C.CH14),
]

FLOORPLAN = """<svg class="plan" viewBox="0 0 560 250" role="img" aria-label="Floor plan of a Human Library: entrance, reception, bookshelf and reading space">
<rect x="2" y="2" width="556" height="246" rx="14" fill="#fff" stroke="#e5e5e5" stroke-width="2"/>
<rect x="20" y="30" width="120" height="190" rx="10" fill="#f3e4d6"/><text x="80" y="58" text-anchor="middle" class="t1">1 Reception</text>
<rect x="40" y="82" width="80" height="26" rx="5" fill="#c4521a"/><text x="80" y="99" text-anchor="middle" class="t3">desk and catalogue</text>
<text x="80" y="140" text-anchor="middle" class="t2">rules poster</text><text x="80" y="158" text-anchor="middle" class="t2">sign in sheet</text><text x="80" y="176" text-anchor="middle" class="t2">roll up banner</text>
<rect x="170" y="30" width="230" height="190" rx="10" fill="#e9f1f8"/><text x="285" y="58" text-anchor="middle" class="t1">3 Reading space</text>
<g fill="#fff" stroke="#3f78a8" stroke-width="2"><rect x="190" y="80" width="64" height="40" rx="8"/><rect x="316" y="80" width="64" height="40" rx="8"/><rect x="190" y="148" width="64" height="40" rx="8"/><rect x="316" y="148" width="64" height="40" rx="8"/></g>
<g class="t2" text-anchor="middle"><text x="222" y="105">table 1</text><text x="348" y="105">table 2</text><text x="222" y="173">table 3</text><text x="348" y="173">table 4</text></g>
<rect x="428" y="30" width="112" height="190" rx="10" fill="#f6e3d4"/><text x="484" y="58" text-anchor="middle" class="t1">2 Bookshelf</text>
<g fill="#1b1917"><circle cx="458" cy="110" r="8"/><circle cx="484" cy="110" r="8"/><circle cx="510" cy="110" r="8"/><circle cx="458" cy="140" r="8"/><circle cx="484" cy="140" r="8"/></g>
<text x="484" y="176" text-anchor="middle" class="t2">books wait, water,</text><text x="484" y="192" text-anchor="middle" class="t2">out of earshot</text>
<g stroke="#9894a8" stroke-width="2.5" fill="none" marker-end="url(#a)"><path d="M144 125 H166"/><path d="M404 125 H424"/></g>
<defs><marker id="a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#9894a8"/></marker></defs>
<text x="12" y="244" class="t2">Entrance at the left. The quiet corner can sit next to the bookshelf.</text>
</svg>"""

TIMELINE = """<div class="tl"><div class="tl-bar"><span style="width:8%" class="a">2</span><span style="width:66%" class="b">The conversation, 20 minutes</span><span style="width:10%" class="a">5</span><span style="width:16%" class="c">Feedback</span></div>
<div class="tl-k"><span>0</span><span>2 min: introduce</span><span>22 min: time is up</span><span>25 min: return</span><span>30 min: feedback done</span></div></div>"""

ANNEX_OPENER = "netherlands-table.jpg"


def e(s):
    return s


def opener(no, part, title, photo, pos):
    return f"""<div class="band" style="background-image:url('{PH}{photo}');background-position:{pos}"></div>
<p class="eyebrow">Chapter {no}</p><p class="part">{part}</p><h1>{title}</h1>"""


def chapter(no, part, title, photo, pos, body):
    body = body.replace("{FLOORPLAN}", FLOORPLAN).replace("{TIMELINE}", TIMELINE).replace("@PH@", PH)
    return f'<section class="chapter">{opener(no, part, title, photo, pos)}{body}</section>'


def toc_html(pages):
    def row(label, title, key):
        n = pages.get(key, "")
        return f'<li><span class="tn">{label}</span><span class="tt">{title}</span><span class="tp">{n}</span></li>'
    parts = {}
    for no, part, title, *_ in C_CHAPTERS:
        parts.setdefault(part, []).append(row(f"{no:02d}", title, f"c{no}"))
    out = ""
    for part, rows in parts.items():
        out += f'<h3>{part.split(" · ")[0]}<small>{part.split(" · ")[1]}</small></h3><ul class="toc">{"".join(rows)}</ul>'
    arows = "".join(row(code, title, f"a{code}") for code, title, *_ in C.A)
    arows += row("R", "Resources and glossary", "aR")
    out += f'<h3>Annexes<small>Materials and resources</small></h3><ul class="toc two">{arows}</ul>'
    return out


C_CHAPTERS = CHAPTERS

CSS = f"""
@font-face{{font-family:'DM Serif Display';src:url('file://{FONTS}/DMSerifDisplay-400.woff2') format('woff2');font-weight:400}}
@font-face{{font-family:'Inter';src:url('file://{FONTS}/Inter-var.woff2') format('woff2');font-weight:400 600}}
@page{{size:A4;margin:14mm 16mm 19mm;background:#faf2ec;
  @bottom-left{{content:"The Human Library handbook \\00B7  Eurolibrary";font:400 7.5pt 'Inter',sans-serif;color:#6f6b73;vertical-align:top;padding-top:6mm}}
  @bottom-right{{content:counter(page);font:500 8pt 'Inter',sans-serif;color:#1b1917;vertical-align:top;padding-top:6mm}}}}
@page cover{{margin:0;@bottom-left{{content:none}}@bottom-right{{content:none}}}}
:root{{--cream:#faf2ec;--deep:#f3e4d6;--ink:#1b1917;--ash:#6f6b73;--orange:#c4521a;--soft:#f2b48c;--sky:#a9cbe8;--mist:#e5e5e5}}
*{{box-sizing:border-box;margin:0;padding:0}}
html{{-webkit-print-color-adjust:exact;print-color-adjust:exact}}
body{{font-family:'Inter',sans-serif;font-size:9.4pt;line-height:1.5;color:var(--ink);background:var(--cream)}}
h1,h2,h3,h4,.display{{font-family:'DM Serif Display',serif;font-weight:400}}
h1{{font-size:27pt;line-height:1.05;margin:1mm 0 4mm;break-after:avoid}}
h2{{font-size:14.5pt;line-height:1.15;margin:5.5mm 0 2mm;break-after:avoid}}
h3{{font-size:12pt;line-height:1.2;margin:4mm 0 1.5mm;break-after:avoid}}
p{{margin:0 0 2.6mm}}
.lead{{font-size:11.3pt;line-height:1.5;margin-bottom:4mm}}
.small{{font-size:8.2pt;color:var(--ash)}}
b{{font-weight:600}}
.chapter{{break-before:page}}
.eyebrow{{font-size:8pt;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--orange);margin-top:4mm}}
.part{{font-size:8pt;color:var(--ash);margin:0}}
.band{{height:50mm;border-radius:3mm;background-size:cover}}
/* cover */
.cover{{page:cover;position:relative;width:210mm;height:297mm;color:#fff;overflow:hidden;break-after:page;
  background:linear-gradient(180deg,rgba(27,25,23,.15) 0%,rgba(27,25,23,.55) 55%,rgba(27,25,23,.94) 100%),url('{PH}spain-hl-conversation.jpg') 40% 20%/cover}}
.cover img{{position:absolute;left:18mm;top:16mm;height:16mm;filter:brightness(0) invert(1)}}
.cover .t{{position:absolute;left:18mm;right:18mm;bottom:56mm}}
.cover .k{{font-size:9pt;letter-spacing:.14em;text-transform:uppercase;color:var(--soft);font-weight:600;margin-bottom:5mm}}
.cover h1{{font-size:50pt;line-height:1;margin:0 0 6mm}}
.cover p{{font-size:13pt;line-height:1.4;max-width:140mm;color:#ece3da}}
.cover .f{{position:absolute;left:18mm;right:18mm;bottom:16mm;display:flex;gap:6mm;align-items:center;font-size:7pt;color:#cfc4ba;line-height:1.4}}
.cover .f img{{position:static;height:11mm;filter:none;flex:none}}
.cover .badge{{display:inline-block;background:var(--orange);color:#fff;font-size:8pt;font-weight:600;border-radius:999px;padding:1.5mm 4mm;margin-top:6mm}}
/* about page */
.about .stats{{display:grid;grid-template-columns:repeat(4,1fr);gap:3mm;margin:5mm 0 2mm}}
.about .stats div{{background:#fff;border-radius:3mm;padding:4mm;text-align:center}}
.about .stats b{{display:block;font-family:'DM Serif Display',serif;font-weight:400;font-size:24pt;line-height:1;color:var(--orange)}}
.about .stats span{{font-size:7.6pt;color:var(--ash);line-height:1.3;display:block;margin-top:1.5mm}}
.credits{{margin-top:6mm;padding-top:4mm;border-top:1px solid var(--mist);font-size:7.8pt;color:var(--ash)}}
.credits img{{height:11mm;margin-bottom:2mm}}
/* toc */
.tocpage{{break-before:page}}
.tocpage h3{{margin:5mm 0 1.5mm;font-size:12pt;color:var(--orange)}}
.tocpage h3 small{{font-family:'Inter',sans-serif;font-size:7.8pt;color:var(--ash);margin-left:3mm}}
.toc{{list-style:none}}
.toc li{{display:flex;gap:3mm;align-items:baseline;padding:1.1mm 0;border-bottom:1px dotted #cfc4ba;font-size:9.4pt}}
.toc .tn{{width:8mm;color:var(--orange);font-weight:600;flex:none}}
.toc .tt{{flex:1}}
.toc .tp{{font-weight:600;flex:none}}
.toc.two{{columns:2;column-gap:10mm}}
.toc.two li{{break-inside:avoid}}
/* boxes */
.box{{border-radius:3mm;padding:4mm 5mm 2.5mm;margin:4mm 0;break-inside:avoid;background:#fff;border-left:1.2mm solid var(--orange)}}
.box.tip{{background:var(--deep)}}
.box.euro{{background:#e9f1f8;border-left-color:#3f78a8}}
.box.care{{background:#fdecec;border-left-color:#b3261e}}
.box.key{{background:var(--ink);color:#fff;border-left-color:var(--soft)}}
.box-t{{font-weight:600;font-size:8.6pt;letter-spacing:.06em;text-transform:uppercase;margin-bottom:1.5mm;color:var(--orange)}}
.box.euro .box-t{{color:#3f78a8}}.box.care .box-t{{color:#b3261e}}.box.key .box-t{{color:var(--soft)}}
.box ul{{margin-bottom:1mm}}
/* lists */
.bul{{list-style:none;margin:1mm 0 3mm}}
.bul li{{position:relative;padding-left:5mm;margin-bottom:1.6mm}}
.bul li::before{{content:"";position:absolute;left:0;top:2.2mm;width:2mm;height:2mm;border-radius:50%;background:var(--orange)}}
.chk{{list-style:none;margin:1mm 0 3mm}}
.chk li{{display:flex;gap:3mm;margin-bottom:1.6mm}}
.cb{{flex:none;width:3.4mm;height:3.4mm;border:.35mm solid var(--ink);border-radius:.8mm;margin-top:1mm;background:#fff}}
ol.num{{margin:2mm 0 3mm 5mm}}ol.num li{{margin-bottom:2mm;padding-left:1mm}}
/* tables */
.tb{{width:100%;border-collapse:collapse;margin:2mm 0 4mm;font-size:8.8pt;background:#fff;border-radius:3mm;overflow:hidden}}
.tb th{{background:var(--ink);color:#fff;text-align:left;font-weight:600;padding:2mm 3mm;font-size:8.2pt}}
.tb td{{padding:2mm 3mm;border-top:1px solid var(--mist);vertical-align:top}}
.tb tr{{break-inside:avoid}}
.tb td:first-child{{font-weight:600}}
.tb.steps td:first-child{{width:8mm;color:var(--orange);font-family:'DM Serif Display',serif;font-size:13pt;font-weight:400}}
.tb.steps td:nth-child(2){{font-weight:600;width:24mm}}
.tb.plan td,.tb.plan th{{font-size:8.6pt}}
.tb.plan td:first-child{{font-weight:500;white-space:nowrap}}
.tb.rec td{{height:9mm}}
.tb.risk td{{height:10mm}}
/* roles & columns */
.roles{{display:grid;gap:2.2mm;margin:2mm 0 4mm}}
.role{{background:#fff;border-radius:3mm;padding:3mm 4mm 1.5mm 14mm;position:relative;break-inside:avoid}}
.role i{{position:absolute;left:4mm;top:3mm;width:6mm;height:6mm;border-radius:50%;background:var(--orange);color:#fff;font-style:normal;font-weight:600;font-size:8.5pt;display:grid;place-items:center}}
.role h3{{margin:0 0 .5mm;font-size:12pt}}.role p{{margin:0 0 1.5mm;font-size:9pt;line-height:1.45}}
.cols2{{display:grid;grid-template-columns:1fr 1fr;gap:2.5mm 6mm;margin:2mm 0 3mm}}
.cols2>div{{background:#fff;border-radius:3mm;padding:3mm 4mm 1mm;break-inside:avoid}}
.cols2 h3{{margin:0 0 1mm;font-size:11pt}}.cols2 p{{font-size:9pt;line-height:1.45}}
.faqs{{display:grid;gap:2mm}}.faqs>div{{background:#fff;border-radius:3mm;padding:3mm 4mm 1mm;break-inside:avoid}}
.faqs h3{{font-size:10.5pt;margin:0 0 1mm}}.faqs p{{font-size:9pt}}
.plan{{width:100%;margin:2mm 0 4mm}}
.plan .t1{{font:600 11px 'Inter',sans-serif;fill:#1b1917}}.plan .t2{{font:400 9px 'Inter',sans-serif;fill:#6f6b73}}.plan .t3{{font:600 8px 'Inter',sans-serif;fill:#fff}}
.tl{{margin:3mm 0 5mm}}.tl-bar{{display:flex;height:9mm;border-radius:2mm;overflow:hidden;font-size:8pt;font-weight:600;color:#fff}}
.tl-bar span{{display:grid;place-items:center;text-align:center}}.tl-bar .a{{background:var(--ink)}}.tl-bar .b{{background:var(--orange)}}.tl-bar .c{{background:#3f78a8}}
.tl-k{{display:flex;justify-content:space-between;font-size:7.4pt;color:var(--ash);margin-top:1.4mm}}
/* cierres */
.q{{background:var(--deep);border-radius:3mm;padding:5mm 7mm;margin:4mm 0;break-inside:avoid;position:relative}}
.q p{{font-family:'DM Serif Display',serif;font-size:14.5pt;line-height:1.25;margin:0 0 2mm}}
.q cite{{font-style:normal;font-size:8.4pt;color:var(--orange);font-weight:600}}
.photos{{display:grid;grid-template-columns:1fr 1fr;gap:3mm;margin:4mm 0}}
.photos div{{height:46mm;border-radius:3mm;background-size:cover;background-position:50% 45%}}
.photos.five{{grid-template-columns:repeat(5,1fr);gap:2mm}}.photos.five div{{height:30mm}}
.tl{{break-inside:avoid}}
/* annex */
.annex{{break-before:page;break-inside:auto}}
.annex .eyebrow{{margin-top:0}}
.annex h1{{font-size:24pt;margin-bottom:2mm}}
.annex .intro{{color:var(--ash);margin-bottom:4mm;font-size:9.6pt}}
.paper{{background:#fff;border:.3mm solid var(--mist);border-radius:2mm;padding:5mm 6mm 3mm;margin:3mm 0 4mm;break-inside:avoid}}
.paper h3{{margin-top:0}}
.paper.poster{{border:.6mm dashed var(--orange);padding:7mm 9mm}}
.field{{display:inline-block;vertical-align:top;margin:0 0 3mm}}.grid2 .field{{width:100%}}
.field span{{display:block;font-size:7.8pt;color:var(--ash);margin-bottom:.5mm}}
.field i{{display:block;border-bottom:.3mm solid var(--ink);height:6mm}}
.grid2{{display:grid;grid-template-columns:1fr 1fr;gap:0 6mm}}
.fl{{font-size:8.6pt;font-weight:600;margin:2mm 0 0}}
.lines i{{display:block;height:7.5mm;border-bottom:.25mm solid #b9b3ad}}
.lines{{margin-bottom:2mm}}
.cat{{display:grid;gap:3mm;margin:2mm 0 3mm}}
.cat-e{{background:#fff;border-radius:3mm;padding:4mm 5mm 1mm 14mm;position:relative}}
.cat-e .no{{position:absolute;left:4.5mm;top:4mm;font-family:'DM Serif Display',serif;font-size:17pt;color:var(--orange)}}
.cat-e h4{{font-size:13pt;margin-bottom:1mm}}.cat-e p{{font-size:8.8pt;margin-bottom:1.5mm}}.tags{{color:var(--ash);font-size:7.8pt}}
/* annex opener */
.anx{{break-before:page}}
.anx ul{{list-style:none;margin-top:3mm;columns:2;column-gap:8mm}}
.anx li{{padding:1.4mm 0;border-bottom:1px dotted #cfc4ba;font-size:9.2pt;break-inside:avoid}}.anx li b{{color:var(--orange);display:inline-block;width:9mm}}
.ccb{{position:absolute;left:18mm;right:18mm;bottom:36mm;display:flex;gap:5mm;align-items:center;font-size:7.4pt;color:#ece3da;line-height:1.45}}
.ccb img{{position:static!important;height:8.4mm!important;width:auto;flex:none;filter:none!important}}
.back .ccb{{left:20mm;right:20mm;bottom:34mm;max-width:150mm}}
/* back cover */
.back{{page:cover;break-before:page;position:relative;width:210mm;height:297mm;color:#fff;overflow:hidden;
  background:linear-gradient(180deg,rgba(27,25,23,.45),rgba(27,25,23,.93)),url('{PH}greece-hillside.jpg') 50% 50%/cover}}
.back .t{{position:absolute;left:20mm;right:20mm;bottom:46mm}}
.back h2{{font-size:28pt;margin:0 0 5mm;line-height:1.1}}.back p{{color:#ece3da;max-width:120mm}}
.back .f{{position:absolute;left:20mm;right:20mm;bottom:16mm;font-size:7pt;color:#cfc4ba;line-height:1.4;display:flex;gap:6mm;align-items:center}}
.back .f img{{height:11mm;flex:none}}
.back .logo{{position:absolute;left:20mm;top:18mm;height:15mm;filter:brightness(0) invert(1)}}
"""


def build(pages):
    parts = []
    parts.append(f"""<section class="cover"><img src="file://{ROOT}/assets/logo-ink.svg" alt="Eurolibrary">
<div class="t"><p class="k">Methodological handbook</p><h1>The Human Library handbook</h1>
<p>How to organise a Human Library with young people and local communities: the method, the preparation, the day itself and ready to use materials.</p>
<span class="badge">First edition, 2026</span></div>
<div class="f"><img src="file://{ROOT}/assets/eu-funded.png" alt="Funded by the European Union"><span>Eurolibrary, an Erasmus+ project. {EU_DISCLAIMER}</span></div>
<div class="ccb"><img src="file://{ROOT}/assets/cc-by.svg" alt="CC BY 4.0"><span>Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0).</span></div></section>""")
    parts.append(f"""<section class="about"><h1 style="margin-top:0">About Eurolibrary and this handbook</h1>{C.ABOUT}
<div class="credits"><img src="file://{ROOT}/assets/eu-funded-blue.png" alt="Funded by the European Union"><p>{EU_DISCLAIMER}</p>
<p>The annex templates are meant to be copied and adapted. Please credit Eurolibrary when you reuse them. eurolibrary.eu</p></div></section>""")
    parts.append(f'<section class="tocpage"><h1 style="margin-top:0">Contents</h1>{toc_html(pages)}</section>')
    for no, part, title, photo, pos, body in CHAPTERS:
        parts.append(chapter(no, part, title, photo, pos, body))
    # apertura de anexos
    items = "".join(f"<li><b>{code}</b>{title}</li>" for code, title, *_ in C.A) + "<li><b>R</b>Resources and glossary</li>"
    parts.append(f"""<section class="anx"><div class="band" style="background-image:url('{PH}{ANNEX_OPENER}');background-position:50% 40%"></div>
<p class="eyebrow">Annexes</p><p class="part">Materials and resources</p><h1>Materials and resources</h1>
<p class="lead">Seventeen ready to use pages for organisers, and a list of resources. Print them as they are, or copy and adapt them to your event, your language and your audience.</p>
<ul>{items}</ul>
{C.box("How to adapt them", "<p>Replace the text in square brackets, add your logo and your contact details, and have your organisation check the consent texts for your country. Keep the order and the structure, which come from what worked for us.</p>", "tip")}</section>""")
    for code, title, intro, body in C.A:
        parts.append(f'<section class="annex"><p class="eyebrow">Annex {code}</p><h1>{title}</h1><p class="intro">{intro}</p>{body}</section>')
    parts.append(f'<section class="annex"><p class="eyebrow">Annex R</p><h1>Resources and glossary</h1>{C.RESOURCES}</section>')
    parts.append(f"""<section class="back"><img class="logo" src="file://{ROOT}/assets/logo-ink.svg" alt="Eurolibrary">
<div class="t"><h2>Open your own library.</h2><p>Every story you make room for is a stereotype fewer. Visit eurolibrary.eu to see the five mobilities, listen to People of EU and follow the project.</p></div>
<div class="ccb"><img src="file://{ROOT}/assets/cc-by.svg" alt="CC BY 4.0"><span>This handbook is licensed under Creative Commons Attribution 4.0 International (CC BY 4.0). You may share and adapt it, even commercially, as long as you credit Eurolibrary and indicate any changes. creativecommons.org/licenses/by/4.0</span></div>
<div class="f"><img src="file://{ROOT}/assets/eu-funded.png" alt="Funded by the European Union"><span>{EU_DISCLAIMER}</span></div></section>""")
    return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>The Human Library handbook</title><style>{CSS}</style></head><body>{"".join(parts)}</body></html>'


def render(html, out):
    chromium = os.environ.get("CHROMIUM", "/opt/pw-browsers/chromium")
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf8") as f:
        f.write(html)
        tmp = f.name
    try:
        subprocess.run([chromium, "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                        "--virtual-time-budget=20000", f"--print-to-pdf={out}", f"file://{tmp}"],
                       check=True, capture_output=True, timeout=180)
    finally:
        if "--html" not in sys.argv:
            os.unlink(tmp)
        else:
            print("html", tmp)


def find_pages(pdf):
    """Número de página de cada capítulo y anexo, buscando su etiqueta en el texto."""
    n = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout).group(1))
    found = {}
    for p in range(1, n + 1):
        t = subprocess.run(["pdftotext", "-f", str(p), "-l", str(p), "-layout", pdf, "-"], capture_output=True, text=True).stdout
        for m in re.finditer(r"^\s*(CHAPTER (\d+)|ANNEX (A\d+|R))\s*$", t, re.M):
            key = f"c{m.group(2)}" if m.group(2) else f"a{m.group(3)}"
            found.setdefault(key, p)
    return found, n


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    tmp_pdf = OUT + ".tmp"
    render(build({}), tmp_pdf)
    pages, n1 = find_pages(tmp_pdf)
    render(build(pages), OUT)
    os.unlink(tmp_pdf)
    pages2, n = find_pages(OUT)
    if pages2 != pages:
        render(build(pages2), OUT)
        pages2, n = find_pages(OUT)
    print(f"escrito {OUT}: {n} páginas")


if __name__ == "__main__":
    main()
