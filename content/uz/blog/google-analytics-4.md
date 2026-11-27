---
title: Google Analytics 4: kichik biznes sayti uchun sozlash qo‘llanmasi
description: Google Analytics 4 ni kichik biznes saytiga o‘rnatish: asosiy hodisalar, UTM, Google Ads bilan ulash, kerakli hisobotlar va ko‘p uchraydigan xatolar.
date: 2026-11-27
slug: google-analytics-4
type: article
tags: Google Analytics 4, GA4, veb-analitika, sayt
key: google-analytics-4
rubric: target
---

Saytga reklama tushyapti, lekin qaysi kanal ariza olib kelayotganini hech kim aniq aytolmaydi — bu holat juda ko‘p uchraydi. **Google Analytics 4** (GA4) aynan shu savolga javob beradi: odamlar qayerdan keldi, saytda nima qildi va qaysi biri ariza qoldirdi. Bu maqolada kichik biznes sayti uchun GA4 ni noldan sozlash, kerakli hisobotlar va xatolarni ko‘rib chiqamiz.

## GA4 nima va biznesga nima beradi

GA4 — Google’ning bepul veb-analitika xizmati. U saytdagi har bir harakatni «hodisa» (event) sifatida yozadi: sahifa ochildi, tugma bosildi, forma yuborildi. Tadbirkor uchun bundan uchta aniq foyda bor:

- **trafik manbalari** — Google, Instagram, Telegram, reklama yoki to‘g‘ridan-to‘g‘ri kirish;
- **asosiy hodisalar** — ariza, qo‘ng‘iroq tugmasi, Telegram’ga o‘tish qaysi kanaldan qancha;
- **sahifalar** — qaysi sahifa ishlayapti, qaysi biridan odam darhol chiqib ketyapti.

GA4 sotuvni o‘zi ko‘rsatmaydi — u saytdagi harakatni ko‘rsatadi. Ariza haqiqiy mijozga aylandimi, buni CRM biladi. Shuning uchun GA4 va CRM raqamlari ba’zan farq qiladi, bu normal; sabablari [kabinet va CRM lidlari mos kelmasligi](/blog/kabinet-va-crm-lidlar/) haqidagi maqolada.

## 1-qadam: hisob, resurs va ma’lumotlar oqimi

Sozlash tartibi:

1. analytics.google.com saytiga kompaniya Google akkaunti bilan kiring (xodimning shaxsiy pochtasi bilan emas).
2. **Account** (hisob) yarating — kompaniya nomi.
3. **Property** (resurs) yarating — sayt nomi, vaqt zonasi «Uzbekistan», valyuta «UZS» yoki siz ishlaydigan valyuta.
4. **Data stream** (ma’lumotlar oqimi) — «Web», sayt manzilini kiriting.
5. Measurement ID (G- bilan boshlanadi) ni oling.

Hisob egasi kompaniya bo‘lsin, dasturchi yoki agentlik esa foydalanuvchi sifatida qo‘shilsin. Aks holda hamkorlik tugaganda statistika ham ketib qoladi.

## 2-qadam: saytga o‘rnatish

Uchta yo‘l bor, saytingizga qarab tanlang:

| Usul | Kimga mos | Qiyinligi |
|---|---|---|
| Konstruktor maydoni (Tilda, WordPress plagini va h.k.) | Tayyor platformadagi sayt | Oson |
| Google tag (gtag.js) kodini sahifaga qo‘yish | Oddiy sayt, dasturchi bor | O‘rtacha |
| Google Tag Manager | Ko‘p tugma, forma va reklama pikseli | O‘rtacha, lekin moslashuvchan |

Agar saytda Meta Pixel ham bo‘lsa, Tag Manager orqali hammasini bir joyda boshqarish qulay. Pixel sozlamalari haqidagi maqola havolasi sahifa oxirida.

O‘rnatgandan keyin tekshiring: saytni telefoningizdan oching va GA4 da **Reports → Realtime** hisobotida o‘zingizni ko‘ring. Ko‘rinmasa, kod noto‘g‘ri joyda yoki boshqa ID qo‘yilgan.

## 3-qadam: dastlabki sozlamalar

Bu to‘rt sozlamani birinchi kuniyoq qiling — keyin kech bo‘ladi.

**Ma’lumotlarni saqlash muddati.** Google yordam sahifasiga ko‘ra, foydalanuvchi darajasidagi ma’lumotlar uchun 2 yoki 14 oy tanlash mumkin ([Google Analytics yordam](https://support.google.com/analytics/answer/7667196)). Ko‘p resursda boshlang‘ich qiymat 2 oy turadi — uni 14 oyga o‘zgartiring: Admin → Data collection and modification → Data retention. O‘zgarish faqat oldinga ishlaydi, o‘chgan ma’lumot qaytmaydi.

**Kengaytirilgan o‘lchov (Enhanced measurement).** Data stream sozlamalarida yoqilgan bo‘lsin: u sahifa ko‘rishlar, aylantirish, tashqi havolalarga bosish, sayt ichidagi qidiruv, fayl yuklab olish va forma bilan ishlashni qo‘shimcha kodsiz yozadi.

**Ichki trafikni ajratish.** Ofis IP manzilini «internal traffic» deb belgilang va filtrni faollashtiring. Aks holda xodimlarning saytga kirishi statistikani buzadi.

**Kirish huquqlari.** Kim admin, kim faqat ko‘radi — ro‘yxat qiling.

## 4-qadam: asosiy hodisalar (key events)

GA4 da avval «konversiyalar» deb atalgan narsa endi **key events** (asosiy hodisalar) deyiladi. Google tushuntirishicha, bu Google Ads’dagi konversiyalar bilan adashtirmaslik uchun qilingan; Google Ads’da esa «konversiya» nomi qolgan ([Google Analytics yordam](https://support.google.com/analytics/answer/13965727)).

Kichik biznes sayti uchun odatda 3–5 ta asosiy hodisa yetarli:

| Hodisa | Nima | Qanday sozlanadi |
|---|---|---|
| generate_lead | Ariza formasi yuborildi | «Rahmat» sahifasi ochilishi yoki forma yuborilishi orqali |
| Telefon bosildi | tel: havolasiga bosish | Tag Manager orqali alohida hodisa |
| Telegram’ga o‘tish | t.me havolasiga bosish | click hodisasidan link_domain = t.me sharti bilan yangi hodisa |
| WhatsApp’ga o‘tish | wa.me havolasiga bosish | Xuddi shunday, wa.me bilan |
| purchase | Onlayn to‘lov (agar bo‘lsa) | Sayt yoki platforma orqali |

Hodisani asosiy deb belgilash: Admin → Events (yoki Key events) → kerakli hodisa yonidagi belgini yoqing.

Shartli misol: Toshkentdagi stomatologiya klinikasi saytida uchta asosiy hodisa bor: forma, qo‘ng‘iroq tugmasi va Telegram. Bir oydan keyin ko‘rinadiki, Google’dan kelganlar ko‘proq qo‘ng‘iroq qiladi, Instagram’dan kelganlar esa Telegram’ga yozadi. Bu raqamlar tushuntirish uchun olingan, lekin xulosa amaliy: har kanal uchun turli aloqa tugmasini birinchi o‘ringa qo‘yish mumkin.

Har bir sahifa ko‘rishni yoki 10 soniya qolishni asosiy hodisa qilmang — bu ko‘rsatkichni ma’nosiz qiladi. [Konversiya nima](/blog/konversiya-nima/) maqolasidagi qoida bu yerda ham amal qiladi: konversiya — biznes uchun pulga yaqin harakat.

## 5-qadam: UTM va Google Ads bilan ulash

**UTM-belgilar.** GA4 manbani o‘zi aniqlaydi, lekin Instagram bio, Telegram post yoki SMS havolalarida u ko‘pincha adashadi — masalan, messenjerlardan kelgan o‘tishlar «direct» bo‘lib tushishi mumkin. Har bir reklama va post havolasiga utm_source, utm_medium va utm_campaign qo‘shing. Batafsil qoidalar [UTM-belgilar](/blog/utm-belgilar/) haqidagi maqolada. Muhim: utm_medium uchun «cpc», «social», «email» kabi standart qiymatlardan foydalaning, aks holda GA4 trafikni «Unassigned» guruhiga tashlaydi.

**Google Ads bilan ulash.** Admin → Product links → Google Ads links. Ulangandan keyin:

- Google Ads kampaniyalari GA4 hisobotlarida alohida ko‘rinadi;
- GA4 dagi asosiy hodisalarni Google Ads’ga konversiya sifatida import qilish mumkin;
- saytga kirganlardan remarketing auditoriyalari yig‘iladi.

**Search Console bilan ulash.** Shu bo‘limda Search Console’ni ham ulang — organik qidiruvdagi so‘rovlar va sahifalar GA4 ichida ko‘rinadi.

## Qaysi hisobotlarni kuzatish kerak

GA4 da hisobot ko‘p, lekin tadbirkor uchun to‘rttasi yetarli:

1. **Acquisition → Traffic acquisition.** Qaysi kanal (Organic Search, Paid Search, Organic Social, Direct, Referral) qancha sessiya va qancha asosiy hodisa berdi.
2. **Engagement → Landing page.** Odamlar qaysi sahifaga birinchi tushdi va u yerdan ariza bo‘ldimi. Reklama sahifasi zaif bo‘lsa, shu yerda ko‘rinadi.
3. **Engagement → Events / Key events.** Har bir asosiy hodisa soni va o‘zgarishi.
4. **Realtime.** Yangi kampaniya yoki post chiqqanda trafik kelyaptimi, darhol tekshirish uchun.

ChatGPT, Gemini kabi AI xizmatlaridan o‘tishlar ham Referral’da ko‘rinishi mumkin — ularni alohida kuzatish foydali, bu mavzu [Google AI Mode](/blog/google-ai-mode/) haqidagi maqolada bor.

Haftada bir marta 15 daqiqa yetarli: kanal bo‘yicha asosiy hodisalar, eng yaxshi va eng yomon kirish sahifasi, o‘tgan hafta bilan farq. Oylik [reklama hisobotiga](/blog/reklama-hisoboti/) GA4 dan shu raqamlarni qo‘shing.

## Ko‘p uchraydigan xatolar

- **Hisob xodim yoki agentlik nomida** — hamkorlik tugasa, tarix yo‘qoladi.
- **Saqlash muddati 2 oyda qolgan** — o‘tgan yilni solishtirish imkoni yo‘q.
- **Asosiy hodisa yo‘q** — trafik ko‘rinadi, natija ko‘rinmaydi.
- **Hamma narsa asosiy hodisa** — aylantirish va sahifa ko‘rish ham «konversiya» bo‘lib qolgan.
- **Kod ikki marta o‘rnatilgan** — konstruktor maydoni va Tag Manager birga, hamma raqam ikki barobar.
- **UTM yo‘q** — Instagram va Telegram trafigi «direct» ichida yo‘qoladi.
- **Ichki trafik filtrlanmagan** — kichik saytda xodimlar statistikaning katta qismi bo‘lishi mumkin.

## Chek-list: GA4 tayyormi

- Hisob egasi — kompaniya Google akkaunti
- Vaqt zonasi Toshkent, valyuta to‘g‘ri tanlangan
- Kod bitta usulda o‘rnatilgan, Realtime’da tashrif ko‘rinadi
- Saqlash muddati 14 oy
- Ichki trafik filtri faol
- 3–5 ta asosiy hodisa belgilangan va test ariza bilan tekshirilgan
- Barcha reklama va post havolalarida UTM bor
- Google Ads va Search Console ulangan
- Haftalik 15 daqiqalik ko‘rib chiqish taqvimda

Test ariza yuborishni unutmang: formani o‘zingiz to‘ldiring va bir necha daqiqadan keyin Realtime’da generate_lead hodisasi chiqqanini ko‘ring.

## Savol-javob

### GA4 pullikmi?

Yo‘q, kichik va o‘rta biznes uchun oddiy GA4 bepul. Yirik kompaniyalar uchun Google Analytics 360 pullik versiyasi bor, lekin kichik sayt uchun u kerak emas.

### GA4 dagi lidlar CRM bilan nega mos kelmaydi?

Sabablar ko‘p: odam formani ikki marta yuboradi, reklama blokeri GA4 kodini to‘sadi, cookie roziligi berilmaydi, ariza telefon orqali keladi. GA4 trend va kanallarni solishtirish uchun, aniq lidlar soni uchun esa CRM asosiy manba.

### Konstruktordagi statistika yetmaydimi?

Tilda yoki boshqa konstruktor statistikasi asosiy raqamlarni ko‘rsatadi, lekin kanallar, asosiy hodisalar va Google Ads bilan bog‘lanish GA4 da ancha to‘liq. Ikkalasi bir-biriga xalaqit bermaydi.

### Natija qachon ko‘rinadi?

Realtime hisobotida — darhol. Oddiy hisobotlarda ma’lumot bir necha soatdan bir kungacha kechikishi mumkin. Xulosa qilish uchun kamida 2–4 hafta ma’lumot to‘plang.

## Xulosa

Google Analytics 4 ni sozlash bir kunlik ish: kompaniya nomida hisob, to‘g‘ri o‘rnatilgan kod, 14 oylik saqlash muddati, ichki trafik filtri va 3–5 ta asosiy hodisa. Keyin UTM-belgilar, Google Ads va Search Console bilan ulash, haftasiga 15 daqiqa to‘rt hisobotga qarash. Shunda «qaysi reklama ishlayapti» degan savolga taxmin emas, raqam bilan javob berasiz.

Level Marketing bepul audit davomida saytingizdagi GA4 sozlamalari va asosiy hodisalar to‘g‘ri yozilayotganini tekshirib berishi mumkin.

## Shu mavzuda yana

- [Google Ads sozlash: qidiruv reklamasini ishga tushirish](/blog/google-ads-sozlash/)
- [Meta Pixel va Conversions API: 2026 uchun o‘rnatish qo‘llanmasi](/blog/meta-pixel-conversions-api/)
- [Landing sahifa: ariza olib keladigan tuzilma](/blog/landing-sahifa/)
