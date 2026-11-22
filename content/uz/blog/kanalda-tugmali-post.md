---
title: Kanaldagi tugmali post: bot orqali joylash va bosishni sanash
description: Kanaldagi tugmali post qanday qilinadi: botni kanalga ulash, tugma turlari, tugma matni uchun qoidalar va bosishlarni sanashning uch usuli — jadvallar bilan.
date: 2026-11-22
slug: kanalda-tugmali-post
type: article
tags: Telegram, kanal, bot, tugma
key: kanalda-tugmali-post
rubric: smm
weight: 1
---

Telegram kanalda post ostida «Narxni bilish» yoki «Yozilish» degan tugma tursa, odam matn ichidan havola qidirmaydi — bitta bosadi. Lekin oddiy post yozish oynasida bunday tugma yo‘q: kanaldagi tugmali post bot orqali joylanadi. Quyida uni qanday ulash, tugmaga nima yozish va eng muhimi — bosishlarni qanday sanash kerakligini qadam-baqadam ko‘rsatamiz.

![Kanaldagi tugmali post nima va u qachon kerak](/img/blog/illus/kanalda-tugmali-post-1.jpg 1200x675)

## Kanaldagi tugmali post nima va u qachon kerak

Tugmali post — bu ostida bir yoki bir nechta tugma turgan oddiy kanal posti. Telegram’da bu tugmalar «inline klaviatura» deyiladi: u xabarning o‘ziga yopishgan bo‘ladi va post bilan birga ko‘rinadi. Bunday klaviaturani faqat bot qo‘sha oladi, shuning uchun postni kanalga siz emas, sizning botingiz joylaydi.

Tugma quyidagi hollarda foyda beradi:

- postning bitta aniq maqsadi bor: yozilish, narx so‘rash, katalogni ochish;
- odamni kanaldan botga yoki saytga olib o‘tmoqchisiz;
- qaysi post nechta odamni olib kelganini bilmoqchisiz.

Agar post shunchaki yangilik yoki foydali maslahat bo‘lsa, tugma shart emas. Har bir postga tugma qo‘ysangiz, obunachilar unga ko‘nikib qoladi va bosmay qo‘yadi.

## Tugma turlari: qaysi biri kanalda ishlaydi

[Telegram Bot API hujjatida](https://core.telegram.org/bots/api#inlinekeyboardbutton) yozilishicha, har bir tugma faqat bitta ish qiladi: yo havola ochadi, yo botga signal yuboradi, yo matnni nusxalaydi. Bitta tugmaga ikki vazifani birdan berib bo‘lmaydi. Biznes uchun kerakli turlari jadvalda.

| Tugma turi | Bosilganda nima bo‘ladi | Kanalda | Qachon ishlatiladi |
|---|---|---|---|
| Havola (url) | Sayt yoki Telegram ichidagi havola ochiladi | Ishlaydi | Botga, saytga, katalogga o‘tkazish |
| Signal (callback) | Bot bosilgani haqida xabar oladi, odam kanaldan chiqmaydi | Ishlaydi | So‘rovnoma, «Menga ham kerak», bosishni sanash |
| Nusxalash (copy_text) | Matn telefon xotirasiga nusxalanadi | Ishlaydi | Promokod, manzil, telefon raqami |
| Mini-ilova (web_app) | Bot ichidagi ilova ochiladi | Faqat bot bilan shaxsiy chatda | Kanal posti uchun mos emas |

Bir nechta chegara ham hujjatda aniq yozilgan:

- signal tugmasida botga yuboriladigan ma’lumot — 1 dan 64 baytgacha, ya’ni qisqa belgi (`narx_divan`), uzun matn emas;
- nusxalanadigan matn — 256 belgigacha;
- matnli post — 4096 belgigacha, rasm ostidagi matn — 1024 belgigacha;
- tugmaga rang berish mumkin: qizil, yashil yoki ko‘k uslub.

Tugmalar qatorlarga teriladi. Bir qatorga ikkita-uchta tugma qo‘yish mumkin, lekin telefonda uzun matn kesilib qoladi. Shuning uchun asosiy tugmani alohida qatorga qo‘ying.

## Botni kanalga ulash: 5 qadam

Dasturchi bo‘lish shart emas, lekin ketma-ketlikni bilish kerak — shunda ishni kimga topshirsangiz ham nazorat qila olasiz.

1. **Bot yarating.** Telegram’da @BotFather’ni oching, yangi bot yarating va token oling. Token — botning kaliti. Uni hech kimga, hatto ekran suratida ham ko‘rsatmang.
2. **Botni kanalga administrator qiling.** Kanal sozlamalarida administratorlar ro‘yxatiga botni qo‘shing va faqat kerakli huquqni bering: post joylash. Keyin postni tahrirlamoqchi bo‘lsangiz — tahrirlash huquqini ham. Boshqa huquqlar (administrator qo‘shish, obunachilarni chiqarish) botga kerak emas.
3. **Postni tayyorlang.** Matn, rasm va tugmalar: har bir tugma uchun yozuv va havola yoki signal belgisi. Havolaga albatta belgi qo‘shing — bu haqda quyida.
4. **Avval sinov kanaliga yuboring.** Yopiq sinov kanali oching, botni u yerga ham qo‘shing. Post telefonda qanday ko‘rinishini, tugma yozuvi kesilmaganini va havola to‘g‘ri ochilishini tekshiring.
5. **Asosiy kanalga joylang.** Bot postni kanal nomidan chiqaradi — obunachi uchun u oddiy postdan farq qilmaydi, faqat ostida tugma bor.

Postni qanday yuborish — ikki yo‘l bor. Birinchisi: tayyor «post-bot» xizmatlari, ularda matn va tugmani oddiy chatda terasiz. Ikkinchisi: o‘z botingiz, uni dasturchi bir marta sozlab beradi. Tayyor xizmat tez, lekin unda ham botga kanalda administrator huquqi beriladi — kimga ishonayotganingizni tekshiring. O‘z botingiz bo‘lsa, baza va statistika o‘zingizda qoladi. Bot allaqachon arizalar qabul qilayotgan bo‘lsa (bu haqda [bot orqali arizalar yig‘ish](/blog/telegram-bot-orqali-arizalar/) maqolasida yozganmiz), postni ham shu bot joylagani qulay.

Yaxshi xabar: post chiqqandan keyin ham tugmani o‘zgartirish mumkin. Bot API’da buning uchun alohida usul bor — u faqat klaviaturani almashtiradi, matnga tegmaydi. Aksiya tugadimi — tugmani «Aksiya tugadi, katalogni ko‘rish»ga almashtirasiz, postni o‘chirish shart emas.

![Tugma matni: 6 qoida](/img/blog/illus/kanalda-tugmali-post-2.jpg 1200x675)

## Tugma matni: 6 qoida

Tugma — postdagi eng qisqa va eng muhim matn. Odam butun postni o‘qimasligi mumkin, lekin tugmani ko‘radi.

1. **Fe’l bilan boshlang.** «Katalog» emas, «Katalogni ochish». Odam bosganda nima bo‘lishini bilsin.
2. **2–4 so‘z.** Uzun yozuv telefonda kesiladi. Sinov kanalida albatta tekshiring.
3. **Bitta post — bitta asosiy tugma.** Uchta teng tugma bo‘lsa, odam tanlay olmay, hech birini bosmaydi.
4. **Natijani va’da qiling, jarayonni emas.** «Botga o‘tish» — jarayon. «Narxni hisoblash» — natija.
5. **Post va tugma bir narsa haqida bo‘lsin.** Post divan haqida, tugma esa «Barcha mahsulotlar» — odam adashadi.
6. **Tugmadan keyin va’da bajarilsin.** «Narxni bilish» bosildi — bot darhol narxni ko‘rsatsin, avval beshta savol bermasin.

| Zaif tugma | Kuchli tugma | Nega |
|---|---|---|
| Batafsil | Narxni bilish | Odam nima olishini biladi |
| Bot | Bo‘sh vaqtni tanlash | Fe’l va natija bor |
| Bosing | Katalogni ochish | Aniq harakat |
| Biz bilan bog‘laning | Menejerga yozish | Qisqa, telefonda kesilmaydi |

## Bosishlarni qanday sanash: 3 usul

Bu yerda ko‘pchilik adashadi. Havola tugmasi bosilganda Telegram botga hech narsa aytmaydi: odam shunchaki havolaga o‘tib ketadi. Demak, «tugma necha marta bosildi» degan tayyor raqam yo‘q. Uni o‘zingiz o‘lchaysiz.

| Usul | Nimani ko‘rasiz | Nima kerak |
|---|---|---|
| Botga start-havola | Qaysi postdan nechta odam botni ishga tushirgani | Har bir postga alohida parametr: `?start=post_2211` |
| Saytga UTM-belgili havola | Qaysi postdan nechta odam saytga kirgani | Havolaga UTM qo‘shish va sayt analitikasi |
| Signal (callback) tugmasi | Har bir bosish va kim bosgani | O‘z botingiz, u bosishlarni yozib boradi |

**Start-havola.** Tugma havolasi `https://t.me/bot_nomi?start=post_2211` ko‘rinishida bo‘ladi. Odam botni ishga tushirsa, bot shu belgini oladi va qaysi postdan kelganini yozib qo‘yadi. Belgi qoidalari va namunalar [kanal obunachilarini botga o‘tkazish](/blog/kanal-obunachilarini-botga-otkazish/) maqolasida bor. Diqqat: bu usul bosishni emas, botni ishga tushirganlarni sanaydi. Bosib, «Start»ni bosmay chiqib ketganlar ko‘rinmaydi.

**UTM-belgi.** Tugma saytga olib borsa, havolaga UTM qo‘shing: manba — telegram, kampaniya — post nomi. Qanday tuzish kerakligi [UTM-belgilar](/blog/utm-belgilar/) maqolasida tushuntirilgan.

**Signal tugmasi.** Bu tugma bosilganda bot har safar xabar oladi va unda kim bosgani ham bo‘ladi. Bot odamga qisqa bildirishnoma ko‘rsata oladi (hujjat bo‘yicha — 200 belgigacha), masalan: «Qabul qilindi, menejer yozadi». Hujjatda yana bir imkoniyat yozilgan: bot bosishga javoban `t.me/bot_nomi?start=...` ko‘rinishidagi havolani ochishi mumkin. Ya’ni bosish sanaladi va odam botga o‘tadi — ikki ish birdan. Buning uchun o‘z botingiz kerak.

Raqamlarni har hafta bitta jadvalga yozing. Quyidagi jadval — **shartli misol**, mebel do‘koni kanali uchun; raqamlar faqat hisoblash tartibini ko‘rsatadi.

| Post | Ko‘rishlar | Botni ishga tushirgan | Ulushi | Ariza |
|---|---|---|---|---|
| Divan, «Narxni hisoblash» | 2 000 | 60 | 3% | 9 |
| Oshxona, «Katalogni ochish» | 1 800 | 27 | 1,5% | 2 |
| Aksiya, «Chegirmani olish» | 2 400 | 96 | 4% | 6 |

Bu jadvaldan ikki xulosa chiqadi. Birinchisi: ulushni postlar orasida solishtiring, «yaxshi» degan umumiy me’yor izlamang — har bir kanalda u boshqacha. Ikkinchisi: oxirgi ustunga qarang. Aksiya posti ko‘p odamni botga olib keldi, lekin ariza divan postidan ko‘proq. Maqsad bosish emas, ariza.

![Tugmali postdagi 6 ta xato](/img/blog/illus/kanalda-tugmali-post-3.jpg 1200x675)

## Tugmali postdagi 6 ta xato

1. **Barcha postlarda bitta havola.** Belgisiz havola bilan qaysi post ishlaganini bilib bo‘lmaydi. Har bir postga alohida parametr bering.
2. **Botga ortiqcha huquq berish.** Post joylaydigan botga administrator qo‘shish yoki obunachilarni boshqarish huquqi kerak emas.
3. **Tokenni chatga tashlash.** Token kimda bo‘lsa, u bot nomidan kanalga post chiqara oladi. Token tarqalib ketgan bo‘lsa, @BotFather’da yangisini oling.
4. **Tugma ortida bo‘sh bot.** Odam «Narxni bilish»ni bosdi, bot esa «Salom!» deb jim turibdi. Avval botdagi yo‘lni tayyorlang, keyin post chiqaring.
5. **Juda ko‘p tugma.** Besh-oltita tugma — bu menyu, post emas. Menyu botning ichida bo‘lsin.
6. **Reklama postida tugmani tekshirmaslik.** Boshqa kanalda [reklama joylashtirganingizda](/blog/telegram-ads-reklama/) ham havolaga alohida parametr qo‘ying va post chiqqach, tugmani o‘zingiz bosib ko‘ring.

## Savol-javob

**Tugmali postni botsiz, oddiy post kabi yozsa bo‘ladimi?**
Post ostidagi tugma — bot klaviaturasi, uni bot qo‘shadi. Botsiz variant — matn ichidagi oddiy havola. U ham ishlaydi, lekin tugmadek ko‘zga tashlanmaydi.

**Bot post joylasa, kanalda «bot» deb yoziladimi?**
Yo‘q, post kanal nomidan chiqadi. Obunachi uni oddiy post kabi ko‘radi.

**Tugmani kim bosganini ko‘rish mumkinmi?**
Havola tugmasida — yo‘q, faqat botni ishga tushirganlar ko‘rinadi. Signal tugmasida bot bosgan odam haqida ma’lumot oladi. Lekin bu unga reklama yozish huquqini bermaydi: odam botni o‘zi ishga tushirmaguncha bot unga yoza olmaydi. Keyingi xabarlar uchun [rassilka qoidalariga](/blog/telegram-bot-rassilka-qoidalari/) amal qiling.

**Eski postga tugma qo‘shsa bo‘ladimi?**
Postni bot joylagan bo‘lsa — ha, bot klaviaturani keyin ham o‘zgartira oladi. O‘zingiz qo‘lda yozgan postlar uchun botga tahrirlash huquqi kerak bo‘ladi; bu ishlashini avval sinov kanalida tekshiring.

**Bitta postga nechta tugma qo‘ygan ma’qul?**
Bitta asosiy tugma, ko‘pi bilan yana bitta yordamchi. Masalan: «Narxni hisoblash» va ostida «Manzilni nusxalash».

Kanaldagi tugmali post murakkab emas: bot kanalga administrator bo‘ladi, postga bitta aniq tugma qo‘yiladi va har bir havolaga alohida belgi beriladi. Qolgani — har hafta raqamlarni solishtirish va ariza bergan postlarni takrorlash. Level Marketing mijozlar bilan ishlaganda kanal postlari, bot va CRM’ni bitta zanjirga ulaydi, shunda har bir ariza qaysi postdan kelgani ko‘rinib turadi.

## Shu mavzuda yana

- [Kanal obunachilarini botga o‘tkazish: havola va birinchi xabar](/blog/kanal-obunachilarini-botga-otkazish/)
- [Telegram kanalni noldan qanday o‘stirish mumkin](/blog/telegram-kanal-osish/)
- [Telegram botda rassilka: mijoz bloklamasligi uchun 7 qoida](/blog/telegram-bot-rassilka-qoidalari/)
