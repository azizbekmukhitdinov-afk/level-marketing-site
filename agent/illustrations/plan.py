#!/usr/bin/env python3
"""Where the three 3D illustrations of every article go: before which ## sections (same index in uz/ru/en)."""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
TAIL = re.compile(r"^(Savol-javob|Xulosa|Shu mavzuda yana|Ko‘p beriladigan savollar|FAQ)", re.I)


def split(path):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", path.read_text(encoding="utf-8"), re.S)
    meta = dict((k.strip(), v.strip()) for k, v in (l.split(":", 1) for l in m.group(1).split("\n") if ":" in l))
    return meta, m.group(2)


def slots(body):
    """Indexes of the ## headings to put images before: after the intro, mid-article, and the last content section."""
    heads = re.findall(r"^## (.+)$", body, re.M)
    content = [i for i, h in enumerate(heads) if not TAIL.match(h)]
    if len(content) < 3:
        content = list(range(min(len(heads), 3)))
    n = len(content)
    picks = sorted({content[0], content[n // 2], content[n - 1]})
    return heads, picks


if __name__ == "__main__":
    plan = {}
    for p in sorted((ROOT / "content" / "uz" / "blog").glob("*.md")):
        meta, body = split(p)
        heads, picks = slots(body)
        plan[meta.get("key", p.stem)] = {"title": meta["title"], "type": meta.get("type", "article"), "slots": picks,
                                          "heads": [heads[i] for i in picks]}
    print(json.dumps(plan, ensure_ascii=False, indent=0))
