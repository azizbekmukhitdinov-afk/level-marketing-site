---
title: Meta Pixel va Conversions API: nima uchun kerak va qanday o‘rnatiladi
description: Meta Pixel va Conversions API reklamaga qanday yordam beradi, qanday hodisalarni kuzatish kerak va o‘rnatishda ko‘p uchraydigan xatolar.
date: 2026-10-22
updated: 2026-10-23
slug: meta-pixel-conversions-api
type: article
tags: target reklama, meta ads
key: meta-pixel-conversions-api
rubric: target
---

Reklama sotuv olib kelyaptimi yoki shunchaki bosishlarmi? Bu savolga aniq javobni faqat kuzatuv beradi. Meta reklamasida kuzatuvning ikki vositasi bor: **Meta Pixel** va **Conversions API**. Ushbu maqolada ular nima uchun kerakligini, qaysi hodisalarni kuzatish va o‘rnatishda qanday xatolardan qochish kerakligini ko‘rib chiqamiz.

## Meta Pixel nima

Pixel — saytingizga qo‘yiladigan kichik kod. U tashrif buyuruvchi saytda nima qilganini — sahifani ko‘rgani, formani yuborgani, xarid qilganini — Meta'ga yuboradi. Natijada:

- reklama kabinetida qaysi reklama ariza va sotuv olib kelganini ko‘rasiz;
- algoritm aynan shu harakatni qiladigan odamlarni qidirishni o‘rganadi;
- saytga kirgan, lekin sotib olmaganlar uchun [retargeting](/blog/retargeting-qanday-ishlaydi/) auditoriyasini yaratasiz.

## Conversions API nima va nega Pixel yetmaydi

Pixel brauzer orqali ishlaydi. Reklama blokerlari, iOS cheklovlari va cookie sozlamalari tufayli hodisalarning bir qismi Meta'ga yetib bormaydi. **Conversions API (CAPI)** xuddi shu hodisalarni sizning serveringizdan yuboradi. Ikkalasi birga ishlaganda Meta ma'lumotni to‘liqroq oladi, bir xil hodisaning ikki nusxasi esa `event_id` orqali birlashtiriladi (deduplikatsiya).

## Qaysi hodisalarni kuzatish kerak

| Hodisa | Qachon ishga tushadi | Kimga muhim |
|---|---|---|
| PageView | Har bir sahifa ochilganda | Hammaga |
| ViewContent | Mahsulot yoki xizmat sahifasi | Do‘konlar, xizmatlar |
| Lead | Forma yuborilganda | Xizmat ko‘rsatuvchi bizneslar |
| Contact | Telegram yoki qo‘ng‘iroq tugmasi bosilganda | Kichik biznes |
| InitiateCheckout | Buyurtma rasmiylashtirila boshlanganda | Onlayn do‘kon |
| Purchase | Xarid yakunlanganda | Onlayn do‘kon |

## Qanday o‘rnatiladi: 5 qadam

1. **Events Manager**'da (business.facebook.com) yangi ma'lumot manbai — Pixel yarating.
2. Kodni saytga qo‘shing. Tilda, WordPress yoki Shopify kabi konstruktorlarda tayyor integratsiya bor; o‘zingiz yozgan saytda kod sahifa boshiga yoki Google Tag Manager orqali qo‘yiladi.
3. Asosiy hodisalarni sozlang: kamida Lead yoki Purchase, kichik biznes uchun Contact ham.
4. **Conversions API**'ni ulang: platformaning tayyor integratsiyasi, Google Tag Manager server konteyneri yoki dasturchi yordamida.
5. **Test Events** bo‘limida tekshiring: har bir hodisa kelyaptimi va moslik sifati (Event Match Quality) qanday.

## Ko‘p uchraydigan xatolar

- Pixel saytga ikki marta o‘rnatilgan — hodisalar ikki baravar hisoblanadi.
- Lead hodisasi «Rahmat» sahifasida emas, forma sahifasining o‘zida ishga tushadi — har bir tashrif ariza bo‘lib ko‘rinadi.
- Domen Business Manager'da tasdiqlanmagan.
- Kampaniya maqsadi bilan optimallashtirish hodisasi mos kelmaydi.

## Saytingiz bo‘lmasa-chi

Ko‘p bizneslar Instagram Direct yoki Telegram orqali sotadi. Bunda Pixel kerak emas, lekin sotuvni qayd qilish baribir zarur: arizalarni CRM yoki jadvalda belgilang va qaysi reklama sotuv olib kelganini solishtiring. Ariza narxini qanday hisoblash haqida — [CPL bo‘yicha qo‘llanmamizda](/blog/lid-narxi-cpl-qanday-kamaytirish/).

## Hodisalarni qanday tekshirish

- **Events Manager → Test Events.** Saytingizni ochib, formani yuboring va hodisa real vaqtda paydo bo‘layotganini ko‘ring.
- **Meta Pixel Helper.** Chrome brauzeri uchun kengaytma — sahifada qaysi hodisalar ishlayotganini ko‘rsatadi.
- **Dublikatlar.** Pixel va Conversions API birga ishlasa, bir hodisa ikki marta sanalmasligi uchun ikkalasida bir xil event_id bo‘lishi kerak.
- **Moslik sifati.** Events Manager'da hodisalarning foydalanuvchilar bilan qanchalik yaxshi moslashganini ko‘rsatuvchi baho bor — u past bo‘lsa, Conversions API orqali qo‘shimcha ma'lumot (masalan, xeshlangan telefon) yuboring.

## Hodisa parametrlari

Purchase va Lead hodisalariga **qiymat** (value) va **valyuta** (currency) qo‘shing. Shunda Meta qaysi reklama ko‘proq pul olib kelayotganini ko‘radi va qimmatroq mijozlarga optimallashtira oladi. Katalog bilan ishlaydigan do‘konlar uchun mahsulot identifikatorlari (content_ids) ham kerak — ular dinamik retargetingni ishga tushiradi.

## Maxfiylik va rozilik

Sayt foydalanuvchilarini maxfiylik siyosatida ma'lumot yig‘ish haqida xabardor qiling. Hodisalar orqali sezgir ma'lumot yubormang: tibbiy holatlar, moliyaviy ahvol va boshqalar. Ayniqsa klinikalar ehtiyot bo‘lishi kerak — sahifa manzili yoki hodisa nomi kasallikni oshkor qilmasin. Klinikalar marketingi haqida — [klinika marketingi](/blog/klinika-marketing/) maqolasida.

## Pixel ma'lumotlaridan qanday foydalanish

- Kampaniyalarni bosishga emas, **Lead** yoki **Purchase** hodisasiga optimallashtiring.
- Saytga kirganlar uchun [retargeting](/blog/retargeting-qanday-ishlaydi/) auditoriyalarini yarating.
- Arizachi va xaridorlardan [lookalike auditoriya](/blog/lookalike-auditoriya/) quring.
- Hisobotlarda qaysi kreativ ariza berayotganini ko‘ring.

## Savol-javob

### Pixel o‘rnatish uchun dasturchi kerakmi?

Ko‘p sayt konstruktorlari va CMS'larda Meta bilan tayyor integratsiya bor — Pixel ID'ni kiritish yetarli. Conversions API'ni ham ko‘pincha hamkor integratsiyalari orqali ulash mumkin. Murakkab sayt yoki o‘z serveringiz bo‘lsa, dasturchi kerak bo‘ladi.

### Bitta saytga bir nechta Pixel qo‘ysa bo‘ladimi?

Texnik jihatdan mumkin, lekin chalkashlik keltiradi. Bitta biznesga bitta Pixel yaxshiroq; agentlikka esa Business Manager orqali kirish huquqi bering.

### Pixel auditoriyalari qancha vaqt saqlanadi?

Sayt tashrif buyuruvchilari auditoriyasi uchun eng uzun muddat — 180 kun. Shuning uchun Pixel'ni reklama boshlanishidan ancha oldin o‘rnating: ma'lumot yig‘ila boshlaydi.

### Conversions API'siz ishlasa bo‘ladimi?

Boshlash uchun — ha. Lekin brauzer cheklovlari va reklama bloklovchilar tufayli ma'lumotlarning bir qismi yo‘qoladi. Byudjet o‘sgan sari Conversions API'ni qo‘shing.

### Hodisalar kabinetda ko‘rinmasa nima qilish kerak?

Kod barcha sahifalarda o‘rnatilganini, to‘g‘ri Pixel ID ishlatilganini va reklama bloklovchi o‘chirilganini tekshiring. Test Events orqali hodisani qayta yuboring — hodisalar biroz kechikish bilan ko‘rinishi mumkin.

### Pixel o‘rnatilgach, reklama darhol yaxshilanadimi?

Darhol emas. Algoritm o‘rganishi uchun yetarlicha hodisa to‘planishi kerak — yangi kampaniya odatda bir necha kun «o‘rganish bosqichida» bo‘ladi. Bu davrda sozlamalarni tez-tez o‘zgartirmang, aks holda o‘rganish qaytadan boshlanadi. Natijani kamida bir haftadan keyin baholang.

## Xulosa

Pixel va Conversions API — reklamaning «ko‘zi». Ularsiz algoritm qorong‘ida ishlaydi, siz esa arzon, lekin sotuvga aylanmaydigan arizalar uchun pul to‘laysiz. Level Marketing har bir loyihada kuzatuvni birinchi haftada sozlaydi.

## Shu mavzuda yana

- [Lookalike auditoriya: mijozlaringizga o‘xshash odamlarni qanday topish](/blog/lookalike-auditoriya/)
- [Retargeting: sotib olmaganlarni qanday qaytarish mumkin](/blog/retargeting-qanday-ishlaydi/)
- [Instagram'da target reklama qanday sozlanadi: bosqichma-bosqich qo‘llanma](/blog/instagramda-target-reklama-sozlash/)
