#!/usr/bin/env python3
"""Genera assets/downloads/eurolibrary-human-library-checklist.pdf a partir de la misma lista
que usa la guía (HL_PLAN, HL_MATERIALS, HL_RULES en build.py). Necesita Chromium: usa la
variable CHROMIUM o /opt/pw-browsers/chromium."""
import os
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build  # noqa: E402

ROOT = build.ROOT
OUT = os.path.join(ROOT, "assets", "downloads", "eurolibrary-human-library-checklist.pdf")
FONTS = os.path.join(ROOT, "tools", "fonts")
e = build.e


def html():
    groups = "".join(
        f'<section class="grp"><h2>{e(t)}</h2><ul>'
        + "".join(f'<li><span class="box"></span><span>{e(x)}</span></li>' for x in items)
        + "</ul></section>" for _, t, items in build.HL_PLAN)
    materials = "".join(f'<li><span class="box"></span><span>{e(m)}</span></li>' for m in build.HL_MATERIALS)
    rules = "".join(f"<li><b>{e(t)}.</b> {e(p)}</li>" for t, p in build.HL_RULES)
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Eurolibrary Human Library checklist</title>
<style>
@font-face{{font-family:'DM Serif Display';src:url('file://{FONTS}/DMSerifDisplay-400.woff2') format('woff2');font-weight:400}}
@font-face{{font-family:'Inter';src:url('file://{FONTS}/Inter-var.woff2') format('woff2');font-weight:400 600}}
@page{{size:A4;margin:10mm 12mm 10mm}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Inter',sans-serif;font-size:8.5pt;line-height:1.33;color:#1b1917;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
header{{display:flex;justify-content:space-between;align-items:flex-start;border-bottom:2px solid #c4521a;padding-bottom:7px;margin-bottom:9px}}
header img{{height:28px}}
h1{{font-family:'DM Serif Display',serif;font-weight:400;font-size:23pt;line-height:1.05;margin:2px 0 4px}}
.sub{{color:#6f6b73;max-width:118mm}}
.tag{{background:#faf2ec;border-radius:8px;padding:8px 12px;font-size:8.6pt;color:#6f6b73;max-width:52mm}}
.tag b{{color:#c4521a}}
.cols{{columns:2;column-gap:10mm}}
.grp{{break-inside:avoid;margin-bottom:8px}}
h2{{font-family:'DM Serif Display',serif;font-weight:400;font-size:12pt;color:#c4521a;margin-bottom:2px}}
ul{{list-style:none}}
li{{display:flex;gap:6px;padding:2px 0;border-top:1px solid #f3e4d6}}
li:first-child{{border-top:0}}
.box{{flex:none;width:10px;height:10px;border:1.3px solid #1b1917;border-radius:2.5px;margin-top:2px}}
.band{{background:#f3e4d6;border-radius:9px;padding:7px 12px 6px;margin-top:4px;break-inside:avoid}}
.band h2{{color:#1b1917}}
.mat{{columns:2;column-gap:10mm}}
.rules{{margin-top:8px;break-inside:avoid}}
.rules li{{display:block;border:0;padding:2px 0}}
.rules ul{{columns:2;column-gap:10mm}}
.rules li{{break-inside:avoid}}
footer{{margin-top:9px;padding-top:6px;border-top:1px solid #e5e5e5;display:flex;gap:14px;align-items:center;font-size:7.4pt;color:#6f6b73}}
footer img{{height:20px;flex:none}}
</style></head><body>
<header>
  <div><img src="file://{ROOT}/assets/logo-ink.svg" alt="Eurolibrary"><h1>Human Library checklist</h1>
  <p class="sub">Everything to prepare, run and close a Human Library, from three weeks before to the day after. Tick each box as you go.</p></div>
  <p class="tag"><b>Full guide</b><br>eurolibrary.eu/human-library</p>
</header>
<div class="cols">{groups}</div>
<div class="band"><h2>What you need</h2><ul class="mat">{materials}</ul></div>
<div class="rules"><h2>The six rules of the library</h2><ul>{rules}</ul></div>
<footer><img src="file://{ROOT}/assets/eu-funded-blue.png" alt="Funded by the European Union"><p>{e(build.EU_DISCLAIMER)}</p></footer>
</body></html>"""


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    chromium = os.environ.get("CHROMIUM", "/opt/pw-browsers/chromium")
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf8") as f:
        f.write(html())
        tmp = f.name
    try:
        subprocess.run([chromium, "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                        f"--print-to-pdf={OUT}", f"file://{tmp}"], check=True, capture_output=True)
    finally:
        os.unlink(tmp)
    print("escrito", OUT)


if __name__ == "__main__":
    main()
