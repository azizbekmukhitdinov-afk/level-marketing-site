#!/usr/bin/env python3
"""Level Marketing static site builder.

Reads site.json, i18n.py and content/<lang>/blog/*.md and writes the finished site to docs/.
Standard library only:
    python3 build.py
"""
import html
import json
import re
import shutil
import sys
from datetime import date, datetime
from pathlib import Path

from i18n import CLIENTS, LANG_NAMES, LANG_SHORT, LANGS, PREFIX, T, TEAM

ROOT = Path(__file__).resolve().parent
# GitHub Pages serves the folder docs/ from the main branch, so the built site is committed.
DIST = ROOT / "docs"
SITE = json.loads((ROOT / "site.json").read_text(encoding="utf-8"))
BASE = SITE["url"].rstrip("/")
# Sub-path the site lives under (e.g. /level-marketing-site on github.io); empty on a custom domain.
ROOT_PATH = re.sub(r"^https?://[^/]+", "", BASE)

# ---------- markdown ----------

def inline(text):
    text = html.escape(text, quote=False)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", text)

    def link(m):
        label, url = m.group(1), m.group(2).replace('"', "%22")
        external = url.startswith("http") and not url.startswith(BASE)
        rel = ' target="_blank" rel="noopener"' if external else ""
        return f'<a href="{url}"{rel}>{label}</a>'

    return re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link, text)


def slugify(text):
    s = re.sub(r"[^\w\s-]", "", text.lower().replace("‘", "").replace("'", ""))
    return re.sub(r"[\s_]+", "-", s).strip("-")[:60]


def markdown(src):
    """Small markdown subset: headings, paragraphs, lists, quotes, tables, hr. Returns (html, toc)."""
    lines = src.replace("\r\n", "\n").split("\n")
    out, toc, para = [], [], []
    i = 0

    def flush():
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>")
            para.clear()

    while i < len(lines):
        line = lines[i]
        s = line.strip()
        if not s:
            flush(); i += 1; continue
        m = re.match(r"^(#{2,4})\s+(.*)$", s)
        if m:
            flush()
            level, text = len(m.group(1)), m.group(2)
            hid = slugify(text)
            if level == 2:
                toc.append((hid, text))
            out.append(f'<h{level} id="{hid}">{inline(text)}</h{level}>')
            i += 1; continue
        if re.match(r"^(-{3,}|\*{3,})$", s):
            flush(); out.append("<hr>"); i += 1; continue
        if s.startswith(">"):
            flush()
            buf = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                buf.append(lines[i].strip()[1:].strip()); i += 1
            out.append("<blockquote><p>" + inline(" ".join(buf)) + "</p></blockquote>")
            continue
        if re.match(r"^[-*]\s+", s) or re.match(r"^\d+[.)]\s+", s):
            flush()
            ordered = bool(re.match(r"^\d+[.)]\s+", s))
            pat = r"^\d+[.)]\s+" if ordered else r"^[-*]\s+"
            items = []
            while i < len(lines) and re.match(pat, lines[i].strip()):
                items.append(re.sub(pat, "", lines[i].strip()))
                i += 1
                while i < len(lines) and lines[i].startswith("  ") and lines[i].strip():
                    items[-1] += " " + lines[i].strip(); i += 1
            tag = "ol" if ordered else "ul"
            out.append(f"<{tag}>" + "".join(f"<li>{inline(x)}</li>" for x in items) + f"</{tag}>")
            continue
        if s.startswith("|") and i + 1 < len(lines) and re.match(r"^\|?\s*:?-+", lines[i + 1].strip()):
            flush()
            cells = lambda r: [c.strip() for c in r.strip().strip("|").split("|")]
            head = cells(s); i += 2
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(cells(lines[i])); i += 1
            t = "<div class=\"table\"><table><thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead><tbody>"
            t += "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rows)
            out.append(t + "</tbody></table></div>")
            continue
        para.append(s); i += 1
    flush()
    return "\n".join(out), toc


# ---------- content ----------

class Post:
    def __init__(self, path, lang):
        raw = path.read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S)
        if not m:
            raise ValueError(f"{path}: missing front matter")
        meta = {}
        for line in m.group(1).split("\n"):
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip().strip('"')
        for key in ("title", "description", "date"):
            if not meta.get(key):
                raise ValueError(f"{path}: front matter needs '{key}'")
        self.lang = lang
        self.title = meta["title"]
        self.description = meta["description"]
        self.date = datetime.strptime(meta["date"], "%Y-%m-%d").date()
        self.updated = datetime.strptime(meta["updated"], "%Y-%m-%d").date() if meta.get("updated") else None
        self.slug = meta.get("slug") or path.stem
        if not re.match(r"^[a-z0-9-]+$", self.slug):
            raise ValueError(f"{path}: slug must be lowercase latin letters, digits and dashes")
        # Versions of one post in different languages share the same key.
        self.key = meta.get("key") or self.slug
        self.kind = meta.get("type", "article")
        # Among posts of the same date, higher weight is listed first.
        self.weight = int(meta.get("weight", "0") or 0)
        self.tags = [t.strip() for t in meta.get("tags", "").split(",") if t.strip()]
        self.image = meta.get("image", "")
        if self.image and not (ROOT / "static" / self.image.lstrip("/")).exists():
            raise ValueError(f"{path}: image {self.image} not found in static/")
        self.draft = meta.get("draft", "").lower() in ("true", "yes", "ha")
        self.body, self.toc = markdown(m.group(2))
        words = len(re.sub(r"<[^>]+>", " ", self.body).split())
        self.minutes = max(1, round(words / 200))

    @property
    def path(self):
        return f"{PREFIX[self.lang]}/blog/{self.slug}/"

    @property
    def cover(self):
        return self.image or f"/covers/{self.lang}-{self.slug}.svg"


def load_posts():
    posts = {}
    today = date.today()
    for lang in LANGS:
        items = []
        folder = ROOT / "content" / lang / "blog"
        for f in sorted(folder.glob("*.md")):
            p = Post(f, lang)
            if not p.draft and p.date <= today:
                items.append(p)
        for attr in ("slug", "key"):
            vals = [getattr(p, attr) for p in items]
            dupes = {v for v in vals if vals.count(v) > 1}
            if dupes:
                raise ValueError(f"duplicate {attr} in {lang}: {dupes}")
        posts[lang] = sorted(items, key=lambda p: (p.date, p.weight, p.slug), reverse=True)
    return posts


# ---------- templates ----------

def fmt_date(d, lang):
    if lang == "en":
        return f"{T[lang]['months'][d.month - 1]} {d.day}, {d.year}"
    return f"{d.day} {T[lang]['months'][d.month - 1]} {d.year}"


def tg_url():
    return "https://t.me/" + SITE["contacts"]["telegram"].lstrip("@") if SITE["contacts"].get("telegram") else ""


def contact_link(lang):
    c = SITE["contacts"]
    if c.get("telegram"):
        return tg_url()
    if c.get("phone"):
        return "tel:" + re.sub(r"[^\d+]", "", c["phone"])
    return f"{PREFIX[lang]}/#contact"


def ext_attr(url):
    return ' target="_blank" rel="noopener"' if url.startswith("http") else ""


def home_alts():
    return {l: PREFIX[l] + "/" for l in LANGS}


def page(lang, title, desc, path, body, alts=None, schema=None, og_type="website", og_image=""):
    t = T[lang]
    alts = alts if alts is not None else home_alts()
    hreflang = ""
    if alts:
        hreflang = "".join(f'<link rel="alternate" hreflang="{l}" href="{BASE}{p}">' for l, p in alts.items())
        if "uz" in alts:
            hreflang += f'<link rel="alternate" hreflang="x-default" href="{BASE}{alts["uz"]}">'
    schema_tag = "".join(
        f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in (schema or [])
    )
    p = PREFIX[lang]
    cta = contact_link(lang)
    langs = "".join(
        f'<a class="lang{" on" if l == lang else ""}" href="{(alts or {}).get(l, PREFIX[l] + "/")}" hreflang="{l}" title="{LANG_NAMES[l]}">{LANG_SHORT[l]}</a>'
        for l in LANGS
    )
    og_img = f'<meta property="og:image" content="{BASE}{og_image}">' if og_image else ""
    return f"""<!doctype html>
<html lang="{t['html_lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{BASE}{path}">
{hreflang}
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{BASE}{path}">
<meta property="og:site_name" content="{SITE['name']}">
<meta property="og:locale" content="{t['og_locale']}">
{og_img}
<meta name="twitter:card" content="{'summary_large_image' if og_image else 'summary'}">
<meta name="theme-color" content="#1d2230">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="alternate" type="application/rss+xml" title="{SITE['name']}" href="{p}/rss.xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/style.css">
{schema_tag}
</head>
<body>
<header class="top"><div class="wrap nav">
  <a class="logo" href="{p}/">LEVEL <b>MARKETING</b></a>
  <div class="langs">{langs}</div>
  <button class="burger" type="button" aria-label="{t['menu']}" aria-expanded="false" aria-controls="menu"><span></span><span></span><span></span></button>
  <nav id="menu">
    <a href="{p}/#services">{t['nav_services']}</a>
    <a href="{p}{t['cases_path']}">{t['nav_cases']}</a>
    <a href="{p}/#team">{t['nav_team']}</a>
    <a href="{p}/blog/">{t['nav_blog']}</a>
    <a href="{p}/#location">{t['nav_location']}</a>
    <a href="{p}/#contact">{t['nav_contact']}</a>
    <a class="btn small" href="{cta}"{ext_attr(cta)}>{t['cta']}</a>
  </nav>
</div></header>
<script>
document.querySelector('.burger').addEventListener('click', function () {{
  var open = document.body.classList.toggle('menu-open');
  this.setAttribute('aria-expanded', open);
}});
document.querySelectorAll('#menu a').forEach(function (a) {{
  a.addEventListener('click', function () {{ document.body.classList.remove('menu-open'); }});
}});
</script>
<main>
{body}
</main>
<footer class="foot"><div class="wrap">
  <div>
    <a class="logo" href="{p}/">LEVEL <b>MARKETING</b></a>
    <p>{t['footer']}</p>
    <p>{t['address']}</p>
  </div>
  <div class="contacts">{footer_contacts(lang)}</div>
  <p class="copy">© {date.today().year} {SITE['name']}</p>
</div></footer>
</body>
</html>
"""


def footer_contacts(lang):
    c = SITE["contacts"]
    links = []
    if c.get("telegram"):
        links.append(f'<a href="{tg_url()}" target="_blank" rel="noopener">Telegram</a>')
    if c.get("instagram"):
        links.append(f'<a href="https://instagram.com/{c["instagram"].lstrip("@")}" target="_blank" rel="noopener">Instagram</a>')
    if c.get("phone"):
        tel = re.sub(r"[^\d+]", "", c["phone"])
        links.append(f'<a href="tel:{tel}">{html.escape(c["phone"])}</a>')
    return "".join(links) or f"<span>{T[lang]['contact_soon']}</span>"


def contact_block(lang):
    t = T[lang]
    c = SITE["contacts"]
    rows = []
    if c.get("telegram"):
        rows.append(f'<a class="contact" href="{tg_url()}" target="_blank" rel="noopener"><small>{t["contact_tg"]}</small><b>@{c["telegram"].lstrip("@")}</b></a>')
    if c.get("phone"):
        tel = re.sub(r"[^\d+]", "", c["phone"])
        rows.append(f'<a class="contact" href="tel:{tel}"><small>{t["contact_call"]}</small><b>{html.escape(c["phone"])}</b></a>')
    if c.get("instagram"):
        rows.append(f'<a class="contact" href="https://instagram.com/{c["instagram"].lstrip("@")}" target="_blank" rel="noopener"><small>{t["contact_ig"]}</small><b>@{c["instagram"].lstrip("@")}</b></a>')
    return f"""<section class="wrap block" id="contact"><h2>{t['contact_h']}</h2>
<p class="lead">{t['contact_p']}</p><div class="contacts-grid">{"".join(rows)}</div></section>"""


def location_block(lang):
    t = T[lang]
    from urllib.parse import quote
    q = quote(SITE.get("map_query") or f"{SITE['name']}, Toshkent")
    return f"""<section class="band"><div class="wrap block" id="location"><h2>{t['location_h']}</h2>
<div class="location"><div><p class="addr">{html.escape(t['address'])}</p><p>{t['location_p']}</p>
<p class="maplinks"><a class="btn small" href="https://www.google.com/maps/search/?api=1&query={q}" target="_blank" rel="noopener">{t['open_google']}</a>
<a class="btn small ghost-light" href="https://yandex.uz/maps/?text={q}" target="_blank" rel="noopener">{t['open_yandex']}</a></p></div>
<iframe class="map" title="{t['location_h']}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://maps.google.com/maps?q={q}&z=15&output=embed"></iframe></div>
</div></section>"""


def card(post):
    t = T[post.lang]
    label = t["case_label"] if post.kind == "case" else t["article_label"]
    return f"""<a class="card" href="{post.path}">
  <span class="thumb"><img src="{post.cover}" alt="{html.escape(post.title)}" loading="lazy" width="600" height="315"></span>
  <span class="card-body">
  <span class="meta"><b>{label}</b> · {fmt_date(post.date, post.lang)} · {post.minutes} {t['min_read']}</span>
  <h3>{html.escape(post.title)}</h3>
  <p>{html.escape(post.description)}</p>
  <span class="more">{t['read_more']} →</span>
  </span>
</a>"""


def org_schema(lang):
    s = {
        "@context": "https://schema.org",
        "@type": "ProfessionalService",
        "name": SITE["name"],
        "url": BASE + PREFIX[lang] + "/",
        "description": T[lang]["home_desc"],
        "areaServed": "UZ",
        "address": {"@type": "PostalAddress", "addressLocality": "Tashkent", "addressCountry": "UZ"},
        "founder": {"@type": "Person", "name": SITE["founder"]},
        "logo": BASE + "/favicon.svg",
    }
    c = SITE["contacts"]
    if c.get("phone"):
        s["telephone"] = c["phone"]
    same = [u for u in (tg_url(), "https://instagram.com/" + c["instagram"].lstrip("@") if c.get("instagram") else "") if u]
    if same:
        s["sameAs"] = same
    return s


def team_block(lang):
    t = T[lang]
    founder = TEAM[0]
    members = "".join(
        f'<figure class="member"><img src="/img/team/{img}" alt="{html.escape(name)}" loading="lazy" width="240" height="280">'
        f'<figcaption><b>{html.escape(name)}</b><span>{t["roles"][role]}</span></figcaption></figure>'
        for img, name, role in TEAM[1:]
    )
    bio = "".join(f"<li>{html.escape(x)}</li>" for x in t["founder_bio"])
    return f"""<section class="wrap block" id="team">
<div class="about">
  <div><h2>{t['about_h']}</h2><p class="lead">{t['about_p']}</p></div>
  <div class="founder"><img src="/img/team/{founder[0]}" alt="{html.escape(founder[1])}" loading="lazy" width="240" height="280">
    <div><b>{html.escape(founder[1])}</b><span>{t['founder_role']}</span><ul>{bio}</ul></div></div>
</div>
<h2 class="team-h">{t['team_h']}</h2>
<div class="team">{members}<div class="member more"><span>{t['team_more']}</span></div></div>
</section>"""


def clients_block(lang):
    t = T[lang]
    names = " · ".join(html.escape(n) for n in CLIENTS)
    return f"""<section class="band clients"><div class="wrap block">
<h2>{t['clients_h']}</h2>
<img class="logos" src="/img/clients-wall.jpg" alt="{html.escape(t['clients_h'])}: {names}" loading="lazy" width="1480" height="1250">
<p class="client-names">{names}</p>
</div></section>"""


def home(lang, posts):
    t = T[lang]
    p = PREFIX[lang]
    cta = contact_link(lang)
    cases = [x for x in posts if x.kind == "case"][:6]
    articles = [x for x in posts if x.kind != "case"][:3]
    stats = "".join(f'<div class="stat"><b>{a}</b><span>{b}</span></div>' for a, b in t["stats"])
    services = "".join(f'<div class="svc"><h3>{a}</h3><p>{b}</p></div>' for a, b in t["services"])
    steps = "".join(f'<li><b>{a}</b><span>{b}</span></li>' for a, b in t["process"])
    why = "".join(f'<div class="why"><h3>{a}</h3><p>{b}</p></div>' for a, b in t["why"])
    faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in t["faq"])
    cases_html = (f'<div class="cards">{"".join(card(c) for c in cases)}</div>' if cases
                  else f'<p class="muted">{t["cases_empty"]}</p>')
    blog_html = ""
    if articles:
        blog_html = f"""<section class="wrap block"><div class="head"><h2>{t['blog_h']}</h2>
<a href="{p}/blog/">{t['blog_all']} →</a></div><div class="cards">{"".join(card(a) for a in articles)}</div></section>"""
    body = f"""
<section class="hero"><div class="wrap">
  <p class="kicker">{t['hero_kicker']}</p>
  <h1>{t['hero_h1']}</h1>
  <p class="lead">{t['hero_p']}</p>
  <div class="actions"><a class="btn" href="{cta}"{ext_attr(cta)}>{t['cta']}</a><a class="btn ghost" href="{p}{t['cases_path']}">{t['hero_cta2']}</a></div>
  <div class="stats">{stats}</div>
</div></section>
<section class="wrap block" id="services"><h2>{t['services_h']}</h2><div class="grid3">{services}</div></section>
<section class="wrap block" id="cases"><div class="head"><h2>{t['cases_h']}</h2>{f'<a href="{p}{t["cases_path"]}">{t["cases_all"]} →</a>' if cases else ''}</div>{cases_html}</section>
{clients_block(lang)}
<section class="wrap block"><h2>{t['why_h']}</h2><div class="grid3">{why}</div></section>
<section class="band"><div class="wrap block" id="process"><h2>{t['process_h']}</h2><ol class="steps">{steps}</ol></div></section>
{team_block(lang)}
{blog_html}
{contact_block(lang)}
{location_block(lang)}
<section class="wrap block faq"><h2>{t['faq_h']}</h2>{faq}</section>
<section class="final"><div class="wrap"><h2>{t['final_h']}</h2><p>{t['final_p']}</p><a class="btn" href="{cta}"{ext_attr(cta)}>{t['cta']}</a></div></section>
"""
    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faq"]],
    }
    return page(lang, t["home_title"], t["home_desc"], f"{p}/", body, home_alts(), [org_schema(lang), faq_schema],
                og_image="/img/clients-wall.jpg")


def listing(lang, posts, kind):
    t = T[lang]
    p = PREFIX[lang]
    if kind == "case":
        items = [x for x in posts if x.kind == "case"]
        title, desc, h = t["cases_title"], t["cases_desc"], t["cases_h"]
        path = p + t["cases_path"]
        alts = {l: PREFIX[l] + T[l]["cases_path"] for l in LANGS}
    else:
        items = [x for x in posts if x.kind != "case"]
        title, desc, h = t["blog_title"], t["blog_desc"], t["nav_blog"]
        path = f"{p}/blog/"
        alts = {l: f"{PREFIX[l]}/blog/" for l in LANGS}
    inner = f'<div class="cards">{"".join(card(x) for x in items)}</div>' if items else f'<p class="muted">{t["cases_empty"]}</p>'
    body = f'<section class="wrap block page-head"><h1>{h}</h1><p class="lead">{desc}</p>{inner}</section>'
    return page(lang, title, desc, path, body, alts)


def post_alts(post, by_key):
    return {l: by_key[l][post.key].path for l in LANGS if post.key in by_key[l]}


def article(post, by_key, posts):
    t = T[post.lang]
    cta = contact_link(post.lang)
    same_kind = [x for x in posts if x.kind == post.kind and x.slug != post.slug]
    related = [x for x in same_kind if set(x.tags) & set(post.tags)][:3]
    if len(related) < 3:
        related += [x for x in same_kind if x not in related][: 3 - len(related)]
    toc = ""
    if len(post.toc) >= 3:
        toc = '<nav class="toc"><ol>' + "".join(f'<li><a href="#{i}">{html.escape(x)}</a></li>' for i, x in post.toc) + "</ol></nav>"
    updated = f" · ✎ {fmt_date(post.updated, post.lang)}" if post.updated else ""
    section = (f'<a href="{PREFIX[post.lang]}{t["cases_path"]}">{t["nav_cases"]}</a>' if post.kind == "case"
               else f'<a href="{PREFIX[post.lang]}/blog/">{t["nav_blog"]}</a>')
    body = f"""
<article class="wrap post">
  <p class="crumbs"><a href="{PREFIX[post.lang]}/">{SITE['name']}</a> / {section}</p>
  <h1>{html.escape(post.title)}</h1>
  <p class="meta">{fmt_date(post.date, post.lang)}{updated} · {post.minutes} {t['min_read']}</p>
  <img class="cover" src="{post.cover}" alt="{html.escape(post.title)}" width="1200" height="630">
  {toc}
  <div class="prose">{post.body}</div>
  <aside class="post-cta"><h2>{t['post_cta_h']}</h2><p>{t['post_cta_p']}</p><a class="btn" href="{cta}"{ext_attr(cta)}>{t['cta']}</a></aside>
</article>
{f'<section class="wrap block"><h2>{t["related"]}</h2><div class="cards">{"".join(card(r) for r in related)}</div></section>' if related else ''}
"""
    schema = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": post.title,
        "description": post.description,
        "image": BASE + post.cover,
        "datePublished": post.date.isoformat(),
        "dateModified": (post.updated or post.date).isoformat(),
        "inLanguage": post.lang,
        "mainEntityOfPage": BASE + post.path,
        "author": {"@type": "Organization", "name": SITE["name"], "url": BASE + "/"},
        "publisher": {"@type": "Organization", "name": SITE["name"], "url": BASE + "/"},
    }
    og = post.image if post.image.endswith((".jpg", ".jpeg", ".png")) else ""
    return page(post.lang, f"{post.title} — {SITE['name']}", post.description, post.path, body,
                post_alts(post, by_key), [schema], "article", og)


def cover_svg(post):
    """Branded cover for posts without a photo: title on the agency's dark/orange background."""
    words, lines, line = post.title.split(), [], ""
    for w in words:
        if len(line) + len(w) + 1 > 26 and line:
            lines.append(line)
            line = w
        else:
            line = (line + " " + w).strip()
    lines.append(line)
    if len(lines) > 4:
        lines = lines[:4]
        lines[-1] = lines[-1].rstrip(".,:;") + "…"
    label = (T[post.lang]["case_label"] if post.kind == "case" else T[post.lang]["article_label"]).upper()
    size = 64 if len(lines) <= 3 else 56
    y0 = 330 - (len(lines) - 1) * size * 0.6
    text = "".join(
        f'<text x="80" y="{y0 + i * size * 1.18:.0f}" font-size="{size}" font-weight="800" fill="#fff">{html.escape(l)}</text>'
        for i, l in enumerate(lines)
    )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" width="1200" height="630">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#1d2230"/><stop offset="1" stop-color="#3a1f1a"/></linearGradient></defs>
<rect width="1200" height="630" fill="url(#g)"/>
<circle cx="1080" cy="120" r="260" fill="#ea5b2a" opacity=".18"/>
<rect x="80" y="80" width="90" height="8" rx="4" fill="#ea5b2a"/>
<text x="80" y="140" font-size="26" font-weight="700" letter-spacing="6" fill="#ea5b2a" font-family="Manrope, Arial, Helvetica, sans-serif">{label}</text>
<g font-family="Manrope, Arial, Helvetica, sans-serif">{text}</g>
<text x="80" y="560" font-size="28" letter-spacing="8" fill="#c4c8d3" font-family="Manrope, Arial, Helvetica, sans-serif">LEVEL <tspan fill="#ea5b2a" font-weight="800">MARKETING</tspan></text>
</svg>"""


def rss(lang, posts):
    p = PREFIX[lang]
    items = "".join(
        f"<item><title>{html.escape(x.title)}</title><link>{BASE}{x.path}</link><guid>{BASE}{x.path}</guid>"
        f"<pubDate>{datetime.combine(x.date, datetime.min.time()).strftime('%a, %d %b %Y 09:00:00 +0500')}</pubDate>"
        f"<description>{html.escape(x.description)}</description></item>"
        for x in posts[:30]
    )
    return (f'<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>{SITE["name"]}</title>'
            f"<link>{BASE}{p}/</link><description>{html.escape(T[lang]['blog_desc'])}</description>"
            f"<language>{lang}</language>{items}</channel></rss>")


def sitemap(posts, by_key):
    groups = [
        (home_alts(), None),
        ({l: f"{PREFIX[l]}/blog/" for l in LANGS}, None),
        ({l: PREFIX[l] + T[l]["cases_path"] for l in LANGS}, None),
    ]
    for lang in LANGS:
        for x in posts[lang]:
            groups.append(({**post_alts(x, by_key), "_self": x.path}, x.updated or x.date))
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for alts, last in groups:
        own = [alts.pop("_self")] if "_self" in alts else list(alts.values())
        for loc in own:
            out.append(f"<url><loc>{BASE}{loc}</loc>")
            if last:
                out.append(f"<lastmod>{last.isoformat()}</lastmod>")
            if len(alts) > 1:
                for l, pth in alts.items():
                    out.append(f'<xhtml:link rel="alternate" hreflang="{l}" href="{BASE}{pth}"/>')
            out.append("</url>")
    out.append("</urlset>")
    return "\n".join(out)


def write(rel, text):
    f = DIST / rel.lstrip("/")
    if rel.endswith("/"):
        f = f / "index.html"
    f.parent.mkdir(parents=True, exist_ok=True)
    if ROOT_PATH and f.suffix == ".html":
        text = re.sub(r'(href|src)="/(?!/)', rf'\1="{ROOT_PATH}/', text)
    f.write_text(text, encoding="utf-8")


def main():
    try:
        posts = load_posts()
    except ValueError as e:
        sys.exit(f"BUILD FAILED: {e}")
    by_key = {lang: {p.key: p for p in posts[lang]} for lang in LANGS}
    if DIST.exists():
        shutil.rmtree(DIST)
    shutil.copytree(ROOT / "static", DIST)
    (DIST / ".nojekyll").write_text("")
    host = re.sub(r"^https?://", "", BASE).split("/")[0]
    if not host.endswith(".github.io"):
        # GitHub Pages reads the custom domain from this file.
        (DIST / "CNAME").write_text(host + "\n")
    for lang in LANGS:
        p = PREFIX[lang]
        write(f"{p}/", home(lang, posts[lang]))
        write(f"{p}/blog/", listing(lang, posts[lang], "article"))
        write(f"{p}{T[lang]['cases_path']}", listing(lang, posts[lang], "case"))
        write(f"{p}/rss.xml", rss(lang, posts[lang]))
        for x in posts[lang]:
            write(x.path, article(x, by_key, posts[lang]))
            if not x.image:
                write(f"/covers/{x.lang}-{x.slug}.svg", cover_svg(x))
    write("/sitemap.xml", sitemap(posts, by_key))
    write("/robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
    nf = f'<section class="wrap block page-head"><h1>404</h1><p class="lead">{T["uz"]["notfound"]} · {T["ru"]["notfound"]} · {T["en"]["notfound"]}</p><a class="btn" href="/">{T["uz"]["home"]}</a></section>'
    write("/404.html", page("uz", "404 — " + SITE["name"], T["uz"]["notfound"], "/404.html", nf, {}))
    keys = {lang: set(by_key[lang]) for lang in LANGS}
    every = set().union(*keys.values())
    missing = [f"{k} (no {', '.join(l for l in LANGS if k not in keys[l])})" for k in sorted(every) if any(k not in keys[l] for l in LANGS)]
    print("OK: " + ", ".join(f"{len(posts[l])} {l}" for l in LANGS) + f" posts -> {DIST}")
    if missing:
        print("WARNING: posts missing a language version: " + "; ".join(missing))


if __name__ == "__main__":
    main()
