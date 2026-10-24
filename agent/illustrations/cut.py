#!/usr/bin/env python3
"""Cuts an exported Canva grid page into article illustrations: python3 cut.py <grid.jpg> <grid number from 1>

media.txt lists "<key>-<n> <media id>" in the order the images were laid out, 30 per grid page
(5 columns × 6 rows of 1200×675). Tiles go to static/img/blog/illus/<key>-<n>.jpg.
"""
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parents[1] / "static" / "img" / "blog" / "illus"
W, H, COLS, PER_PAGE = 1200, 675, 5, 30

grid, page = pathlib.Path(sys.argv[1]), int(sys.argv[2])
names = [line.split()[0] for line in (HERE / "media.txt").read_text().split("\n") if line.strip()]
OUT.mkdir(parents=True, exist_ok=True)
# sips treats a zero horizontal offset as "centre the crop", so first-column tiles are cut from the grid turned 180°.
turned = grid.with_name(grid.stem + "-180.jpg")
subprocess.run(["sips", "-r", "180", str(grid), "--out", str(turned)], check=True, capture_output=True)
gw, gh = COLS * W, PER_PAGE // COLS * H


def crop(src, y, x, dest, *extra):
    subprocess.run(["sips", "-c", str(H), str(W), "--cropOffset", str(y), str(x), *extra, "-s", "format", "jpeg",
                    "-s", "formatOptions", "82", str(src), "--out", str(dest)], check=True, capture_output=True)


for cell, name in enumerate(names[(page - 1) * PER_PAGE: page * PER_PAGE]):
    y, x = cell // COLS * H, cell % COLS * W
    dest = OUT / f"{name}.jpg"
    if x:
        crop(grid, y, x, dest)
    else:
        crop(turned, gh - y - H, gw - x - W, dest)
        subprocess.run(["sips", "-r", "180", str(dest), "--out", str(dest)], check=True, capture_output=True)
    print(dest.name)
turned.unlink()
