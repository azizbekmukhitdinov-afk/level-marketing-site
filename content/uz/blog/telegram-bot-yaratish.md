---
title: Telegram bot yaratish: BotFather’dan birinchi arizagacha
description: Biznes uchun Telegram bot qanday yaratiladi: BotFather orqali bot ochish, token xavfsizligi, konstruktor yoki dasturchi, menyu va ariza ssenariysi, CRM’ga ulash va xatolar.
date: 2026-11-24
slug: telegram-bot-yaratish
type: article
tags: Telegram bot, avtomatlashtirish, arizalar, sozlash
key: telegram-bot-yaratish
rubric: biznes
---

Telegram bot — biznes uchun 24 soat ishlaydigan yordamchi: arizani qabul qiladi, narx ro‘yxatini yuboradi, buyurtma holatini aytadi, menejerga xabar beradi. Botni yaratish bir necha daqiqa oladi, lekin uni foydali qilish — to‘g‘ri ssenariy va integratsiya masalasi. Qadamma-qadam ko‘rib chiqamiz. Botlar arizalar uchun qanday ishlashi — [Telegram bot orqali arizalar](/blog/telegram-bot-orqali-arizalar/).

## 1-qadam: BotFather orqali bot ochish

1. Telegram’da rasmiy **@BotFather** ni toping (ko‘k belgili).
2. `/newbot` buyrug‘ini yuboring.
3. Bot nomini kiriting — masalan, «Zamon Mebel yordamchi» (shartli misol).
4. Username kiriting — u «bot» bilan tugashi shart: @zamonmebel_bot.
5. BotFather sizga **token** beradi — bu botning kaliti.

## 2-qadam: tokenni himoya qiling

Token — bot ustidan to‘liq nazorat. Uni:

- faqat ishonchli dasturchi yoki konstruktorga bering;
- chatlarda, skrinshotlarda va ochiq joylarda saqlamang;
- sizib chiqsa — BotFather’da darhol yangilang.

## 3-qadam: qanday ishlatish — konstruktor yoki dasturchi

| | Bot konstruktori | Dasturchi |
|---|---|---|
| Muddat | Bir necha soat–kun | Bir necha kun–hafta |
| Narx | Arzon, oylik to‘lov | Yuqoriroq |
| Imkoniyat | Shablon ssenariylar | Har qanday mantiq, CRM, to‘lov |
| Kimga | Ariza, FAQ, oddiy katalog | Murakkab jarayonlar |

Oddiy prototipni AI bilan ham yasash mumkin — [vibe coding biznes uchun](/blog/vibe-coding-biznes/).

## 4-qadam: ariza ssenariysi

Yaxshi bot — qisqa:

1. **Salomlashish**: «Assalomu alaykum! Oshxona narxini 1 daqiqada hisoblaymiz».
2. **2–3 ta savol**: nima kerak, o‘lcham yoki byudjet, tuman.
3. **Telefon**: «Raqamni ulashish» tugmasi bilan.
4. **Yakun**: «Menejer 15 daqiqada qo‘ng‘iroq qiladi» — va va’dani bajaring.

Ko‘p savol — arizalar kamayadi. Savollar haqida — [lid forma savollari](/blog/lid-forma-savollari/).

## 5-qadam: menyu va tugmalar

- Asosiy menyu: «Narxlar», «Katalog», «Buyurtma», «Menejer bilan bog‘lanish».
- Tugmalar matn yozishdan osonroq — ayniqsa telefonda.

## 6-qadam: CRM va menejerga ulash

Ariza botda qolib ketmasin:

- har bir ariza — CRM’ga yoki menejer guruhiga;
- manba belgisi: botga havola parametri bilan qaysi reklamadan kelgani — [UTM belgilar](/blog/utm-belgilar/);
- javob tezligini kuzating — [arizaga javob tezligi](/blog/arizaga-javob-tezligi/).

## Qonun va maxfiylik

Bot telefon va ism yig‘sa — bu shaxsiy ma’lumot. Rozilik matni va maxfiylik siyosati kerak — [mijozlar bazasi va shaxsiy ma’lumotlar](/blog/mijozlar-bazasi-shaxsiy-malumotlar/). Bot orqali reklama xabarlari yuborish qoidalari — [Telegram bot rassilka qoidalari](/blog/telegram-bot-rassilka-qoidalari/).

## Savol-javob

### Bot bepulmi?

Botni ochish bepul. Konstruktor yoki server va dasturchi ishi pullik bo‘lishi mumkin.

### Botga AI ulasa bo‘ladimi?

Ha, savollarga javob berish uchun — lekin narx va murakkab savollar menejerga — [Telegram AI javobchi](/blog/telegram-ai-javobchi/).

### Bot va Telegram Business farqi?

Bot — alohida akkaunt va avtomat. Telegram Business — shaxsiy akkauntga biznes funksiyalari — [Telegram Business](/blog/telegram-business/).

## Xulosa

Telegram bot yaratish — BotFather’da 5 daqiqa, lekin natija ssenariyga bog‘liq: qisqa savollar, telefon tugmasi, CRM’ga ulash va tez javob. Tokenni himoya qiling va shaxsiy ma’lumot qoidalariga amal qiling. Level Marketing arizalarga 30 daqiqada javob beradi — bepul auditda ariza jarayoningizni tekshiramiz.

## Shu mavzuda yana

- [Telegram bot orqali arizalarni yig‘ish: biznes uchun qo‘llanma](/blog/telegram-bot-orqali-arizalar/)
- [Telegram’da AI-javobchi: arizalarga 24/7 javob](/blog/telegram-ai-javobchi/)
- [Telegram kanal ochish: biznes uchun qadamma-qadam qo‘llanma](/blog/telegram-kanal-ochish/)
