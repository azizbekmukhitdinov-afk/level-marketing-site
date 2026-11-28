---
title: Google Tag Manager: teglar, triggerlar va xatolarsiz o‘rnatish
description: Google Tag Manager asoslari: konteyner, teg, trigger va o‘zgaruvchilar, GA4 va Meta Pixel o‘rnatish, Preview rejimida tekshirish va tez-tez uchraydigan xatolar.
date: 2026-11-28
slug: google-tag-manager
type: article
tags: Google Tag Manager, GTM, veb-analitika, GA4, Meta Pixel
key: google-tag-manager
rubric: target
---

Saytga GA4, Yandex Metrika, Meta Pixel qo‘yish kerak, keyin qo‘ng‘iroq tugmasi va Telegram bosishlarini ham sanash kerak — har safar dasturchiga yozasiz va bir hafta kutasiz. **Google Tag Manager** (GTM) bu muammoni hal qiladi: saytga bitta kod qo‘yiladi, qolgan barcha teglar esa GTM interfeysidan boshqariladi. Bu maqolada asosiy tushunchalar, GA4 va Meta Pixel o‘rnatish, Preview rejimi va tipik xatolarni ko‘rib chiqamiz.

## GTM nima va qachon kerak

GTM — bepul «teglar menejeri». Teg — bu saytga qo‘yiladigan har qanday kod parchasi: analitika, piksel, chat vidjeti. GTM ularni saytdagi kodga tegmasdan qo‘shish, o‘zgartirish va o‘chirish imkonini beradi.

| Vaziyat | GTM kerakmi |
|---|---|
| Faqat GA4, sayt konstruktorida tayyor maydon bor | Shart emas |
| GA4 + Metrika + Meta Pixel | Ha, hammasi bir joyda |
| Tugma, telefon, Telegram bosishlarini sanash kerak | Ha |
| Reklama tez-tez o‘zgaradi, dasturchi doim band | Ha |
| Sayt egasining kodga umuman kirish imkoni yo‘q | Avval kirish masalasini hal qiling |

Qoida oddiy: saytda ikkitadan ortiq teg bo‘lsa yoki tugmalarni kuzatish kerak bo‘lsa, GTM vaqtni tejaydi.

## Uch asosiy tushuncha

GTM’da hamma narsa uchta element atrofida quriladi:

| Element | Nima | Misol |
|---|---|---|
| Teg (tag) | Nima ishga tushadi | Google tag (GA4), Meta Pixel, Metrika kodi |
| Trigger | Qachon ishga tushadi | Barcha sahifalar, «Rahmat» sahifasi, t.me havolasiga bosish |
| O‘zgaruvchi (variable) | Qaysi qiymat ishlatiladi | Bosilgan havola manzili, sahifa URL’i, o‘lchov ID |

Formulani eslab qoling: **teg + trigger = harakat**. Masalan, «generate_lead hodisasini GA4 ga yubor» (teg) «foydalanuvchi /rahmat/ sahifasini ochganda» (trigger).

## 1-qadam: akkaunt va konteyner

1. tagmanager.google.com saytiga **kompaniya** Google akkaunti bilan kiring.
2. Akkaunt yarating (kompaniya nomi) va konteyner qo‘shing.
3. Konteyner turini tanlang. Google yordam bo‘limiga ko‘ra, sayt uchun eng ko‘p ishlatiladigani — Web; iOS, Android, AMP va Server turlari ham bor. Konteyner nomi sifatida saytning asosiy manzilini yozish tavsiya etiladi, har bir sahifa uchun alohida konteyner kerak emas ([Tag Manager yordami](https://support.google.com/tagmanager/answer/6103696)).
4. Ikkita kod parchasini o‘rnating: birinchisini `<head>` ichida iloji boricha yuqoriga, ikkinchisini (noscript) ochiluvchi `<body>` tegidan darhol keyin ([o‘rnatish bo‘yicha qo‘llanma](https://support.google.com/tagmanager/answer/14847097)).

Konteyner ID’si GTM- bilan boshlanadi. Ko‘p konstruktor va CMS’larda uni kiritish uchun alohida maydon bor.

## 2-qadam: GA4 ni GTM orqali ulash

GA4 ni GTM’ga ulash uchun Google yordam bo‘limi quyidagi tartibni beradi ([Google tag sozlash](https://support.google.com/analytics/answer/15756616)):

1. Teglar → Yangi.
2. Teg turi — **Google tag**.
3. Tag ID maydoniga GA4 ma’lumotlar oqimining ID’sini kiriting (G- bilan boshlanadi).
4. Trigger — **Initialization – All Pages**, shunda teg boshqa triggerlardan oldin ishga tushadi.
5. Saqlang va Submit (nashr) qiling. Yordam bo‘limiga ko‘ra, ma’lumot yig‘ilishi 30 daqiqagacha vaqt olishi mumkin.

Muhim: agar GA4 kodi saytga avval to‘g‘ridan-to‘g‘ri qo‘yilgan bo‘lsa va siz uni GTM orqali ham qo‘shsangiz, sahifa ko‘rishlar ikki marta yozilishi mumkin. Bitta usulni tanlang va ikkinchisini olib tashlang. GA4 hisobotlari va asosiy hodisalar haqida — [Google Analytics 4: kichik biznes sayti uchun sozlash qo‘llanmasi](/blog/google-analytics-4/).

## 3-qadam: arizalar va tugmalarni kuzatish

Bu GTM’ning eng foydali qismi. Kichik biznes saytiga odatda to‘rtta trigger yetadi:

| Nimani sanaymiz | Trigger turi | Shart |
|---|---|---|
| Ariza yuborildi | Page View | Page Path = /rahmat/ |
| Qo‘ng‘iroq tugmasi | Click – Just Links | Click URL «tel:» bilan boshlanadi |
| Telegram | Click – Just Links | Click URL tarkibida «t.me» |
| WhatsApp | Click – Just Links | Click URL tarkibida «wa.me» |

Click URL kabi bosish o‘zgaruvchilari bosish triggerlari orqali to‘ldiriladi ([o‘rnatilgan o‘zgaruvchilar](https://support.google.com/tagmanager/answer/7182738)). Agar ro‘yxatda ko‘rinmasa, O‘zgaruvchilar bo‘limida o‘rnatilgan o‘zgaruvchilarni sozlash orqali yoqing.

Har bir trigger uchun GA4 hodisa tegi yarating (masalan, generate_lead, click_phone, click_telegram) va GA4 da ularni asosiy hodisa sifatida belgilang. Shu triggerlardan Meta Pixel va Yandex Metrika maqsadlari uchun ham foydalanish mumkin — bitta trigger, uchta tizim. Metrika maqsadlari haqida — [Yandex Metrika sozlash: hisoblagich, maqsadlar va Vebvizor](/blog/yandex-metrika-sozlash/).

**Forma uchun maslahat:** eng ishonchli usul — forma yuborilgandan keyin alohida «Rahmat» sahifasiga o‘tkazish. GTM’ning forma yuborish triggeri ba’zi forma konstruktorlarida ishonchsiz ishlashi mumkin, shuning uchun uni albatta Preview’da tekshiring.

## 4-qadam: Meta Pixel

GTM’da Meta Pixel uchun Google’ning rasmiy tegi yo‘q. Meta hujjatlarida ikki yo‘l ko‘rsatilgan: Custom HTML tegi orqali yoki Meta tomonidan taqdim etilgan GTM shabloni orqali ([Meta hujjatlari](https://developers.facebook.com/documentation/ads-commerce/gateway-products/signals-gateway/pixel-setup-google-tag-manager)).

Asosiy tartib:

- bazaviy piksel kodi — barcha sahifalarda;
- «Lead» standart hodisasi — «Rahmat» sahifasida yoki ariza triggerida;
- Pixel ID’ni o‘zgaruvchiga saqlang, shunda uni bir joyda o‘zgartirasiz.

Brauzer pikseli cookie va blokirovkalar sababli hamma hodisani ko‘rmaydi, shuning uchun Conversions API ham kerak — batafsil [Meta Pixel va Conversions API: 2026 uchun o‘rnatish qo‘llanmasi](/blog/meta-pixel-conversions-api/) maqolasida.

## 5-qadam: Preview rejimi va nashr

GTM’da o‘zgarish darhol saytga chiqmaydi: avval qoralama (workspace), keyin tekshiruv, keyin nashr.

**Preview.** Google yordam bo‘limiga ko‘ra, Preview tugmasi saytni joriy qoralama nashr qilingandek ko‘rsatadi, Tag Assistant esa qaysi teg va trigger ishlaganini ko‘rsatadi. Bu rejim faqat preview yoqilgan brauzerda yoki havola ulashilgan odamlarda ko‘rinadi, oddiy tashrif buyuruvchilar uni ko‘rmaydi ([Preview va debug](https://support.google.com/tagmanager/answer/6107056)).

Nashrdan oldingi tekshiruv ro‘yxati:

- bosh sahifani oching — Google tag bir marta ishladimi;
- telefon tugmasini bosing — click_phone tegi ishladimi;
- formani yuboring — «Rahmat» sahifasida generate_lead va Lead ishladimi;
- boshqa sahifalarda ariza tegi **ishlamaganini** tekshiring.

**Nashr.** Submit bosganda versiyaga tushunarli nom bering: «Telegram va telefon bosishlari, 28.11». Biror narsa buzilsa, Versiyalar bo‘limidan oldingi versiyaga qaytish mumkin.

## Kirish huquqlari

Konteyner darajasida beshta huquq bor ([foydalanuvchi huquqlari](https://support.google.com/tagmanager/answer/6107011)):

| Huquq | Nima qila oladi | Kimga |
|---|---|---|
| No access | Konteynerni ko‘rmaydi | — |
| Read | Faqat ko‘radi | Rahbar, tahlilchi |
| Edit | O‘zgartiradi, nashr qila olmaydi | Kichik mutaxassis |
| Approve | Versiya yaratadi, nashr qila olmaydi | Tekshiruvchi |
| Publish | To‘liq huquq | Mas’ul mutaxassis yoki agentlik |

Akkaunt darajasida Admin huquqi kompaniyada qolsin.

## Shartli misol: GTM’dan keyin lid narxi qanday o‘zgaradi

Shartli misol. Klinika bir oyda reklamaga 6 000 000 so‘m sarflaydi. GTM’gacha faqat sayt formalari sanalgan: 40 ta ariza, lid narxi 150 000 so‘m. Reklama «qimmat» ko‘rinadi va byudjetni qisqartirish taklif qilinadi.

GTM orqali telefon va Telegram bosishlari qo‘shildi:

| Kanal | Oyiga |
|---|---|
| Formalar | 40 |
| Telefon tugmasi | 35 |
| Telegram | 25 |
| Jami kontaktlar | 100 |
| Kontakt narxi | 6 000 000 / 100 = 60 000 so‘m |

Raqamlar shartli, lekin xulosa amaliy: kuzatuv to‘liq bo‘lmasa, ishlayotgan reklamani o‘chirib qo‘yish xavfi bor. Bundan tashqari, reklama algoritmlari faqat formalarni emas, barcha kontaktlarni ko‘rib o‘qiydi. Keyingi qadam — bu 100 kontaktni CRM bilan solishtirish, chunki bosish hali ariza degani emas; nima uchun raqamlar farq qilishi — [Kabinetdagi lidlar va CRM mos kelmasa: 7 sabab va tekshiruv](/blog/kabinet-va-crm-lidlar/) maqolasida.

## Ko‘p uchraydigan xatolar

- **Konteyner agentlik yoki dasturchi akkauntida.** Hamkorlik tugasa, kirish ham yo‘qoladi.
- **Kod ikki marta qo‘yilgan** (saytda to‘g‘ridan-to‘g‘ri va GTM orqali). Ko‘rishlar va konversiyalar ikki baravar.
- **Preview’siz nashr.** Ariza tegi barcha sahifalarda ishlaydi — kabinetda «lidlar» ko‘payadi, CRMda yo‘q.
- **Nomlashda tartib yo‘q.** «Tag 1», «New trigger» — yarim yildan keyin hech kim tushunmaydi. Format: «GA4 – generate_lead», «Click – Telegram».
- **Eski teglar o‘chirilmagan.** Ishlamaydigan piksellar saytni sekinlashtiradi.
- **Versiyalarga nom berilmagan.** Qaysi o‘zgarish nimani buzganini topish qiyin.

## Savol-javob

### GTM saytni sekinlashtiradimi?

GTM’ning o‘zi bitta skript. Sekinlik odatda unga qo‘shilgan teglar soni va og‘irligidan keladi. Shuning uchun keraksiz teglarni muntazam o‘chiring.

### Dasturchisiz GTM’ni sozlash mumkinmi?

Konteyner kodini o‘rnatish uchun saytga bir marta kirish kerak — ko‘p konstruktorlarda buni o‘zingiz qilasiz. Keyingi teg va triggerlar GTM interfeysida, kod yozmasdan sozlanadi.

### GTM va Google Analytics farqi nima?

GA4 ma’lumotni yig‘adi va hisobot ko‘rsatadi. GTM esa faqat kodlarni yetkazib beradi va hech qanday hisobot ko‘rsatmaydi. GTM — «quvur», GA4 — «idish».

### Yandex Metrikani ham GTM orqali qo‘ysa bo‘ladimi?

Ha, Metrika kodini Custom HTML tegi orqali barcha sahifalarga qo‘yish mumkin. O‘rnatgandan keyin Preview’da va Metrika hisobotida tashrif yozilganini tekshiring.

## Xulosa

Google Tag Manager — saytdagi barcha kodlarni bir joyda boshqarish usuli. Kompaniya akkauntida bitta konteyner, Initialization triggeri bilan Google tag, to‘rtta asosiy trigger (forma, telefon, Telegram, WhatsApp), Meta Pixel va har safar Preview orqali tekshiruv. Shunda reklama natijalari to‘liq ko‘rinadi va har kichik o‘zgarish uchun dasturchini kutish shart bo‘lmaydi.

Level Marketing bepul audit davomida saytingizdagi GTM, GA4 va Meta Pixel to‘g‘ri ishlayotganini va kontaktlar to‘liq sanalayotganini tekshirib berishi mumkin.

## Shu mavzuda yana

- [Google Analytics 4: kichik biznes sayti uchun sozlash qo‘llanmasi](/blog/google-analytics-4/)
- [Meta Pixel va Conversions API: 2026 uchun o‘rnatish qo‘llanmasi](/blog/meta-pixel-conversions-api/)
- [UTM-belgilar: har bir mijoz qayerdan kelganini qanday bilish](/blog/utm-belgilar/)
