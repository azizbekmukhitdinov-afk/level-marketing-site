"""Home page in the style of the client portfolio deck (~/level-content/portfolio-deck).

Only the home page uses it: its own stylesheet static/home.css and the body class «deck».
Uzbek and Russian wording comes from the approved deck. Public-site rule (Aziz, 2026-11-18):
cases show advertising numbers only (budget, enquiries, cost per enquiry, reach, followers);
client sales are said vaguely and without the work period. Exact numbers stay for meetings.
"""
import html

IMG = "/img/home/"

# ---------- texts ----------

UI = {
    "uz": {
        "projects": ["50+", "loyiha — 3 yil ichida"],
        "services_s": "to‘liq sikl",
        "clients_s": "30+ brend",
        "clients_p": "Ko‘p mijozlar biz bilan 2, 3 va 4 yildan ortiq ishlaydi. Kuchli yo‘nalishlarimiz: ishlab chiqarish va mebel, B2B, ta’lim, elektronika, tibbiyot va ko‘chmas mulk.",
        "profiles_h": "Profillar", "profiles_s": "ekspertlar va biznes",
        "cases_s": "reklama raqamlarida",
        "cases_p": "Saytda reklama raqamlarini ko‘rsatamiz: byudjet, murojaatlar va ularning narxi. Sotuvlar va to‘liq hisobotlar — uchrashuvda.",
        "case": "Keys", "read_case": "Keysni o‘qish",
        "pb_h": "Shaxsiy brend", "pb_s": "yurist, shifokor, ekspert",
        "cab_h": "Reklama kabinetlari", "cab_s": "o‘zgarishsiz",
        "cab_p": "Mijozlar kabinetlaridan skrinshotlar. Loyiha nomlari va to‘liq hisobotlarni uchrashuvda ko‘rsatamiz.",
        "process_s": "A nuqtadan B nuqtagacha",
        "why_h": "Nega Level", "why_s": "4 sabab",
        "team_s": "25+ mutaxassis",
        "contact_pill": "Nimadan boshlaymiz", "contact_h": "Bepul audit", "contact_s": "pul qayerga ketyapti?",
        "contact_p": "Hozirgi marketingingizni ko‘rib chiqamiz va arizalar hamda byudjet qayerda yo‘qolayotganini ko‘rsatamiz. 30 daqiqa ichida javob beramiz.",
        "phone": "Telefon", "address": "Manzil",
        "why": [
            ["Natijaga bog‘langan jamoa", "Mutaxassislar bonusi mijoz hamkorlikni davom ettirishiga bog‘liq."],
            ["Shaffof hisobot", "Har oy aniq raqamlar: qamrov, arizalar, ariza narxi va sotuvlar. Yuzma-yuz ko‘rsatamiz."],
            ["To‘liq sikl bitta joyda", "Strategiya, video, SMM, target va analitika: frilanserlar orasida yugurish shart emas."],
            ["Uzoq muddatli hamkorlik", "Ko‘p mijozlar biz bilan 2, 3 va 4 yildan ortiq ishlaydi — biz uchun asosiy ko‘rsatkich shu."],
        ],
    },
    "ru": {
        "projects": ["50+", "проектов за 3 года"],
        "services_s": "под ключ",
        "clients_s": "30+ брендов",
        "clients_p": "Многие клиенты работают с нами 2, 3 и больше 4 лет. Сильные ниши: производство и мебель, B2B, обучение, электроника, медицина и недвижимость.",
        "profiles_h": "Профили", "profiles_s": "эксперты и бизнес",
        "cases_s": "в цифрах рекламы",
        "cases_p": "На сайте показываем рекламные цифры: бюджет, обращения и их цену. Продажи и полные отчёты — на встрече.",
        "case": "Кейс", "read_case": "Читать кейс",
        "pb_h": "Личный бренд", "pb_s": "юристы, врачи, эксперты",
        "cab_h": "Рекламные кабинеты", "cab_s": "как есть",
        "cab_p": "Скриншоты из кабинетов клиентов. Названия проектов и полные отчёты показываем на встрече.",
        "process_s": "от точки А до точки Б",
        "why_h": "Почему Level", "why_s": "4 причины",
        "team_s": "25+ специалистов",
        "contact_pill": "С чего начать", "contact_h": "Бесплатный аудит", "contact_s": "где утекают деньги?",
        "contact_p": "Разберём ваш текущий маркетинг и покажем, где теряются заявки и бюджет. Отвечаем в течение 30 минут.",
        "phone": "Телефон", "address": "Адрес",
        "why": [
            ["Команда привязана к результату", "Бонус специалистов зависит от того, продлевает ли клиент сотрудничество."],
            ["Прозрачный отчёт", "Каждый месяц точные цифры: охват, заявки, цена заявки и продажи. Показываем лично."],
            ["Полный цикл в одном месте", "Стратегия, видео, SMM, таргет и аналитика: не нужно бегать между фрилансерами."],
            ["Долгое сотрудничество", "Многие клиенты работают с нами 2, 3 и больше 4 лет — для нас это главный показатель."],
        ],
    },
    "en": {
        "projects": ["50+", "projects in 3 years"],
        "services_s": "end to end",
        "clients_s": "30+ brands",
        "clients_p": "Many clients have stayed with us for 2, 3 and more than 4 years. Strong niches: manufacturing and furniture, B2B, education, electronics, healthcare and real estate.",
        "profiles_h": "Profiles", "profiles_s": "experts and businesses",
        "cases_s": "in ad numbers",
        "cases_p": "On the site we show advertising numbers: budget, enquiries and their cost. Sales and full reports are shown at a meeting.",
        "case": "Case", "read_case": "Read the case",
        "pb_h": "Personal brand", "pb_s": "lawyers, doctors, experts",
        "cab_h": "Ad accounts", "cab_s": "as they are",
        "cab_p": "Screenshots from clients' ad accounts. Project names and full reports are shown at a meeting.",
        "process_s": "from point A to point B",
        "why_h": "Why Level", "why_s": "4 reasons",
        "team_s": "25+ specialists",
        "contact_pill": "Where to start", "contact_h": "Free audit", "contact_s": "where is the money leaking?",
        "contact_p": "We review your current marketing and show where leads and budget get lost. We reply within 30 minutes.",
        "phone": "Phone", "address": "Address",
        "why": [
            ["A team tied to results", "Our specialists' bonus depends on whether the client renews."],
            ["Transparent reports", "Exact numbers every month: reach, leads, cost per lead and sales. Presented in person."],
            ["The full cycle in one place", "Strategy, video, SMM, ads and analytics: no running between freelancers."],
            ["Long partnerships", "Many clients have stayed with us for 2, 3 and more than 4 years — our main metric."],
        ],
    },
}

# Featured cases: big number + three phone screenshots. Post keys link to the case articles.
FEATURED = [
    {"key": "keys-teh", "name": "TEH", "imgs": ["teh-1", "teh-2", "teh-3"],
     "uz": ["Elektr asboblari", "18 661", "ta reklama murojaati $0,51 dan", [
         ["A nuqta", "Kompaniya faqat ulgurji sotardi: onlayn savdo umuman yo‘q edi."],
         ["Nima qildik", "Strategiya va taklif — boshlang‘ich to‘lovsiz muddatli to‘lov, 217 ta Reels, Meta’da target reklama va Telegram kanal."],
         ["Natija", "Reklamaga $9 500 ga yaqin sarflandi; onlayn savdo noldan oyiga bir necha yuz million so‘mga chiqdi."]]],
     "ru": ["Электроинструменты", "18 661", "обращение с рекламы по $0,51", [
         ["Точка А", "Компания продавала только оптом: онлайн-продаж не было совсем."],
         ["Что сделали", "Стратегия и оффер — рассрочка без первого взноса, 217 Reels, таргет в Meta и Telegram-канал."],
         ["Результат", "Около $9 500 на рекламу; онлайн-продажи выросли с нуля до сотен миллионов сумов в месяц."]]],
     "en": ["Power tools", "18,661", "ad enquiries at $0.51 each", [
         ["Starting point", "The company sold only wholesale: there were no online sales at all."],
         ["What we did", "Strategy and offer — instalments with no down payment, 217 Reels, Meta ads and a Telegram channel."],
         ["Result", "About $9,500 in ad spend; online sales grew from zero to hundreds of millions of sum a month."]]]},
    {"key": "", "name": "Beki Kitchen", "imgs": ["bk-1", "bk-2", "bk-3"],
     "uz": ["B2B · HoReCa uskunalari", "9 666", "ta reklama murojaati $1,30 dan", [
         ["A nuqta", "Yangi biznes: kafe va novvoyxonalar uchun Xitoydan uskunalar, na profil, na ariza bor edi."],
         ["Nima qildik", "Strategiya va taklif, Instagram noldan, Reels suratga olish, Meta’da target va arizalar yo‘qolmasligi uchun o‘z CRM tizimi."],
         ["Natija", "$12 538 byudjet bilan 6 038 ta qo‘ng‘iroq, 1 962 ta yozishma va 1 666 ta ariza; Instagram noldan 13,4 ming obunachiga yetdi."]]],
     "ru": ["B2B · оборудование для HoReCa", "9 666", "обращений с рекламы по $1,30", [
         ["Точка А", "Новый бизнес: оборудование для кафе и пекарен из Китая, ни профиля, ни заявок."],
         ["Что сделали", "Стратегия и оффер, Instagram с нуля, съёмка Reels, таргет в Meta и собственная CRM, чтобы заявки не терялись."],
         ["Результат", "6 038 звонков, 1 962 переписки и 1 666 заявок при бюджете $12 538; Instagram вырос с нуля до 13,4 тыс. подписчиков."]]],
     "en": ["B2B · HoReCa equipment", "9,666", "ad enquiries at $1.30 each", [
         ["Starting point", "A new business importing café and bakery equipment from China: no profile and no leads."],
         ["What we did", "Strategy and offer, Instagram from scratch, Reels production, Meta ads and our own CRM so that no lead gets lost."],
         ["Result", "6,038 calls, 1,962 chats and 1,666 form leads on a $12,538 budget; Instagram grew from zero to 13.4K followers."]]]},
    {"key": "keys-icomfort", "name": "iComfort", "imgs": ["ic-1", "ic-2", "ic-3"],
     "uz": ["Apple texnikasi do‘koni", "2 mln+", "oylik qamrov", [
         ["A nuqta", "Marketing strategiyasi yo‘q edi, ijtimoiy tarmoqdagi sahifa ishonch uyg‘otmasdi."],
         ["Nima qildik", "Strategiyani noldan tuzdik, Instagram’ni qayta qurdik: ekspert videolar, obzorlar, ochiq narx va muddatli to‘lov shartlari. Qamrov — Reels va target orqali."],
         ["Natija", "Oyiga 2 mln+ qamrov, sotuvlar bir necha baravar oshdi."]]],
     "ru": ["Магазин техники Apple", "2 млн+", "охват в месяц", [
         ["Точка А", "Не было маркетинговой стратегии, страница в соцсетях не вызывала доверия."],
         ["Что сделали", "Стратегия с нуля, новый Instagram: экспертные видео, обзоры, открытые цены и условия рассрочки. Охват — через Reels и таргет."],
         ["Результат", "Охват 2 млн+ в месяц, продажи выросли в разы."]]],
     "en": ["Apple electronics store", "2M+", "monthly reach", [
         ["Starting point", "There was no marketing strategy, and the social media page did not inspire trust."],
         ["What we did", "Strategy from scratch and a rebuilt Instagram: expert videos, reviews, open prices and instalment terms. Reach through Reels and paid ads."],
         ["Result", "2M+ monthly reach, and sales grew several times over."]]]},
    {"key": "keys-express-school", "name": "Express School", "imgs": ["ex-1", "ex-2", "ex-3"],
     "uz": ["Avtomaktab", "5 mln+", "qamrov", [
         ["A nuqta", "O‘quvchilar kam edi, reklama barqaror oqim bermasdi."],
         ["Nima qildik", "Guvohnomasini qo‘lida ushlab turgan haqiqiy bitiruvchilar bilan Reels, asosiy savollarga video-javoblar va eng yaxshi roliklarga target."],
         ["Natija", "Noldan 43 ming obunachi, o‘quvchilar bir necha baravar ko‘paydi; maktab Toshkentning eng gavjum joylarida 4 ta filial ochdi."]]],
     "ru": ["Автошкола", "5 млн+", "охват", [
         ["Точка А", "Учеников было мало, реклама не давала стабильного потока."],
         ["Что сделали", "Reels с реальными выпускниками с правами в руках, видео-ответы на главные вопросы и таргет на лучшие ролики."],
         ["Результат", "43 тыс. подписчиков с нуля, учеников стало в разы больше; школа открыла 4 филиала в самых проходных местах Ташкента."]]],
     "en": ["Driving school", "5M+", "reach", [
         ["Starting point", "There were few students, and ads did not bring a steady flow."],
         ["What we did", "Reels with real graduates holding their licences, video answers to the main questions, and paid ads on the best videos."],
         ["Result", "43K followers from zero and several times more students; the school opened 4 branches in the busiest parts of Tashkent."]]]},
]

# Compact case cards: [label, title, number, caption, text]; img (optional), logo (optional), post key.
CARDS = [
    {"key": "", "img": "", "logo": "",
     "uz": ["O‘quv markazi · logistika", "New Age Academy", "3 042", "ta reklama murojaati $0,36 dan", "Kursni emas, bepul oflayn master-klassni reklama qildik. Reklamaga $1 000 ga yaqin sarflandi — $500 lik kursga taxminan 60 o‘quvchi."],
     "ru": ["Учебный центр · логистика", "New Age Academy", "3 042", "обращения с рекламы по $0,36", "Рекламировали не курс, а бесплатный офлайн-мастер-класс. Около $1 000 на рекламу — примерно 60 учеников на курс за $500."],
     "en": ["Training centre · logistics", "New Age Academy", "3,042", "ad enquiries at $0.36 each", "We advertised a free offline masterclass, not the course. About $1,000 in ads — roughly 60 students for a $500 course."]},
    {"key": "keys-itops", "img": "", "logo": "lg-itops.png",
     "uz": ["Organik o‘sish", "iTOPS", "6 mln", "organik ko‘rish", "Apple gadjetlari ulgurji savdosi yetakchilaridan biri. Kontent strategiyasi va yuzi bor jonli Reels: noldan 1 000 obunachi, eng yaxshi roliklar 6 mln va 4 mln ko‘rish yig‘di."],
     "ru": ["Органический рост", "iTOPS", "6 млн", "органических просмотров", "Один из лидеров оптовых продаж гаджетов Apple. Контент-стратегия и живые Reels с лицом: 1 000 подписчиков с нуля, лучшие ролики — 6 млн и 4 млн просмотров."],
     "en": ["Organic growth", "iTOPS", "6M", "organic views", "One of the leading Apple gadget wholesalers. Content strategy and live Reels with a face: 1,000 followers from zero, the best videos got 6M and 4M views."]},
    {"key": "keys-autorobot", "img": "", "logo": "lg-autorobot.png",
     "uz": ["Organik o‘sish", "AutoRobot", "11 000", "obunachi noldan — targetsiz", "Premium-klass detailing. Jarayon, «oldin / keyin» natija, ekspertlik va mijoz hikoyalari almashib boradigan kontent-matritsa."],
     "ru": ["Органический рост", "AutoRobot", "11 000", "подписчиков с нуля — без таргета", "Детейлинг премиум-класса. Контент-матрица, в которой чередуются процесс, результат «до / после», экспертиза и истории клиентов."],
     "en": ["Organic growth", "AutoRobot", "11,000", "followers from zero — no paid ads", "Premium car detailing. A content matrix that alternates the process, before/after results, expertise and client stories."]},
    {"key": "keys-onlayn-kurslar", "img": "p-dilrabo.jpg", "logo": "",
     "uz": ["Onlayn kurs · psixologiya", "Dilrabo Isroilova", "35 000", "obunachi Telegram’da noldan · reklamaga $6 000", "Psixolog: onlayn kurs sotuvidan oldin auditoriya yig‘dik."],
     "ru": ["Онлайн-курс · психология", "Дилрабо Исроилова", "35 000", "подписчиков в Telegram с нуля · $6 000 на рекламу", "Психолог: собрали аудиторию до старта продаж онлайн-курса."],
     "en": ["Online course · psychology", "Dilrabo Isroilova", "35,000", "Telegram subscribers from zero · $6,000 in ads", "A psychologist: we built the audience before the online course went on sale."]},
    {"key": "keys-onlayn-kurslar", "img": "p-barno.jpg", "logo": "",
     "uz": ["Onlayn kurs · dietologiya", "Barno Suleymanova", "25 000", "obunachi Telegram’da noldan · reklamaga $6 000", "Dietolog: mualliflik dasturi sotuvidan oldin auditoriya yig‘dik."],
     "ru": ["Онлайн-курс · диетология", "Барно Сулейманова", "25 000", "подписчиков в Telegram с нуля · $6 000 на рекламу", "Диетолог: собрали аудиторию до старта продаж авторской программы."],
     "en": ["Online course · nutrition", "Barno Suleymanova", "25,000", "Telegram subscribers from zero · $6,000 in ads", "A dietitian: we built the audience before her own programme went on sale."]},
    {"key": "keys-chorsu-gold", "img": "case-chorsu.jpg", "logo": "",
     "uz": ["Zargarlik markazi", "Chorsu Gold Center", "", "", "Aydentika va bozor uchun noyob taklif — 5 yilga foizsiz muddatli to‘lov — hamda firma uslubidagi reklama kampaniyasi."],
     "ru": ["Ювелирный центр", "Chorsu Gold Center", "", "", "Айдентика и уникальное предложение для рынка — беспроцентная рассрочка на 5 лет — и рекламная кампания в фирменном стиле."],
     "en": ["Jewellery centre", "Chorsu Gold Center", "", "", "Brand identity, a unique offer for the market — 5-year interest-free instalments — and an ad campaign in the brand style."]},
    {"key": "keys-global-avenue", "img": "case-global-avenue.jpg", "logo": "",
     "uz": ["Turar joy majmuasi", "Global Avenue", "", "", "O‘ziga xos geraldikali Marokash uslubidagi brending va noyob taklif — 3 yilga foizsiz muddatli to‘lov."],
     "ru": ["Жилой комплекс", "Global Avenue", "", "", "Брендинг в стиле Марокко с собственной геральдикой и уникальное предложение — беспроцентная рассрочка на 3 года."],
     "en": ["Residential complex", "Global Avenue", "", "", "Moroccan-style branding with its own heraldry and a unique offer — 3-year interest-free instalments."]},
    {"key": "keys-farmatsevtika", "img": "case-loxen.jpg", "logo": "",
     "uz": ["Farmatsevtika", "Loxen va Grippomiks", "", "", "Xaridor shifokor va farmatsevtga ishonadi, shuning uchun ikki auditoriyaga ishlaymiz: aydentika, mahsulot haqida videolar, shifokorlar ishtirokidagi ekspert roliklar va dorixona tarmoqlari uchun aksiyalar."],
     "ru": ["Фармацевтика", "Loxen и Grippomiks", "", "", "Покупатель доверяет врачу и фармацевту, поэтому работаем на две аудитории: айдентика, видео о препаратах, экспертные ролики с врачами и акции для аптечных сетей."],
     "en": ["Pharmaceuticals", "Loxen and Grippomiks", "", "", "Buyers trust doctors and pharmacists, so we work with both audiences: identity, product videos, expert videos with doctors and promotions for pharmacy chains."]},
]

PROFILES = [
    ("pf-dilrabo", {"uz": ["Dilrabo Isroilova", "Psixolog"], "ru": ["Дилрабо Исроилова", "Психолог"], "en": ["Dilrabo Isroilova", "Psychologist"]}),
    ("pf-barno", {"uz": ["Barno Suleymanova", "Dietolog"], "ru": ["Барно Сулейманова", "Диетолог"], "en": ["Barno Suleymanova", "Dietitian"]}),
    ("pf-akmal", {"uz": ["Akmal Abdullayev", "Mobilograf, mentor"], "ru": ["Акмал Абдуллаев", "Мобилограф, ментор"], "en": ["Akmal Abdullayev", "Mobile videographer, mentor"]}),
    ("pf-housemall", {"uz": ["House Mall", "Uy-joy xaridi"], "ru": ["House Mall", "Покупка жилья"], "en": ["House Mall", "Home buying"]}),
    ("pf-chorsu", {"uz": ["Chorsu Gold", "Zargarlik markazi"], "ru": ["Chorsu Gold", "Ювелирный центр"], "en": ["Chorsu Gold", "Jewellery centre"]}),
    ("pf-global", {"uz": ["Global Avenue", "Yangi uylar"], "ru": ["Global Avenue", "Новостройки"], "en": ["Global Avenue", "New homes"]}),
]

PERSONAL = [
    ("pb-1", {"uz": ["Nodirbek Xudoyqulov", "Korporativ yurist"], "ru": ["Нодирбек Худойкулов", "Корпоративный юрист"], "en": ["Nodirbek Khudoykulov", "Corporate lawyer"]}),
    ("pb-2", {"uz": ["Afzal G‘afurov", "Manual terapevt"], "ru": ["Афзал Гафуров", "Мануальный терапевт"], "en": ["Afzal Gafurov", "Manual therapist"]}),
    ("pb-3", {"uz": ["Bobir Ruzimatov", "Tadbirkor"], "ru": ["Бобир Рузиматов", "Предприниматель"], "en": ["Bobir Ruzimatov", "Entrepreneur"]}),
    ("pb-4", {"uz": ["Shaxnoza Sharipova", "Shifokor-nutritsiolog"], "ru": ["Шахноза Шарипова", "Врач-нутрициолог"], "en": ["Shakhnoza Sharipova", "Nutritionist, MD"]}),
    ("pb-5", {"uz": ["Bektosh Xatamov", "Biznes advokat"], "ru": ["Бектош Хатамов", "Бизнес-адвокат"], "en": ["Bektosh Khatamov", "Business attorney"]}),
]

CABINETS = ["cab-traffic", "cab-leads", "cab-engage", "cab-direct", "cab-hol", "cab-smm"]


# ---------- rendering ----------

def e(s):
    return html.escape(s, quote=True)


def h2s(text, script, cls=""):
    return f'<div class="h2row{(" " + cls) if cls else ""}"><h2>{text}</h2><span class="scr">{script}</span></div>'


def phones(items, lang, cls):
    return f'<div class="strip {cls}">' + "".join(
        f'<figure class="ph"><img src="{IMG}{f}.jpg" alt="{e(d[lang][0])} — {e(d[lang][1])}" loading="lazy" width="360" height="780">'
        f'<figcaption><b>{e(d[lang][0])}</b><span>{e(d[lang][1])}</span></figcaption></figure>'
        for f, d in items) + "</div>"


def render(lang, posts, ctx):
    """ctx: t (i18n texts), p (prefix), cta, ext, card, by_key, team, contacts, location, faq."""
    t, u, p = ctx["t"], UI[lang], ctx["p"]
    cta, ext = ctx["cta"], ctx["ext"]
    by_key = ctx["by_key"]

    def case_link(key, label):
        post = by_key.get(key) if key else None
        return f'<a class="more" href="{post.path}">{label} →</a>' if post else ""

    st = t["stats"]
    tiles = [st[0], u["projects"], st[2], st[1]]
    stats = "".join(f'<div class="stat"><b>{a}</b><span>{b}</span></div>' for a, b in tiles)
    services = "".join(f'<div class="svc"><h3>{a}</h3><p>{b}</p></div>' for a, b in t["services"])
    steps = "".join(f'<li><b>{a}</b><span>{b}</span></li>' for a, b in t["process"])
    why = "".join(f'<div class="rw"><span class="rw-n">{i}</span><h3>{a}</h3><p>{b}</p></div>' for i, (a, b) in enumerate(u["why"], 1))

    featured = ""
    for n, c in enumerate(FEATURED, 1):
        label, num, cap, facts = c[lang]
        shots = "".join(f'<img src="{IMG}{f}.jpg" alt="{e(c["name"])}" loading="lazy" width="360" height="640">' for f in c["imgs"])
        facts_html = "".join(f'<li><b>{a}.</b> {b}</li>' for a, b in facts)
        featured += f"""<article class="fcase{' flip' if n % 2 == 0 else ''}">
<div class="fc-txt"><p class="pills"><span class="pill">{u['case']} {n:02d}</span><span class="pill pill-l">{e(label)}</span></p>
<h3 class="fc-name">{e(c['name'])}</h3>
<p class="fc-num">{num}</p><p class="fc-cap">{cap}</p>
<ul class="facts">{facts_html}</ul>{case_link(c['key'], u['read_case'])}</div>
<div class="fc-shots">{shots}</div>
</article>"""

    cards = ""
    for c in CARDS:
        label, title, num, cap, text = c[lang]
        top = ""
        if c["img"]:
            top = f'<img class="cc-img" src="{IMG}{c["img"]}" alt="{e(title)}" loading="lazy">'
        elif c["logo"]:
            top = f'<span class="cc-logo"><img src="{IMG}{c["logo"]}" alt="{e(title)}" loading="lazy"></span>'
        numhtml = f'<p class="cc-num">{num}</p><p class="cc-cap">{cap}</p>' if num else ""
        cards += f"""<article class="ccase">{top}<div class="cc-body"><p class="cc-label">{e(label)}</p><h3>{e(title)}</h3>{numhtml}<p class="cc-p">{text}</p>{case_link(c['key'], u['read_case'])}</div></article>"""

    cabs = "".join(f'<img src="{IMG}{f}.jpg" alt="Ads Manager" loading="lazy" width="720" height="370">' for f in CABINETS)
    team = "".join(
        f'<figure class="member"><img src="/img/team/{img}" alt="{e(name)}" loading="lazy" width="240" height="280">'
        f'<figcaption><b>{e(name)}</b><span>{t["roles"][role]}</span></figcaption></figure>'
        for img, name, role in ctx["team"])
    articles = [x for x in posts if x.kind != "case"][:3]
    blog = ""
    if articles:
        blog = f"""<section class="wrap block"><div class="head"><h2>{t['blog_h']}</h2><a href="{p}/blog/">{t['blog_all']} →</a></div>
<div class="cards">{"".join(ctx["card"](a) for a in articles)}</div></section>"""
    faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in t["faq"])
    c = ctx["contacts"]
    rows = [(u["phone"], c["phone"], "tel:" + c["tel"], ""), ("Telegram", "@" + c["telegram"], c["tg_url"], ' target="_blank" rel="noopener"'),
            ("Instagram", "@" + c["instagram"], "https://instagram.com/" + c["instagram"], ' target="_blank" rel="noopener"')]
    ct = "".join(f'<a class="ct" href="{h}"{x}><small>{k}</small><b>{e(v)}</b></a>' for k, v, h, x in rows)
    ct += f'<div class="ct"><small>{u["address"]}</small><b>{e(t["address"])}</b></div>'

    return f"""
<section class="hero"><div class="wrap">
  <span class="sq sq-o" aria-hidden="true"></span><span class="sq sq-l" aria-hidden="true"></span>
  <div class="hero-copy">
  <p class="kicker">{t['hero_kicker']}</p>
  <h1>{t['hero_h1']}</h1>
  <p class="lead">{t['hero_p']}</p>
  <div class="actions"><a class="btn" href="{cta}"{ext(cta)}>{t['cta']}</a><a class="btn ghost" href="#cases">{t['hero_cta2']}</a></div>
  </div>
  <div class="stats">{stats}</div>
</div></section>
<section class="wrap block" id="services">{h2s(t['services_h'], u['services_s'])}<div class="svcs">{services}</div></section>
<section class="band"><div class="wrap block">{h2s(t['clients_h'], u['clients_s'])}<p class="band-p">{u['clients_p']}</p>
<img class="logos" src="/img/clients-wall.jpg" alt="{e(t['clients_h'])}" loading="lazy" width="1480" height="1250"></div></section>
<section class="wrap block">{h2s(u['profiles_h'], u['profiles_s'])}{phones(PROFILES, lang, 'profiles')}</section>
<section class="wrap block" id="cases"><div class="head">{h2s(t['cases_h'], u['cases_s'])}<a href="{p}{t['cases_path']}">{t['cases_all']} →</a></div>
<p class="sub">{u['cases_p']}</p>
{featured}
<div class="ccases">{cards}</div></section>
<section class="wrap block">{h2s(u['pb_h'], u['pb_s'])}{phones(PERSONAL, lang, 'pbrand')}{case_link('keys-shaxsiy-brend', u['read_case'])}</section>
<section class="band"><div class="wrap block">{h2s(u['cab_h'], u['cab_s'])}<p class="band-p">{u['cab_p']}</p><div class="cabs">{cabs}</div></div></section>
<section class="wrap block" id="process">{h2s(t['process_h'], u['process_s'])}<ol class="steps">{steps}</ol></section>
<section class="wrap block">{h2s(u['why_h'], u['why_s'])}<div class="rows">{why}</div></section>
<section class="wrap block" id="team"><h2>{t['about_h']}</h2><p class="about-p">{t['about_p']}</p>
{h2s(t['team_h'], u['team_s'], 'team-h')}<div class="team">{team}<div class="member more"><span>{t['team_more']}</span></div></div></section>
{blog}
<section class="hot" id="contact"><div class="wrap block">
<div class="hot-l"><p class="kicker">{u['contact_pill']}</p><h2>{u['contact_h']}</h2><p class="scr">{u['contact_s']}</p>
<p class="hot-p">{u['contact_p']}</p><a class="btn" href="{cta}"{ext(cta)}>{t['cta']}</a></div>
<div class="cts">{ct}</div></div></section>
{ctx['location']}
<section class="wrap block faq"><h2>{t['faq_h']}</h2>{faq}</section>
"""
