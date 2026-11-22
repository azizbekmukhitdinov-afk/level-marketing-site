---
title: Kanal obunachilarini botga o‘tkazish: havola va birinchi xabar
description: Kanal obunachilarini botga o‘tkazish rejasi: start-havola (deep link), botga kirish uchun sabab, birinchi xabar, rozilik tugmasi va natijani o‘lchash jadvali.
date: 2026-11-15
slug: kanal-obunachilarini-botga-otkazish
type: article
tags: Telegram, bot, kanal, mijozlar bazasi
key: kanal-obunachilarini-botga-otkazish
rubric: smm
---

Telegram kanalda 5 000 obunachi bo‘lishi mumkin, lekin siz ularning birortasiga shaxsan yoza olmaysiz: kim o‘qidi, kim xarid qilmoqchi — ko‘rinmaydi. Kanal obunachilarini botga o‘tkazish shu muammoni hal qiladi: odam botda «Start» bosgach, u bilan alohida gaplashish, qiziqishini bilish va taklif yuborish mumkin bo‘ladi. Quyida buni qanday qilish kerakligi qadam-baqadam: havola, sabab, birinchi xabar, rozilik va o‘lchash.

## Nega kanal obunachilarini botga o‘tkazish kerak

Kanal — bir tomonlama efir. Siz post yozasiz, odamlar o‘qiydi yoki o‘qimaydi. Bot esa har bir odam bilan alohida chat. Farqni jadvalda ko‘ring.

| | Kanal obunachisi | Botni ishga tushirgan odam |
|---|---|---|
| Unga shaxsan yozish | Mumkin emas | Mumkin (u «Start» bosgan) |
| Qayerdan kelgani | Umumiy statistika | Har bir odam bo‘yicha ko‘rinadi (start-parametr) |
| Qiziqishi | Noma’lum | Botda bosgan tugmalaridan bilinadi |
| Telefon raqami | Yo‘q | Odam o‘zi ulashsa — bor |
| Segment bo‘yicha taklif | Hammaga bir xil post | Til, filial, qiziqish bo‘yicha |

Yana bir sabab — xavfsizlik. Kanal obunachilari ro‘yxatini siz eksport qila olmaysiz. Botda esa baza o‘zingizda: kim kirgan, qachon, nimaga rozilik bergan.

Muhim cheklov: Telegram qoidasiga ko‘ra bot odamga birinchi bo‘lib yoza olmaydi, foydalanuvchi avval botni o‘zi ishga tushirishi kerak. Shuning uchun «kanal obunachilarini botga ko‘chirib qo‘yish» degan tugma yo‘q. Har bir odam o‘zi o‘tishi kerak — va unga buning uchun sabab berish sizning vazifangiz.

## Start-havola (deep link) qanday ishlaydi

Har bir botning havolasi bor: `https://t.me/bot_nomi`. Unga parametr qo‘shish mumkin: `https://t.me/bot_nomi?start=kanal_pin`. Odam shu havola orqali kirib «Start» bossa, bot `/start kanal_pin` degan buyruqni oladi va odam aynan qaysi joydan kelganini biladi.

Telegram’ning [botlar uchun rasmiy qo‘llanmasida](https://core.telegram.org/bots/features) parametr qoidalari yozilgan:

- faqat lotin harflari (A–Z, a–z), raqamlar (0–9), pastki chiziq `_` va defis `-` ishlatiladi;
- uzunligi 64 belgigacha;
- odam botni birinchi marta ochganda «Start» tugmasini ko‘radi.

Ya’ni bo‘sh joy, kirill harflari va `o‘` kabi belgilar bo‘lmaydi. Qisqa va tushunarli nom bering.

| Havola qayerda turadi | Parametr namunasi |
|---|---|
| Kanaldagi mahkamlangan post | `start=kanal_pin` |
| Oddiy post ostidagi tugma | `start=kanal_post_1511` |
| Kanal tavsifi (bio) | `start=kanal_bio` |
| Boshqa kanaldagi reklama | `start=reklama_kanal1` |
| Do‘kondagi QR-kod | `start=qr_dokon` |

Parametr orqali faqat manbani emas, mavzuni ham uzatish mumkin: `start=katalog_divan` bilan kirgan odamga bot darhol divanlar katalogini ochadi. Reklama manbalarini parametr bilan ajratish haqida [bot orqali arizalar yig‘ish](/blog/telegram-bot-orqali-arizalar/) maqolasida ham yozganmiz.

## Odamga botga o‘tish uchun sabab bering

«Botimizga ham obuna bo‘ling» — bu sabab emas. Odam kanalda hamma narsani ko‘rib turibdi, botga nega kirsin? Unga kanalda yo‘q narsa kerak.

Ishlaydigan sabablar:

1. **Shaxsiy hisob-kitob.** «O‘lchamni yozing — narxini bot hisoblab beradi» (mebel, deraza, ta’mir).
2. **Foydali fayl.** Narxlar ro‘yxati, katalog PDF, chek-list. Bu klassik [lid-magnit](/blog/lid-magnit/), faqat e-mail o‘rniga bot.
3. **Yozilish yoki band qilish.** Klinika, salon, o‘quv markazi uchun: bo‘sh vaqtni tanlash.
4. **Buyurtma holati.** «Buyurtmangiz qayerda — botdan ko‘ring».
5. **Faqat botdagilar uchun taklif.** Aksiya haqida birinchi bo‘lib xabar olish.
6. **Savolga tez javob.** «Savolingizni botga yozing — menejer javob beradi».

Bitta postda bitta sabab ayting. Eng yaxshisi — odam hozir hal qilmoqchi bo‘lgan masalaga bog‘liq sabab: divan tanlayotgan odamga katalog, kursga qiziqqan odamga sinov darsi jadvali.

## Havolani kanalda qayerga qo‘yish

Bitta post bilan ish bitmaydi: postni obunachilarning bir qismigina ko‘radi. Havola doim ko‘z oldida tursin.

- **Mahkamlangan post.** Bot nima berishini 2–3 jumlada tushuntiring va havolani qo‘ying. Yangi obunachi birinchi shuni ko‘radi.
- **Post ostidagi tugma.** Tugmali postni odatda kanalga admin qilib qo‘shilgan bot yoki post tayyorlash servisi orqali joylanadi. Tugma matni aniq bo‘lsin: «Narxini hisoblash», «Katalogni olish».
- **Kanal tavsifi.** Qisqa jumla va havola: «Buyurtma va savollar — @bot_nomi».
- **Muntazam eslatma.** Har 5–7 postdan birida mavzuga mos chaqiriq. Mebel haqidagi postdan keyin — «shu modellar narxi botda».
- **Kanaldan tashqari.** Instagram bio, sayt, do‘kondagi QR-kod. Har biriga alohida parametr.

Kanalning o‘zini qanday o‘stirish — [alohida maqolada](/blog/telegram-kanal-osish/). Bu yerda vazifa boshqa: bor obunachini botga olib kirish.

## Botdagi birinchi xabar va rozilik tugmasi

Odam «Start» bosdi. Keyingi 10 soniyada u yo foyda oladi, yo botni yopadi. Birinchi xabar uch ishni qilishi kerak.

**1. Va’dani darhol bajaring.** Katalog va’da qilingan bo‘lsa — birinchi xabarda katalog. Avval «ismingiz, telefoningiz, shahringiz» so‘rab, keyin fayl berish — ko‘pchilikni yo‘qotadi.

**2. Bot nima qilishini ayting.** Bir-ikki jumla: «Bu yerda narx hisoblash, buyurtma berish va menejerga savol yozish mumkin».

**3. Xabar yuborishga rozilik so‘rang.** Ikki tugma:

> Salom! Mana va’da qilingan katalog (fayl).
> Yangi kolleksiya va aksiyalar haqida haftada bir marta yozib tursak maylimi?
> [Ha, yozib turing] [Yo‘q, faqat buyurtmam bo‘yicha]

«Ha» bosilgan sana va vaqtni bazada saqlang. Reklama xabarlarini faqat shu odamlarga yuboring. Nega bu muhim va keyin qanday yozish kerakligi — [botda rassilka qoidalari](/blog/telegram-bot-rassilka-qoidalari/) maqolasida. Bot ism va telefonni saqlasa, bu shaxsga doir ma’lumot: talablar [mijozlar bazasi haqidagi maqolada](/blog/mijozlar-bazasi-shaxsiy-malumotlar/).

Telefon raqamini keyinroq, sabab bilan so‘rang: «Menejer qo‘ng‘iroq qilishi uchun raqamingizni ulashing». Telegram’da buning uchun maxsus «Kontaktni ulashish» tugmasi bor — odam raqamni qo‘lda yozmaydi.

## Natijani qanday o‘lchash

Kamida to‘rtta raqamni har hafta yozib boring.

| Ko‘rsatkich | Qanday hisoblanadi | Nimani ko‘rsatadi |
|---|---|---|
| Botga o‘tish ulushi | Botga kirganlar ÷ post ko‘rishlari | Sabab va chaqiriq ishlayaptimi |
| Manba bo‘yicha kirishlar | Start-parametrlar bo‘yicha | Qaysi joy ko‘proq olib keladi |
| Rozilik ulushi | «Ha» bosganlar ÷ botga kirganlar | Birinchi xabar ishonch uyg‘otdimi |
| Ariza yoki buyurtma | Botdan kelgan arizalar soni | Bot sotuvga olib keldimi |

*Shartli misol — raqamlar tushunarli bo‘lishi uchun o‘ylab topilgan.* Toshkentdagi mebel do‘konining kanalida 4 000 obunachi bor. Do‘kon «o‘lchamni yozing — oshxona narxini bot hisoblaydi» degan post qo‘ydi va uni mahkamladi.

| Manba | Parametr | Botga kirdi | Rozilik berdi | Ariza |
|---|---|---|---|---|
| Mahkamlangan post | `kanal_pin` | 180 | 95 | 14 |
| Post ostidagi tugma | `kanal_post` | 120 | 70 | 11 |
| Kanal tavsifi | `kanal_bio` | 40 | 18 | 3 |

Jadvaldan ko‘rinadi: mahkamlangan post eng ko‘p odam olib kelgan, tavsifdagi havola esa deyarli ishlamagan. Keyingi oyda do‘kon tavsif matnini o‘zgartiradi va boshqa sabab bilan ikkinchi postni sinaydi. Sizning raqamlaringiz boshqacha bo‘ladi — muhimi, ularni manba bo‘yicha alohida ko‘rish.

## 5 ta keng tarqalgan xato

1. **Sababsiz chaqiriq.** «Botimizga o‘ting» — nega? Foyda aytilmasa, hech kim o‘tmaydi.
2. **Hamma joyda bitta havola.** Parametrsiz havola bilan qaysi post ishlaganini bilib bo‘lmaydi.
3. **Birinchi xabarda so‘rovnoma.** Besh savoldan keyin foyda — odam ikkinchi savolda chiqib ketadi.
4. **Roziliksiz reklama.** Botga katalog uchun kirgan odamga ertasi kuni uchta aksiya yuborish — bloklashga to‘g‘ri yo‘l.
5. **Bot javobsiz qoladi.** Odam savol yozdi, menejer ikki kundan keyin ko‘rdi. Botga kelgan xabarlar kimga borishini oldindan belgilang.

## Savol-javob

### Kanal obunachilarini botga avtomatik qo‘shish mumkinmi?

Yo‘q. Bot odamga birinchi bo‘lib yoza olmaydi, obunachilar ro‘yxatini botga «yuklash» ham mumkin emas. Har bir odam havolani bosib, botni o‘zi ishga tushiradi.

### Start-parametrda nima yozish mumkin?

Lotin harflari, raqamlar, `_` va `-`, 64 belgigacha. Masalan: `kanal_pin`, `qr_dokon`, `katalog_divan`. Shaxsiy ma’lumotni (telefon, ism) parametrga yozmang.

### Bot yaratish uchun dasturchi kerakmi?

Oddiy bot (salomlashuv, fayl, tugmalar, ariza) tayyor konstruktorlarda dasturchisiz yig‘iladi. Narx hisoblash, CRM bilan ulanish, murakkab segmentlar uchun dasturchi kerak bo‘ladi. Tanlashda start-parametrni va rozilik belgisini saqlay olishini tekshiring.

### Obunachilarning qancha qismi botga o‘tadi?

Umumiy me’yor yo‘q: bu sababga, kanal faolligiga va chaqiriq qayerda turganiga bog‘liq. O‘z raqamingizni o‘lchang va har oy bitta narsani o‘zgartirib solishtiring.

### Botga o‘tgan odam kanaldan chiqib ketmaydimi?

Yo‘q, bular alohida narsalar: odam kanalda qoladi va botdan ham foydalanadi. Kanal — kontent uchun, bot — shaxsiy muloqot va buyurtma uchun.

## Xulosa

Kanal obunachilarini botga o‘tkazish — bu texnik hiyla emas, oddiy ketma-ketlik: odamga kanalda yo‘q foydani va’da qiling, har bir joyga alohida start-havola qo‘ying, birinchi xabarda va’dani bajaring va rozilik so‘rang, keyin raqamlarni manba bo‘yicha solishtiring. Level Marketing mijozlar bilan ishlaganda kanal, bot va CRM’ni bitta zanjirga ulaydi, shunda har bir ariza qaysi postdan kelgani ko‘rinib turadi.

## Shu mavzuda yana

- [Telegram botda rassilka: mijoz bloklamasligi uchun 7 qoida](/blog/telegram-bot-rassilka-qoidalari/)
- [Telegram kanalni noldan qanday o‘stirish mumkin](/blog/telegram-kanal-osish/)
- [Kanaldagi tugmali post: bot orqali joylash va bosishni sanash](/blog/kanalda-tugmali-post/)
