---
title: Meta Pixel va Conversions API: 2026 uchun o‘rnatish qo‘llanmasi
description: Meta Pixel va Conversions API qanday o‘rnatiladi, qaysi hodisalarni kuzatish kerak va 12-noyabrdan hisobotda nima o‘zgaradi: 2026 uchun qo‘llanma.
date: 2026-10-22
updated: 2026-11-09
slug: meta-pixel-conversions-api
type: article
tags: target reklama, meta ads
key: meta-pixel-conversions-api
rubric: target
---

Reklama sotuv olib kelyaptimi yoki shunchaki bosishlarmi? Bu savolga aniq javobni faqat kuzatuv beradi. Meta reklamasida kuzatuvning ikki vositasi bor: **Meta Pixel** va **Conversions API**. Ushbu maqolada ular nima uchun kerakligini, qaysi hodisalarni kuzatish kerakligini va 2026-yil noyabridan hisobotlarda nima o‘zgarishini ko‘rib chiqamiz.

![Meta Pixel nima](/img/blog/illus/meta-pixel-conversions-api-1.jpg 1200x675)

## Meta Pixel nima

Pixel — saytingizga qo‘yiladigan kichik kod. U tashrif buyuruvchi saytda nima qilganini — sahifani ko‘rgani, formani yuborgani, xarid qilganini — Meta'ga yuboradi. Natijada:

- reklama kabinetida qaysi reklama ariza va sotuv olib kelganini ko‘rasiz;
- algoritm aynan shu harakatni qiladigan odamlarni qidirishni o‘rganadi;
- saytga kirgan, lekin sotib olmaganlar uchun [retargeting](/blog/retargeting-qanday-ishlaydi/) auditoriyasini yaratasiz.

## Conversions API nima va nega Pixel yetmaydi

Pixel brauzer orqali ishlaydi. Reklama blokerlari, iOS cheklovlari va cookie sozlamalari tufayli hodisalarning bir qismi Meta'ga yetib bormaydi. **Conversions API (CAPI)** xuddi shu hodisalarni sizning serveringizdan yuboradi. Ikkalasi birga ishlaganda Meta ma'lumotni to‘liqroq oladi, bir xil hodisaning ikki nusxasi esa `event_id` orqali birlashtiriladi (deduplikatsiya).

## 2026-yilda Meta Pixel va Conversions API'da nima o‘zgardi

2026-yilda uchta o‘zgarish kuzatuvga bevosita ta'sir qiladi. Eng shoshilinchi — birinchisi.

**1. Konversiyalarni mijoz qurilmasida o‘lchash.** Pixel sozlamalarida **Measure conversions on customer devices** degan yangi tugma paydo bo‘ldi. U reklama ko‘rilishini xarid bilan to‘g‘ridan to‘g‘ri mijozning qurilmasida solishtiradi: mijoz biznesga bergan ma'lumot (masalan, email) va vaqtinchalik qurilma ma'lumotlari ishlatiladi. Meta buni [yordam markazida](https://www.facebook.com/business/help/4237575203200036) tushuntirgan. Mos Pixel'larda sozlama sukut bo‘yicha yoqilgan. Yevropa Ittifoqi va Buyuk Britaniyadagi odamlar uchun ishlamaydi, O‘zbekiston bu istisnoga kirmaydi. Events Manager panelida o‘lchash boshlanadigan sana sifatida [2026-yil 12-noyabr](https://ppc.land/meta-pixel-will-count-more-conversions-from-nov-12-unless-advertisers-opt-out/) ko‘rsatilmoqda, Meta yordam sahifalarida esa sana yo‘q — shuning uchun o‘z kabinetingizni tekshiring.

**2. Bir bosishda Conversions API.** 2026-yil aprelida Meta [dasturchisiz ulanadigan variantni](https://www.facebook.com/business/news/pixel-conversionsapi-updates) e'lon qildi. Unda Pixel yuborgan hodisalar serverdan ham avtomatik yuboriladi va dublikatlar birlashtiriladi.

**3. Pixel'dagi AI-funksiya.** Pixel sahifa va mahsulot haqidagi ma'lumotni (nomlar, mavjudligi, biznes ma'lumotlari) hodisalarga o‘zi qo‘sha oladi. Uni Events Manager'da o‘chirish yoki qaysi toifalar yuborilishini tanlash mumkin.

### Yangi sozlama saytingizga tegishlimi

Meta yordam markaziga tayangan sharhlarga ko‘ra, funksiya ishlashi uchun ikki shart kerak: Pixel to‘g‘ridan to‘g‘ri sahifada turishi (iframe ichida yoki faqat rasm-Pixel emas) va saytga email yoki telefon raqami bilan kirish majburiy bo‘lishi.

| Sayt turi | Sozlama ishlaydimi | Nima qilish kerak |
|---|---|---|
| Lending yoki forma, akkauntsiz | Yo‘q | Hisobot o‘zgarmaydi, Conversions API'ni ulang |
| Akkauntsiz xarid qilinadigan do‘kon | Shart bajarilmaydi | Settings'da holatini tekshiring |
| Email yoki telefon bilan kirish majburiy do‘kon | Ha, sukut bo‘yicha | Quyidagi 4 qadamni bajaring |
| Pixel iframe ichida yoki rasm ko‘rinishida | Yo‘q | Kodni to‘g‘ridan to‘g‘ri sahifaga qo‘ying, agar bu funksiya kerak bo‘lsa |
| Sayt yo‘q, faqat Direct va Telegram | Yo‘q | CRM yoki jadvalda sotuvni yozib boring |

### 12-noyabrgacha 4 qadam

1. **Holatni ko‘ring.** Events Manager → Data sources → Pixel'ingiz → Settings. Sozlama bormi, yoqilganmi?
2. **Bazaviy ko‘rsatkichni yozib qo‘ying.** Oxirgi 2–4 hafta uchun kabinetdagi xaridlar soni, xarid narxi, ROAS va CRM'dagi haqiqiy sotuvlar.
3. **Hisobotga sanani belgilang.** O‘lchash qachon boshlanganini yozib qo‘ying — keyin kim «reklama yaxshilandi» desa, shu belgiga qaraysiz.
4. **Kabinetni CRM bilan solishtiring.** Kabinetda xaridlar ko‘paydi-yu, CRM va kassada o‘zgarmadi — demak, o‘lchash o‘zgargan, reklama emas. Bu solishtirish qanday qilinishi — [kabinet va CRM farqi](/blog/kabinet-va-crm-lidlar/) maqolasida.

Atributsiya oynasi va modeli o‘zgarmaydi — o‘zgaradigani o‘lchana oladigan konversiyalar doirasi. [Atributsiya oynasi](/blog/meta-atributsiya-oynasi/) qanday ishlashini bilish hisobotni to‘g‘ri o‘qishga yordam beradi. Natijada xarid narxi pastroq, ROAS esa yuqoriroq ko‘rinishi mumkin, haqiqiy sotuv o‘sishi shart emas.

## Qaysi hodisalarni kuzatish kerak

| Hodisa | Qachon ishga tushadi | Kimga muhim |
|---|---|---|
| PageView | Har bir sahifa ochilganda | Hammaga |
| ViewContent | Mahsulot yoki xizmat sahifasi | Do‘konlar, xizmatlar |
| Lead | Forma yuborilganda | Xizmat ko‘rsatuvchi bizneslar |
| Contact | Telegram yoki qo‘ng‘iroq tugmasi bosilganda | Kichik biznes |
| InitiateCheckout | Buyurtma rasmiylashtirila boshlanganda | Onlayn do‘kon |
| Purchase | Xarid yakunlanganda | Onlayn do‘kon |

## Qanday o‘rnatiladi: 5 qadam

1. **Events Manager**'da (business.facebook.com) **Connect Data → Web** orqali Pixel yarating yoki mavjudini tanlang.
2. Kodni saytga qo‘shing. Tilda, WordPress yoki Shopify kabi konstruktorlarda tayyor integratsiya bor; o‘zingiz yozgan saytda kod sahifa boshiga yoki Google Tag Manager orqali qo‘yiladi.
3. Asosiy hodisalarni sozlang: kamida Lead yoki Purchase, kichik biznes uchun Contact ham.
4. **Conversions API**'ni ulang. Eng oddiy yo‘l — Connect Data → Web → Pixel'ni tanlang → See other ways to setup → **Set up with Meta**: bepul va dasturchisiz. Hodisalarni o‘zingiz tanlamoqchi bo‘lsangiz — platforma integratsiyasi, Google Tag Manager server konteyneri yoki dasturchi.
5. **Test Events** bo‘limida tekshiring: har bir hodisa kelyaptimi va moslik sifati (Event Match Quality) qanday.

## Ko‘p uchraydigan xatolar

- Pixel saytga ikki marta o‘rnatilgan — hodisalar ikki baravar hisoblanadi.
- Lead hodisasi «Rahmat» sahifasida emas, forma sahifasining o‘zida ishga tushadi — har bir tashrif ariza bo‘lib ko‘rinadi.
- Domen Business Manager'da tasdiqlanmagan.
- Kampaniya maqsadi bilan optimallashtirish hodisasi mos kelmaydi.

![Saytingiz bo‘lmasa-chi](/img/blog/illus/meta-pixel-conversions-api-2.jpg 1200x675)

## Saytingiz bo‘lmasa-chi

Ko‘p bizneslar Instagram Direct yoki Telegram orqali sotadi. Bunda Pixel kerak emas, lekin sotuvni qayd qilish baribir zarur: arizalarni CRM yoki jadvalda belgilang va qaysi reklama sotuv olib kelganini solishtiring. Ariza narxini qanday hisoblash haqida — [CPL bo‘yicha qo‘llanmamizda](/blog/lid-narxi-cpl-qanday-kamaytirish/).

## Hodisalarni qanday tekshirish

- **Events Manager → Test Events.** Saytingizni ochib, formani yuboring va hodisa real vaqtda paydo bo‘layotganini ko‘ring.
- **Meta Pixel Helper.** Chrome brauzeri uchun kengaytma — sahifada qaysi hodisalar ishlayotganini ko‘rsatadi.
- **Dublikatlar.** Pixel va Conversions API birga ishlasa, bir hodisa ikki marta sanalmasligi uchun ikkalasida bir xil event_id va bir xil hodisa nomi bo‘lishi kerak. Meta ularni birinchi hodisa kelganidan keyin [48 soat ichida](https://developers.facebook.com/docs/marketing-api/conversions-api/deduplicate-pixel-and-server-events/) birlashtiradi. Bir bosishli variantda buni Meta o‘zi qiladi.
- **Moslik sifati.** Events Manager'da hodisalarning foydalanuvchilar bilan qanchalik yaxshi moslashganini ko‘rsatuvchi baho bor — u past bo‘lsa, Conversions API orqali qo‘shimcha ma'lumot (masalan, xeshlangan telefon) yuboring.

## Hodisa parametrlari

Purchase va Lead hodisalariga **qiymat** (value) va **valyuta** (currency) qo‘shing. Shunda Meta qaysi reklama ko‘proq pul olib kelayotganini ko‘radi va qimmatroq mijozlarga optimallashtira oladi. Katalog bilan ishlaydigan do‘konlar uchun mahsulot identifikatorlari (content_ids) ham kerak — ular dinamik retargetingni ishga tushiradi.

## Maxfiylik va rozilik

Sayt foydalanuvchilarini maxfiylik siyosatida ma'lumot yig‘ish haqida xabardor qiling. Hodisalar orqali sezgir ma'lumot yubormang: tibbiy holatlar, moliyaviy ahvol va boshqalar. Ayniqsa klinikalar ehtiyot bo‘lishi kerak — sahifa manzili yoki hodisa nomi kasallikni oshkor qilmasin. Bir bosishli Conversions API Pixel yuborgan hamma narsani takrorlaydi va alohida filtr bermaydi, Pixel'ning AI-funksiyasi esa sahifa ma'lumotini qo‘shadi. Shuning uchun klinika va moliya saytlari ikkalasini yoqishdan oldin nima yuborilayotganini tekshirsin. Bu mas'uliyat reklama beruvchida qoladi. Klinikalar marketingi haqida — [klinika marketingi](/blog/klinika-marketing/) maqolasida.

![Pixel ma'lumotlaridan qanday foydalanish](/img/blog/illus/meta-pixel-conversions-api-3.jpg 1200x675)

## Pixel ma'lumotlaridan qanday foydalanish

- Kampaniyalarni bosishga emas, **Lead** yoki **Purchase** hodisasiga optimallashtiring.
- Saytga kirganlar uchun [retargeting](/blog/retargeting-qanday-ishlaydi/) auditoriyalarini yarating.
- Arizachi va xaridorlardan [lookalike auditoriya](/blog/lookalike-auditoriya/) quring.
- Hisobotlarda qaysi kreativ ariza berayotganini ko‘ring.

## Savol-javob

### Pixel o‘rnatish uchun dasturchi kerakmi?

Ko‘p sayt konstruktorlari va CMS'larda Meta bilan tayyor integratsiya bor — Pixel ID'ni kiritish yetarli. Conversions API'ni endi Events Manager'dagi **Set up with Meta** orqali dasturchisiz ulash mumkin. Dasturchi faqat hodisalarni alohida tanlash, ilova yoki oflayn hodisalarni yuborish kerak bo‘lganda zarur.

### Bitta saytga bir nechta Pixel qo‘ysa bo‘ladimi?

Texnik jihatdan mumkin, lekin chalkashlik keltiradi. Bitta biznesga bitta Pixel yaxshiroq; agentlikka esa Business Manager orqali kirish huquqi bering.

### Pixel auditoriyalari qancha vaqt saqlanadi?

Sayt tashrif buyuruvchilari auditoriyasi uchun eng uzun muddat — 180 kun. Shuning uchun Pixel'ni reklama boshlanishidan ancha oldin o‘rnating: ma'lumot yig‘ila boshlaydi.

### Conversions API'siz ishlasa bo‘ladimi?

Boshlash uchun — ha. Lekin brauzer cheklovlari va reklama bloklovchilar tufayli ma'lumotlarning bir qismi yo‘qoladi. Endi ulash bepul va bir necha daqiqa olgani uchun kechiktirishga sabab kam. Meta'ning o‘z ma'lumotiga ko‘ra, web-hodisalar uchun Conversions API ishlatadigan reklama beruvchilarda natija narxi [o‘rtacha 17,8% past](https://www.facebook.com/business/news/pixel-conversionsapi-updates) — bu o‘rtacha ko‘rsatkich, kafolat emas.

### Hodisalar kabinetda ko‘rinmasa nima qilish kerak?

Kod barcha sahifalarda o‘rnatilganini, to‘g‘ri Pixel ID ishlatilganini va reklama bloklovchi o‘chirilganini tekshiring. Test Events orqali hodisani qayta yuboring — hodisalar biroz kechikish bilan ko‘rinishi mumkin.

### Qurilmada o‘lchash sozlamasini o‘chirish kerakmi?

Majburiy emas. Meta uni kabinetda ko‘proq konversiya ko‘rsatish va signalni kuchaytirish uchun yoqib qo‘yishni tavsiya qiladi. Lekin hisobotingiz ROAS'ga bog‘liq bo‘lsa va aksiya davrida taqqoslash buzilmasligi muhim bo‘lsa, uni vaqtincha o‘chirib turish mumkin — tugma har bir Pixel uchun alohida va istalgan vaqtda o‘zgartiriladi. Qaysi yo‘lni tanlasangiz ham, sanani [hisobotda](/blog/reklama-hisoboti/) yozib qo‘ying.

### Conversions API allaqachon ulangan bo‘lsa, bir bosishli variantga o‘tish kerakmi?

Yo‘q. Meta'ning aytishicha, hamkor yoki o‘z server integratsiyasi bor reklama beruvchilar hech narsani o‘zgartirmasa bo‘ladi. Yangi sozlama ham Pixel va Conversions API o‘rnini bosmaydi, ular bilan birga ishlaydi.

### Pixel o‘rnatilgach, reklama darhol yaxshilanadimi?

Darhol emas. Algoritm o‘rganishi uchun yetarlicha hodisa to‘planishi kerak — yangi kampaniya odatda bir necha kun «o‘rganish bosqichida» bo‘ladi. Bu davrda sozlamalarni tez-tez o‘zgartirmang, aks holda o‘rganish qaytadan boshlanadi. Natijani kamida bir haftadan keyin baholang.

## Xulosa

Pixel va Conversions API — reklamaning «ko‘zi». Ularsiz algoritm qorong‘ida ishlaydi, siz esa arzon, lekin sotuvga aylanmaydigan arizalar uchun pul to‘laysiz. Noyabrdan esa kabinetdagi raqamlarni CRM bilan solishtirish yana ham muhim: raqam o‘sishi har doim ham sotuv o‘sishi emas. Level Marketing har bir loyihada kuzatuvni birinchi haftada sozlaydi.

## Shu mavzuda yana

- [Atributsiya oynasi Meta’da: hisobotdagi natijani qanday o‘qish](/blog/meta-atributsiya-oynasi/)
- [Retargeting: sotib olmaganlarni qanday qaytarish mumkin](/blog/retargeting-qanday-ishlaydi/)
- [Instagram'da target reklama qanday sozlanadi: bosqichma-bosqich qo‘llanma](/blog/instagramda-target-reklama-sozlash/)
