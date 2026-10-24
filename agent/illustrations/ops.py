#!/usr/bin/env python3
"""Prints Canva insert_fill operations for grid page N (1-based) from media.txt: python3 ops.py N [first_cell]"""
import json
import pathlib
import sys

PAGES = ["PB2YyzJHywdYP2dH", "PBblsdv2Kjx13JKy", "PBDDnVVRF7zdyCQS", "PB3mKWQCGZ1dr7qt",
         "PBQkkGhpZjGNzjNr", "PBCkZkrx8Gt2gmDn", "PBqFlcbFYNJYsztM", "PBP4R9RFdrxZYRMv"]
lines = [l.split() for l in (pathlib.Path(__file__).parent / "media.txt").read_text().split("\n") if l.strip()]
page, first = int(sys.argv[1]), int(sys.argv[2]) if len(sys.argv) > 2 else 0
ops = []
for cell in range(first, 30):
    i = (page - 1) * 30 + cell
    if i >= len(lines):
        break
    ops.append({"type": "insert_fill", "page_id": PAGES[page - 1], "asset_type": "image", "asset_id": lines[i][1],
                "alt_text": lines[i][0], "top": cell // 5 * 675, "left": cell % 5 * 1200, "width": 1200, "height": 675})
print(json.dumps(ops, separators=(",", ":")))
