---
title: Lid formani CRM’ga ulash: 4 usul va tekshiruv ro‘yxati
description: Lid formani CRM’ga ulash yo‘llari: tayyor integratsiya, ulagich-servis, webhook va qo‘lda yuklash. Maydonlarni bog‘lash, sinov lidi va uzilishni sezish tartibi.
date: 2026-11-14
slug: lid-formani-crmga-ulash
type: article
tags: CRM, lid forma, sotuv, Meta
key: lid-formani-crmga-ulash
rubric: sotuv
weight: 1
---

Reklama ishlayapti, lidlar kelyapti — lekin ular Meta ichida yotibdi va menejer ularni kuniga bir marta faylga yuklab oladi. Shu orada mijoz boshqa do‘konga qo‘ng‘iroq qilib bo‘lgan. Lid formani CRM’ga ulash bu bo‘shliqni yopadi: ariza qoldirilishi bilan sotuv bo‘limida kartochka ochiladi. Bu maqolada 4 ta ulash usulini solishtiramiz, maydonlarni qanday bog‘lashni, ulanishni qanday sinashni va u uzilganini qanday sezishni ko‘rsatamiz.

![Nega lidlarni qo‘lda yuklash yetarli emas](/img/blog/illus/lid-formani-crmga-ulash-1.jpg 1200x675)

## Nega lidlarni qo‘lda yuklash yetarli emas

Instant forma orqali kelgan ariza avval Meta’da saqlanadi. Uni u yerdan uch xil yo‘l bilan olish mumkin: qo‘lda yuklab olish, Meta Business Suite’dagi Leads Center’da ko‘rish yoki CRM’ga avtomatik uzatish.

Qo‘lda yuklashning uchta kamchiligi bor:

- **Sekinlik.** Ariza kechqurun soat 21:00 da keldi, menejer faylni ertalab ochdi. O‘n ikki soat ichida mijozning qiziqishi sovib ulguradi. Tezlik nimaga ta’sir qilishi haqida — [arizaga javob berish tezligi](/blog/arizaga-javob-tezligi/) maqolasida.
- **Muddat.** Meta lidlarni cheksiz saqlamaydi: yuklab olish uchun ular 90 kun turadi ([Meta Business Help](https://www.facebook.com/business/help/734933888443065)). Faylni vaqtida olmagan bo‘lsangiz, ariza yo‘qoladi.
- **Inson omili.** Fayl bir kishining kompyuterida qoladi, kim qaysi lidga qo‘ng‘iroq qilgani ko‘rinmaydi, bitta ariza ikki marta yoki umuman ishlanmay qoladi.

Meta’ning o‘zi ham ishlab chiquvchilar uchun qo‘llanmasida qo‘lda yuklashni tavsiya etilmaydigan, faqat boshqa usul ishlamay qolganda vaqtincha ishlatiladigan yo‘l deb ataydi ([Meta for Developers](https://developers.facebook.com/docs/marketing-api/conversions-api/conversion-leads-integration/crm-integration/1-connecting-your-crm-with-lead-ads)).

## Lid formani CRM’ga ulash: 4 ta usul

| Usul | Qanday ishlaydi | Kimga mos | Zaif tomoni |
|---|---|---|---|
| CRM’ning tayyor integratsiyasi | CRM ichida «Facebook/Instagram lidlari» bo‘limi ochiladi, sahifa va forma tanlanadi | CRM’i Meta bilan to‘g‘ridan-to‘g‘ri ishlaydigan biznes | Hamma CRM’da yo‘q; sozlamalar cheklangan bo‘lishi mumkin |
| Ulagich-servis (Zapier, Make va shunga o‘xshashlar) | Servis Meta’dan lidni oladi va CRM, jadval yoki Telegram’ga uzatadi | Tayyor integratsiyasi yo‘q CRM, bir nechta joyga uzatish kerak bo‘lsa | Oylik to‘lov; servisdagi limit yoki to‘lov tugasa, lidlar to‘xtaydi |
| O‘z integratsiyangiz (webhook) | Dasturchi Meta’dan xabar oladigan manzil yozadi va CRM’ga yozib qo‘yadi | O‘z CRM’i yoki nostandart jarayoni bor kompaniya | Dasturchi va texnik qo‘llab-quvvatlash kerak |
| Qo‘lda yuklash | Menejer Leads Center’dan faylni oladi | Faqat zaxira yo‘l sifatida | Sekin, 90 kunlik muddat, xato ko‘p |

Qaysi birini tanlash kerak? Oddiy qoida: avval CRM’ingizda tayyor integratsiya bor-yo‘qligini tekshiring — bu eng kam bo‘g‘inli yo‘l. Yo‘q bo‘lsa — ulagich-servis. Webhook faqat dasturchingiz doimiy bo‘lsa. CRM’ning o‘zini hali tanlamagan bo‘lsangiz, tanlashda «Meta lid formalari bilan integratsiya bormi» degan savolni ro‘yxatga qo‘shing — batafsil [CRM tanlash](/blog/crm-tanlash/) maqolasida.

Tezlik haqida: Meta’ning yozishicha, webhook orqali lidlar «deyarli real vaqtda» keladi, lekin xabar bir necha daqiqagacha kechikishi mumkin. Ya’ni avtomatik ulanish ham soniyama-soniya emas, lekin qo‘lda yuklash bilan solishtirib bo‘lmaydi.

## Ulashdan oldin: 5 ta narsa tayyor bo‘lsin

1. **Sahifaga to‘liq kirish huquqi.** Integratsiyani Facebook sahifasi va biznes-portfel ustidan to‘liq nazorati bor odam ulaydi. Agar sahifa agentlik yoki sobiq xodim nomida bo‘lsa, avval shuni tartibga soling — [agentlikka kabinetga kirish](/blog/agentlikka-kabinetga-kirish/) maqolasida aktivlar kimda turishi kerakligi yozilgan.
2. **Lidlarga kirish sozlamasi.** Meta’da lidlarni kim va qaysi CRM olishi mumkinligini boshqaradigan alohida sozlama bor (Leads Access). Meta hujjatiga ko‘ra, u o‘zgartirilmagan bo‘lsa, lidlarga sahifaning barcha adminlari kira oladi. Kimdir uni qo‘lda cheklagan bo‘lsa, CRM’ga ham ruxsat berish kerak bo‘ladi.
3. **CRM’da voronka va mas’ul.** Lid qaysi bosqichga tushadi, kimga biriktiriladi, bildirishnoma qayerga boradi — buni ulashdan oldin hal qiling. Aks holda arizalar «hech kimniki» bo‘lib yig‘ilib qoladi.
4. **Maydonlar ro‘yxati.** Formada qanday savollar bor va CRM’da ularga qaysi maydon mos keladi (pastdagi jadval).
5. **Rozilik matni.** Formadagi maxfiylik siyosati havolasi va ma’lumot qayerda saqlanishi. Mijoz ma’lumotlari CRM’ga o‘tgach, ular uchun siz javob berasiz — [mijozlar bazasi va shaxsga doir ma’lumotlar](/blog/mijozlar-bazasi-shaxsiy-malumotlar/) maqolasiga qarang.

## Maydonlarni bog‘lash: nima qayerga tushadi

Ulanishning eng ko‘p xato qilinadigan joyi — maydonlar. Lid CRM’ga keladi, lekin telefon raqami izoh ichida, ism esa bo‘sh.

| Meta’dan keladigan ma’lumot | CRM’dagi maydon | Nega kerak |
|---|---|---|
| Ism | Kontakt ismi | Menejer mijozga ismi bilan murojaat qiladi |
| Telefon | Telefon (xalqaro formatda, +998…) | Dubllarni topish va qo‘ng‘iroq uchun |
| Formadagi savollarga javoblar | Alohida maydonlar yoki izoh | Menejer qayta so‘ramaydi |
| Forma nomi | Manba yoki teg | Qaysi taklifdan kelgani ko‘rinadi |
| Kampaniya va e’lon nomi | UTM yoki manba maydonlari | Qaysi reklama sotuv bergani hisoblanadi |
| Lid ID (Meta bergan raqam) | Alohida maydon | Kabinet bilan solishtirish va sifatli lidlarni Meta’ga qaytarish uchun |
| Yaratilgan vaqt | Ariza vaqti | Javob tezligini o‘lchash uchun |

Lid ID haqida alohida. Meta qo‘llanmasida CRM’ga tushadigan ma’lumot ichida 15–17 xonali Lid ID bo‘lishi kerakligi yozilgan. Bu raqam hozir keraksiz ko‘rinsa ham, uni saqlang: keyinchalik [kabinetdagi lidlar va CRM mos kelmasa](/blog/kabinet-va-crm-lidlar/), aynan shu raqam orqali qaysi ariza yo‘qolganini topasiz.

Yana ikki amaliy maslahat:

- Telefonni bitta formatga keltiring. «90 123 45 67» va «+998901234567» CRM uchun ikki xil odam bo‘lib qolmasin.
- Formaga yangi savol qo‘shsangiz, ulanishni ham yangilang. Yangi maydon o‘z-o‘zidan CRM’ga tushmaydi.

![Sinov: ulanish ishlayotganini qanday tekshirish](/img/blog/illus/lid-formani-crmga-ulash-2.jpg 1200x675)

## Sinov: ulanish ishlayotganini qanday tekshirish

Reklamani yoqishdan oldin bitta sinov lidi yuboring.

1. **Sinov lidini yarating.** Meta’ning ishlab chiquvchilar saytida Lead Ads Testing Tool bor: sahifa va formani tanlaysiz, sinov lidi yaratiladi. Bu vosita shartli ma’lumot yuboradi; CRM’ingiz maydonlarni qattiq tekshirsa, uni rad etishi mumkin. Unda formani o‘zingiz haqiqiy ma’lumot bilan to‘ldiring.
2. **CRM’ni oching.** Kartochka paydo bo‘ldimi? Necha daqiqada?
3. **Maydonlarni ko‘ring.** Ism, telefon, javoblar, forma nomi, Lid ID — har biri o‘z joyidami?
4. **Bildirishnomani tekshiring.** Mas’ul menejerga xabar bordimi (CRM, Telegram yoki telefon)?
5. **Sinov kartochkasini o‘chiring**, hisobot buzilmasin.

Vosita interfeysi va nomlari o‘zgarib turadi, shuning uchun aniq tugmalarni emas, mantiqni eslab qoling: sinov lidi → CRM → maydonlar → bildirishnoma.

## Uzilishni qanday sezish

Ulanish bir marta sozlab qo‘yiladigan narsa emas. U jimgina uziladi — xato xabari chiqmaydi, shunchaki lidlar kelmay qoladi.

| Sabab | Qanday ko‘rinadi | Nima qilish kerak |
|---|---|---|
| Ulagan odam parolini o‘zgartirdi yoki sahifadan chiqarildi | Lidlar bir kunda to‘xtaydi | Ulanishni sahifa egasi nomidan qayta ulash |
| Yangi forma yaratildi, lekin integratsiyaga qo‘shilmadi | Eski formadan keladi, yangisidan yo‘q | Har yangi formadan keyin sinov lidi |
| Lidlarga kirish sozlamasi o‘zgartirildi | CRM’ga ruxsat yo‘q degan xato | Leads Access’da CRM’ni qayta qo‘shish |
| Ulagich-servisda limit yoki to‘lov tugadi | Oy oxirida lidlar to‘xtaydi | Tarif va to‘lov sanasini kalendarga yozish |
| Formaga yangi savol qo‘shildi | Lid keladi, lekin maydon bo‘sh | Maydonlarni qayta bog‘lash |

Uzilishni tez sezish uchun uchta oddiy odat:

- **Kunlik solishtirish.** Ertalab ikki raqamni yonma-yon qo‘ying: kabinetdagi kechagi lidlar soni va CRM’dagi yangi kartochkalar soni. Besh daqiqa.
- **«Jimlik» signali.** Odatda kuniga 10 ta ariza kelsa-yu, tushgacha birorta ham bo‘lmasa — bu reklama emas, ulanish muammosi bo‘lishi mumkin. Avval Leads Center’ni oching.
- **Zaxira yo‘l.** Uzilish topilsa, lidlarni Leads Center’dan qo‘lda yuklab oling va CRM’ga kiriting. 90 kun ichida ular yo‘qolmaydi, lekin har bir soat sotuvga ta’sir qiladi.

## Shartli misol: mebel do‘koni

Toshkentdagi mebel do‘koni oshxona mebeli uchun lid forma bilan reklama beradi (bu shartli misol, raqamlar tushuntirish uchun).

**Oldin.** Menejer lidlarni kuniga bir marta, ertalab faylga yuklaydi. Shanba kechqurun va yakshanba kuni kelgan 14 ta ariza dushanba kuni soat 10:00 da ochiladi. Ularning bir qismi telefonni ko‘tarmaydi, bir qismi «allaqachon buyurtma berdik» deydi.

**Keyin.** Forma CRM’ga ulandi: ariza kelishi bilan kartochka ochiladi, navbatchi menejerga Telegram’da xabar boradi. Formadagi «oshxona o‘lchami» va «qachon kerak» javoblari alohida maydonlarga tushadi, menejer qo‘ng‘iroqni shu ma’lumot bilan boshlaydi. Har ertalab rahbar kabinet va CRM raqamlarini solishtiradi.

O‘zgargan narsa reklama emas — arizadan birinchi qo‘ng‘iroqqacha bo‘lgan vaqt.

![5 ta ko‘p uchraydigan xato](/img/blog/illus/lid-formani-crmga-ulash-3.jpg 1200x675)

## 5 ta ko‘p uchraydigan xato

- **Ulanishni xodimning shaxsiy akkaunti orqali ulash.** U ishdan ketsa yoki parolini o‘zgartirsa, lidlar to‘xtaydi.
- **Sinovsiz ishga tushirish.** «Ulandi» degan yozuv lid to‘g‘ri maydonga tushishini kafolatlamaydi.
- **Lid ID va forma nomini saqlamaslik.** Keyin qaysi reklama sotuv berganini aniqlab bo‘lmaydi.
- **Bildirishnomasiz ulash.** Lid CRM’da turibdi, lekin hech kim bilmaydi — bu qo‘lda yuklashdan farq qilmaydi.
- **Bir marta sozlab, unutish.** Kunlik solishtirish bo‘lmasa, uzilish bir hafta sezilmasligi mumkin.

## Savol-javob

### CRM’im yo‘q. Lidlarni Google Sheets yoki Telegram’ga uzatsa bo‘ladimi?

Ha, ulagich-servislar buni qila oladi. Boshlanish uchun bu qo‘lda yuklashdan yaxshi: ariza darhol ko‘rinadi. Lekin jadvalda kim qo‘ng‘iroq qilgani va natijasi yaxshi yuritilmaydi, shuning uchun arizalar ko‘paygach CRM’ga o‘tgan ma’qul.

### Ulanishdan oldin kelgan eski lidlar CRM’ga tushadimi?

Odatda yo‘q — integratsiya ulangan paytdan keyingi lidlarni uzatadi. Eskilarini Leads Center’dan yuklab olib, CRM’ga import qiling. 90 kunlik muddatni unutmang.

### Agentlik ulab bersa, nimani so‘rash kerak?

Uch narsani: ulanish kimning akkaunti orqali qilingan (sizning sahifangiz egasi nomidan bo‘lishi kerak), ulagich-servis akkaunti kimniki va to‘lovi kimda, maydonlar jadvali yozma ko‘rinishda bormi.

### CRM’dan Meta’ga ma’lumot qaytarish ham kerakmi?

Bu keyingi bosqich. Avval lidlar barqaror tushsin va menejerlar statuslarni to‘g‘ri yuritsin. Keyin sifatli lid hodisalarini Meta’ga qaytarish mumkin — buning uchun aynan Lid ID kerak bo‘ladi. Asoslari [Meta Pixel va Conversions API](/blog/meta-pixel-conversions-api/) maqolasida.

## Xulosa

Lid formani CRM’ga ulash — bir soatlik texnik ish, lekin u arizadan birinchi qo‘ng‘iroqqacha bo‘lgan vaqtni soatlardan daqiqalarga tushiradi. Usulni tanlang (tayyor integratsiya, ulagich yoki webhook), maydonlarni jadval bo‘yicha bog‘lang, sinov lidi yuboring va har ertalab ikki raqamni solishtiring. Level Marketing’da biz reklamani yoqishdan oldin sinov lidi mijozning sotuv bo‘limigacha yetib borganini tekshiramiz — shunda birinchi kunning arizalari yo‘lda qolmaydi.

## Shu mavzuda yana

- [Kabinetdagi lidlar va CRM mos kelmasa: 7 sabab va tekshiruv](/blog/kabinet-va-crm-lidlar/)
- [CRM nima va kichik biznesga qaysi biri mos](/blog/crm-tanlash/)
- [Arizaga javob berish tezligi sotuvga qanday ta'sir qiladi](/blog/arizaga-javob-tezligi/)
