---
title: Telegram bot orqali arizalarni yig‘ish: biznes uchun qo‘llanma
description: Telegram bot orqali arizalarni yig‘ish: savollar ketma-ketligi, menejerga bildirishnoma, CRM, reklama manbasini kuzatish va 1-noyabrdan SMS qoidalari.
date: 2026-10-23
slug: telegram-bot-orqali-arizalar
type: article
tags: telegram, sotuv, avtomatlashtirish, CRM
key: telegram-bot-orqali-arizalar
rubric: sotuv
---

O‘zbekistonda mijoz birinchi navbatda Telegram'ga yozadi. Shuning uchun Telegram bot orqali arizalarni yig‘ish — sayt yoki lid-formadan keyin eng tabiiy kanal: mijoz tanish ilovada qoladi, siz esa tayyor ism, raqam va ehtiyojni olasiz. Bu maqolada bot qanday savollar berishi, ariza qayerga tushishi va uni menejer qanday qayta ishlashini bosqichma-bosqich ko‘rib chiqamiz.

![Nega aynan Telegram bot](/img/blog/illus/telegram-bot-orqali-arizalar-1.jpg 1200x675)

## Nega aynan Telegram bot

Telegram asoschisi Pavel Durov 2024-yil iyunida Toshkentga tashrifidan keyin O‘zbekiston aholisining 70% dan ortig‘i Telegram'da ekanini yozgan edi ([Spot](https://www.spot.uz/oz/2024/06/30/pavel-durov/)). Bu kompaniyaning o‘z ma'lumoti, lekin kundalik tajriba ham shuni ko‘rsatadi: mijozlar do‘kon, klinika yoki o‘quv markaziga qo‘ng‘iroq qilishdan ko‘ra Telegram'da yozishni afzal ko‘radi.

Oddiy «Telegram'ga yozing» tugmasining muammosi bor: har bir mijoz o‘zicha yozadi. Biri «narxi qancha?» deb yozadi, boshqasi ovozli xabar yuboradi, uchinchisi raqamini qoldirmaydi. Menejer har biridan ma'lumotni qaytadan so‘raydi. Bot esa:

- **bir xil tartibda** kerakli savollarni beradi;
- telefon raqamini **bitta tugma** bilan oladi;
- arizani **darhol** menejerga yoki guruhga yuboradi;
- tunda va dam olish kunlarida ham **javob beradi**;
- har bir ariza **qaysi reklamadan** kelganini belgilaydi.

Bu [sotuv voronkasi](/blog/sotuv-voronkasi/)ning «qiziqish → ariza» bosqichini tartibga soladi va menejer vaqtini sotuvga bo‘shatadi.

## Ariza uchun bot qanday savollar berishi kerak

Asosiy qoida: **savol qancha kam bo‘lsa, ariza shuncha ko‘p**. Faqat menejerga birinchi qo‘ng‘iroq uchun kerak bo‘lgan narsani so‘rang. Qolganini suhbatda aniqlaysiz.

Toshkentdagi mebel do‘koni uchun namunaviy ketma-ketlik:

1. **Salomlashish va til tanlash** — «Assalomu alaykum! Tilni tanlang: O‘zbekcha / Русский».
2. **Nima kerak** — tugmalar: «Oshxona», «Shkaf-kupe», «Yotoqxona», «Boshqa».
3. **Taxminiy muddat** — «Shu oy», «1–3 oy ichida», «Hali tanlayapman».
4. **Ism** — erkin matn.
5. **Telefon raqami** — «Raqamni yuborish» tugmasi.
6. **Yakun** — «Rahmat! Dizaynerimiz 15 daqiqa ichida qo‘ng‘iroq qiladi» (ish vaqtida) yoki «Ertalab soat 9:00 da qo‘ng‘iroq qilamiz» (ish vaqtidan tashqari).

Bir nechta amaliy maslahat:

- **Tugmalar matndan yaxshi.** Mijoz bosadi, yozmaydi — xato va tashlab ketish kamayadi.
- **Raqamni tugma orqali oling.** Telegram'da botga kontakt yuborish tugmasi bor: mijoz bir marta bosadi va raqam to‘g‘ri formatda keladi. Bu imkoniyat faqat shaxsiy chatda ishlaydi.
- **Narxni yashirmang.** Agar mijoz birinchi navbatda narxni so‘rasa, botda «Narxlar» bo‘limi bo‘lsin: taxminiy diapazon va «aniq hisob uchun raqam qoldiring».
- **Uzun anketa — sotuvdan keyin.** Xona o‘lchamlari, rang va material — bu dizayner bilan suhbat uchun.

> Botning vazifasi — suhbatni boshlash, menejerni almashtirish emas.

## Ariza qayerga tushadi: uchta variant

Bot arizani yig‘di — endi u yo‘qolmasligi kerak. Biznes hajmiga qarab uchta yo‘l bor:

| Variant | Kimga mos | Afzalligi | Kamchiligi |
|---|---|---|---|
| Menejerlar Telegram guruhiga | 1–3 menejer, kuniga o‘nlab ariza | Tez va bepul sozlanadi | Statuslar va tarix yo‘q, arizalar lentada yo‘qoladi |
| Google Sheets jadvaliga | Kichik jamoa, oddiy hisobot kerak | Barcha arizalar bir joyda, filtr va hisob | Eslatma va vazifalar yo‘q |
| CRM tizimiga | Doimiy reklama, bir nechta menejer | Har bir ariza vazifaga aylanadi, voronka va hisobotlar | Sozlash va oylik to‘lov |

Ko‘pincha eng yaxshi variant — **aralash**: ariza CRM'ga tushadi va bir vaqtning o‘zida menejerga Telegram'da bildirishnoma keladi. Qaysi CRM'ni tanlash haqida — [CRM nima va kichik biznesga qaysi biri mos](/blog/crm-tanlash/) maqolasida.

Guruhga keladigan xabar qisqa va o‘qishga qulay bo‘lsin:

- Yangi ariza: Oshxona
- Ism: Dilnoza
- Telefon: +998 ...
- Muddat: shu oy
- Manba: instagram_oshxona_oktyabr

Menejer xabarni o‘qishi bilan qo‘ng‘iroq qila oladi — qo‘shimcha savol kerak emas.

## Telegram bot arizalarini qanday qayta ishlash kerak

Bot ariza yig‘adi, lekin pulni menejer olib keladi. Eng ko‘p uchraydigan muammo — ariza botga tushib, soatlab javobsiz qoladi. Shuning uchun qayta ishlash qoidasini oldindan yozib qo‘ying:

1. **Mas'ul.** Har bir smenada arizalarga kim javob berishi aniq bo‘lsin.
2. **Javob vaqti.** Ish vaqtida — bir necha daqiqa. Nega bu muhimligi — [arizaga javob berish tezligi](/blog/arizaga-javob-tezligi/) maqolasida.
3. **Birinchi aloqa.** Qo‘ng‘iroq yoki Telegram'da shaxsiy xabar. Mijoz qaysi usulni xohlashini botda so‘rash mumkin.
4. **Status.** Har bir ariza: «yangi» → «bog‘lanildi» → «uchrashuv/o‘lchov» → «sotuv» yoki «rad etdi (sabab)».
5. **Skript.** Menejer birinchi daqiqada nima deyishini bilsin — tuzilma [sotuv skripti](/blog/sotuv-skripti/) maqolasida.

Menejerlar guruhida oddiy kelishuv ham yordam beradi: arizani olgan menejer xabarga reaksiya qo‘yadi yoki «oldim» deb javob yozadi. Shunda ikki kishi bitta mijozga qo‘ng‘iroq qilmaydi va hech biri javobsiz qolmaydi.

![Reklama manbasini qanday kuzatish](/img/blog/illus/telegram-bot-orqali-arizalar-2.jpg 1200x675)

## Reklama manbasini qanday kuzatish

Botning katta afzalligi — har bir ariza qaysi reklamadan kelganini bilish mumkin. Buning uchun Telegram'ning start parametri bor: bot havolasiga belgi qo‘shasiz, masalan `t.me/sizning_bot?start=insta_oshxona`. Mijoz shu havola orqali kirsa, bot bu belgini ko‘radi va arizaga yozib qo‘yadi.

Har bir kanal va reklama uchun alohida havola tayyorlang:

| Qayerda | Havola belgisi |
|---|---|
| Instagram profil (bio) | `start=insta_bio` |
| Instagram'dagi oshxona reklamasi | `start=insta_oshxona` |
| Telegram kanaldagi post | `start=tg_kanal` |
| Do‘kondagi QR-kod | `start=qr_dokon` |

Oy oxirida arizalarni belgi bo‘yicha guruhlaysiz va qaysi reklama ko‘proq va arzonroq ariza olib kelganini ko‘rasiz. Bu sayt uchun UTM-belgilar bilan bir xil mantiq — batafsil [UTM-belgilar](/blog/utm-belgilar/) maqolasida. Keyin reklama xarajatini arizalar soniga bo‘lib, [lid narxi (CPL)](/blog/lid-narxi-cpl-qanday-kamaytirish/)ni hisoblaysiz.

## SMS reklama qoidalari va bot: nimani bilish kerak

Ko‘p bizneslar mijoz bazasiga SMS orqali aksiya yuboradi. Anhor.uz xabariga ko‘ra, 2026-yil 1-noyabrdan mobil aloqa orqali reklama uchun yangi talablar kuchga kiradi: reklama SMS faqat qabul qiluvchining yozma yoki elektron roziligi bilan yuboriladi, reklama qo‘ng‘iroqlari va xabarlari soat 18:00 dan 09:00 gacha taqiqlanadi ([Anhor](https://anhor.uz/news/v-uzbekistane-zapretyat-reklamnye-zvonki-i-sms-po-vecheram-i-nochyu/)). Aniq tafsilotlarni hujjatning rasmiy matni bo‘yicha yurist bilan tekshiring.

Telegram bot bu muammoni boshqa tomondan hal qiladi: **mijoz botni o‘zi ishga tushiradi**. Lekin bot ham spam qilmasligi kerak:

- **Avval ruxsat so‘rang.** Ariza oxirida: «Aksiya va yangiliklardan xabar olishni xohlaysizmi? Ha / Yo‘q».
- **Kam va foydali yozing.** Har kuni reklama yuborsangiz, mijoz botni bloklaydi.
- **Shaxsiy ma'lumotni ehtiyot qiling.** Ism va telefon — shaxsga doir ma'lumot. Kirishni faqat kerakli xodimlarga bering va bazani begona xizmatlarga bermang.

## Botni kim va qanday yaratadi

Telegram bot yaratish uchun dasturchi bo‘lish shart emas. Bot @BotFather orqali bir necha daqiqada ro‘yxatdan o‘tkaziladi, keyin unga «miya» kerak. Uchta yo‘l bor:

- **Konstruktorlar** — tayyor xizmatlar, kod yozmasdan savollar va tugmalarni sichqoncha bilan yig‘asiz. Oddiy ariza boti uchun yetarli. Oylik to‘lovga e'tibor bering.
- **Freelancer yoki studiya** — sizning jarayoningizga moslab yoziladi, CRM bilan integratsiya qilinadi. Narx funksiyalarga bog‘liq, shuning uchun bir nechta takliflarni solishtiring.
- **CRM ichidagi bot** — ba'zi CRM tizimlarida Telegram integratsiyasi bor: ariza darhol mijoz kartochkasiga aylanadi.

Qaysi yo‘lni tanlasangiz ham, ishga tushirishdan oldin tekshiring:

- Bot o‘zbek va rus tilida ishlaydi.
- Savollar 5–6 tadan oshmaydi.
- Raqam tugma orqali olinadi.
- Ariza 1 daqiqa ichida menejerga yetib keladi.
- Ish vaqtidan tashqari avtojavob bor.
- Har bir reklama uchun alohida start havolasi bor.
- O‘zingiz yoki tanishingiz orqali sinov arizasi qoldirdingiz.

![Ko‘p uchraydigan xatolar](/img/blog/illus/telegram-bot-orqali-arizalar-3.jpg 1200x675)

## Ko‘p uchraydigan xatolar

- **Bot — labirint.** O‘nlab menyu va bo‘limlar. Mijoz ariza qoldirish tugmasini topolmaydi.
- **Jonli odam yo‘q.** Bot savolga javob bera olmasa, «Menejer bilan bog‘lanish» tugmasi bo‘lishi shart.
- **Ariza hech kimga kelmaydi.** Bildirishnoma o‘chirilgan yoki guruhdan menejer chiqib ketgan. Har hafta sinov arizasi qoldiring.
- **Manba belgilanmagan.** Barcha reklamalarda bitta havola — qaysi biri ishlayotganini bilmaysiz.
- **Bot reklama bilan mos emas.** Reklamada «bepul o‘lchov» deb yozilgan, botda esa bu haqda bir so‘z yo‘q. Mijoz adashadi.

## Xulosa

Telegram bot orqali arizalarni yig‘ish — mijozga qulay va biznes uchun tartibli kanal. Kam savol, raqam uchun tugma, darhol bildirishnoma, har bir reklama uchun start havolasi va aniq qayta ishlash qoidasi — shu besh narsa botni haqiqiy sotuv vositasiga aylantiradi. Bot ariza yig‘adi, sotuvni esa tez javob beradigan menejer qiladi.

Level Marketing'da reklama kampaniyasini ishga tushirishda arizalar qayerga tushishi va kim javob berishini ham oldindan kelishib olamiz: reklama, bot va sotuv bo‘limi bitta zanjirdek ishlasa, har bir ariza hisobga olinadi.

## Shu mavzuda yana

- [Arizaga javob berish tezligi sotuvga qanday ta'sir qiladi](/blog/arizaga-javob-tezligi/)
- [CRM nima va kichik biznesga qaysi biri mos](/blog/crm-tanlash/)
- [UTM-belgilar: har bir mijoz qayerdan kelganini qanday bilish](/blog/utm-belgilar/)
