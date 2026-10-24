#!/usr/bin/env python3
"""3D illustrations for one new article (used by the daily agent, see agent/AGENT.md).

  python3 new.py plan <key>              which sections get an image, and the prompt prefix for Canva
  python3 new.py missing                 articles that still have no illustrations, newest first
  python3 new.py save <key> <url> ...    download the Canva JPG exports (in slot order) and put them into uz/ru/en
"""
import subprocess
import sys
import urllib.request

from insert import ILLUS, insert
from plan import ROOT, slots, split
from subjects import STYLE

BLOG = {lang: ROOT / "content" / lang / "blog" for lang in ("uz", "ru", "en")}


def files(key):
    out = {}
    for lang, d in BLOG.items():
        for p in d.glob("*.md"):
            if split(p)[0].get("key", p.stem) == key:
                out[lang] = p
    return out


def plan(key):
    f = files(key)
    if "uz" not in f:
        sys.exit(f"no uz article with key: {key}")
    heads, picks = slots(split(f["uz"])[1])
    print(f"{len(picks)} images for {key}:")
    for n, i in enumerate(picks, 1):
        print(f"  {n}. before ## {heads[i]}  ->  static/img/blog/illus/{key}-{n}.jpg")
    print(f"\nprompt = STYLE + scene, STYLE:\n{STYLE}")


def missing():
    rows = []
    for p in BLOG["uz"].glob("*.md"):
        meta, body = split(p)
        if "/img/blog/illus/" not in body:
            rows.append((meta.get("date", ""), meta.get("key", p.stem)))
    for date, key in sorted(rows, reverse=True):
        print(date, key)


def save(key, urls):
    f = files(key)
    picks = slots(split(f["uz"])[1])[1]
    if len(urls) != len(picks):
        sys.exit(f"{key} needs {len(picks)} images, got {len(urls)} urls")
    ILLUS.mkdir(parents=True, exist_ok=True)
    for n, url in enumerate(urls, 1):
        dst = ILLUS / f"{key}-{n}.jpg"
        with urllib.request.urlopen(url, timeout=60) as r:
            dst.write_bytes(r.read())
        info = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", "-g", "format", str(dst)],
                              capture_output=True, text=True).stdout
        if "pixelWidth: 1200" not in info or "pixelHeight: 675" not in info or "jpeg" not in info:
            dst.unlink()
            sys.exit(f"image {n} is not a 1200x675 JPG:\n{info}")
        subprocess.run(["sips", "-s", "formatOptions", "82", str(dst)], capture_output=True, check=True)
        print("saved", dst.relative_to(ROOT))
    changed = [lang for lang, p in f.items() if insert(p, key, picks)]
    print("inserted into:", ", ".join(changed) or "nothing (already there)")


if __name__ == "__main__":
    cmd, args = (sys.argv[1], sys.argv[2:]) if len(sys.argv) > 1 else ("", [])
    if cmd == "plan" and len(args) == 1:
        plan(args[0])
    elif cmd == "missing":
        missing()
    elif cmd == "save" and len(args) >= 2:
        save(args[0], args[1:])
    else:
        sys.exit(__doc__)
