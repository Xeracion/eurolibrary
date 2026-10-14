#!/usr/bin/env python3
"""Genera las imágenes para compartir en redes (1200 x 630) en assets/social/.

Uso: python3 tools/social_cards.py
Cada tarjeta lleva la foto de cabecera de la página, el título y el logo. Se pesan por debajo de
300 KB porque WhatsApp descarta las imágenes mayores. Necesita Chromium y ImageMagick."""
import os
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build  # noqa: E402

ROOT = build.ROOT
FONTS = os.path.join(ROOT, "tools", "fonts")
PH = f"file://{ROOT}/assets/photos/"
OUT = os.path.join(ROOT, "assets", "social")

CARDS = {
    "home": ("greece-ios-group.jpg", "50% 55%", "Erasmus+ project", "5 countries, 5 topics, 5 ways to move",
             "A living library made of people"),
    "about": ("about-banner.jpg", "50% 28%", "About", "About Eurolibrary",
              "Five organisations, five countries, one living library"),
    "hl": ("human-library-talk.jpg", "50% 50%", "Guide and handbook", "The Human Library guide",
           "What it is and how to organise one"),
    "podcast": (None, None, "Podcast", "People of EU",
                "100 stories worth sharing from all over Europe"),
}
for k in build.CHAPTERS:
    c = build.CH[k]
    CARDS[k] = (c["hero"].split("/")[-1], "50% 50%", f"Chapter {c['no']} · {c['mode_short']}", c["name"],
                f"{c['country']}, {c['dates']}")


def html(photo, pos, kicker, title, sub):
    bg = (f"background:linear-gradient(90deg,rgba(27,25,23,.9) 0%,rgba(27,25,23,.68) 46%,rgba(27,25,23,.12) 100%),"
          f"url('{PH}{photo}') {pos}/cover") if photo else (
          f"background:linear-gradient(90deg,rgba(27,25,23,.92),rgba(27,25,23,.7)),url('file://{ROOT}/assets/podcast/show.jpg') center/cover")
    cover = (f'<div class="cv"><img src="file://{ROOT}/assets/podcast/show.jpg"></div>' if not photo else "")
    size = 74 if len(title) < 22 else 62 if len(title) < 36 else 52
    return f"""<!doctype html><meta charset="utf-8"><style>
@font-face{{font-family:'DM Serif Display';src:url('file://{FONTS}/DMSerifDisplay-400.woff2') format('woff2')}}
@font-face{{font-family:'Inter';src:url('file://{FONTS}/Inter-var.woff2') format('woff2');font-weight:400 600}}
*{{margin:0;box-sizing:border-box}}
body{{width:1200px;height:630px;overflow:hidden;position:relative;{bg};font-family:'Inter',sans-serif;color:#fff}}
.logo{{position:absolute;left:72px;top:58px;height:46px;filter:brightness(0) invert(1)}}
.t{{position:absolute;left:72px;bottom:84px;width:{'600' if not photo else '720'}px}}
.k{{font-size:20px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:#f2b48c;margin-bottom:22px}}
.bar{{width:72px;height:6px;border-radius:3px;background:#c4521a;margin-bottom:26px}}
h1{{font-family:'DM Serif Display',serif;font-weight:400;font-size:{size}px;line-height:1.06;margin-bottom:22px}}
p{{font-size:29px;line-height:1.35;color:#eee5dc;font-weight:500}}
.cv{{position:absolute;right:80px;top:85px;width:460px;height:460px;transform:rotate(3deg);box-shadow:0 30px 70px rgba(0,0,0,.55);border-radius:14px;overflow:hidden}}
.cv img{{width:100%;height:100%;object-fit:cover;display:block}}
</style><img class="logo" src="file://{ROOT}/assets/logo-ink.svg">{cover}
<div class="t"><div class="k">{kicker}</div><div class="bar"></div><h1>{title}</h1><p>{sub}</p></div>"""


def main():
    chromium = os.environ.get("CHROMIUM", "/opt/pw-browsers/chromium")
    os.makedirs(OUT, exist_ok=True)
    for key, (photo, pos, kicker, title, sub) in CARDS.items():
        with tempfile.TemporaryDirectory() as d:
            page, png = os.path.join(d, "c.html"), os.path.join(d, "c.png")
            open(page, "w", encoding="utf8").write(html(photo, pos, kicker, title, sub))
            subprocess.run([chromium, "--headless", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
                            "--window-size=1200,900", "--virtual-time-budget=8000", f"--screenshot={png}", f"file://{page}"],
                           check=True, capture_output=True, timeout=120)
            dst = os.path.join(OUT, key + ".jpg")
            for q in (88, 80, 72, 64):
                subprocess.run(["convert", png, "-crop", "1200x630+0+0", "+repage", "-quality", str(q), "-strip", dst], check=True)
                if os.path.getsize(dst) < 280_000:
                    break
            print(f"{key}.jpg {os.path.getsize(dst) // 1024} KB")


if __name__ == "__main__":
    main()
