#!/usr/bin/env python3
"""Write the batch articles into content/<lang>/blog/ and link every article to other articles on the site.

Bodies live in agent/batch/bNN.py as BODIES = {key: {"uz": md, "ru": md, "en": md}}. Only articles with a body
are written, and "more on this topic" links only point at articles that exist, so this can run after each part.
"""
import importlib
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(HERE))
from plan import EXISTING, PLAN  # noqa: E402

LANGS = ["uz", "ru", "en"]
PREFIX = {"uz": "", "ru": "/ru", "en": "/en"}
DATE = "2026-10-22"
HEAD = {"uz": "Shu mavzuda yana", "ru": "Ещё по теме", "en": "More on this topic"}
TAGS = {
    "target": ("target reklama, meta ads", "таргет, meta ads", "paid ads, meta ads"),
    "smm": ("smm, instagram", "smm, instagram", "smm, instagram"),
    "video": ("reels, video", "reels, видео", "reels, video"),
    "brend": ("brend, obro‘", "бренд, репутация", "brand, reputation"),
    "sotuv": ("sotuv, analitika", "продажи, аналитика", "sales, analytics"),
    "biznes": ("biznes, strategiya", "бизнес, стратегия", "business, strategy"),
}


def existing_title(lang, slug):
    text = (ROOT / "content" / lang / "blog" / f"{slug}.md").read_text(encoding="utf-8")
    return re.search(r"^title: (.+)$", text, re.M).group(1).strip()


def main():
    bodies = {}
    for f in sorted(HERE.glob("b[0-9]*.py")):
        bodies.update(importlib.import_module(f.stem).BODIES)
    written = [p for p in PLAN if p[0] in bodies]
    by_rubric = {}
    for p in written:
        by_rubric.setdefault(p[1], []).append(p)
    # Slugs that exist per language: already on the site or written in this run.
    known = {lang: {f.stem for f in (ROOT / "content" / lang / "blog").glob("*.md")} for lang in LANGS}
    for p in written:
        for li, lang in enumerate(LANGS):
            known[lang].add(p[2 + li][0])

    def keep_live_links(md, lang):
        # Links to articles from later parts stay plain text until those articles are written.
        def fix(m):
            return m.group(0) if m.group(2) in known[lang] else m.group(1)
        return re.sub(r"\[([^\]]+)\]\(" + re.escape(PREFIX[lang]) + r"/blog/([a-z0-9-]+)/\)", fix, md)

    for key, rubric, *versions in written:
        peers = by_rubric[rubric]
        i = next(n for n, p in enumerate(peers) if p[0] == key)
        neighbours = []
        for step in (1, 2, -1):
            other = peers[(i + step) % len(peers)]
            if other[0] != key and other not in neighbours:
                neighbours.append(other)
        neighbours = neighbours[:2]
        for li, lang in enumerate(LANGS):
            slug, title, desc = versions[li]
            links = [(n[2 + li][1], f"{PREFIX[lang]}/blog/{n[2 + li][0]}/") for n in neighbours]
            old = EXISTING[rubric][li]
            links.append((existing_title(lang, old), f"{PREFIX[lang]}/blog/{old}/"))
            more = "\n".join(f"- [{t}]({u})" for t, u in links)
            body = keep_live_links(bodies[key][lang].strip(), lang)
            text = (f"---\ntitle: {title}\ndescription: {desc}\ndate: {DATE}\nslug: {slug}\ntype: article\n"
                    f"tags: {TAGS[rubric][li]}\nkey: {key}\nrubric: {rubric}\n---\n\n{body}\n\n## {HEAD[lang]}\n\n{more}\n")
            (ROOT / "content" / lang / "blog" / f"{slug}.md").write_text(text, encoding="utf-8")
    print(f"written {len(written)} articles x 3 languages")


if __name__ == "__main__":
    main()
