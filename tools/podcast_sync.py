#!/usr/bin/env python3
"""Sincroniza el catálogo de People of EU desde el feed RSS del programa.

Uso: python3 tools/podcast_sync.py
Descarga el feed, descarta los episodios duplicados, guarda las portadas en assets/podcast/ep/
(400 px) y escribe tools/podcast_all.py. Después hay que ejecutar python3 tools/build.py.
Necesita curl y ImageMagick (convert)."""
import html
import os
import re
import subprocess
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime

FEED = "https://anchor.fm/s/10f4bf978/podcast/rss"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COVERS = os.path.join(ROOT, "assets", "podcast", "ep")
NS = {"itunes": "http://www.itunes.com/dtds/podcast-1.0.dtd"}
# Errata conocidas del feed: título -> número de episodio que figura en su portada
NUMBER_FIX = {"All the tales we used to believe": 96}


def text(desc):
    t = re.sub(r"<[^>]+>", " ", html.unescape(desc or ""))
    t = re.sub(r"\s*[\u2014\u2013]\s*|\s+-\s+", ", ", t)
    return re.sub(r"\s+", " ", t).replace(" ,", ",").strip()


def seconds(d):
    p = [int(x) for x in (d or "0").split(":")]
    while len(p) < 3:
        p.insert(0, 0)
    return p[0] * 3600 + p[1] * 60 + p[2]


def main():
    xml = subprocess.run(["curl", "-sS", "-m", "60", "-L", "-A", "Mozilla/5.0", FEED], capture_output=True, check=True).stdout
    items = ET.fromstring(xml).find("channel").findall("item")
    os.makedirs(COVERS, exist_ok=True)
    out, seen = [], set()
    for it in items:
        title = it.findtext("title").strip()
        guid = it.findtext("guid")
        enc = it.find("enclosure").get("url")
        key = (title, it.find("enclosure").get("length"))
        if key in seen:
            continue
        seen.add(key)
        date = parsedate_to_datetime(it.findtext("pubDate")).date().isoformat()
        img = it.find("itunes:image", NS).get("href")
        name = guid[:8] + ".jpg"
        dst = os.path.join(COVERS, name)
        if not os.path.exists(dst):
            tmp = dst + ".src"
            subprocess.run(["curl", "-sS", "-m", "60", "-L", "-o", tmp, img], check=True)
            subprocess.run(["convert", tmp, "-resize", "400x400", "-quality", "80", "-strip", dst], check=True)
            os.unlink(tmp)
        num = NUMBER_FIX.get(title) or int(it.findtext("itunes:episode", namespaces=NS) or 0) or None
        out.append(dict(title=title, date=date, secs=seconds(it.findtext("itunes:duration", namespaces=NS)),
                        text=text(it.findtext("description")), audio=enc, cover=name, no=num,
                        page=it.findtext("link")))
    used = {e["cover"] for e in out}
    for f in os.listdir(COVERS):
        if f not in used:
            os.unlink(os.path.join(COVERS, f))
    with open(os.path.join(ROOT, "tools", "podcast_all.py"), "w", encoding="utf8") as f:
        f.write('"""Catálogo de People of EU, generado por tools/podcast_sync.py a partir del feed RSS.\nNo editar a mano."""\n\nALL = [\n')
        for e in out:
            f.write("    " + repr(e) + ",\n")
        f.write("]\n")
    print(f"{len(out)} episodios de {len(items)} en el feed")


if __name__ == "__main__":
    main()
