#!/usr/bin/env python3
"""Tell Yandex and Bing (IndexNow) about site pages. No args: every URL in docs/sitemap.xml; or pass URLs."""
import json
import pathlib
import re
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
KEY = (ROOT / "agent" / "indexnow.key").read_text().strip()
urls = sys.argv[1:] or re.findall(r"<loc>([^<]+)</loc>", (ROOT / "docs" / "sitemap.xml").read_text())
body = json.dumps({"host": "levelm.uz", "key": KEY, "keyLocation": f"https://levelm.uz/{KEY}.txt", "urlList": urls}).encode()
for endpoint in ("https://yandex.com/indexnow", "https://api.indexnow.org/indexnow"):
    req = urllib.request.Request(endpoint, data=body, headers={"Content-Type": "application/json; charset=utf-8"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            print(endpoint, r.status, len(urls), "urls")
    except urllib.error.HTTPError as e:
        print(endpoint, e.code, e.read()[:200])
    except OSError as e:  # dropped connection or timeout: report and try the next endpoint
        print(endpoint, "error:", e)
