---
title: Atributsiya oynasi Meta’da: hisobotdagi natijani qanday o‘qish
description: Atributsiya oynasi Meta’da nima: 7 kunlik bosish, 1 kunlik ko‘rish va engage-through farqi, 2026-yildagi o‘zgarishlar va hisobotni to‘g‘ri o‘qish tartibi.
date: 2026-11-07
slug: meta-atributsiya-oynasi
type: article
tags: target reklama, meta ads, atributsiya, reklama hisoboti
key: meta-atributsiya-oynasi
rubric: target
weight: 1
---

Reklama kabinetida «32 ta sotuv» deyilgan, kassada esa bu haftada reklamadan kelgan xaridor kamroq. Ko‘pincha sabab yolg‘on emas, **atributsiya oynasi**da: Meta qaysi sotuvni reklamaga «yozish» qoidasi. Bu maqolada atributsiya oynasi Meta’da qanday ishlashini, 2026-yilda nima o‘zgarganini va hisobotni qanday o‘qish kerakligini oddiy tilda tushuntiramiz.

## Atributsiya nima va «oyna» qayerdan keladi

Atributsiya — natijani (xarid, ro‘yxatdan o‘tish, savatga qo‘shish) qaysi reklamaga bog‘lash. Odam bugun reklamani ko‘radi, ertaga saytga o‘zi kiradi, uch kundan keyin xarid qiladi. Bu xarid reklama tufaylimi? Meta bunga qoida bilan javob beradi: agar odam reklama bilan ma’lum **vaqt oralig‘i** ichida aloqada bo‘lgan bo‘lsa, natija reklamaga yoziladi. Shu oraliq atributsiya oynasi deyiladi.

Oyna ikki narsadan iborat:

- **Aloqa turi** — odam reklamani bosganmi, u bilan boshqacha munosabatda bo‘lganmi (layk, saqlash, video ko‘rish) yoki faqat ko‘rganmi.
- **Muddat** — aloqadan keyin necha kun ichida bo‘lgan natija hisobga olinadi.

Muhim nuqta: atributsiya oynasi asosan **sayt konversiyalari** uchun ahamiyatli — Pixel va Conversions API orqali keladigan xarid va arizalar. Ular qanday ulanishini [Meta Pixel va Conversions API haqidagi maqolada](/blog/meta-pixel-conversions-api/) yozganmiz. Instant forma yoki Direct’ga xabar orqali kelgan ariza esa Meta ichida qayd etiladi, shuning uchun u yerda savol boshqacha — kabinet va CRM raqamlari mos kelishi.

## Meta’dagi uch xil oyna: bosish, engage-through va ko‘rish

Meta reklama to‘plami sozlamalarida (Ads Manager → reklama to‘plami → «Konversiya» bloki → atributsiya sozlamasi) uch turdagi oynani ko‘rsatadi. Aniq nomlar va variantlar kabinet tiliga va kampaniya turiga qarab farq qilishi mumkin, shuning uchun o‘z kabinetingizda tekshiring.

| Oyna | Nima hisoblanadi | Muddat variantlari |
|---|---|---|
| Bosish (click-through) | Odam reklamadagi havolani bosgan va keyin natija bo‘lgan | 1 kun yoki 7 kun |
| Engage-through | Havola emas, boshqa aloqa: layk, izoh, saqlash, ulashish, videoni bir necha soniya ko‘rish | 1 kun yoki o‘chirilgan |
| Ko‘rish (view-through) | Odam reklamani faqat ko‘rgan, bosmagan, keyin natija bo‘lgan | 1 kun yoki o‘chirilgan |

Sayt konversiyalari uchun standart sozlama odatda shunday: **7 kunlik bosish, 1 kunlik engage-through va 1 kunlik ko‘rish**. Ya’ni reklamani bosgandan keyin bir hafta ichida qilingan xarid va reklamani faqat ko‘rgandan keyin bir sutka ichidagi xarid reklamaga yoziladi.

## 2026-yilda nima o‘zgardi

Agar kabinetingizdagi raqamlar o‘tgan yilgi hisobotlar bilan solishtirganda «tushib ketgan» bo‘lsa, bunga ikki o‘zgarish sabab bo‘lishi mumkin.

**1. Uzun «ko‘rish» oynalari olib tashlandi.** Meta dasturchilar blogida 2025-yil oktyabrda e’lon qilganidek, [12-yanvar 2026-yildan Ads Insights API 7 kunlik va 28 kunlik ko‘rish oynalarini qaytarmaydi](https://developers.facebook.com/blog/post/2025/10/16/ads-insights-api-metric-availability-updates/). Endi eng uzun ko‘rish oynasi — 1 kun. Ilgari 28 kunlik ko‘rish bilan hisobot olgan bo‘lsangiz, eski va yangi davr raqamlarini to‘g‘ridan-to‘g‘ri solishtirib bo‘lmaydi.

**2. «Bosish» tor ma’noda tushuniladigan bo‘ldi.** 2026-yil mart oyida Meta [bosish atributsiyasini faqat havola bosishlari bilan cheklashini e’lon qildi](https://searchengineland.com/meta-introduces-click-and-engage-through-attribution-updates-470629): layk, saqlash yoki ulashish endi «bosish» hisoblanmaydi. Havola bosishiga sayt havolasi, qo‘ng‘iroq, xabar yozish, lid-forma kabi tugmalar kiradi. Qolgan aloqalar yangi **engage-through** turiga o‘tdi — u eski «engaged-view» (videoni ko‘rish) o‘rnini egalladi va endi barcha formatlarga tegishli.

Amaliy xulosa: o‘tgan yilgi va bu yilgi «bosishdan keyingi sotuvlar»ni yonma-yon qo‘yganda ular bir xil narsani o‘lchamaydi. Taqqoslashda shu sanalarni hisobotga izoh qilib yozib qo‘ying.

## Hisobotni qanday o‘qish: 5 qadam

### 1. Avval qaysi oyna ishlatilganini bilib oling

Ads Manager’dagi «Natijalar» ustuni reklama to‘plamining atributsiya sozlamasi bo‘yicha hisoblanadi. Hisobotni ochganda, avvalo reklama to‘plamini tahrirlash oynasida sozlamani tekshiring. Turli to‘plamlarda turli oyna bo‘lsa, ularni bir jadvalda solishtirish xato.

### 2. «Atributsiya sozlamalarini solishtirish» ustunlarini qo‘shing

Ads Manager’da ustunlarni sozlashda **Compare attribution settings** (atributsiya sozlamalarini solishtirish) bo‘limi bor. U bir xil natijani oynalar bo‘yicha alohida ko‘rsatadi: 1 kunlik bosish, 7 kunlik bosish, 1 kunlik ko‘rish va boshqalar. Shu ustunlar bilan bitta jadvalda ko‘rasiz: sotuvlarning qanchasi bosishdan, qanchasi faqat ko‘rishdan kelgan.

### 3. Ko‘rishdan kelgan ulushga qarang

Agar natijalarning katta qismi faqat **ko‘rishdan** kelayotgan bo‘lsa, ehtiyot bo‘ling. Bu odamlar reklamani ko‘rgan va baribir xarid qilishi mumkin edi — masalan, sizni allaqachon biladigan doimiy mijozlar. Ayniqsa [retargeting](/blog/retargeting-qanday-ishlaydi/) kampaniyalarida ko‘rish oynasi natijani bo‘rttirib ko‘rsatishi mumkin, chunki bu auditoriya saytingizga baribir qaytadi.

### 4. Natijani CRM va kassa bilan solishtiring

Kabinet — reklamaning o‘z «ko‘zi». Haqiqiy pul esa CRM’da va kassada. Har hafta kabinetdagi xaridlar sonini CRM’dagi reklama manbali sotuvlar bilan solishtiring. Manbani aniqlash uchun [UTM-belgilar](/blog/utm-belgilar/) va «bizni qayerdan bildingiz» savoli yordam beradi. Farq doim bo‘ladi; muhimi — u har hafta taxminan bir xil bo‘lishi. Agar birdan oshib ketsa, sababini [kabinet va CRM mos kelmasligi haqidagi tekshiruv](/blog/kabinet-va-crm-lidlar/) bo‘yicha qidiring.

### 5. Bitta oynada qoling

Hisobot uchun bitta asosiy oynani tanlang va oylar davomida uni o‘zgartirmang. Agar o‘zgartirsangiz, o‘zgarish sanasini yozib qo‘ying: undan oldingi va keyingi raqamlarni solishtirib bo‘lmaydi. Agentlik hisobotida ham qaysi oyna ishlatilgani yozilgan bo‘lishi kerak — bu haqda [reklama hisobotida qanday raqamlar bo‘lishi shart](/blog/reklama-hisoboti/) maqolasida batafsil.

## Qaysi oynani tanlash: biznes turiga qarab

Bitta to‘g‘ri javob yo‘q — oyna mijozning qaror qabul qilish tezligiga mos bo‘lishi kerak.

| Biznes | Qaror tezligi | Mantiqiy boshlang‘ich |
|---|---|---|
| Kiyim, kosmetika, aksessuar onlayn do‘koni | Bir-ikki kun | 1 kunlik bosish + 1 kunlik ko‘rish, 7 kunlik bosishni solishtirish ustunida kuzatish |
| Mebel, maishiy texnika | Bir necha kundan bir haftagacha | 7 kunlik bosish + 1 kunlik ko‘rish |
| Ko‘chmas mulk, avtomobil, o‘quv kursi | Haftalar | 7 kunlik bosish; asosiy natija — ariza, sotuvni CRM’da kuzatish |
| Ariza instant forma yoki Direct orqali | Ariza Meta ichida | Oyna kam ta’sir qiladi; ariza sifatini CRM’da tekshiring |

*Shartli misol:* Toshkentdagi mebel do‘koni saytdan xarid qilish uchun reklama beradi. Kabinet 7 kunlik bosish + 1 kunlik ko‘rish bo‘yicha haftada 30 ta xarid ko‘rsatadi. Solishtirish ustunlarida ko‘rinadiki, 18 tasi 1 kunlik bosishdan, 7 tasi 2–7 kun ichidagi bosishdan, 5 tasi faqat ko‘rishdan. Demak, ishonch bilan reklamaga 25 ta xaridni bog‘lash mumkin, 5 tasi esa — «reklama ta’sir qilgan bo‘lishi mumkin» toifasi. [ROMI hisoblashda](/blog/romi-hisoblash/) ehtiyotkor variant uchun 25 ni, optimistik variant uchun 30 ni olish mumkin.

## 5 ta keng tarqalgan xato

1. **Turli oynalardagi raqamlarni solishtirish.** Bir to‘plam 7 kunlik bosishda, boshqasi 1 kunlikda — «qaysi biri yaxshi?» degan savolga bu jadval javob bermaydi.
2. **Kabinet raqamini haqiqiy sotuv deb qabul qilish.** Meta va Google Analytics, CRM turli qoidalar bilan hisoblaydi. Bir xil xarid ikki tizimda ikki marta «reklamaniki» bo‘lishi ham mumkin.
3. **Ko‘rish oynasini butunlay e’tiborsiz qoldirish.** Ko‘rish natijasi «yolg‘on» emas — video reklama yoki brendni tanitish kampaniyalarida u ta’sirning bir qismini ko‘rsatadi. Uni alohida qatorda ko‘ring, lekin asosiy KPI qilmang.
4. **Natija «yomon» bo‘lgani uchun oynani o‘zgartirish.** Oynani kengaytirsangiz, raqam o‘sadi, lekin sotuv o‘smaydi. Natija pasaysa, avval kreativ, auditoriya va [o‘rganish bosqichi](/blog/learning-limited-meta/)ni tekshiring.
5. **2026-yil o‘zgarishlarini hisobga olmaslik.** Yanvar va mart o‘zgarishlaridan oldingi davr bilan solishtirsangiz, «reklama yomonlashdi» degan xato xulosaga kelish oson.

## Savol-javob

**Atributsiya oynasini o‘zgartirsam, reklama yaxshiroq ishlaydimi?**
Oyna sotuvni ko‘paytirmaydi, faqat qaysi sotuv reklamaga yozilishini o‘zgartiradi. Lekin konversiyaga optimallashtirilgan reklamada Meta tizimi shu oynadagi natijalardan o‘rganadi, shuning uchun oyna xaridor qaror qilish tezligiga mos bo‘lgani yaxshi.

**28 kunlik oyna endi umuman yo‘qmi?**
28 va 7 kunlik ko‘rish oynalari 2026-yil yanvaridan hisobotlarda qaytarilmaydi. 28 kunlik bosish esa optimallashtirish sozlamasi sifatida mavjud emas; ba’zi hisobot va solishtirish vositalarida ko‘rinishi mumkin — o‘z kabinetingizda tekshiring.

**Instant forma bilan ishlasam, oyna muhimmi?**
Kamroq. Forma Meta ichida to‘ldiriladi va ariza darhol reklamaga yoziladi. U yerda asosiy savol — arizalar sifati va ularning CRM’ga to‘liq yetib kelishi.

**Google Analytics boshqa raqam ko‘rsatyapti. Qaysi biri to‘g‘ri?**
Ikkalasi ham o‘z qoidasi bo‘yicha to‘g‘ri. Google Analytics odatda ko‘rishni hisoblamaydi va sotuvni oxirgi manbaga bog‘laydi. Bitta tizimni asosiy deb belgilab, ikkinchisini nazorat uchun ishlating.

## Xulosa

Atributsiya oynasi — bu reklama natijasini o‘lchaydigan «chizg‘ich». Chizg‘ichni bilmasangiz, raqamlar aldaydi: bir hisobotda 30 ta sotuv, boshqasida 20 ta, haqiqatda esa bir xil hafta. Qaysi oyna ishlatilganini tekshiring, bosish va ko‘rishni alohida ko‘ring, kabinetni CRM bilan solishtiring va 2026-yil o‘zgarishlarini hisobotda belgilab qo‘ying.

Kabinet va kassadagi raqamlar mos kelmasa, Level Marketing jamoasi reklama hisobotingizni ko‘rib chiqib, biznesingizga qaysi oyna mos kelishini tushuntirib beradi.

## Shu mavzuda yana

- [Learning limited nima: Meta reklamasi nega beqaror ishlaydi](/blog/learning-limited-meta/)
- [Retargeting: sotib olmaganlarni qanday qaytarish mumkin](/blog/retargeting-qanday-ishlaydi/)
- [Instant forma yoki Direct'ga xabar: qaysi biri ko‘proq sotuv olib keladi](/blog/instant-forma-yoki-xabarlar/)
