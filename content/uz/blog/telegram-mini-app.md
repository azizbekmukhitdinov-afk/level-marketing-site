---
title: Telegram Mini App biznes uchun: katalog, bron va to‘lov
description: Telegram Mini App nima, katalog, bron va sodiqlik uchun qanday ishlatiladi, Telegram Stars va jismoniy tovar to‘lovi qoidalari, narxni baholash va oddiy bot qachon yetarli.
date: 2026-11-28
slug: telegram-mini-app
type: article
tags: Telegram Mini App, Telegram bot, Telegram Stars, onlayn savdo
key: telegram-mini-app
rubric: smm
---

Telegram’da mijozlar allaqachon yozishadi, kanalni o‘qishadi va buyurtma berishadi. Lekin oddiy botda tugmalar va xabarlar bilan katalogni ko‘rish yoki vaqt tanlash noqulay. Telegram Mini App bu muammoni hal qiladi: Telegram ichida to‘liq sayt kabi interfeys ochiladi. Bu maqolada Mini App nima ekanini, biznesda qayerda foyda berishini, to‘lov qoidalarini va oddiy bot qachon yetarli ekanini ko‘rib chiqamiz.

## Telegram Mini App nima

Mini App — bu Telegram ichida ochiladigan veb-ilova. Telegram’ning [rasmiy hujjatiga](https://core.telegram.org/bots/webapps) ko‘ra, u JavaScript’da yoziladi, botga bog‘lanadi va istalgan saytning o‘rnini bosa oladigan moslashuvchan interfeys beradi. Foydalanuvchi uchun bu oddiy: botga kiradi, tugmani bosadi va katalog, bron sahifasi yoki shaxsiy kabinet ochiladi — brauzerga chiqmasdan.

Mini App’ni bir necha joydan ochish mumkin:

- bot profilidagi asosiy ilova tugmasi yoki `t.me/botnomi?startapp` havolasi;
- chatdagi menyu tugmasi;
- xabar ostidagi inline tugma yoki klaviatura tugmasi;
- `t.me/botnomi/ilovanomi` ko‘rinishidagi to‘g‘ridan-to‘g‘ri havola.

Hujjatga ko‘ra, Mini App foydalanuvchining Telegram mavzusini (kunduzgi yoki tungi rang) oladi, ism va til kabi asosiy ma’lumotni avtomatik biladi, to‘liq ekranda ochila oladi va telefon bosh ekraniga yorliq sifatida qo‘shilishi mumkin. Ruxsat bilan geolokatsiya va QR-kod skaneri ham ishlaydi. Biznes uchun asosiy foyda: mijoz ro‘yxatdan o‘tmaydi va parol kiritmaydi — Telegram uni allaqachon taniydi.

Mini App bot ustiga quriladi, shuning uchun avval bot kerak bo‘ladi. Botni noldan qanday ochish — [Telegram bot yaratish](/blog/telegram-bot-yaratish/) maqolasida.

## Bot, Mini App yoki sayt: farqi

| Mezon | Oddiy bot | Mini App | Sayt |
|---|---|---|---|
| Interfeys | Xabarlar va tugmalar | Sahifalar, rasmlar, filtrlar, savatcha | Istalgan |
| Ro‘yxatdan o‘tish | Kerak emas | Kerak emas, Telegram taniydi | Odatda kerak yoki forma |
| Qayta aloqa | Bot xabar yubora oladi | Bot orqali xabar yuboriladi | Email, SMS yoki reklama |
| Google’dan trafik | Yo‘q | Yo‘q | Bor (SEO) |
| Ishlab chiqish hajmi | Kichik | O‘rtacha | O‘rtacha yoki katta |
| Eng mos vazifa | Ariza, savol-javob, eslatma | Katalog, bron, shaxsiy kabinet | Qidiruvdan mijoz, ishonch |

Muhim nuqta: Mini App saytning o‘rnini to‘liq bosmaydi. Odamlar Google’da qidirganda Mini App chiqmaydi. U Telegram’da allaqachon bor auditoriya — kanal obunachilari, bot foydalanuvchilari, Telegram’dagi reklama orqali kelganlar uchun eng yaxshi ishlaydi.

## Biznes uchun to‘rtta foydalanish holati

**1. Katalog va buyurtma.** Do‘kon, kafe, gul yetkazib berish, qurilish materiallari: filtrlar, rasmlar, savatcha va manzil. Mijoz «narxi qancha?» deb yozish o‘rniga o‘zi tanlaydi, menejer esa tayyor buyurtmani oladi. Onlayn do‘kon uchun umumiy marketing — [onlayn do‘kon marketingi](/blog/onlayn-dokon-marketing/) maqolasida.

**2. Bron va yozilish.** Go‘zallik saloni, klinika, avto-servis, o‘quv markazi: xizmat, mutaxassis va bo‘sh vaqtni tanlash. Bot esa avtomatik eslatma yuboradi. Bu yerda Mini App eng tez o‘zini oqlaydi, chunki chatda vaqt kelishish ko‘p xabar talab qiladi.

**3. Sodiqlik kartasi.** Plastik karta o‘rniga Telegram ichidagi bonus balansi va QR-kod. Kassir kodni skanerlaydi, bot esa «sizda 35 000 so‘m bonus bor» deb eslatadi. Bonus mexanikasini qanday tuzish — [sodiqlik dasturi](/blog/sodiqlik-dasturi/) maqolasida.

**4. Kalkulyator, test yoki tanlov yordamchisi.** Ta’mir narxi kalkulyatori, «qaysi kurs sizga mos» testi, kredit to‘lovi hisoblagichi. Natija oxirida mijoz kontakt qoldiradi — bu sifatli ariza, chunki odam allaqachon o‘z vazifasini aniqlagan. Arizalarni bot orqali yig‘ish bo‘yicha — [Telegram bot orqali arizalar](/blog/telegram-bot-orqali-arizalar/).

## To‘lovlar: raqamli va jismoniy tovar qoidalari

Bu qism eng ko‘p xato qilinadigan joy. Telegram raqamli va jismoniy tovarlarni alohida ko‘radi.

| Nima sotasiz | Qanday to‘lov | Manba |
|---|---|---|
| Raqamli tovar va xizmat (onlayn kurs, obuna, elektron kitob, ilova ichidagi imkoniyat) | Faqat Telegram Stars | [Telegram Stars qoidalari](https://core.telegram.org/bots/payments-stars) |
| Jismoniy tovar va oflayn xizmat (kiyim, ovqat, salon xizmati) | Turli valyuta va to‘lov provayderlari | [Bot Payments qoidalari](https://core.telegram.org/bots/payments) |

Telegram’ning [Stars sahifasida](https://core.telegram.org/bots/payments-stars) aniq yozilgan: raqamli tovar va xizmatlar uchun to‘lovlar faqat Telegram Stars’da bo‘lishi kerak. Sabab — App Store va Google Play qoidalari. Agar bu qoida buzilsa, Telegram botni yoki Mini App’ni mobil foydalanuvchilarga ko‘rsatmasligi mumkin. Demak, onlayn kurs sotadigan biznes Mini App ichida karta orqali to‘lov qabul qilishni rejalashtirmasligi kerak.

Jismoniy tovar va xizmatlar uchun boshqa valyuta va provayderlardan foydalanish mumkin. Provayder BotFather’dagi to‘lov sozlamalari orqali ulanadi; [Bot Payments hujjatidagi](https://core.telegram.org/bots/payments) valyutalar jadvalida O‘zbekiston so‘mi (UZS) bor. Qaysi mahalliy provayderlar ulanishi mumkinligini BotFather’dagi joriy ro‘yxatdan tekshiring va tanlangan provayderning o‘z qoidalariga rioya qiling. Ko‘p biznes uchun oddiyroq variant ham bor: buyurtmani Mini App’da qabul qilish, to‘lovni esa yetkazib berishda yoki o‘z to‘lov tizimingiz orqali olish — buni oldindan dasturchi va to‘lov tizimi bilan kelishing.

## Narxni qanday baholash

Mini App narxi uning hajmiga bog‘liq. Bozor narxlarini taxmin qilish o‘rniga, ishni soatlarda baholash foydaliroq. Quyidagi raqamlar shartli misol, aniq taklif emas:

| Variant | Taxminiy ish hajmi (shartli) | Nimalar kiradi |
|---|---|---|
| Oddiy bot | 20–40 soat | Ariza, savol-javob, menejerga xabar |
| Katalog yoki bron Mini App | 80–200 soat | Dizayn, sahifalar, admin panel, bot bilan bog‘lash |
| + to‘lov va CRM integratsiyasi | +40–80 soat | Provayder, buyurtmani CRM’ga yozish, holat xabarlari |
| Qo‘llab-quvvatlash | Oyiga 5–15 soat | Xatolar, narx va katalog yangilanishi |

Yakuniy narx = soatlar × dasturchi yoki jamoaning soatlik stavkasi. Qo‘llab-quvvatlashni unutmang: katalog va narxlar o‘zgaradi, Telegram yangi funksiyalar qo‘shadi.

## Shartli misol: salon uchun bron Mini App

Quyidagi raqamlar shartli misol. Salonga Telegram orqali oyiga 400 kishi yoziladi.

**Hozir (chatda):** 400 ta suhbatdan 25% bron bilan tugaydi — 100 ta bron. Administrator har bir suhbatga o‘rtacha 4 daqiqa sarflaydi: 400 × 4 = 1 600 daqiqa, taxminan 27 soat.

**Mini App bilan:** 400 kishidan 30% o‘zi bron qiladi — 120 ta bron. Administrator faqat savollari bor 100 kishi bilan gaplashadi: 100 × 4 = 400 daqiqa, taxminan 7 soat.

O‘rtacha chek 250 000 so‘m bo‘lsa, qo‘shimcha 20 ta bron oyiga 5 000 000 so‘m tushum beradi. Yalpi marja 40% bo‘lsa, bu 2 000 000 so‘m foyda. Agar ishlab chiqish 120 soat va shartli stavka soatiga 150 000 so‘m bo‘lsa, xarajat 18 000 000 so‘m. Qoplanish muddati tushum bo‘yicha emas, foyda bo‘yicha: 18 000 000 ÷ 2 000 000 = 9 oy, administrator vaqtini hisobga olmasdan. Agar bu muddat siz uchun uzun bo‘lsa, avval oddiy bot bilan bron qilishni sinang.

## Oddiy bot qachon yetarli

Mini App’ga pul sarflashdan oldin quyidagi savollarga javob bering:

- **Mahsulot 10–15 tadan kammi?** Unda tugmali bot yoki kanal posti yetarli.
- **Mijoz tanlashdan oldin baribir gaplashishni xohlaydimi?** Masalan, ta’mir yoki ko‘chmas mulk. Unda ariza yig‘uvchi bot va tez javob muhimroq.
- **Telegram’da auditoriya hali yo‘qmi?** Mini App trafik keltirmaydi. Avval kanal va bot auditoriyasini quring; obunachilarni botga qanday o‘tkazish — [kanal obunachilarini botga o‘tkazish](/blog/kanal-obunachilarini-botga-otkazish/) maqolasida.
- **Katalogni kim yangilaydi?** Agar narxlar har kuni o‘zgarsa va buni qiladigan odam bo‘lmasa, Mini App tezda eskiradi.

Mini App mantiqiy bo‘ladigan holat: ko‘p mahsulot yoki ko‘p vaqt slotlari, Telegram’da faol auditoriya, takroriy buyurtmalar va katalogni yangilaydigan mas’ul odam.

## Ko‘p uchraydigan xatolar

- **Saytni Mini App ichiga shunchaki joylash.** Mobil ekranga moslashtirilmagan sayt Telegram ichida ham noqulay.
- **Bot xabarlaridan foydalanmaslik.** Mini App’ning kuchi — bot orqali eslatma va holat xabarlari. Buyurtmadan keyin jim qolish imkoniyatni yo‘qotadi.
- **Raqamli mahsulotga karta to‘lovi.** Telegram qoidalariga zid va mobil foydalanuvchilarga ko‘rinmay qolish xavfi bor.
- **Manbani o‘lchamaslik.** Har bir kanal posti va reklama uchun alohida `startapp` parametri qo‘ying, shunda qaysi manba buyurtma berganini ko‘rasiz.
- **Ishga tushirgandan keyin unutish.** Har oy ochilishlar, buyurtmalar va tashlab ketilgan savatchalarni ko‘rib chiqing.

## Savol-javob

### Mini App uchun alohida ilova yuklab olish kerakmi?

Yo‘q. Mini App Telegram ichida ochiladi. Foydalanuvchiga faqat Telegram kerak, hujjatga ko‘ra uni hatto telefon bosh ekraniga yorliq sifatida qo‘shish mumkin.

### Telegram Stars’ni jismoniy tovar uchun ishlatsa bo‘ladimi?

Telegram qoidalarida Stars majburiy bo‘lgan holat — raqamli tovar va xizmatlar. Jismoniy tovar uchun boshqa provayderlar va valyutalarga ruxsat bor. Mahalliy mijoz uchun odatda so‘mdagi to‘lov qulayroq.

### Mini App reklamasini qanday qilish mumkin?

Kanal postidagi tugma, botning menyu tugmasi, Telegram’dagi va boshqa platformalardagi reklama havolalari orqali. Har bir manba uchun alohida havola parametri qo‘ying, shunda natijani o‘lchash mumkin.

### Mini App’ni konstruktorda qilsa bo‘ladimi?

Oddiy katalog yoki bron uchun konstruktorlar ham mavjud va ular tezroq ishga tushadi. Lekin o‘ziga xos logika, CRM bilan chuqur integratsiya yoki noodatiy dizayn kerak bo‘lsa, alohida ishlab chiqish kerak bo‘ladi.

## Xulosa

Telegram Mini App — Telegram’da allaqachon auditoriyasi bor biznes uchun katalog, bron, sodiqlik va kalkulyator vositasi. Raqamli tovarlar faqat Telegram Stars orqali sotiladi, jismoniy tovar va xizmatlar uchun boshqa provayderlarga ruxsat bor. Qarorni ishlab chiqish soatlari va foyda bo‘yicha qoplanish muddatini hisoblab qabul qiling, kichik katalog yoki suhbat talab qiladigan sotuv uchun esa oddiy bot bilan boshlang.

Telegram’dagi sotuv voronkangizga Mini App kerakmi yoki bot yetarlimi — Level Marketing buni bepul audit davomida siz bilan birga ko‘rib chiqishi mumkin.

## Shu mavzuda yana

- [Telegram botda rassilka: mijoz bloklamasligi uchun 7 qoida](/blog/telegram-bot-rassilka-qoidalari/)
- [Kanaldagi tugmali post: bot orqali joylash va bosishni sanash](/blog/kanalda-tugmali-post/)
- [Telegram’da AI-javobchi: arizalarga 24/7 javob](/blog/telegram-ai-javobchi/)
