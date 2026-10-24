#!/usr/bin/env python3
"""Appends generated media ids to media.txt in plan order: python3 add.py <id> <id> ...; prints the next scenes."""
import json
import pathlib
import sys

import subjects

HERE = pathlib.Path(__file__).resolve().parent
plan = json.loads((HERE / "plan.json").read_text())
order = [f"{k}-{i}" for k in plan for i in range(1, len(subjects.SUBJECTS[k]) + 1)]
media = HERE / "media.txt"
done = [l.split()[0] for l in media.read_text().split("\n") if l.strip()]
todo = [n for n in order if n not in done]
with media.open("a") as f:
    for name, mid in zip(todo, sys.argv[1:]):
        f.write(f"{name} {mid}\n")
left = todo[len(sys.argv) - 1:]
print(f"{len(order) - len(left)}/{len(order)} done")
for name in left[:12]:
    k, i = name.rsplit("-", 1)
    print(f"{name}: {subjects.SUBJECTS[k][int(i) - 1]}")
