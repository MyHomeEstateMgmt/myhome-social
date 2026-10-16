"""Render a MyHome Instagram post (1080x1350 PNG) from a JSON spec.

Usage: python3 render.py posts/<slug>.json
Spec keys: slug, eyebrow, title_line1, title_line2, art_svg (full <svg class="art" ...> element,
viewBox 0 0 1080 560, preserveAspectRatio="xMidYMid slice"), items (list of up to 4 short strings),
cta_head, cta_sub. Writes posts/<slug>.png next to the spec.
"""
import json, os, sys, html
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.abspath(__file__))

def build(spec):
    t = open(os.path.join(ROOT, "templates", "base.html")).read()
    items = "\n".join(
        f'    <div class="item"><div class="num">{i}</div>{html.escape(x)}</div>'
        for i, x in enumerate(spec["items"], 1))
    rep = {
        "{{EYEBROW}}": html.escape(spec["eyebrow"]),
        "{{TITLE_LINE1}}": html.escape(spec["title_line1"]),
        "{{TITLE_LINE2}}": html.escape(spec["title_line2"]),
        "{{ART_SVG}}": spec["art_svg"],
        "{{ITEMS}}": items,
        "{{CTA_HEAD}}": html.escape(spec["cta_head"]),
        "{{CTA_SUB}}": spec["cta_sub"],  # may contain <b>
    }
    for k, v in rep.items():
        t = t.replace(k, v)
    return t

def main(path):
    spec = json.load(open(path))
    out_html = os.path.join(ROOT, "templates", f"_render_{spec['slug']}.html")
    open(out_html, "w").write(build(spec))
    out_png = os.path.join(ROOT, "posts", f"{spec['slug']}.png")
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1350})
        pg.goto("file://" + out_html)
        pg.wait_for_timeout(400)
        pg.screenshot(path=out_png)
        b.close()
    os.remove(out_html)
    print(out_png)

if __name__ == "__main__":
    main(sys.argv[1])
