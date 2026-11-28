---
title: Suv yetkazib berish marketingi: obuna, bot va takroriy buyurtma
description: Ichimlik suvi yetkazib berish biznesi marketingi: birinchi buyurtma taklifi, Telegram bot orqali qayta buyurtma, ofislar bilan shartnoma va mijozni ushlab qolish.
date: 2026-11-28
slug: suv-yetkazib-berish-marketing
type: article
tags: suv yetkazib berish, takroriy sotuv, Telegram bot, B2B
key: suv-yetkazib-berish-marketing
rubric: biznes
---

Suv yetkazib berish — odat biznesi. Oila yoki ofis bir marta yetkazib beruvchini tanlaydi va keyin oylab, hatto yillab o‘ylamasdan o‘sha raqamga qo‘ng‘iroq qiladi. Demak, marketingning vazifasi ikki qismdan iborat: birinchi buyurtmani olish va qayta buyurtmani shunchalik oson qilishki, mijozning boshqa joyga qarashga sababi qolmasin. Bu maqolada 19 litrli idishdagi suv yetkazib beruvchi uchun ana shu ikki qismni raqamlar bilan ko‘rib chiqamiz.

## Nega bu biznesda reklama emas, ushlab qolish pul topadi

Bitta idish suvdan qoladigan foyda kichik. Reklama orqali kelgan mijoz birinchi buyurtmada deyarli hech qachon o‘zini oqlamaydi — u 3–4-oyda, ba’zan undan ham kechroq foyda bera boshlaydi. Shuning uchun bu sohadagi asosiy savol «arizani qanchaga oldik?» emas, balki «mijoz necha oy qoladi?».

Quyidagi hisob shartli misol, raqamlar o‘ylab topilgan, lekin mantiq har qanday shaharda bir xil:

| Ko‘rsatkich | Shartli qiymat |
|---|---|
| Bitta idish narxi (mijoz uchun) | 18 000 so‘m |
| Suv, idish yuvish, yetkazish xarajati | 11 000 so‘m |
| Bitta idishdan yalpi foyda | 7 000 so‘m |
| Oila bir oyda oladigan idishlar | 3 ta |
| Oilaning oylik yalpi foydasi | 21 000 so‘m |
| Reklamadagi bitta ariza narxi | 25 000 so‘m |
| Arizadan birinchi buyurtmaga o‘tish | 40% |
| Bitta yangi mijozni jalb qilish narxi | 62 500 so‘m |

Bu misolda yangi mijoz faqat uchinchi oyning oxirida o‘zini oqlaydi. Agar mijozlarning yarmi birinchi oydan keyin ketib qolsa, reklama zarar keltiradi. Agar mijoz 12 oy qolsa, undan 252 000 so‘m yalpi foyda olinadi — jalb qilish narxidan to‘rt barobar ko‘p. Xulosa: reklama byudjetini oshirishdan oldin ushlab qolishni tuzating. Hisob-kitob uslubi batafsil [takroriy sotuv va LTV](/blog/takroriy-sotuv-ltv/) maqolasida, mijozlar ketishini o‘lchash esa [churn](/blog/mijozlar-ketishi-churn/) maqolasida.

## Birinchi buyurtma taklifi: kimni chaqirasiz?

Eng keng tarqalgan xato — «birinchi idish bepul» deb reklama berish. Bunday taklifga bepul narsa izlaydiganlar ko‘p keladi: bir marta oladi va yo‘qoladi. Yaxshi kirish taklifi mijozni ikkinchi va uchinchi buyurtmaga olib kirishi kerak.

Ishlaydigan variantlar:

- **Idish garovisiz boshlash.** Ko‘pchilikni to‘xtatadigan narsa suv narxi emas, idish uchun garov summasi. Garovni birinchi buyurtmada olmang yoki uni 3 oyga bo‘lib qo‘ying — shart: kamida 2 ta idish.
- **Pompa yoki dispenser obuna bilan.** Oyiga kamida N ta idish olgan mijozga pompa bepul, ofisga esa dispenser ijaraga. Uyingizda turgan sizning jihozingiz — eng kuchli ushlab qolish vositasi.
- **Birinchi oy paketi.** «4 ta idish + pompa» belgilangan narxda. Mijoz bir oy davomida sizning xizmatingizga o‘rganadi.

Qoida: taklif qancha arzon bo‘lmasin, u kamida bir oylik iste’molni qamrab olishi kerak. Bitta bepul idish odat yaratmaydi. Kirish taklifini qanday qurish — [kirish taklifi](/blog/kirish-taklifi/) maqolasida.

## Qayta buyurtma: Telegram bot bir tugma bo‘lsin

Mijoz raqobatchiga qaysi daqiqada o‘tadi? Suv tugagan va sizga qo‘ng‘iroq qilganda hech kim javob bermagan daqiqada. Shuning uchun qayta buyurtma kanali telefondan tezroq bo‘lishi kerak.

Telegram bot uchun minimal ssenariy:

1. Birinchi kirishda bot telefon raqamini tugma orqali so‘raydi. Telegram Bot API’da bunday tugma bor: u raqamni kontakt sifatida yuboradi va faqat shaxsiy chatda ishlaydi ([Bot API, KeyboardButton](https://core.telegram.org/bots/api#keyboardbutton)).
2. Manzil, qavat, domofon kodi bir marta saqlanadi.
3. Keyingi safar mijoz faqat «Yana 2 ta idish» tugmasini bosadi va yetkazish vaqtini tanlaydi.
4. Bot buyurtmani tasdiqlaydi va kuryer yo‘lga chiqqanda xabar beradi.
5. Bo‘sh idishlar soni so‘raladi — kuryer nechta olib ketishini oldindan biladi.

Botni noldan yaratish — [Telegram bot yaratish](/blog/telegram-bot-yaratish/) maqolasida.

### Eslatma — reklamadan arzon sotuv

Har bir mijozning iste’mol oralig‘i bor: bir oila 10 kunda bir idish oladi, boshqasi 5 kunda. CRM yoki botda oxirgi ikki buyurtma orasidagi kunlarni hisoblang va suv tugashidan bir kun oldin shaxsiy eslatma yuboring: «Odatda shu kunlarda buyurtma berasiz. Ertaga ertalab olib kelaylikmi?» va ikkita tugma — «Ha» va «Keyinroq».

Bu umumiy rassilka emas, har bir mijozga o‘z vaqtida keladigan xabar. Shuning uchun u bloklanmaydi. Ommaviy xabarlarda Telegram texnik chegaralari ham bor: bot bepul rejimda taxminan sekundiga 30 tadan ortiq xabar tarqata olmaydi ([Telegram Bots FAQ](https://core.telegram.org/bots/faq)). Rassilka odobi haqida — [Telegram botda rassilka](/blog/telegram-bot-rassilka-qoidalari/).

## Obuna modellari: qaysi biri kimga mos

| Model | Kimga | Afzallik | Xavf |
|---|---|---|---|
| Chaqiruv bo‘yicha | Kam iste’mol qiladigan oilalar | Mijoz uchun oddiy | Raqobatchiga o‘tish oson |
| Belgilangan jadval (masalan, har seshanba) | Ofislar, katta oilalar | Kuryer marshruti oldindan ma’lum | Suv yig‘ilib qolsa mijoz bekor qiladi |
| Oldindan to‘langan paket (10–20 idish) | Doimiy mijozlar | Pul oldindan keladi, mijoz bog‘lanadi | Chegirma marjani yeydi |
| Ofis bilan shartnoma | Kompaniyalar | Katta va barqaror hajm | Hujjat va to‘lov muddati |

Amaliy qoida: oddiy mijozga chaqiruv bo‘yicha va bot bilan boshlang, uchinchi buyurtmadan keyin paket yoki jadval taklif qiling. Mijoz sizni sinab ko‘rmasdan obunaga rozi bo‘lmaydi.

## Ofislar: alohida kanal, alohida taklif

Ofis — bu oyiga o‘nlab idish va yillab davom etadigan mijoz. Lekin qarorni boshqa odam qabul qiladi: ofis-menejer yoki ma’mur. Uning muammolari oilanikidan farq qiladi:

- shartnoma va hisob-faktura, pul o‘tkazish orqali to‘lov;
- har hafta bir xil kunda yetkazish, uni eslatib turish shart emas;
- dispenser va uning vaqti-vaqti bilan tozalanishi;
- bitta mas’ul raqam — «qo‘ng‘iroq markaziga» emas, aniq menejerga.

Ofisni Instagram reklamasi emas, to‘g‘ridan-to‘g‘ri murojaat olib keladi: biznes markazlar ro‘yxati, ma’murlarga qo‘ng‘iroq, sinov uchun bir hafta bepul dispenser. Bir binoda bitta ofis bilan ishlasangiz, qo‘shni ofislarga ham taklif qiling — kuryer baribir o‘sha yerga keladi. B2B yondashuv haqida — [B2B marketing](/blog/b2b-marketing/).

## Geografiya: zichlik foydani belgilaydi

Yetkazish xarajati masofaga emas, marshrut zichligiga bog‘liq. Bitta ko‘chada 20 ta mijoz bo‘lsa, kuryer bir soatda ularning hammasiga yetadi. Shahar bo‘ylab tarqalgan 20 ta mijozga esa butun kun ketadi.

Shuning uchun:

- reklamani avval marshrutlaringiz bor tumanlarga qarating, radius bo‘yicha;
- yangi tumanni ochishdan oldin u yerda kamida bitta kunlik marshrutni to‘ldiradigan mijozlar to‘plang;
- Google va Yandex Xaritalarda kartochka oching — «suv yetkazib berish» deb qidirgan odam yaqin xizmatni tanlaydi. Qanday qo‘shish — [biznesni Xaritalarga qo‘shish](/blog/biznesni-xaritalarga-qoshish/).

## Sifatga ishonch: nimani ko‘rsatish kerak

Mijoz suvni ichishdan oldin uning qayerdan kelganini bilmaydi. Ishonchni aniq dalillar bilan quring:

- suv qayerdan olinadi va qanday tozalanadi — sexdan qisqa video;
- idishlar qanday yuviladi va tekshiriladi;
- laboratoriya tahlili natijalari — faqat haqiqiy hujjatlar, sanasi bilan;
- kuryer formasi, toza mashina, idishni ko‘tarib berish.

Reklamada «eng toza suv» kabi isbotsiz da’volardan qoching: solishtirma va mutlaq da’volar uchun dalil kerak bo‘ladi.

## Ushlab qolishni o‘lchash: 5 ta raqam

| Raqam | Qanday hisoblanadi | Nima uchun kerak |
|---|---|---|
| Faol mijozlar | Oxirgi 30 kunda buyurtma berganlar | Bazaning haqiqiy hajmi |
| Ikkinchi buyurtma ulushi | Birinchi oy ichida qayta buyurtma berganlar / yangilar | Kirish taklifi sifatini ko‘rsatadi |
| Oylik ketish | O‘z oralig‘ining ikki barobaridan ko‘p buyurtma bermaganlar | Erta ogohlantirish |
| Aylanadagi idishlar | Mijozlardagi idishlar soni | Garov va zaxira hisobi |
| Bot orqali buyurtmalar ulushi | Botdagi buyurtmalar / hammasi | Operator yuki va tezlik |

Mijoz odatiy oralig‘idan ikki barobar ko‘p vaqt buyurtma bermasa, unga bot emas, operator qo‘ng‘iroq qilsin va sababini so‘rasin: narxmi, kechikishmi, ko‘chib ketdimi. Ketgan mijozni qaytarish yangi mijozni topishdan deyarli har doim arzon.

## Ko‘p uchraydigan xatolar

- Bir martalik bepul taklif va undan keyin hech qanday tizim yo‘q.
- Mijoz manzili va iste’moli faqat kuryerning xotirasida.
- «2 soatda yetkazamiz» deb va’da berib, ertasi kuni olib borish.
- Hamma tumanlarga birdaniga reklama — kuryerlar shaharni aylanib chiqadi.
- Ofislarga ham oilalarga mo‘ljallangan taklifni yuborish.

## Savol-javob

### Suv yetkazib berish uchun Instagram kerakmi?

Kerak, lekin asosiy sotuv kanali sifatida emas. Instagram ishonch uchun: sex, tozalash, kuryerlar. Arizalar esa xaritalar, qidiruv, tuman bo‘yicha target reklama va tavsiyalardan keladi.

### Chegirmali paket marjani yo‘q qilmaydimi?

Paketdagi chegirma oldindan olingan pul va mijozning bir necha oy qolishi evaziga beriladi. Paket chegirmasini bitta idish foydasining yarmidan oshirmang va uni faqat uchinchi buyurtmadan keyin taklif qiling.

### Mijoz raqobatchi arzonroq dedi. Narxni tushirish kerakmi?

Avval nima uchun ketayotganini aniqlang. Ko‘pincha sabab narx emas, kechikish yoki javob bermaslik. Agar sabab haqiqatan narx bo‘lsa, narx o‘rniga paket yoki pompa taklif qiling.

### Tavsiya dasturi ishlaydimi?

Ha, chunki qo‘shnilar va hamkasblar bir-biridan so‘raydi. Oddiy mexanika: tavsiya qilgan mijoz va yangi mijozga bittadan bepul idish, lekin yangi mijozning ikkinchi buyurtmasidan keyin.

## Xulosa

Suv yetkazib berishda g‘olib — eng ko‘p reklama qilgan emas, mijozni eng uzoq ushlab qolgan kompaniya. Kirish taklifi bir oylik odatni shakllantirsin, bot qayta buyurtmani bir tugmaga aylantirsin, eslatma suv tugashidan oldin kelsin, ofislar esa alohida shartnoma va menejer olsin. Level Marketing bepul auditda reklamangiz, voronkangiz va qayta buyurtmalar tizimingizni ko‘rib chiqadi va qayerda pul yo‘qolayotganini ko‘rsatadi.

## Shu mavzuda yana

- [Sodiqlik dasturi: mijozni qaytaradigan bonus va keshbek tizimi](/blog/sodiqlik-dasturi/)
- [Unit-ekonomika: reklamaga qancha to‘lash mumkinligini qanday bilish](/blog/unit-ekonomika/)
- [Arizaga javob berish tezligi sotuvga qanday ta'sir qiladi](/blog/arizaga-javob-tezligi/)
