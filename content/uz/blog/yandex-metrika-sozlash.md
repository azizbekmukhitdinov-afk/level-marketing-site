---
title: Yandex Metrika sozlash: hisoblagich, maqsadlar va Vebvizor
description: Yandex Metrikani noldan sozlash: hisoblagich o‘rnatish, maqsadlar, Vebvizor, UTM-belgilar va Yandex Direkt bilan ulash. Shartli misol va xatolar ro‘yxati bilan.
date: 2026-11-28
slug: yandex-metrika-sozlash
type: article
tags: Yandex Metrika, veb-analitika, Yandex Direkt, sayt
key: yandex-metrika-sozlash
rubric: target
---

Yandex Direktga pul ketyapti, saytga odam kelyapti, lekin «qaysi kalit so‘z ariza olib keldi» degan savolga hech kim aniq javob bera olmaydi. **Yandex Metrika** — bepul veb-analitika xizmati bo‘lib, tashriflar, manbalar va saytdagi harakatlarni yozadi, Vebvizor esa tashrifni video kabi ko‘rsatadi. Bu maqolada hisoblagichni o‘rnatishdan Direkt bilan ulashgacha bo‘lgan tartibni, qaror qoidalari va tipik xatolarni ko‘rib chiqamiz.

## Metrika nima beradi va GA4 dan farqi

Ko‘pchilik «bizda Google Analytics bor, Metrika shart emas» deydi. Agar Yandex Direkt ishlatsangiz, Metrika deyarli majburiy: Direkt strategiyalari va hisobotlari Metrika ma’lumotlariga tayanadi. Ikkalasini birga qo‘yish ham normal holat — ular bir-biriga xalaqit bermaydi.

| Savol | Yandex Metrika | Google Analytics 4 |
|---|---|---|
| Qaysi reklama bilan yaxshi ishlaydi | Yandex Direkt | Google Ads |
| Tashrif yozuvi (video kabi) | Bor — Vebvizor | O‘zida yo‘q |
| Maqsad / asosiy hodisa | «Maqsadlar» | «Key events» |
| Tez boshlash | Tayyor maqsad turlari ko‘p | Hodisalarni ko‘proq qo‘lda sozlash kerak |

GA4 haqida batafsil — [Google Analytics 4: kichik biznes sayti uchun sozlash qo‘llanmasi](/blog/google-analytics-4/) maqolasida. Ikki tizimda raqamlar biroz farq qilishi tabiiy: ular tashrifni turlicha hisoblaydi.

## 1-qadam: hisoblagich yaratish

Hisoblagich (schyotchik) — saytga qo‘yiladigan kod. Tartib:

1. metrika.yandex.ru saytiga **kompaniya** Yandex akkaunti bilan kiring. Xodim yoki dasturchining shaxsiy akkaunti bilan emas — hamkorlik tugasa, statistika ham ketib qoladi.
2. Yangi hisoblagich qo‘shing: nomi, sayt domeni, vaqt mintaqasi (Toshkent).
3. Asosiy sozlamalarda **Vebvizor, skroll xaritasi va formalar analitikasi** opsiyasini yoqing. Yandex yordam bo‘limiga ko‘ra, bu opsiya hisoblagich yaratilayotganda yoki keyinroq hisoblagich sozlamalarida yoqiladi ([Yandex Metrika yordami](https://yandex.ru/support/metrika/general/creating-counter.html)).
4. Kodni o‘rnating: tayyor platformada (CMS) — maxsus maydon yoki plagin orqali, oddiy saytda — kodni barcha sahifalarga, Tag Manager ishlatsangiz — u orqali.

Saytda tugma va formalar ko‘p bo‘lsa yoki Meta Pixel ham bor bo‘lsa, kodlarni bir joyda boshqarish qulay — bu haqda [Google Tag Manager: teglar, triggerlar va xatolarsiz o‘rnatish](/blog/google-tag-manager/) maqolasida.

**Tekshirish.** O‘rnatgandan keyin telefoningizdan saytga kiring va bir necha daqiqadan so‘ng bugungi hisobotda tashrif paydo bo‘lganini ko‘ring. Ko‘rinmasa — kod hamma sahifada emas yoki boshqa hisoblagich raqami qo‘yilgan.

## 2-qadam: maqsadlar

Maqsad — sizga muhim harakat: ariza, qo‘ng‘iroq tugmasi, Telegramga o‘tish. Maqsadsiz Metrika faqat «nechta odam keldi»ni ko‘rsatadi, bu biznes uchun yarim ma’lumot.

Yandex yordam bo‘limida maqsadning 16 turi sanab o‘tilgan: sahifaga tashrif, forma yuborish, telefon raqamiga bosish, messenjerga o‘tish, tugmani bosish, JavaScript-hodisa, tarkibiy (bosqichli) maqsad va boshqalar ([maqsad turlari](https://yandex.ru/support/metrika/general/goals.html)). Kichik biznes saytiga odatda shular yetadi:

| Maqsad | Turi | Nima uchun |
|---|---|---|
| Ariza yuborildi | Forma yuborish yoki «Rahmat» sahifasiga tashrif | Asosiy maqsad, CPL shu bo‘yicha |
| Qo‘ng‘iroq tugmasi | Telefon raqamiga bosish | Mobil trafikda ko‘p uchraydi |
| Telegram / WhatsApp | Messenjerga o‘tish | Ariza formasiz yozadiganlar |
| Narxlar sahifasi | Sahifaga tashrif | Qiziqish belgisi, asosiy emas |

Bilib qo‘yish kerak bo‘lgan qoidalar (manba — [Yandex Metrika yordami](https://yandex.com/support/metrica/ru/general/multi)):

- bitta hisoblagichda **200 tagacha** maqsad yaratish mumkin;
- yangi maqsad bo‘yicha statistika bir necha daqiqada yig‘ila boshlaydi — o‘tgan kunlar uchun ma’lumot bo‘lmaydi, shuning uchun maqsadlarni reklamadan **oldin** yarating;
- maqsadni tahrirlash oldin yig‘ilgan ma’lumotni o‘zgartirmaydi;
- maqsadni o‘chirsangiz, u bo‘yicha ma’lumot hisobotlarda ko‘rinmay qoladi.

**Avtomaqsadlar.** Metrika telefon, email va messenjer havolalariga bosishni avtomatik maqsad sifatida yozishi mumkin. Yordam bo‘limiga ko‘ra, avtomaqsadlar umumiy limitga kirmaydi va tarkibiy maqsad ichida ishlatilmaydi ([avtomaqsadlar](https://yandex.com/support/metrica/ru/general/auto-goals)). Ular boshlash uchun qulay, lekin asosiy maqsadni (ariza) baribir o‘zingiz aniq sozlang.

**Qaror qoidasi:** bitta asosiy maqsad (pulga eng yaqin harakat) va 2–4 ta yordamchi. «Saytda 30 soniya» yoki «2 sahifa ko‘rdi» kabi maqsadlarni Direkt strategiyasi uchun asosiy qilmang — algoritm arzon, lekin sotib olmaydigan tashriflarni qidira boshlaydi. Nima uchun aynan shunday — [Konversiya nima: qanday hisoblash va qanday oshirish](/blog/konversiya-nima/) maqolasida.

## 3-qadam: Vebvizor

Vebvizor tashrifni yozib oladi: sichqoncha harakati, skroll, bosishlar, formani to‘ldirish. Raqamlar «nima» bo‘lganini aytadi, Vebvizor esa «nima uchun»ni ko‘rsatadi.

Yandex yordam bo‘limiga ko‘ra, yozuvlar joriy kunni qo‘shib **15 kun** saqlanadi, kuniga nechta yozuv saqlanishi esa maxsus algoritm bilan belgilanadi ([Vebvizor talablari](https://yandex.ru/support/metrica/webvisor/requirements.html)). Demak, Vebvizor — arxiv emas: muammoni ikki hafta ichida ko‘rib chiqish kerak.

Yozuvlarni qanday ko‘rish foydali:

- **reklamadan kelib, maqsadga yetmaganlar** — ular qayerda to‘xtagan;
- **ariza qoldirganlar** — ular qaysi bloklarni o‘qigan, narxga qaytganmi;
- **mobil tashriflar** — tugma ekranga sig‘adimi, forma klaviatura ostida qolmayaptimi.

Haftasiga 20–30 ta yozuv ko‘rish yetarli. Bir xil xato 5–6 marta takrorlansa — bu tasodif emas, tuzatish kerak. Sahifa tuzilmasi haqida — [Landing sahifa: ariza olib keladigan tuzilma](/blog/landing-sahifa/).

## 4-qadam: UTM-belgilar

Metrika Direkt, qidiruv va ijtimoiy tarmoqlardan kelgan trafikni o‘zi ajratadi, lekin Instagram reklamasi, Telegram post yoki hamkor sayt haqida aniq ma’lumot uchun havolalarga UTM-belgilar qo‘shing. Nomlash qoidalari va shablon — [UTM-belgilar: har bir mijoz qayerdan kelganini qanday bilish](/blog/utm-belgilar/) maqolasida. Metrikada natijani manbalar bo‘limidagi UTM-belgilar hisobotida ko‘rasiz.

Asosiy qoida bir xil: faqat kichik harflar, bir xil kanal — doim bir xil nom, barcha nomlar bitta jadvalda.

## 5-qadam: Yandex Direkt bilan ulash

Bu qadamni ko‘pchilik o‘tkazib yuboradi, keyin hisobotlarda chalkashlik bo‘ladi.

**Hisoblagichni kampaniyaga biriktiring.** Direktda kampaniya sozlamalarida Metrika hisoblagichini tanlang. Yordam bo‘limiga ko‘ra, hisoblagich biriktirilmasa, Metrika hisobotlarida reklamadan kelgan o‘tishlar «begona kampaniyalar» sifatida ko‘rinadi ([Direkt hisobotlarini ulash](https://yandex.ru/support/metrika/general/direct.html)).

**yclid belgisi.** Direkt havolaga avtomatik ravishda yclid — bosishning noyob raqamini qo‘shadi, hisoblagich u orqali tashrifni aniq bosish bilan bog‘laydi. Redirekt ishlatsangiz, yclid oxirgi manzilgacha yetib borishini tekshiring.

**Dinamik parametrlar.** Direkt havoladagi {keyword}, {campaign_id}, {source}, {device_type} kabi parametrlarni o‘zi to‘ldiradi ([URL parametrlari](https://yandex.ru/support/direct/statistics/url-tags.html)). Masalan:

`https://sayt.uz/?utm_source=yandex&utm_medium=cpc&utm_campaign={campaign_id}&utm_term={keyword}`

Shunda CRMga ariza bilan birga kalit so‘z ham tushadi va qaysi so‘z sotuv berganini ko‘rasiz.

**Maqsadni strategiyaga ulang.** Direktning avtomatik strategiyalari Metrika maqsadlari bo‘yicha optimallashtiradi, shuning uchun strategiyaga asosiy maqsadni (ariza) tanlang. Direktni qachon boshlash kerakligi haqida — [Yandex Direkt O‘zbekistonda: qachon foydali va qanday boshlash](/blog/yandex-direkt-ozbekistonda/).

## Shartli misol: bir oylik hisob

Shartli misol. Mebel do‘koni bir oyda Direktga 4 000 000 so‘m sarfladi. Metrika ko‘rsatadi:

| Ko‘rsatkich | Qiymat |
|---|---|
| Direktdan tashriflar | 1 600 |
| «Ariza yuborildi» maqsadi | 48 |
| «Qo‘ng‘iroq tugmasi» | 32 |
| «Telegramga o‘tish» | 20 |
| Jami kontaktlar | 100 |
| Kontakt narxi | 4 000 000 / 100 = 40 000 so‘m |

Endi Vebvizor: mobil tashriflarning ko‘pchiligi forma ustida to‘xtab, sahifadan chiqib ketgan — forma 7 ta maydondan iborat. Maydonlar 3 taga qisqartirildi, keyingi oyda xuddi shu byudjet bilan formalar soni 48 dan, deylik, 70 ga chiqdi (bu ham shartli raqam). Kontakt narxi 32 000 so‘m atrofiga tushdi.

Keyingi qadam — CRM bilan solishtirish. Metrikada 100 ta kontakt, CRMda esa 76 ta haqiqiy lid bo‘lishi mumkin: takroriy bosishlar, javobsiz qo‘ng‘iroqlar, bir odamning ikki xil kanaldan yozishi. Bu farq normal, sabablari — [Kabinetdagi lidlar va CRM mos kelmasa: 7 sabab va tekshiruv](/blog/kabinet-va-crm-lidlar/) maqolasida.

## Ko‘p uchraydigan xatolar

- **Hisoblagich dasturchining akkauntida.** Hamkorlik tugaydi — tarix ham ketadi.
- **Ikki hisoblagich bir saytda** (eski va yangi). Raqamlar ikkiga bo‘linadi yoki ikki marta sanaladi.
- **Maqsadlar reklamadan keyin yaratilgan.** Birinchi haftaning konversiyalari yo‘q — strategiya ma’lumotsiz o‘qiydi.
- **Asosiy maqsad sifatida «yengil» harakat.** Direkt arzon tashriflarni olib keladi, arizalar ko‘paymaydi.
- **Hisoblagich kampaniyaga biriktirilmagan.** Reklama trafigi hisobotlarda noto‘g‘ri manbada ko‘rinadi.
- **Vebvizor yoqilmagan yoki hech kim ko‘rmaydi.** 15 kundan keyin yozuvlar yo‘qoladi.
- **Ofis xodimlarining tashriflari.** Kichik saytda o‘z xodimlaringiz statistikani sezilarli buzadi — ularni filtr bilan ajrating.

## Savol-javob

### Saytda Google Analytics bor. Metrika ham kerakmi?

Yandex Direkt ishlatsangiz — ha, chunki Direkt strategiyalari va hisobotlari Metrika maqsadlariga tayanadi. Faqat Google Ads va Meta bo‘lsa, Metrika majburiy emas, lekin Vebvizor uchun uni qo‘yish foydali.

### Vebvizor saytni sekinlashtiradimi?

Har qanday qo‘shimcha skript sahifaga biroz yuk qo‘shadi. Amalda kichik biznes sayti uchun asosiy muammo odatda og‘ir rasmlar va ortiqcha skriptlar bo‘ladi. Tezlikni o‘rnatishdan oldin va keyin o‘lchab, solishtiring.

### Nima uchun Direkt va Metrikada bosishlar soni farq qiladi?

Direkt bosishlarni, Metrika esa tashriflarni sanaydi. Odam bosib, sahifa yuklanishidan oldin chiqib ketsa, Direktda bosish bor, Metrikada tashrif yo‘q. Bundan tashqari, Direkt firibgarlikdan himoya filtrdan o‘tgan bosishlarnigina hisoblaydi ([Direkt yordami](https://yandex.ru/support/direct/ru/statistics/metrika)).

### Maqsadlarni qancha vaqtda tekshirish kerak?

Yaratganingizdan so‘ng darhol: o‘zingiz formani to‘ldiring, tugmani bosing va bir necha daqiqadan keyin maqsad yozilganini hisobotda ko‘ring. Keyin oyiga bir marta Metrikadagi arizalarni CRM bilan solishtiring.

## Xulosa

Yandex Metrikani to‘g‘ri sozlash bir kunlik ish: kompaniya akkauntida bitta hisoblagich, reklamadan oldin yaratilgan 3–5 ta maqsad, yoqilgan Vebvizor, UTM-belgilar va Direkt kampaniyalariga biriktirilgan hisoblagich. Shundan keyin haftasiga yarim soat: maqsadlar dinamikasi, 20–30 ta Vebvizor yozuvi va oylik CRM bilan solishtirish. Bu reklama byudjetini taxmin bilan emas, raqam bilan boshqarishga imkon beradi.

Level Marketing bepul audit davomida saytingizdagi Metrika hisoblagichi, maqsadlar va Direkt ulanishi to‘g‘ri ishlayotganini tekshirib berishi mumkin.

## Shu mavzuda yana

- [Yandex Direkt O‘zbekistonda: qachon foydali va qanday boshlash](/blog/yandex-direkt-ozbekistonda/)
- [UTM-belgilar: har bir mijoz qayerdan kelganini qanday bilish](/blog/utm-belgilar/)
- [Google Analytics 4: kichik biznes sayti uchun sozlash qo‘llanmasi](/blog/google-analytics-4/)
