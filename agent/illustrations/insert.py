#!/usr/bin/env python3
"""Puts the 3D illustrations into the articles: python3 insert.py [key ...]

Each image goes on its own line right before the ## section it illustrates (slots from plan.py, the same
section index in uz, ru and en), with that section's heading in the reader's language as alt text.
Only images that exist in static/img/blog/illus/ are added; running it again changes nothing.
"""
import pathlib
import re
import sys

from plan import ROOT, slots, split

ILLUS = ROOT / "static" / "img" / "blog" / "illus"


def insert(path, key, picks):
    text = path.read_text(encoding="utf-8")
    lines, changed, h2 = text.split("\n"), False, -1
    out, in_body = [], False
    for n, line in enumerate(lines):
        if line.startswith("## ") and in_body:
            h2 += 1
            if h2 in picks:
                img = f"/img/blog/illus/{key}-{picks.index(h2) + 1}.jpg"
                if (ILLUS / img.rsplit("/", 1)[1]).exists() and img not in text:
                    alt = re.sub(r"[*`\[\]\"]", "", line[3:]).strip()
                    out += [f"![{alt}]({img} 1200x675)", ""]
                    changed = True
        if line == "---" and n > 0:
            in_body = True
        out.append(line)
    if changed:
        path.write_text("\n".join(out), encoding="utf-8")
    return changed


if __name__ == "__main__":
    wanted = set(sys.argv[1:])
    # Slots are picked on the uz version (its tail headings are known) and reused by index for ru and en.
    picks = {}
    for p in (ROOT / "content" / "uz" / "blog").glob("*.md"):
        meta, body = split(p)
        picks[meta.get("key", p.stem)] = slots(body)[1]
    done = 0
    for lang in ("uz", "ru", "en"):
        for p in sorted((ROOT / "content" / lang / "blog").glob("*.md")):
            meta, _ = split(p)
            key = meta.get("key", p.stem)
            if (not wanted or key in wanted) and insert(p, key, picks[key]):
                done += 1
    print(f"updated {done} files")
