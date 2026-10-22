#!/usr/bin/env python3
"""Level Marketing static site builder.

Reads site.json + content/<lang>/blog/*.md and writes the finished site to dist/.
Standard library only, so it runs on the Mac and on Cloudflare Pages unchanged:
    python3 build.py
"""
import html
import json
import re
import shutil
import sys
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
# GitHub Pages serves the folder docs/ from the main branch, so the built site is committed.
DIST = ROOT / "docs"
SITE = json.loads((ROOT / "site.json").read_text(encoding="utf-8"))
BASE = SITE["url"].rstrip("/")
# Sub-path the site lives under (e.g. /level-marketing-site on github.io); empty on a custom domain.
ROOT_PATH = re.sub(r"^https?://[^/]+", "", BASE)
LANGS = ["uz", "ru"]
PREFIX = {"uz": "", "ru": "/ru"}

T = {
    "uz": {
        "html_lang": "uz",
        "og_locale": "uz_UZ",
        "nav_services": "Xizmatlar",
        "nav_process": "Qanday ishlaymiz",
        "nav_cases": "Keyslar",
        "nav_blog": "Maqolalar",
        "nav_location": "Lokatsiya",
        "nav_contact": "Bog‘lanish",
        "menu": "Menyu",
        "contact_h": "Bog‘lanish",
        "contact_p": "Reklamangiz haqida yozing yoki qo‘ng‘iroq qiling — 30 daqiqa ichida javob beramiz va bepul audit vaqtini kelishib olamiz.",
        "contact_tg": "Telegram'da yozish",
        "contact_call": "Qo‘ng‘iroq qilish",
        "contact_ig": "Instagram",
        "location_h": "Lokatsiya",
        "location_p": "Ofisimizga keling yoki hisobotni o‘zimiz ofisingizga olib boramiz.",
        "open_google": "Google Xaritada ochish",
        "open_yandex": "Yandex Xaritada ochish",
        "cta": "Bepul audit olish",
        "other_lang": "Русский",
        "home_title": "Level Marketing — Toshkentdagi target reklama va performance-marketing agentligi",
        "home_desc": "Meta, Google va TikTok'da target reklama, Reels suratga olish va har oy ofisingizda shaffof hisobot. Toshkentdagi Level Marketing agentligi.",
        "hero_kicker": "Performance-marketing agentligi · Toshkent",
        "hero_h1": "Reklamaga sarflangan har bir dollar <em>ariza</em> olib kelsin",
        "hero_p": "Meta, Google va TikTok'da target reklamani sozlaymiz, Reels suratga olamiz va har oy hisobotni ofisingizga o‘zimiz olib boramiz: qamrov, arizalar, ariza narxi.",
        "hero_cta2": "Keyslarni ko‘rish",
        "services_h": "Xizmatlar",
        "services": [
            ["Meta Ads", "Instagram va Facebook'da target reklama: auditoriya segmentatsiyasi, kreativlar, A/B testlar va ariza narxini doimiy optimallashtirish."],
            ["Google Ads", "Qidiruvda sizni hozir izlayotgan mijozlar uchun reklama: kalit so‘zlar, e'lonlar va konversiyalarni kuzatish."],
            ["TikTok Ads", "Yosh va faol auditoriyaga qisqa videolar orqali chiqish, trendlarga mos kreativlar."],
            ["Reels va video", "Ssenariy, suratga olish va montaj. Tayyor Reels suratga olingandan keyin 48 soat ichida topshiriladi."],
            ["Strategiya", "Biznesingiz, raqobatchilar va auditoriya tahlili asosida reklama strategiyasi va oylik reja."],
            ["CRM va analitika", "Pixel, Google Analytics va CRM integratsiyasi: har bir ariza qayerdan kelganini ko‘rasiz."],
        ],
        "process_h": "Qanday ishlaymiz",
        "process": [
            ["Brif", "Biznesingiz, mahsulot, narx va maqsadlarni birga aniqlaymiz."],
            ["Strategiya", "Platformalar, auditoriya, byudjet va oylik reja (fakt / reja) tuziladi."],
            ["Kontent", "Kerak bo‘lsa, videografimiz Reels va reklama kreativlarini suratga oladi."],
            ["Ishga tushirish", "Kampaniyalar ishga tushadi, ariza narxi har kuni nazorat qilinadi."],
            ["Optimallashtirish", "A/B testlar natijasiga qarab byudjet eng samarali joyga yo‘naltiriladi."],
            ["Oylik hisobot", "Hisobot kuni ofisingizga kelib natijalarni ko‘rsatamiz va keyingi oy rejasini taqdim etamiz."],
        ],
        "why_h": "Nega Level Marketing",
        "why": [
            ["Natijaga bog‘langan jamoa", "Targetologlarimiz bonusi siz bilan hamkorlikni davom ettirishingizga bog‘liq. Shuning uchun biz uchun chiroyli hisobot emas, sizning arizalaringiz muhim."],
            ["Shaffof hisobot", "Har oy aniq raqamlar: qamrov, arizalar soni va ariza narxi. Hisobotni yuz-yuz ko‘rsatamiz."],
            ["Bitta jamoa — to‘liq sikl", "Strategiya, video, target va analitika bitta joyda. Turli frilanserlar orasida yugurishingiz shart emas."],
        ],
        "cases_h": "Keyslar",
        "cases_empty": "Mijozlarimiz ruxsati bilan keyslarni tez orada shu yerda e'lon qilamiz.",
        "blog_h": "Blogdan",
        "blog_all": "Barcha maqolalar",
        "faq_h": "Ko‘p beriladigan savollar",
        "faq": [
            ["Reklama uchun qancha byudjet kerak?", "Bu soha, shahar va maqsadga bog‘liq. Brifdan keyin aniq raqam va kutilayotgan ariza narxini hisoblab beramiz."],
            ["Birinchi arizalar qachon keladi?", "Odatda kampaniya ishga tushgan dastlabki kunlarda. Barqaror ariza narxiga test va optimallashtirishdan keyin chiqiladi."],
            ["Qaysi platformalarda ishlaysiz?", "Meta (Instagram, Facebook), Google Ads va TikTok Ads. Biznesingizga qaysi biri mos kelishini strategiya bosqichida aniqlaymiz."],
            ["Videoni ham o‘zingiz suratga olasizmi?", "Ha. Jamoamizda videograf-montajchi bor: Reels, intervyu va reklama roliklari tayyorlaymiz."],
            ["Hisobot qanday beriladi?", "Har oy loyihaning o‘z sanasida targetolog ofisingizga kelib qamrov, arizalar va ariza narxini ko‘rsatadi."],
        ],
        "final_h": "Reklamangiz qancha ariza olib kelishi mumkinligini bilib oling",
        "final_p": "Bepul audit: hozirgi reklamangizni ko‘rib chiqamiz va qayerda pul behuda ketayotganini aytamiz.",
        "blog_title": "Marketing blogi — Level Marketing",
        "blog_desc": "Target reklama, Meta Ads, Google Ads, TikTok va O‘zbekistonda biznesni o‘stirish haqida amaliy maqolalar.",
        "cases_title": "Keyslar — Level Marketing",
        "cases_desc": "Level Marketing mijozlari uchun target reklama va video loyihalari natijalari.",
        "read_more": "O‘qish",
        "min_read": "daqiqa o‘qish",
        "related": "Yana o‘qing",
        "post_cta_h": "Biznesingiz uchun shunday natija kerakmi?",
        "post_cta_p": "Bepul audit uchun yozing — reklamangizni ko‘rib chiqib, aniq tavsiyalar beramiz.",
        "contact_soon": "Kontaktlar tez orada",
        "footer": "Toshkentdagi performance-marketing agentligi",
        "months": ["yanvar", "fevral", "mart", "aprel", "may", "iyun", "iyul", "avgust", "sentabr", "oktabr", "noyabr", "dekabr"],
        "notfound": "Sahifa topilmadi",
        "home": "Bosh sahifa",
        "address": SITE["contacts"]["address_uz"],
        "cases_path": "/keyslar/",
    },
    "ru": {
        "html_lang": "ru",
        "og_locale": "ru_RU",
        "nav_services": "Услуги",
        "nav_process": "Как работаем",
        "nav_cases": "Кейсы",
        "nav_blog": "Статьи",
        "nav_location": "Локация",
        "nav_contact": "Связаться",
        "menu": "Меню",
        "contact_h": "Связаться с нами",
        "contact_p": "Напишите или позвоните — ответим в течение 30 минут и договоримся о бесплатном аудите вашей рекламы.",
        "contact_tg": "Написать в Telegram",
        "contact_call": "Позвонить",
        "contact_ig": "Instagram",
        "location_h": "Локация",
        "location_p": "Приезжайте к нам в офис — или мы сами привезём отчёт к вам.",
        "open_google": "Открыть в Google Картах",
        "open_yandex": "Открыть в Яндекс Картах",
        "cta": "Получить бесплатный аудит",
        "other_lang": "O‘zbekcha",
        "home_title": "Level Marketing — агентство таргетированной рекламы и performance-маркетинга в Ташкенте",
        "home_desc": "Таргетированная реклама в Meta, Google и TikTok, съёмка Reels и прозрачный отчёт каждый месяц у вас в офисе. Агентство Level Marketing, Ташкент.",
        "hero_kicker": "Performance-маркетинг · Ташкент",
        "hero_h1": "Каждый доллар в рекламе должен приносить <em>заявки</em>",
        "hero_p": "Настраиваем таргет в Meta, Google и TikTok, снимаем Reels и каждый месяц сами привозим отчёт к вам в офис: охват, заявки, цена заявки.",
        "hero_cta2": "Смотреть кейсы",
        "services_h": "Услуги",
        "services": [
            ["Meta Ads", "Таргет в Instagram и Facebook: сегментация аудитории, креативы, A/B-тесты и постоянная оптимизация цены заявки."],
            ["Google Ads", "Реклама в поиске для клиентов, которые ищут вас прямо сейчас: ключевые слова, объявления, отслеживание конверсий."],
            ["TikTok Ads", "Выход на молодую активную аудиторию через короткие видео и креативы в тренде."],
            ["Reels и видео", "Сценарий, съёмка и монтаж. Готовые Reels сдаём в течение 48 часов после съёмки."],
            ["Стратегия", "Рекламная стратегия и помесячный план на основе анализа бизнеса, конкурентов и аудитории."],
            ["CRM и аналитика", "Интеграция Pixel, Google Analytics и CRM: видно, откуда пришла каждая заявка."],
        ],
        "process_h": "Как мы работаем",
        "process": [
            ["Бриф", "Вместе разбираем бизнес, продукт, цены и цели."],
            ["Стратегия", "Площадки, аудитории, бюджет и план на месяц (факт / план)."],
            ["Контент", "Если нужно, наш видеограф снимает Reels и рекламные креативы."],
            ["Запуск", "Запускаем кампании и каждый день контролируем цену заявки."],
            ["Оптимизация", "По итогам A/B-тестов переносим бюджет туда, где он работает лучше всего."],
            ["Отчёт за месяц", "В день отчёта приезжаем к вам в офис, показываем результаты и план на следующий месяц."],
        ],
        "why_h": "Почему Level Marketing",
        "why": [
            ["Команда, привязанная к результату", "Бонус наших таргетологов зависит от того, продлеваете ли вы сотрудничество. Поэтому нам важны ваши заявки, а не красивый отчёт."],
            ["Прозрачный отчёт", "Каждый месяц точные цифры: охват, количество заявок и цена заявки. Показываем лично."],
            ["Одна команда — полный цикл", "Стратегия, видео, таргет и аналитика в одном месте. Не нужно бегать между фрилансерами."],
        ],
        "cases_h": "Кейсы",
        "cases_empty": "С разрешения клиентов скоро опубликуем здесь кейсы.",
        "blog_h": "Из блога",
        "blog_all": "Все статьи",
        "faq_h": "Частые вопросы",
        "faq": [
            ["Какой нужен рекламный бюджет?", "Зависит от ниши, города и цели. После брифа посчитаем точную сумму и ожидаемую цену заявки."],
            ["Когда придут первые заявки?", "Обычно в первые дни после запуска. Стабильная цена заявки появляется после тестов и оптимизации."],
            ["На каких площадках работаете?", "Meta (Instagram, Facebook), Google Ads и TikTok Ads. Какая подходит вашему бизнесу — определяем на этапе стратегии."],
            ["Видео тоже снимаете сами?", "Да. В команде есть видеограф-монтажёр: Reels, интервью и рекламные ролики."],
            ["Как вы отчитываетесь?", "Каждый месяц в дату проекта таргетолог приезжает к вам и показывает охват, заявки и цену заявки."],
        ],
        "final_h": "Узнайте, сколько заявок может приносить ваша реклама",
        "final_p": "Бесплатный аудит: разберём текущую рекламу и покажем, где утекают деньги.",
        "blog_title": "Блог о маркетинге — Level Marketing",
        "blog_desc": "Практические статьи о таргетированной рекламе, Meta Ads, Google Ads, TikTok и росте бизнеса в Узбекистане.",
        "cases_title": "Кейсы — Level Marketing",
        "cases_desc": "Результаты проектов Level Marketing по таргетированной рекламе и видео.",
        "read_more": "Читать",
        "min_read": "мин чтения",
        "related": "Читайте также",
        "post_cta_h": "Нужен такой же результат для вашего бизнеса?",
        "post_cta_p": "Напишите для бесплатного аудита — разберём вашу рекламу и дадим конкретные рекомендации.",
        "contact_soon": "Контакты скоро",
        "footer": "Агентство performance-маркетинга в Ташкенте",
        "months": ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"],
        "notfound": "Страница не найдена",
        "home": "На главную",
        "address": SITE["contacts"]["address_ru"],
        "cases_path": "/keysy/",
    },
}


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
        self.kind = meta.get("type", "article")
        self.tags = [t.strip() for t in meta.get("tags", "").split(",") if t.strip()]
        self.translation = meta.get("translation", "")
        self.draft = meta.get("draft", "").lower() in ("true", "yes", "ha")
        self.body, self.toc = markdown(m.group(2))
        words = len(re.sub(r"<[^>]+>", " ", self.body).split())
        self.minutes = max(1, round(words / 200))

    @property
    def path(self):
        return f"{PREFIX[self.lang]}/blog/{self.slug}/"


def load_posts():
    posts = {}
    today = date.today()
    for lang in LANGS:
        items = []
        for f in sorted((ROOT / "content" / lang / "blog").glob("*.md")):
            p = Post(f, lang)
            if not p.draft and p.date <= today:
                items.append(p)
        slugs = [p.slug for p in items]
        dupes = {s for s in slugs if slugs.count(s) > 1}
        if dupes:
            raise ValueError(f"duplicate slugs in {lang}: {dupes}")
        posts[lang] = sorted(items, key=lambda p: p.date, reverse=True)
    return posts


# ---------- templates ----------

def fmt_date(d, lang):
    return f"{d.day} {T[lang]['months'][d.month - 1]} {d.year}"


def contact_link(lang):
    c = SITE["contacts"]
    if c.get("telegram"):
        return "https://t.me/" + c["telegram"].lstrip("@")
    if c.get("phone"):
        return "tel:" + re.sub(r"[^\d+]", "", c["phone"])
    return f"{PREFIX[lang]}/#contact"


def page(lang, title, desc, path, body, alt_path=None, schema=None, og_type="website"):
    t = T[lang]
    other = "ru" if lang == "uz" else "uz"
    alt_path = alt_path if alt_path is not None else PREFIX[other] + "/"
    hreflang = ""
    if alt_path:
        pairs = {lang: path, other: alt_path}
        hreflang = "".join(f'<link rel="alternate" hreflang="{l}" href="{BASE}{p}">' for l, p in pairs.items())
        hreflang += f'<link rel="alternate" hreflang="x-default" href="{BASE}{pairs["uz"]}">'
    schema_tag = "".join(
        f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in (schema or [])
    )
    p = PREFIX[lang]
    cta = contact_link(lang)
    ext = ' target="_blank" rel="noopener"' if cta.startswith("http") else ""
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
<meta name="twitter:card" content="summary">
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
  <button class="burger" type="button" aria-label="{t['menu']}" aria-expanded="false" aria-controls="menu"><span></span><span></span><span></span></button>
  <nav id="menu">
    <a href="{p}/#services">{t['nav_services']}</a>
    <a href="{p}{t['cases_path']}">{t['nav_cases']}</a>
    <a href="{p}/blog/">{t['nav_blog']}</a>
    <a href="{p}/#location">{t['nav_location']}</a>
    <a href="{p}/#contact">{t['nav_contact']}</a>
    <a class="lang" href="{alt_path or PREFIX[other] + '/'}">{t['other_lang']}</a>
    <a class="btn small" href="{cta}"{ext}>{t['cta']}</a>
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
        links.append(f'<a href="https://t.me/{c["telegram"].lstrip("@")}" target="_blank" rel="noopener">Telegram</a>')
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
        rows.append(f'<a class="contact" href="https://t.me/{c["telegram"].lstrip("@")}" target="_blank" rel="noopener"><small>{t["contact_tg"]}</small><b>@{c["telegram"].lstrip("@")}</b></a>')
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
    q = quote(SITE.get("map_query") or f"{SITE['name']}, {t['address']}")
    return f"""<section class="band"><div class="wrap block" id="location"><h2>{t['location_h']}</h2>
<div class="location"><div><p class="addr">{html.escape(t['address'])}</p><p>{t['location_p']}</p>
<p class="maplinks"><a class="btn small" href="https://www.google.com/maps/search/?api=1&query={q}" target="_blank" rel="noopener">{t['open_google']}</a>
<a class="btn small ghost-light" href="https://yandex.uz/maps/?text={q}" target="_blank" rel="noopener">{t['open_yandex']}</a></p></div>
<iframe class="map" title="{t['location_h']}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://maps.google.com/maps?q={q}&z=15&output=embed"></iframe></div>
</div></section>"""


def card(post):
    t = T[post.lang]
    return f"""<a class="card" href="{post.path}">
  <span class="meta">{fmt_date(post.date, post.lang)} · {post.minutes} {t['min_read']}</span>
  <h3>{html.escape(post.title)}</h3>
  <p>{html.escape(post.description)}</p>
  <span class="more">{t['read_more']} →</span>
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
    }
    c = SITE["contacts"]
    if c.get("phone"):
        s["telephone"] = c["phone"]
    same = []
    if c.get("telegram"):
        same.append("https://t.me/" + c["telegram"].lstrip("@"))
    if c.get("instagram"):
        same.append("https://instagram.com/" + c["instagram"].lstrip("@"))
    if same:
        s["sameAs"] = same
    return s


def home(lang, posts):
    t = T[lang]
    p = PREFIX[lang]
    cta = contact_link(lang)
    ext = ' target="_blank" rel="noopener"' if cta.startswith("http") else ""
    cases = [x for x in posts if x.kind == "case"][:3]
    articles = [x for x in posts if x.kind != "case"][:3]
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
  <div class="actions"><a class="btn" href="{cta}"{ext}>{t['cta']}</a><a class="btn ghost" href="{p}{t['cases_path']}">{t['hero_cta2']}</a></div>
</div></section>
<section class="wrap block" id="services"><h2>{t['services_h']}</h2><div class="grid3">{services}</div></section>
<section class="band"><div class="wrap block" id="process"><h2>{t['process_h']}</h2><ol class="steps">{steps}</ol></div></section>
<section class="wrap block"><h2>{t['why_h']}</h2><div class="grid3">{why}</div></section>
<section class="wrap block" id="cases"><div class="head"><h2>{t['cases_h']}</h2>{f'<a href="{p}{t["cases_path"]}">{t["nav_cases"]} →</a>' if cases else ''}</div>{cases_html}</section>
{blog_html}
{contact_block(lang)}
{location_block(lang)}
<section class="wrap block faq"><h2>{t['faq_h']}</h2>{faq}</section>
<section class="final"><div class="wrap"><h2>{t['final_h']}</h2><p>{t['final_p']}</p><a class="btn" href="{cta}"{ext}>{t['cta']}</a></div></section>
"""
    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faq"]],
    }
    other = "ru" if lang == "uz" else "uz"
    return page(lang, t["home_title"], t["home_desc"], f"{p}/", body, PREFIX[other] + "/", [org_schema(lang), faq_schema])


def listing(lang, posts, kind):
    t = T[lang]
    p = PREFIX[lang]
    other = "ru" if lang == "uz" else "uz"
    if kind == "case":
        items = [x for x in posts if x.kind == "case"]
        title, desc, h, path, alt = t["cases_title"], t["cases_desc"], t["cases_h"], p + t["cases_path"], PREFIX[other] + T[other]["cases_path"]
    else:
        items = posts
        title, desc, h, path, alt = t["blog_title"], t["blog_desc"], t["nav_blog"], f"{p}/blog/", f"{PREFIX[other]}/blog/"
    inner = f'<div class="cards">{"".join(card(x) for x in items)}</div>' if items else f'<p class="muted">{t["cases_empty"]}</p>'
    body = f'<section class="wrap block page-head"><h1>{h}</h1><p class="lead">{desc}</p>{inner}</section>'
    return page(lang, title, desc, path, body, alt)


def article(post, by_slug, posts):
    t = T[post.lang]
    other = "ru" if post.lang == "uz" else "uz"
    twin = by_slug[other].get(post.translation)
    alt = twin.path if twin else ""
    cta = contact_link(post.lang)
    ext = ' target="_blank" rel="noopener"' if cta.startswith("http") else ""
    related = [x for x in posts if x.slug != post.slug and (set(x.tags) & set(post.tags))][:3]
    if len(related) < 3:
        related += [x for x in posts if x.slug != post.slug and x not in related][: 3 - len(related)]
    toc = ""
    if len(post.toc) >= 3:
        toc = '<nav class="toc"><ol>' + "".join(f'<li><a href="#{i}">{html.escape(x)}</a></li>' for i, x in post.toc) + "</ol></nav>"
    updated = f" · ✎ {fmt_date(post.updated, post.lang)}" if post.updated else ""
    body = f"""
<article class="wrap post">
  <p class="crumbs"><a href="{PREFIX[post.lang]}/">{SITE['name']}</a> / <a href="{PREFIX[post.lang]}/blog/">{t['nav_blog']}</a></p>
  <h1>{html.escape(post.title)}</h1>
  <p class="meta">{fmt_date(post.date, post.lang)}{updated} · {post.minutes} {t['min_read']}</p>
  {toc}
  <div class="prose">{post.body}</div>
  <aside class="post-cta"><h2>{t['post_cta_h']}</h2><p>{t['post_cta_p']}</p><a class="btn" href="{cta}"{ext}>{t['cta']}</a></aside>
</article>
{f'<section class="wrap block"><h2>{t["related"]}</h2><div class="cards">{"".join(card(r) for r in related)}</div></section>' if related else ''}
"""
    schema = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": post.title,
        "description": post.description,
        "datePublished": post.date.isoformat(),
        "dateModified": (post.updated or post.date).isoformat(),
        "inLanguage": post.lang,
        "mainEntityOfPage": BASE + post.path,
        "author": {"@type": "Organization", "name": SITE["name"], "url": BASE + "/"},
        "publisher": {"@type": "Organization", "name": SITE["name"], "url": BASE + "/"},
    }
    return page(post.lang, f"{post.title} — {SITE['name']}", post.description, post.path, body, alt, [schema], "article")


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


def sitemap(posts, by_slug):
    urls = []
    for path_uz, path_ru, last in [
        ("/", "/ru/", None),
        ("/blog/", "/ru/blog/", None),
        (T["uz"]["cases_path"], "/ru" + T["ru"]["cases_path"], None),
    ]:
        urls.append((path_uz, {"uz": path_uz, "ru": path_ru}, last))
        urls.append((path_ru, {"uz": path_uz, "ru": path_ru}, last))
    for lang in LANGS:
        other = "ru" if lang == "uz" else "uz"
        for x in posts[lang]:
            twin = by_slug[other].get(x.translation)
            alts = {lang: x.path, other: twin.path} if twin else {}
            urls.append((x.path, alts, x.updated or x.date))
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for loc, alts, last in urls:
        out.append(f"<url><loc>{BASE}{loc}</loc>")
        if last:
            out.append(f"<lastmod>{last.isoformat()}</lastmod>")
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
    by_slug = {lang: {p.slug: p for p in posts[lang]} for lang in LANGS}
    if DIST.exists():
        shutil.rmtree(DIST)
    shutil.copytree(ROOT / "static", DIST)
    (DIST / ".nojekyll").write_text("")
    for lang in LANGS:
        p = PREFIX[lang]
        write(f"{p}/", home(lang, posts[lang]))
        write(f"{p}/blog/", listing(lang, posts[lang], "article"))
        write(f"{p}{T[lang]['cases_path']}", listing(lang, posts[lang], "case"))
        write(f"{p}/rss.xml", rss(lang, posts[lang]))
        for x in posts[lang]:
            write(x.path, article(x, by_slug, posts[lang]))
    write("/sitemap.xml", sitemap(posts, by_slug))
    write("/robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
    nf = f'<section class="wrap block page-head"><h1>404</h1><p class="lead">{T["uz"]["notfound"]} · {T["ru"]["notfound"]}</p><a class="btn" href="/">{T["uz"]["home"]}</a></section>'
    write("/404.html", page("uz", "404 — " + SITE["name"], T["uz"]["notfound"], "/404.html", nf, ""))
    missing = [f"{x.lang}:{x.slug}" for l in LANGS for x in posts[l] if not x.translation or x.translation not in by_slug["ru" if l == "uz" else "uz"]]
    print(f"OK: {len(posts['uz'])} uz + {len(posts['ru'])} ru posts -> {DIST}")
    if missing:
        print("WARNING: posts without a translation pair: " + ", ".join(missing))


if __name__ == "__main__":
    main()
