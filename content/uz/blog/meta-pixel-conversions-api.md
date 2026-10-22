---
title: Meta Pixel va Conversions API: nima uchun kerak va qanday o‘rnatiladi
description: Meta Pixel va Conversions API reklamaga qanday yordam beradi, qanday hodisalarni kuzatish kerak va o‘rnatishda ko‘p uchraydigan xatolar.
date: 2026-10-22
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

## Xulosa

Pixel va Conversions API — reklamaning «ko‘zi». Ularsiz algoritm qorong‘ida ishlaydi, siz esa arzon, lekin sotuvga aylanmaydigan arizalar uchun pul to‘laysiz. Level Marketing har bir loyihada kuzatuvni birinchi haftada sozlaydi.

## Shu mavzuda yana

- [Lookalike auditoriya: mijozlaringizga o‘xshash odamlarni qanday topish](/blog/lookalike-auditoriya/)
- [Retargeting: sotib olmaganlarni qanday qaytarish mumkin](/blog/retargeting-qanday-ishlaydi/)
- [Instagram'da target reklama qanday sozlanadi: bosqichma-bosqich qo‘llanma](/blog/instagramda-target-reklama-sozlash/)
