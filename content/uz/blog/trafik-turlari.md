---
title: Trafik turlari: organik, pullik, to‘g‘ridan-to‘g‘ri va AI trafik
description: Trafik turlari nima: organik, pullik, to‘g‘ridan-to‘g‘ri, referal, ijtimoiy va AI trafik. GA4’da qayerdan ko‘rish va kichik biznes qaysi birini birinchi o‘stirishi kerak.
date: 2026-11-27
slug: trafik-turlari
type: article
tags: trafik turlari, GA4, sayt trafigi, target
key: trafik-turlari
rubric: target
---

Saytga har kuni 200 kishi kirsa, bu yaxshimi? Javob ular qayerdan kelganiga bog‘liq. **Trafik turlari** — odamlar saytga qaysi yo‘l bilan kelganini ko‘rsatadigan guruhlar: qidiruvdan, reklamadan, Instagram’dan, boshqa saytdan yoki AI-yordamchidan. Bu maqolada har bir trafik turini oddiy tilda tushuntiramiz, GA4’da qayerdan ko‘rishni va qaysi birini birinchi o‘stirish kerakligini aytamiz.

## Trafik nima

Trafik — saytga kelgan tashriflar oqimi. Google Analytics 4 (GA4) har bir tashrifni seans deb ataydi va uni manbasiga qarab kanal guruhiga joylaydi. Manba — qayerdan kelgani (google, instagram.com, t.me), kanal — qaysi turdagi yo‘l (organik qidiruv, pullik ijtimoiy tarmoq va hokazo).

Trafik turini bilish uch savolga javob beradi:

- **pul qayerga ketyapti** — reklama trafigi ariza beryaptimi;
- **nima tekin ishlayapti** — qidiruv, sharhlar, tavsiyalar;
- **qayerda xavf bor** — hamma trafik bitta kanaldan kelsa, u to‘xtaganda sayt bo‘shab qoladi.

## Asosiy trafik turlari: jadval

GA4’da standart kanal guruhida o‘ndan ortiq kanal bor ([Google Analytics yordami](https://support.google.com/analytics/answer/9756891)). Kichik biznes uchun eng muhimlari:

| Trafik turi | GA4’dagi nomi | Qayerdan keladi | Misol |
|---|---|---|---|
| Organik qidiruv | Organic Search | Google, Yandex’dagi reklama bo‘lmagan natijalar | «Toshkentda ofis mebeli» qidirib, saytingizni topdi |
| Pullik qidiruv | Paid Search | Qidiruv reklamasi | Google Ads e’loni orqali kirdi |
| To‘g‘ridan-to‘g‘ri | Direct | Manzilni o‘zi yozgan yoki saqlangan havola | Vizitkadagi manzilni brauzerga yozdi |
| Referal | Referral | Boshqa sayt yoki ilovadagi havola | Yangilik saytidagi maqoladan o‘tdi |
| Organik ijtimoiy | Organic Social | Ijtimoiy tarmoqlardagi oddiy havola | Instagram bio’dagi havolani bosdi |
| Pullik ijtimoiy | Paid Social | Ijtimoiy tarmoqdagi reklama | Instagram reklamasidan saytga kirdi |
| Email | Email | Xatdagi havola | Rassilka xatidan o‘tdi |
| AI-yordamchi | AI Assistant | ChatGPT, Gemini, Copilot kabi chatbotlar | ChatGPT javobidagi havolani bosdi |
| Aniqlanmagan | Unassigned | Hech bir qoidaga tushmagan | Noto‘g‘ri UTM bilan kelgan tashrif |

Display, Organic Video, Paid Video kabi boshqa kanallar ham bor, lekin boshlash uchun shu to‘qqiztasi yetarli.

## Har bir trafik turi haqida qisqacha

### Organik qidiruv

Odam o‘zi qidiradi va sizni topadi — bu eng «issiq» trafiklardan biri. Uni SEO, Google va Yandex xaritalardagi kartochka va foydali maqolalar o‘stiradi. Natija sekin keladi, lekin pul to‘xtaganda ham ishlayveradi. Asoslar — [SEO haqidagi maqolada](/blog/seo-nima/).

### Pullik trafik

Qidiruv reklamasi, Instagram va Facebook reklamasi, TikTok, banner. Tez yoqiladi va tez o‘chadi: byudjet to‘xtasa, trafik ham to‘xtaydi. Bu trafikni faqat tashriflar bilan emas, ariza va sotuv bilan baholang.

### To‘g‘ridan-to‘g‘ri trafik

Rasmiy ta’rif bo‘yicha — manzilni o‘zi yozgan yoki saqlangan havola orqali kelganlar. Amalda Direct’ga manbasi aniqlanmagan tashriflar ham tushadi: masalan, ba’zi messenjerlar va ilovalar ichidagi havolalar manbani uzatmasligi mumkin. Shuning uchun Direct’ning o‘sishi har doim ham «brendimiz tanildi» degani emas.

### Referal trafik

Boshqa saytlardagi havolalar: yangilik saytlari, kataloglar, hamkorlar. Sifatli referal trafik ham tashrif, ham ishonch beradi — odam sizni o‘zi ishonadigan joyda ko‘rdi.

### Ijtimoiy trafik

Instagram, Facebook, TikTok, YouTube’dagi havolalar. GA4 pullik va organik ijtimoiy trafikni ajratadi, lekin buning uchun reklama havolalarida to‘g‘ri belgilar bo‘lishi kerak. Belgisiz reklama havolasi organik ijtimoiy yoki referal sifatida yozilib qolishi mumkin va reklama natijasi hisobotda yo‘qoladi.

### AI trafik

ChatGPT, Gemini, Copilot kabi yordamchilar javobida saytingizga havola bersa va odam uni bossa, bu AI trafik. Google yordam sahifasiga ko‘ra GA4’da buning uchun alohida **AI Assistant** kanali bor, Google’ning AI Overviews va AI Mode’dan kelgan tashriflar esa Organic Search’ga yoziladi ([Google Analytics yordami](https://support.google.com/analytics/answer/9756891)). Kanal 2026-yilda qo‘shilgan, shuning uchun eski davr ma’lumotlarida bunday tashriflar Referral’da turgan bo‘lishi mumkin.

O‘zbekistonda AI trafik hozircha kichik, lekin u o‘sib boradi. AI javoblarida qanday chiqish — [neyrotarmoqlarda ko‘rinish (GEO)](/blog/neyrotarmoqlarda-korinish-geo/) maqolasida, Google’ning AI rejimi sayt uchun nimani o‘zgartirishi esa [Google AI Mode haqidagi maqolada](/blog/google-ai-mode/).

## GA4’da trafik turlarini qanday ko‘rish

Oddiy yo‘l:

1. GA4’ni oching va chap menyuda **Reports** (Hisobotlar) bo‘limiga kiring.
2. **Acquisition → Traffic acquisition** hisobotini tanlang.
3. Jadvalda seanslar kanal guruhi bo‘yicha ko‘rinadi: Organic Search, Direct, Paid Social va hokazo.
4. Yuqorida sanalar oralig‘ini tanlang va o‘tgan davr bilan solishtirishni yoqing.
5. Batafsil ko‘rish uchun asosiy ustunni **Session source / medium** ga almashtiring — google / organic, instagram / paid kabi.

Har bir kanal uchun faqat seanslarni emas, quyidagilarni ham ko‘ring:

- **jalb qilingan seanslar** (engaged sessions) — odam saytda haqiqatan qoldimi;
- **asosiy hodisalar** (key events) — ariza, qo‘ng‘iroq tugmasi, Telegram’ga o‘tish;
- **asosiy hodisa darajasi** — kelganlarning qancha qismi harakat qildi.

Asosiy hodisalar sozlanmagan bo‘lsa, trafik hisoboti faqat «nechta odam keldi»ni ko‘rsatadi — «nechta mijoz bo‘ldi»ni emas.

## Trafikni to‘g‘ri yozish: UTM va ulanishlar

GA4 trafikni manba ma’lumotlariga qarab tasniflaydi. Ma’lumot bo‘lmasa yoki noto‘g‘ri bo‘lsa, tashrif boshqa kanalga tushadi. Uch qoida:

- **Har bir reklama havolasiga UTM qo‘ying.** Instagram reklamasi, Telegram kanaldagi post, rassilka, QR-kod — hammasi. Qanday yozish — [UTM-belgilar haqidagi maqolada](/blog/utm-belgilar/).
- **Google Ads’ni GA4 bilan ulang** va avto-belgilashni yoqing — shunda qidiruv reklamasi Paid Search’ga to‘g‘ri tushadi.
- **UTM’ni bir xil yozing.** «Instagram», «instagram» va «IG» GA4 uchun uch xil manba. Kichik harf va bitta lug‘at ishlating.

> **Shartli misol.** Toshkentdagi mebel do‘koni Instagram reklamasiga UTM qo‘ymagan. GA4’da Paid Social deyarli nol, Organic Social esa birdan o‘sgan. Tadbirkor «reklama ishlamayapti, organika o‘syapti» deb o‘ylaydi — aslida bu o‘sha reklama, faqat noto‘g‘ri yozilgan.

## Qaysi trafikni birinchi o‘stirish kerak

Hamma kanalni birdaniga o‘stirish shart emas. Biznes bosqichiga qarab tartib boshqacha:

| Biznes holati | Birinchi navbatda | Keyin |
|---|---|---|
| Yangi biznes, sayt yangi | Pullik qidiruv va ijtimoiy reklama — tez talab tekshiriladi | Xaritalar, SEO asoslari |
| Barqaror sotuv bor, reklama qimmatlashdi | Organik qidiruv, xaritalar, sharhlar | Referal: hamkorlar, kataloglar |
| Ko‘p odam keladi, lekin sotib olmaydi | Retargeting va sayt konversiyasi | Email yoki bot orqali qayta aloqa |
| Brend tanilgan, takroriy xaridlar ko‘p | To‘g‘ridan-to‘g‘ri va email, sodiqlik | AI va qidiruvda ko‘rinish |

Uchinchi qatorga alohida e’tibor bering: trafik ko‘p, sotuv kam bo‘lsa, yangi trafik sotib olishdan oldin kelganlarni qaytarishni o‘ylang. Bu haqda — [retargeting](/blog/retargeting-qanday-ishlaydi/) maqolasida.

Sog‘lom aralashma uchun bitta mo‘ljal: bitta kanal trafikning ko‘p qismini bermasin. Agar 80–90% bitta reklama kabinetidan kelsa (shartli chegara), kabinet bloklanganda biznes to‘xtab qoladi.

## Ko‘p uchraydigan xatolar

- **Faqat seanslarga qarash.** 1 000 ta tashrif va 0 ta ariza — bu natija emas.
- **UTM’siz reklama.** Pullik trafik organik yoki Direct bo‘lib ko‘rinadi.
- **Direct’ni brend deb o‘ylash.** Direct’ga manbasi yo‘qolgan tashriflar ham tushadi.
- **Bot va spam trafigini hisobga olmaslik.** Bir kunda to‘satdan yuzlab 0 soniyalik tashriflar — tekshirish kerak.
- **Asosiy hodisalar sozlanmagan.** GA4 qaysi kanal mijoz berganini ko‘rsata olmaydi.
- **Ichki tashriflarni filtrlamaslik.** Xodimlar har kuni saytni ochsa, raqamlar shishadi.

## Savol-javob

### Qaysi trafik eng yaxshi?

Yagona eng yaxshi trafik yo‘q. Organik qidiruv odatda arzon va issiq, lekin sekin o‘sadi. Pullik trafik tez, lekin byudjetga bog‘liq. Eng yaxshi natija — bir nechta kanal bir-birini to‘ldirganda: reklama yangi odamni olib keladi, qidiruv va to‘g‘ridan-to‘g‘ri trafik uni qaytaradi.

### Nega GA4’dagi raqamlar reklama kabinetidagi kliklar bilan mos kelmaydi?

Klik va seans har xil narsa. Odam bosgan, lekin sahifa yuklanmasdan chiqib ketgan bo‘lishi mumkin, ba’zi foydalanuvchilar kuzatuvni rad etadi, kabinet va GA4 vaqt va atributsiyani har xil hisoblaydi. Farq bo‘lishi normal, lekin u juda katta bo‘lsa, havolalar va GA4 o‘rnatilishini tekshiring.

### Telegram’dan kelgan trafik qayerda ko‘rinadi?

Bu havolaga va qurilmaga bog‘liq: ba’zan Referral, ba’zan Organic Social, manba uzatilmasa — Direct. Ishonchli usul — Telegram’dagi har bir havolaga UTM qo‘yish: masalan, utm_source=telegram va kanal nomi. Shunda tashriflar qayerga tushishidan qat’i nazar, manba bo‘yicha ajratib ko‘rasiz.

### AI trafikni hozir o‘stirish kerakmi?

Alohida byudjet ajratish shart emas, lekin poydevorni hozir qo‘ygan ma’qul: aniq narx va xizmatlar sahifasi, savol-javob bo‘limi, xaritalardagi to‘liq kartochka, sharhlar. Bular odatiy qidiruvga ham, AI javoblariga ham foyda beradi. GA4’dagi AI Assistant kanalini oyiga bir marta kuzatib boring.

## Xulosa

Trafik turlari — saytga kelgan odamlarning yo‘llari: organik va pullik qidiruv, to‘g‘ridan-to‘g‘ri, referal, ijtimoiy, email va AI-yordamchilar. Ularni GA4’ning Traffic acquisition hisobotida ko‘ring, har bir reklama havolasiga UTM qo‘ying, kanallarni seans bilan emas, ariza bilan baholang va biznes bosqichiga qarab qaysi kanalni birinchi o‘stirishni tanlang.

Level Marketing bepul audit paytida GA4 va reklama kabinetlaringiz trafikni to‘g‘ri yozayotganini ham ko‘rib chiqishi mumkin.

## Shu mavzuda yana

- [Performance marketing nima: natija uchun ishlaydigan marketing](/blog/performance-marketing-nima/)
- [Landing sahifa: ariza olib keladigan tuzilma](/blog/landing-sahifa/)
- [Kontekst reklama nima: qidiruv va tarmoq reklamasi oddiy tilda](/blog/kontekst-reklama-nima/)
