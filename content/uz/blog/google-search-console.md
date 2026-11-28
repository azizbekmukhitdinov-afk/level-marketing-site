---
title: Google Search Console: biznes egasi uchun qo‘llanma
description: Google Search Console nima va qanday ishlatish: saytni tasdiqlash, sitemap yuborish, Samaradorlik hisoboti, indeksatsiya hisoboti va URL tekshiruvi.
date: 2026-11-28
slug: google-search-console
type: article
tags: Google Search Console, SEO, sayt, indeksatsiya
key: google-search-console
rubric: target
---

Saytingiz Google’da qaysi so‘rovlar bo‘yicha chiqyapti, nechta odam ko‘rib, nechtasi bosyapti, qaysi sahifalar umuman qidiruvga tushmagan — bularni faqat bitta bepul vosita aniq ko‘rsatadi: **Google Search Console**. Bu maqolada biznes egasi uchun eng kerakli qismlarni ko‘rib chiqamiz: tasdiqlash, sitemap, Samaradorlik hisoboti, indeksatsiya va URL tekshiruvi, hamda oyiga 20 daqiqalik tekshiruv tartibi.

## Search Console nima va nimani ko‘rsatmaydi

Search Console — Google’ning o‘zidan keladigan ma’lumot: sayt qidiruvda qanday ko‘rinadi va Google uni qanday «o‘qiydi». Analitika tizimlaridan farqi shundaki, u odam saytga kirishidan **oldingi** bosqichni ko‘rsatadi.

| Savol | Search Console | GA4 / Yandex Metrika |
|---|---|---|
| Qaysi so‘rov bo‘yicha qidiruvda chiqdik | Ha | Yo‘q (deyarli) |
| Nechta odam ko‘rdi, nechtasi bosdi | Ha | Faqat kirganlar |
| Sahifa indeksdami | Ha | Yo‘q |
| Saytda nima qildi, ariza qoldirdimi | Yo‘q | Ha |

Demak, Search Console analitikani almashtirmaydi, uni to‘ldiradi. Saytdagi harakatlar uchun [Google Analytics 4: kichik biznes sayti uchun sozlash qo‘llanmasi](/blog/google-analytics-4/) yoki [Yandex Metrika sozlash: hisoblagich, maqsadlar va Vebvizor](/blog/yandex-metrika-sozlash/) kerak. SEO’ning umumiy mantig‘i — [SEO nima: saytni Google va Yandex’da qanday ko‘tarish](/blog/seo-nima/) maqolasida.

## 1-qadam: saytni tasdiqlash

Search Console’da ikki xil «resurs» (property) bor:

| Resurs turi | Nimani qamraydi | Tasdiqlash usuli |
|---|---|---|
| Domen | Butun domen: http va https, www va subdomenlar | Faqat DNS yozuvi |
| URL-prefiks | Faqat ko‘rsatilgan manzil (masalan, https://sayt.uz/) | HTML-fayl, meta-teg, Google Analytics, Tag Manager yoki DNS |

Google yordam bo‘limiga ko‘ra, Domen resursini faqat DNS orqali tasdiqlash mumkin, qo‘lda qo‘shilgan DNS yozuvi esa ikki-uch kungacha kuchga kirishi mumkin. Tasdiqlangan holatda qolish uchun yozuvni o‘chirmaslik kerak ([Google Search Console yordami](https://support.google.com/webmasters/answer/9008080)).

**Qaror qoidasi:** domen boshqaruviga (DNS) kirish imkoningiz bo‘lsa — Domen resursini tanlang, u saytning barcha variantlarini bitta hisobotda ko‘rsatadi. Kirish bo‘lmasa yoki tez kerak bo‘lsa — URL-prefiks va meta-teg yoki Google Analytics orqali tasdiqlash.

Muhim: resurs egasi **kompaniya** Google akkaunti bo‘lsin, dasturchi yoki agentlik foydalanuvchi sifatida qo‘shiladi. Aks holda hamkorlik tugaganda tarix ham ketadi.

## 2-qadam: sitemap yuborish

Sitemap — saytdagi muhim sahifalar ro‘yxati (odatda sayt.uz/sitemap.xml). Ko‘pchilik konstruktor va CMS uni avtomatik yaratadi. Search Console’ning Sitemaps bo‘limida manzilni kiritib, yuborasiz.

Google yordam bo‘limidagi asosiy faktlar ([Sitemaps hisoboti](https://support.google.com/webmasters/answer/7451001)):

- bitta sitemap’da 50 000 tagacha URL va siqilmagan holda 50 MB gacha hajm bo‘lishi mumkin, kattaroq bo‘lsa — bir nechta faylga bo‘linadi;
- holatlar: muvaffaqiyatli, xatolar bor, yuklab bo‘lmadi;
- sitemap yuborish sahifalar albatta skanerlanishi yoki indeksga tushishini kafolatlamaydi.

Sitemap — bu Google uchun xarita, buyruq emas. Agar sahifa sifatsiz yoki takroriy bo‘lsa, u sitemap’da bo‘lsa ham indeksga tushmasligi mumkin.

## 3-qadam: Samaradorlik hisoboti

Bu hisobot biznes uchun eng foydali qism. To‘rtta ko‘rsatkich ([Google yordami](https://support.google.com/webmasters/answer/7576553)):

- **Bosishlar** — qidiruv natijasidan saytga necha marta bosilgan;
- **Ko‘rsatishlar** — sayt natijalarda necha marta ko‘ringan;
- **CTR** — bosishlar ko‘rsatishlarga bo‘lingan;
- **O‘rtacha pozitsiya** — saytning eng yuqori natijasining o‘rtacha o‘rni.

Bilish kerak bo‘lgan cheklovlar:

- Search Console ma’lumotlarni oxirgi **16 oy** davomida saqlaydi ([Google Analytics yordami](https://support.google.com/analytics/answer/13682862)) — uzoq tarix kerak bo‘lsa, oylik eksportni o‘zingiz saqlang;
- interfeysdan 1 000 qatorgacha eksport qilish mumkin; kam odam qidirgan so‘rovlar maxfiylik uchun anonimlashtiriladi va jadvalda alohida qator sifatida ko‘rinmaydi, shuning uchun qatorlar yig‘indisi umumiy grafikdan kam chiqadi ([Google Search Central blogi](https://developers.google.com/search/blog/2022/10/performance-data-deep-dive));
- eng yangi ma’lumot dastlabki bo‘lishi va bir necha soat ichida o‘zgarishi mumkin.

Hisobotdan qaror qabul qilish jadvali:

| Holat | Nimani bildiradi | Nima qilish |
|---|---|---|
| Ko‘rsatish ko‘p, CTR past | Sahifa ko‘rinadi, lekin sarlavha jalb qilmaydi | Title va description’ni qayta yozish, narx yoki foydani qo‘shish |
| Pozitsiya 8–20 | Birinchi sahifaga yaqin | Matnni boyitish, savollarga javob, ichki havolalar |
| Brend so‘rovlari ko‘p, xizmat so‘rovlari kam | Sizni bilganlar topadi, yangi mijozlar yo‘q | Xizmat sahifalari va maqolalar |
| Bosishlar keskin tushgan | Texnik muammo yoki raqobat | Indeksatsiya hisobotini tekshirish |

Qaysi so‘rovlarga e’tibor berish kerakligini tanlash — [Kalit so‘zlar tanlash: Google Ads va SEO uchun semantik yadro](/blog/kalit-sozlar-tanlash/) maqolasida.

## Shartli misol: CTR’dan arizagacha

Shartli misol. Toshkentdagi stomatologiya klinikasining «implant narxi» sahifasi oyiga 12 000 marta ko‘rsatiladi, o‘rtacha pozitsiya 6, bosishlar 180 ta, ya’ni CTR 1,5%.

Sarlavha «Implantatsiya — Klinika nomi» edi. Uni «Implant narxi Toshkentda: 2026 yil narxlari va bo‘lib to‘lash» deb o‘zgartirishdi, description’ga konsultatsiya bepul ekanini yozishdi. Keyingi oyda pozitsiya o‘zgarmagan holda CTR, deylik, 3% ga chiqdi.

| Ko‘rsatkich | Oldin | Keyin |
|---|---|---|
| Ko‘rsatishlar | 12 000 | 12 000 |
| CTR | 1,5% | 3% |
| Bosishlar | 180 | 360 |
| Sayt konversiyasi (shartli 4%) | 7 ariza | 14 ariza |

Hech qanday reklama byudjetisiz oyiga qo‘shimcha 7 ta ariza. Raqamlar shartli, lekin mantiq real: Search Console sizga qayerda «yo‘qotilgan bosishlar» borligini ko‘rsatadi. Sarlavhalarni o‘zgartirgandan keyin natijani kamida 2–4 hafta kuting — bir kunlik tebranishlar ko‘p.

## 4-qadam: indeksatsiya hisoboti

«Sahifalarni indekslash» hisoboti qaysi sahifalar Google indeksida borligini va qaysilari nima uchun yo‘qligini ko‘rsatadi. Asosiy sabablar ([Google yordami](https://support.google.com/webmasters/answer/7440203)):

| Sabab | Ma’nosi | Odatda nima qilish |
|---|---|---|
| Skanerlangan, hozircha indekslanmagan | Google ko‘rdi, lekin indeksga olmadi | Sahifa qiymatini oshirish, takrorlarni birlashtirish |
| Topilgan, hozircha skanerlanmagan | Google biladi, lekin hali kirmagan | Ichki havolalar, sitemap |
| Kanonik ko‘rsatilmagan dublikat | Boshqa sahifaning nusxasi | Kanonik sahifani belgilash |
| «noindex» bilan chiqarilgan | Sahifada indekslamaslik buyrug‘i bor | Tasodifan qo‘yilganmi — tekshirish |
| Topilmadi (404) | Sahifa yo‘q | Muhim bo‘lsa — redirekt |
| Redirektli sahifa | Boshqa manzilga yo‘naltiradi | Odatda normal |
| robots.txt bilan bloklangan | Skanerlash taqiqlangan | Taqiq kerakmi — tekshirish |

Google o‘zi yozganidek, saytdagi har bir URL indekslanishini kutmaslik kerak, lekin barcha muhim sahifalar indeksda bo‘lishi lozim. Shuning uchun «indekslanmagan» soniga emas, **muhim sahifalar** ro‘yxatiga qarang: bosh sahifa, xizmatlar, narxlar, kontaktlar, asosiy maqolalar.

Eng xavfli holat — yangi sayt chiqargandan keyin dasturchi test rejimidagi «noindex»ni olib tashlashni unutishi. Sayt yasashda bu bosqichni tekshirish ro‘yxatiga kiriting — batafsil [Biznes uchun sayt yasash: konstruktor, AI yoki dasturchi](/blog/sayt-yasash/) maqolasida.

## 5-qadam: URL tekshiruvi

Yuqoridagi qidiruv qatoriga sahifa manzilini kiritsangiz, Search Console uning holatini ko‘rsatadi. Google yordam bo‘limiga ko‘ra ([URL tekshiruvi](https://support.google.com/webmasters/answer/9012289)):

- birinchi navbatda indeksdagi versiya ko‘rsatiladi, u eskirgan bo‘lishi mumkin;
- «jonli test» sahifani hozirning o‘zida tekshiradi, lekin muvaffaqiyatli test indeksatsiyani kafolatlamaydi;
- «Indekslashni so‘rash» tugmasi bor, lekin so‘rovlarning kunlik limiti mavjud va so‘rov indeksga tushishni kafolatlamaydi;
- ko‘p yangi yoki yangilangan sahifalar uchun Google sitemap yuborishni tavsiya qiladi.

Amaliy qoida: yangi xizmat sahifasi yoki muhim o‘zgarish bo‘lsa — bitta URL uchun so‘rov yuboring. Har kuni bir xil sahifani qayta yuborish natijani tezlashtirmaydi.

## Oyiga 20 daqiqalik tekshiruv

| Har oy | Nimaga qarash |
|---|---|
| Samaradorlik | Bosishlar va ko‘rsatishlar o‘tgan oy va o‘tgan yil bilan |
| So‘rovlar | Yangi paydo bo‘lgan so‘rovlar, CTR past bo‘lgan top-10 sahifa |
| Indeksatsiya | Muhim sahifalar indeksdami, yangi xatolar bormi |
| Sitemap | Holat «muvaffaqiyatli»mi |
| Eksport | Oylik ma’lumotni jadvalga saqlash (16 oy chegarasi uchun) |

Search Console’ni Google Analytics 4 bilan ham bog‘lash mumkin — shunda qidiruv so‘rovlari va saytdagi harakatlar bitta joyda ko‘rinadi.

## Savol-javob

### Search Console reklama uchun kerakmi?

To‘g‘ridan-to‘g‘ri emas: u organik qidiruvni ko‘rsatadi. Lekin Google Ads uchun kalit so‘z tanlashda organik so‘rovlar foydali manba bo‘ladi, va aksincha — reklamada yaxshi ishlagan so‘rovlarga SEO sahifa qilish mumkin.

### Nima uchun Search Console va Analytics’da bosishlar soni farq qiladi?

Search Console qidiruv natijasidagi bosishlarni sanaydi, analitika esa saytdagi tashrifni. Odam bosib, sahifa yuklanishidan oldin chiqib ketsa yoki cookie’larni rad etsa, analitikada tashrif yozilmaydi.

### Yangi sayt qachon Google’da ko‘rinadi?

Aniq muddat yo‘q. URL tekshiruvi yordamida Google indeksatsiya odatda bir kun atrofida, ba’zan ancha uzoq davom etishini yozadi. Sitemap yuboring, muhim sahifalarga ichki havolalar qo‘ying va «noindex» yo‘qligini tekshiring.

### Yandex uchun shunday vosita bormi?

Ha, Yandex’ning o‘z vebmaster paneli bor va mantiqi o‘xshash: saytni tasdiqlash, sitemap, indeksatsiya, so‘rovlar. Agar mijozlaringiz Yandex’dan ham qidirsa, ikkalasini sozlang.

## Xulosa

Search Console — bepul va to‘g‘ridan-to‘g‘ri Google’dan keladigan ma’lumot. Bir marta sozlang: kompaniya akkauntida Domen resursi, yuborilgan sitemap, GA4 bilan bog‘lanish. Keyin oyiga 20 daqiqa: CTR past sahifalarni topish, muhim sahifalar indeksda ekanini tekshirish va ma’lumotni eksport qilish. Bu reklama byudjetisiz qo‘shimcha arizalar topishning eng arzon yo‘llaridan biri.

Level Marketing bepul audit davomida saytingiz Search Console’da qanday ko‘rinishini va qaysi sahifalar indeksdan tushib qolganini ko‘rib chiqishi mumkin.

## Shu mavzuda yana

- [SEO nima: saytni Google va Yandex’da qanday ko‘tarish](/blog/seo-nima/)
- [Kalit so‘zlar tanlash: Google Ads va SEO uchun semantik yadro](/blog/kalit-sozlar-tanlash/)
- [Trafik turlari: organik, pullik, to‘g‘ridan-to‘g‘ri va AI trafik](/blog/trafik-turlari/)
