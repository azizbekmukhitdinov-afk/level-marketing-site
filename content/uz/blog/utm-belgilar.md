---
title: UTM-belgilar: har bir mijoz qayerdan kelganini qanday bilish
description: UTM nima, parametrlar, havolani qanday yaratish, nomlash qoidalari va natijani qayerda ko‘rish.
date: 2026-10-22
updated: 2026-10-23
slug: utm-belgilar
type: article
tags: sotuv, analitika
key: utm-belgilar
rubric: sotuv
---

Saytga Instagram, Telegram, Google va hamkor kanallardan odamlar keladi — lekin qaysi biri ariza va sotuv olib kelyapti? **UTM-belgilar** bu savolga javob beradi: ular havolaga qo‘shiladigan kichik «yorliqlar» bo‘lib, analitikada har bir tashrif manbasini ko‘rsatadi. Bu maqolada UTM nima ekanini, havolani qanday yaratish va natijani qayerda ko‘rishni ko‘rib chiqamiz.

![UTM parametrlari](/img/blog/illus/utm-belgilar-1.jpg 1200x675)

## UTM parametrlari

| Parametr | Nimani bildiradi | Misol |
|---|---|---|
| utm_source | Manba | instagram, telegram, google |
| utm_medium | Kanal turi | cpc, post, stories, email |
| utm_campaign | Kampaniya | divan_oktyabr |
| utm_content | Kreativ yoki variant | video_a, banner_b |
| utm_term | Kalit so‘z (qidiruv reklamasi uchun) | divan_toshkent |

Misol havola:

`https://levelm.uz/?utm_source=instagram&utm_medium=cpc&utm_campaign=audit_oktyabr&utm_content=video_a`

## Havolani qanday yaratish

- Google'ning **Campaign URL Builder** vositasi — maydonlarni to‘ldirasiz, havola tayyor.
- Jadval shabloni: ustunlarda parametrlar, oxirgi ustunda formula bilan yig‘ilgan havola — butun jamoa bir xil nomlardan foydalanadi.

## Nomlash qoidalari

1. Faqat kichik harflar: «Instagram» va «instagram» — analitikada ikki xil manba.
2. Bo‘sh joy o‘rniga pastki chiziq yoki chiziqcha.
3. Bir xil narsa — doim bir xil nom.
4. Barcha nomlarni bitta hujjatda yozib qo‘ying.

## Natijani qayerda ko‘rish

- **Google Analytics 4** — trafik manbalari hisobotida source, medium va campaign kesimida.
- **Yandex Metrika** — UTM-belgilar bo‘yicha hisobotlar.
- **CRM** — sayt formasi orqali kelgan arizaga UTM qiymatlarini saqlasangiz, sotuvni aniq manbaga bog‘laysiz. CRM tanlash haqida — [alohida maqolada](/blog/crm-tanlash/).

![Sayt bo‘lmasa-chi](/img/blog/illus/utm-belgilar-2.jpg 1200x675)

## Sayt bo‘lmasa-chi

Instagram va Telegram ichida UTM ishlamaydi. U holda:

- Telegram kanal uchun har bir manbaga alohida nomli taklif havolasi yarating — bu haqda [Telegram reklama](/blog/telegram-ads-reklama/) maqolasida.
- Do‘konlar uchun — har bir kanal uchun alohida promokod.
- Arizada «Bizni qayerdan topdingiz?» degan savol.

## Ko‘p uchraydigan xatolar

- Bir kampaniyaga turli nomlar.
- Sayt ichidagi havolalarga UTM qo‘yish — bu manbani «buzadi».
- Havolani qo‘lda yozib, xato qilish — har doim tekshirib ko‘ring.

## Tayyor UTM jadvali (namuna)

| Kanal | utm_source | utm_medium | utm_campaign |
|---|---|---|---|
| Instagram reklama | instagram | cpc | divan_oktyabr |
| Instagram bio havolasi | instagram | bio | doimiy |
| Telegram kanal posti | telegram | post | divan_oktyabr |
| Telegram Ads | telegram | cpc | divan_oktyabr |
| Google qidiruv | google | cpc | divan_oktyabr |
| Email rassilka | email | newsletter | noyabr_aksiya |

Bitta kampaniya barcha kanallarda bitta utm_campaign nomiga ega bo‘lsin — shunda uning umumiy natijasini bir qatorda ko‘rasiz.

## UTM natijasini qanday o‘qish

GA4'dagi trafik manbalari hisobotida tashriflar bilan birga arizalarni (konversiyalarni) ham ko‘ring. Faqat tashriflar soniga qarash noto‘g‘ri xulosaga olib keladi.

**Misol (shartli raqamlar):** Instagram reklamadan 1 000 ta tashrif va 20 ta ariza, Telegram postdan 300 ta tashrif va 15 ta ariza. Birinchisi ko‘proq odam olib keladi, lekin Telegram'dan kelganlar ancha «issiqroq»: 5% ga qarshi 2%. Bunday solishtirish byudjetni qayerga ko‘paytirishni ko‘rsatadi.

![UTM'ni arizagacha yetkazish](/img/blog/illus/utm-belgilar-3.jpg 1200x675)

## UTM'ni arizagacha yetkazish

Analitika tashrif manbasini ko‘rsatadi, lekin sotuvni ko‘rish uchun UTM arizaning o‘zida saqlanishi kerak. Buning oddiy usuli — sayt formasidagi yashirin maydonlar: sahifa ochilganda havoladagi utm_source, utm_medium va utm_campaign qiymatlari ularga yoziladi va ariza bilan birga CRM'ga tushadi. Shundan keyin hisobot «qaysi kampaniya qancha tashrif berdi» degan savolga emas, balki «qaysi kampaniya qancha sotuv va daromad keltirdi» degan savolga javob beradi. Ko‘p sayt konstruktorlari va CRM integratsiyalarida bunday maydonlar tayyor bo‘ladi — sozlashdan oldin tekshiring.

## Savol-javob

### UTM saytning qidiruvdagi o‘rniga zarar qiladimi?

Yo‘q, agar UTM'lar faqat tashqi havolalarda bo‘lsa. Ularni sayt ichidagi havolalarga qo‘ymang va sahifalarning asosiy manzili (canonical) to‘g‘ri ko‘rsatilganiga ishonch hosil qiling.

### UTM'li havolani qisqartirsa bo‘ladimi?

Ha. Qisqa havola bosilganda baribir to‘liq havola ochiladi va belgilar saqlanadi. Faqat qisqartirilgandan keyin ham bir marta bosib tekshirib ko‘ring.

### Instagram bio'dagi havolaga UTM qo‘yish kerakmi?

Ha — shunda profil orqali kelgan tashriflarni reklamadan ajratasiz. Masalan: utm_source=instagram va utm_medium=bio.

### utm_content qachon kerak?

Bitta kampaniyada bir nechta kreativ yoki bitta postda bir nechta havola bo‘lsa. Masalan, video_a va video_b yoki «tugma» va «matndagi havola» — shunda qaysi variant ko‘proq ariza berganini ko‘rasiz.

## Xulosa

UTM-belgilar — har bir mijoz qayerdan kelganini bilishning eng oddiy usuli. Ularsiz [ROMI](/blog/romi-hisoblash/) va kanallar samaradorligini to‘g‘ri hisoblab bo‘lmaydi. Bitta shablon yarating, nomlash qoidalariga amal qiling va natijani har oy tahlil qiling.

## Shu mavzuda yana

- [Takroriy sotuv va LTV: mavjud mijozlardan ko‘proq daromad](/blog/takroriy-sotuv-ltv/)
- [Mijozlardan fikr-mulohaza qanday yig‘iladi va undan qanday foydalaniladi](/blog/mijoz-fikrini-yigish/)
- [Lid narxi (CPL) nima va uni qanday kamaytirish mumkin: tadbirkor uchun qo‘llanma](/blog/lid-narxi-cpl-qanday-kamaytirish/)
