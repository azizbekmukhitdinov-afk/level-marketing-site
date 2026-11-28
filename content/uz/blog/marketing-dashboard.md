---
title: Marketing dashboard: biznes egasi uchun bir sahifalik panel
description: Marketing dashboard qanday tuziladi: voronka bosqichlari bo‘yicha metrikalar, manbalar kesimi, haftalik va oylik ritm, Google Sheets va Looker Studio’da yig‘ish.
date: 2026-11-28
slug: marketing-dashboard
type: article
tags: dashboard, analitika, Looker Studio, Google Sheets, KPI
key: marketing-dashboard
rubric: biznes
---

Rahbar odatda raqamlarni uch joydan oladi: reklama kabinetidan, CRM’dan va menejerning og‘zaki «hafta yaxshi o‘tdi» degan gapidan. Ular bir-biriga mos kelmaydi va qaror sezgi bo‘yicha qabul qilinadi. Marketing dashboard — bu reklamadan to‘lovgacha bo‘lgan yo‘lni bitta sahifada ko‘rsatadigan panel. Bu maqolada unda qaysi metrikalar bo‘lishi, qaysi ritmda qarash va Google Sheets hamda Looker Studio’da qanday yig‘ish kerakligini ko‘rib chiqamiz.

## Dashboard va hisobotning farqi

Hisobot o‘tgan davrni tushuntiradi: nima bo‘ldi, nega va keyingi oy nima qilamiz. Dashboard esa hozirgi holatni ko‘rsatadi va savolga tez javob beradi: «reja bo‘yicha ketyapmizmi, qayerda muammo bor?». Hisobot oyiga bir marta o‘qiladi, dashboard esa har kuni yoki har hafta ochiladi.

Shuning uchun dashboard qisqa bo‘lishi kerak. Agar unda 40 ta ko‘rsatkich bo‘lsa, rahbar uni ochmay qo‘yadi. Yaxshi panelda 8–12 ta raqam bor, har biri reja bilan solishtirilgan va har biri bo‘yicha kim mas’ul ekani ma’lum. Hisobot tuzilmasi haqida — [reklama hisoboti](/blog/reklama-hisoboti/) maqolasida, umumiy ko‘rsatkichlar haqida — [KPI nima](/blog/kpi-nima/) maqolasida.

## Voronka bosqichlari bo‘yicha metrikalar

Dashboard’ni voronka bo‘yicha qurish eng oson: yuqoridan pastga, puldan pulga. Har bosqichda bitta asosiy raqam va bitta nisbat yetarli.

| Bosqich | Asosiy raqam | Nisbat | Manba |
|---|---|---|---|
| Reklama | Sarf | CPM yoki CPC | Reklama kabineti |
| Qiziqish | Arizalar soni | CPL = sarf ÷ arizalar | Kabinet va CRM |
| Sifat | Sifatli arizalar | Sifatli ulush, % | CRM |
| Aloqa | Javob berilgan arizalar | Javob vaqti, daqiqa | CRM |
| Uchrashuv yoki konsultatsiya | Uchrashuvlar | Arizadan uchrashuvga, % | CRM |
| Sotuv | Sotuvlar va tushum | CAC = sarf ÷ sotuvlar | CRM yoki kassa |
| Foyda | Yalpi foyda | ROMI | Hisob-kitob |

Eng muhim qoida: **arizalar sonini kabinetdan emas, CRM’dan oling**, kabinetdagi raqamni esa yonida solishtirish uchun qoldiring. Agar ular bir necha foizdan ko‘proq farq qilsa, ulanishda muammo bor — sabablarini [kabinet va CRM mos kelmasa](/blog/kabinet-va-crm-lidlar/) maqolasida qidiring. ROMI qanday hisoblanishi [ROMI](/blog/romi-hisoblash/) maqolasida yozilgan.

## Manbalar bo‘yicha kesim

Umumiy raqamlar yaxshi bo‘lsa ham, bitta kanal boshqalarning pulini «yeb» qo‘yishi mumkin. Shuning uchun dashboard’da ikkinchi jadval — manbalar kesimi kerak. Har bir ariza CRM’da manba bilan yozilishi uchun reklama havolalariga [UTM-belgilar](/blog/utm-belgilar/) qo‘ying va lid-formalardan kelgan ma’lumotda kampaniya nomini saqlang.

Kesimda besh ustun yetarli: sarf, arizalar, CPL, sotuvlar, CAC. Asosiy xulosa odatda CPL va CAC solishtirilganda chiqadi: eng arzon ariza har doim ham eng arzon sotuv emas.

## Qaysi ritmda qarash kerak

Har bir raqamga har kuni qarash shart emas. Aksincha, kunlik tebranishlarga reaksiya qilish ko‘pincha zarar keltiradi: reklama algoritmi o‘rganish uchun vaqt talab qiladi.

| Ritm | Kim qaraydi | Nimaga qaraydi | Qaror |
|---|---|---|---|
| Har kuni, 5 daqiqa | Sotuv rahbari | Yangi arizalar, javobsiz arizalar, javob vaqti | Kim kimga qo‘ng‘iroq qiladi |
| Har hafta, 30 daqiqa | Rahbar + marketolog | Sarf, CPL, sifatli ulush, uchrashuvlar, reja bo‘yicha foiz | Kreativ almashtirish, byudjetni ko‘chirish |
| Har oy, 1–2 soat | Rahbar + jamoa | Sotuvlar, CAC, ROMI, manbalar kesimi, reja va fakt | Keyingi oy rejasi va byudjet |

Level Marketing’da oylik natija mijoz ofisida taqdim etiladi: reja va fakt yonma-yon ko‘rsatiladi va keyingi oy rejasi shu raqamlar asosida kelishiladi. Haftalik dashboard esa oy oxirida kutilmagan holat bo‘lmasligi uchun kerak.

## Qayerda yig‘ish: Google Sheets va Looker Studio

Kichik biznes uchun ikki bosqichli yechim yetarli: ma’lumotlar Google Sheets’da, ko‘rinish Looker Studio’da. Looker Studio’ning [bepul versiyasi](https://docs.cloud.google.com/looker/docs/studio/about-looker-studio-pro-content) bor, pullik Pro versiyasi esa asosan kompaniya darajasida boshqaruv va jamoa funksiyalarini qo‘shadi.

**Sheets tuzilmasi.** Uchta varaq qiling:

- **«Xom ma’lumot»** — har qatorda bitta kun va bitta manba: sana, manba, sarf, arizalar, sifatli arizalar, uchrashuvlar, sotuvlar, tushum. Bu yerga ma’lumot qo‘lda yoki avtomatik tushadi.
- **«Reja»** — oy bo‘yicha har bir ko‘rsatkich uchun maqsad.
- **«Panel»** — formulalar bilan hafta va oy yig‘indilari, reja bo‘yicha foiz.

Looker Studio’ga ulash uchun Google’ning [Sheets konnektori bo‘yicha qo‘llanmasi](https://docs.cloud.google.com/looker/docs/studio/connect-to-google-sheets) ma’lumot jadval ko‘rinishida bo‘lishini, bitta sarlavha qatori va har bir ustunda bir xil turdagi qiymatlar bo‘lishini talab qiladi. Shuning uchun «Xom ma’lumot» varag‘ida birlashtirilgan katakchalar, oraliq yig‘indilar va izohlar bo‘lmasin.

**Yangilanish tezligi.** Google [hujjatlariga](https://docs.cloud.google.com/looker/docs/studio/manage-data-freshness) ko‘ra, Looker Studio Sheets ma’lumotini sukut bo‘yicha har 15 daqiqada, Google Analytics ma’lumotini esa har 12 soatda yangilaydi. Demak, Analytics’dan olingan raqamlar kunlik nazorat uchun emas, haftalik tahlil uchun mos. Saytda Analytics’ni sozlash haqida — [Google Analytics 4](/blog/google-analytics-4/) qo‘llanmasida.

Meta reklama raqamlarini eng oddiy yo‘l bilan — Ads Manager’dan haftalik eksport qilib «Xom ma’lumot» varag‘iga qo‘shish mumkin. Bu jarayonni keyinroq avtomatlashtirish mumkin; qanday — [marketing avtomatlashtirish](/blog/marketing-avtomatlashtirish/) maqolasida.

## Shartli misol: bir haftalik panel

Quyidagi raqamlar shartli misol, real kompaniya emas. Biznes konsultatsiya orqali sotadi, o‘rtacha chek 3 000 000 so‘m, yalpi marja 30%.

| Ko‘rsatkich | Fakt | Reja | Reja bo‘yicha |
|---|---|---|---|
| Sarf | 6 000 000 so‘m | 6 000 000 so‘m | 100% |
| Arizalar | 400 | 380 | 105% |
| CPL | 15 000 so‘m | 15 800 so‘m | yaxshi |
| Sifatli arizalar | 240 (60%) | 65% | past |
| Konsultatsiyalar | 60 | 70 | 86% |
| Sotuvlar | 18 | 20 | 90% |
| Tushum | 54 000 000 so‘m | 60 000 000 so‘m | 90% |

CAC = 6 000 000 ÷ 18 ≈ 333 000 so‘m. Yalpi foyda = 54 000 000 × 0,3 = 16 200 000 so‘m. ROMI = (16 200 000 − 6 000 000) ÷ 6 000 000 = 170%.

Manbalar kesimi:

| Manba | Sarf | Arizalar | CPL | Sotuvlar | CAC |
|---|---|---|---|---|---|
| Meta | 4 000 000 | 320 | 12 500 | 11 | ~364 000 |
| Google qidiruv | 2 000 000 | 80 | 25 000 | 7 | ~286 000 |

Faqat CPL’ga qarasangiz, Google ikki baravar qimmat ko‘rinadi. Lekin bitta sotuv narxi Google’da arzonroq. Panelning asosiy xulosasi: muammo arizalar sonida emas, sifatli ulushda (60% va reja 65%) va konsultatsiyaga yozilishda. Demak, keyingi haftada byudjetni oshirish emas, balki Meta formasidagi savollarni kuchaytirish va konsultatsiyaga yozish skriptini tekshirish kerak.

## Signal qoidalari

Dashboard qaror chiqarishga yordam berishi uchun oldindan «agar … bo‘lsa, … qilamiz» qoidalarini yozib qo‘ying. Shartli namuna:

- CPL ikki hafta ketma-ket rejadan 20% yuqori bo‘lsa — kreativlarni almashtiramiz.
- Sifatli ulush 50% dan tushsa — forma savollari va auditoriyani qayta ko‘ramiz.
- Javob vaqti o‘rtacha 30 daqiqadan oshsa — sotuv rahbari navbatni qayta taqsimlaydi.
- Bitta manbada CAC o‘rtachadan 1,5 baravar yuqori bo‘lsa — uning byudjetini 20–30% ga kamaytirib, boshqa manbaga o‘tkazamiz.

Chegaralarni o‘z unit-ekonomikangizdan hisoblang: qaysi CAC’da sotuv zararga ishlay boshlaydi, shu chegara.

## Ko‘p uchraydigan xatolar

- **Faqat reklama metrikalari.** Qamrov, CTR va layk bor, sotuv yo‘q — bu dashboard emas, kabinet nusxasi.
- **Reja ustuni yo‘q.** 400 ta ariza yaxshimi yoki yomonmi, reja bo‘lmasa bilib bo‘lmaydi.
- **Turli joydagi turli raqamlar.** Bir xil ko‘rsatkich uchun bitta manba belgilang va buni panelda yozib qo‘ying.
- **Juda ko‘p grafik.** Har bir grafik qaror bilan bog‘liq bo‘lmasa, uni olib tashlang.
- **Egasi yo‘q.** Panelni kim yangilashi va kim tekshirishi aniq bo‘lmasa, ikki haftadan keyin u eskiradi.

## Savol-javob

### Dashboard uchun dasturchi kerakmi?

Yo‘q. Google Sheets va Looker Studio’da oddiy panelni bir-ikki kunda yig‘sa bo‘ladi. Dasturchi yoki pullik konnektor ma’lumotni avtomatik tortish kerak bo‘lganda foydali, lekin boshlash uchun haftalik qo‘lda eksport ham yetarli.

### CRM’ning o‘z hisobotlari yetmaydimi?

CRM sotuv qismini yaxshi ko‘rsatadi, lekin reklama sarfini odatda bilmaydi. Dashboard sarf va sotuvni bitta joyda birlashtirgani uchun kerak: shunda CAC va ROMI ko‘rinadi.

### Qaysi metrikadan boshlash kerak?

Uchtadan: sarf, CRM’dagi arizalar va sotuvlar. Shu uchtasi bilan CPL va CAC hisoblanadi. Keyin sifatli ulush va javob vaqtini qo‘shing.

### Dashboard’ni agentlik bilan ulashsa bo‘ladimi?

Ha, va bu foydali: agentlik va sotuv bo‘limi bir xil raqamlarni ko‘radi. Faqat ko‘rish huquqini bering, tahrirlash huquqini esa panel egasiga qoldiring.

## Xulosa

Yaxshi marketing dashboard — bitta sahifa, 8–12 ta raqam, reja bilan solishtiruv va har bir ko‘rsatkich uchun bitta manba. Uni voronka bosqichlari bo‘yicha quring, manbalar kesimini qo‘shing, kunlik, haftalik va oylik ritmni belgilang va signal qoidalarini oldindan yozing. Boshlash uchun Google Sheets va Looker Studio yetarli.

Raqamlaringizni bitta panelga yig‘ishda yordam kerak bo‘lsa, Level Marketing bepul audit davomida reklama va CRM ma’lumotlaringizni ko‘rib chiqishi mumkin.

## Shu mavzuda yana

- [Unit-ekonomika: reklamaga qancha to‘lash mumkinligini qanday bilish](/blog/unit-ekonomika/)
- [Menejerlar konversiyasi: kim arizani sotuvga aylantiradi](/blog/menejerlar-konversiyasi/)
- [Lid narxi (CPL) nima va uni qanday kamaytirish mumkin: tadbirkor uchun qo‘llanma](/blog/lid-narxi-cpl-qanday-kamaytirish/)
