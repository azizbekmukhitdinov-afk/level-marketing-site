---
title: Oflayn reklama natijasini o‘lchash: QR, promokod va CRM
description: Oflayn reklama natijasini o‘lchash: peshlavha, banner, mashina va flayer uchun QR-kod, promokod, alohida raqam va «bizni qayerdan bildingiz» savoli CRM'da.
date: 2026-11-08
slug: oflayn-reklama-natijasi
type: article
tags: sotuv, analitika, oflayn reklama, crm
key: oflayn-reklama-natijasi
rubric: sotuv
---

Kompaniya mashinasiga logotip yopishtirdingiz, yo‘l bo‘yida banner turibdi, ko‘rgazmada flayer tarqatdingiz. Pul ketdi, lekin bu reklama mijoz olib keldimi — hech kim aniq aytolmaydi. Oflayn reklama natijasini o‘lchash mumkin, faqat buni reklama chiqmasdan **oldin** rejalash kerak. Bu maqolada to‘rtta oddiy usul, ularni CRM'ga ulash tartibi va bir oylik hisob jadvali bor.

![Nega oflayn reklama «ko‘rinmaydi»](/img/blog/illus/oflayn-reklama-natijasi-1.jpg 1200x675)

## Nega oflayn reklama «ko‘rinmaydi»

Instagram yoki Google reklamasida har bir bosish yoziladi: kim bosdi, qaysi reklamadan, keyin ariza qoldirdimi. Banner yoki peshlavhada bunday hisoblagich yo‘q. Odam bannerni ko‘radi, eslab qoladi, uch kundan keyin brend nomini Instagram'da qidiradi yoki to‘g‘ridan-to‘g‘ri do‘konga keladi. Natijada bu mijoz hisobotda «organika» yoki «to‘g‘ridan-to‘g‘ri» bo‘lib qoladi.

Shuning uchun oflayn reklamaga o‘zining **izi** kerak — mijoz qayerdan kelganini ko‘rsatadigan belgi. Iz to‘rt xil bo‘ladi:

| Usul | Nimani ko‘rsatadi | Qayerga mos |
|---|---|---|
| QR-kod + UTM | Kim skaner qilib saytga yoki botga o‘tdi | Flayer, menyu, posilka, ko‘rgazma stendi |
| Promokod | Kim xarid paytida kodni aytdi | Banner, radio, bloger, flayer |
| Alohida telefon raqami yoki bot havolasi | Qaysi raqamga qo‘ng‘iroq bo‘ldi | Mashina, bilbord, gazeta |
| «Bizni qayerdan bildingiz?» savoli | Mijoz o‘zi nimani eslaydi | Hamma joyda, qo‘shimcha sifatida |

Bitta usul hamma narsani ko‘rsatmaydi. Eng yaxshisi — har bir reklama joyi uchun bitta asosiy iz va hamma mijozlar uchun bitta umumiy savol.

## 1-usul: QR-kod va UTM-belgi

QR-kodning o‘zi hech narsani sanamaydi. U shunchaki havolani ochadi. Sanash uchun havolaga UTM-belgi qo‘yiladi — xuddi onlayn reklamadagidek. Google Analytics yordam sahifasida aytilganidek, har bir belgili havolada kamida uchta parametr bo‘lishi kerak: `utm_source`, `utm_medium` va `utm_campaign` ([Google Analytics Help](https://support.google.com/analytics/answer/10917952)). UTM haqida batafsil — [UTM-belgilar](/blog/utm-belgilar/) maqolasida.

Oflayn reklama uchun nomlashni bir xil qiling:

- `utm_medium=qr` — hamma QR-kodlar uchun bir xil;
- `utm_source` — joy: `flayer-korgazma`, `menyu-stol`, `posilka`;
- `utm_campaign` — davr yoki aksiya: `noyabr-2026`.

**Muhim qoidalar:**

1. Har bir joy uchun **alohida** QR-kod. Bitta kod hamma flayer va bannerga qo‘yilsa, qaysi biri ishlaganini bilmaysiz.
2. Havola uzun bo‘lsa, QR zich va mayda bo‘lib qoladi. Qisqartirilgan havoladan foydalaning va chop etishdan oldin 2–3 xil telefonda skaner qilib ko‘ring.
3. QR yoniga sabab yozing: «Skaner qiling — narxlar ro‘yxati» yoki «Skaner qiling — 10% chegirma». Sababsiz kodni kam odam skaner qiladi.
4. Ochiq joydagi QR-kodni vaqti-vaqti bilan tekshirib turing: ustidan boshqa kod yopishtirilmaganmi. Ba'zi shaharlarda firibgarlar haqiqiy QR ustiga o‘z kodini yopishtirgani haqida xabarlar bor ([Sostav](https://www.sostav.ru/blogs/276144/52774)).

Saytingiz bo‘lmasa, QR-kod Telegram botga olib borishi mumkin. Botda start parametri bilan har bir joyga alohida havola yaratiladi va bot qaysi havoladan kirilganini yozib qo‘yadi. Bot bilan ishlash haqida — [Telegram bot orqali arizalar](/blog/telegram-bot-orqali-arizalar/).

## 2-usul: promokod

Promokod — odam QR skaner qilmasa ham ishlaydigan iz. Mijoz kassada yoki telefonda kodni aytadi va siz uni qaysi reklamadan olganini bilasiz.

Promokod ishlashi uchun:

- **Har bir reklama joyiga o‘z kodi.** Masalan, Chilonzordagi banner uchun `CHILONZOR`, Sergeli yo‘lidagi banner uchun `SERGELI`. Bitta umumiy kod faqat «aksiya ishladimi» degan savolga javob beradi.
- **Kodni aytishga sabab bo‘lsin.** Kichik chegirma, sovg‘a yoki bepul yetkazib berish. Sababsiz hech kim kod aytmaydi.
- **Kod oson aytilsin.** Bitta so‘z, raqam va murakkab harflarsiz. «X7QK2» emas, «BAHOR».
- **Kassada yoki CRM'da kod uchun maydon bo‘lsin.** Kassir kodni qog‘ozga yozsa, oy oxirida u yo‘qoladi.

Promokodning kamchiligi — kodlar tarqab ketadi. Mijoz kodni do‘stiga Telegram'da yuboradi va endi u «banner» natijasi bo‘lib ko‘rinadi, aslida esa tavsiya. Shuning uchun promokod natijasini taxminiy deb qabul qiling va boshqa usullar bilan solishtiring.

## 3-usul: alohida raqam yoki bot havolasi

Mashina, bilbord yoki gazetada odam QR skaner qilmaydi va promokodni eslab qolmaydi. U raqamni ko‘radi va qo‘ng‘iroq qiladi. Agar bu joylarda **alohida telefon raqami** bo‘lsa, qo‘ng‘iroqlar soni — tayyor natija.

Amalda bu shunday ko‘rinadi (shartli misol): mebel do‘koni kompaniya mashinasiga asosiy raqam emas, boshqa SIM-karta raqamini yozdi. Bir oyda bu raqamga kelgan qo‘ng‘iroqlar alohida hisoblanadi va menejer ularni CRM'da «mashina» manbasi bilan belgilaydi.

Agar mijozlar asosan Telegram'da yozsa, raqam o‘rniga qisqa bot yoki kanal havolasini ishlating — har bir joy uchun alohida start parametri bilan.

Bu usul eng aniq, lekin unga intizom kerak: alohida raqamga qo‘ng‘iroqqa ham asosiy raqamdagidek tez javob berilishi lozim. Javobsiz qolgan qo‘ng‘iroq reklama ishlamagandek ko‘rinadi, aslida esa sotuv bo‘limi ishlamagan bo‘ladi.

![4-usul: «Bizni qayerdan bildingiz?» savoli CRM'da](/img/blog/illus/oflayn-reklama-natijasi-2.jpg 1200x675)

## 4-usul: «Bizni qayerdan bildingiz?» savoli CRM'da

Bu eng arzon usul va u boshqa usullar ko‘rmagan narsani ko‘rsatadi: tavsiya, do‘konning yonidan o‘tib qolish, bannerni ko‘rib keyin Instagram'da qidirish.

Lekin savolni to‘g‘ri berish kerak:

- **Ro‘yxatdan tanlash.** CRM'da bo‘sh matn emas, tayyor variantlar bo‘lsin: Instagram, Telegram, Google/xarita, banner, mashina, peshlavha, tanish tavsiyasi, boshqa. Bo‘sh matnda «insta», «instagramdan», «IG» — uch xil yoziladi va hisoblab bo‘lmaydi.
- **Majburiy maydon.** Menejer maydonni to‘ldirmasdan arizani keyingi bosqichga o‘tkaza olmasin.
- **Bir xil savol.** Hamma menejerlar bir xil so‘zlar bilan so‘rasin. Buni [sotuv skripti](/blog/sotuv-skripti/)ga kiritib qo‘ying.
- **«Birinchi marta qayerda ko‘rdingiz?»** va **«Bugun nima sababdan yozdingiz?»** — ikki xil savol. Birinchisi qaysi reklama tanishtirganini, ikkinchisi qaysi biri harakatga undaganini ko‘rsatadi. Agar bitta savol qoldirsangiz, qaysi birini so‘rayotganingizni aniq belgilang.

Bu usulning kamchiligi — odamlar eslay olmaydi yoki eng oxirgi ko‘rgan narsasini aytadi. Shuning uchun uni yagona manba sifatida emas, **tekshiruv** sifatida ishlating: promokod va qo‘ng‘iroqlar bilan solishtiring.

## Hammasini bitta jadvalga yig‘ish

Usullar alohida ishlasa, oy oxirida to‘rtta turli joydagi raqamlar chiqadi. Ularni bitta jadvalga yig‘ing. Har bir oflayn reklama joyi uchun bitta qator:

| Reklama joyi | Xarajat | QR o‘tishlar | Promokod | Qo‘ng‘iroqlar | «Qayerdan bildingiz» | Sotuvlar | Sotuv summasi |
|---|---|---|---|---|---|---|---|
| Chilonzordagi banner | 4 mln so‘m | — | 9 | — | 14 | 6 | 21 mln so‘m |
| Kompaniya mashinasi | 1 mln so‘m | — | — | 11 | 5 | 2 | 7 mln so‘m |
| Ko‘rgazma flayeri | 2 mln so‘m | 38 | 4 | — | 3 | 1 | 3 mln so‘m |

*Shartli misol: raqamlar faqat jadvalni qanday to‘ldirishni ko‘rsatish uchun.*

Jadvalda ikki narsaga qarang:

1. **Bitta sotuv narxi** — xarajatni sotuvlar soniga bo‘ling. Uni onlayn reklamadagi mijoz jalb qilish narxi bilan solishtiring.
2. **Reklama o‘zini oqladimi** — sotuvdan keladigan foyda bilan xarajatni solishtiring. Hisoblash tartibi — [ROMI qanday hisoblanadi](/blog/romi-hisoblash/) maqolasida.

Oflayn reklama sekin ishlaydi: odam bannerni bugun ko‘radi, ikki haftadan keyin keladi. Shuning uchun natijani bir haftada emas, kamida bir oy, imkoni bo‘lsa ikki-uch oy kuzating.

## Oflayn reklamaning onlaynga ta'sirini ko‘rish

Ko‘p mijozlar bannerni ko‘rib QR skaner qilmaydi, balki keyinroq brend nomini qidiradi. Bu ta'sirni bilvosita ko‘rish mumkin:

- **Brend nomi bo‘yicha qidiruv.** Google Business Profile va Yandex Biznes kartochkasida qidiruvlar va marshrut so‘rovlari statistikasi bor. Banner qo‘yilgan oyda ular o‘sdimi? Kartochka haqida — [biznesni xaritalarga qo‘shish](/blog/biznesni-xaritalarga-qoshish/).
- **Instagram profilga kirishlar.** Statistikada profilga tashriflar va obunachilar o‘sishi banner davrida o‘zgardimi.
- **Hududdagi arizalar.** Agar banner bitta tumanda tursa, CRM'da shu tumandan kelgan arizalar ulushini kuzating.

Bu raqamlar aniq dalil emas, chunki bir vaqtda boshqa narsalar ham o‘zgarishi mumkin. Lekin bir nechta belgi bir xil yo‘nalishda o‘zgarsa, xulosa chiqarish mumkin.

![Bir oylik reja: qadam-baqadam](/img/blog/illus/oflayn-reklama-natijasi-3.jpg 1200x675)

## Bir oylik reja: qadam-baqadam

1. **Reklamadan oldin:** har bir oflayn joy uchun izni tanlang — QR, promokod yoki raqam.
2. **CRM'ni tayyorlang:** «Manba» maydoniga oflayn variantlarni qo‘shing, promokod uchun maydon oching, maydonni majburiy qiling.
3. **Menejerlarni o‘rgating:** bitta savol, bitta yozish tartibi.
4. **Chop etishdan oldin tekshiring:** QR-kodlar ochiladimi, UTM to‘g‘ri yozilganmi, promokod kassada ishlaydimi.
5. **Har hafta:** QR o‘tishlar, qo‘ng‘iroqlar va promokodlarni jadvalga ko‘chiring.
6. **Oy oxirida:** sotuvlar va summani qo‘shing, bitta sotuv narxini hisoblang, qaysi joyni davom ettirish va qaysi birini to‘xtatishni hal qiling.

## Savol-javob

**Kichik do‘kon uchun bu juda murakkab emasmi?**
Yo‘q. Eng oddiy variant — CRM'da yoki hatto Google Sheets'da «Bizni qayerdan bildingiz?» ustuni va har bir banner uchun bitta promokod. Bu bir kunlik ish.

**QR-kodni skaner qilish sonini qayerdan ko‘raman?**
UTM-belgili havola saytga olib borsa — Google Analytics'da manba va kanal bo‘yicha. Botga olib borsa — botning o‘zida start parametri bo‘yicha. Ba'zi QR xizmatlari skanerlar sonini o‘zi ko‘rsatadi, lekin bu ma'lumot ular serverida qoladi.

**Mijoz «Instagram'dan» deydi, lekin aslida bannerni ko‘rgan. Nima qilish kerak?**
Bu normal holat. Shuning uchun bitta savolga tayanmang: promokod, alohida raqam va brend qidiruvi o‘sishi bilan solishtiring. Bir nechta manba bir xil narsani ko‘rsatsa — ishonch ortadi.

**Natijasi yomon bo‘lsa, reklamani darhol to‘xtatish kerakmi?**
Avval tekshiring: iz to‘g‘ri ishladimi, menejerlar savol berdimi, qo‘ng‘iroqlarga javob berildimi. Oflayn reklama sekin natija beradi, shuning uchun kamida bir oy kuting.

## Xulosa

Oflayn reklama natijasini o‘lchash uchun murakkab tizim kerak emas. Har bir reklama joyiga o‘z izi — QR, promokod yoki raqam — va CRM'da majburiy «Bizni qayerdan bildingiz?» savoli yetarli. Muhimi, buni reklama chiqmasdan oldin rejalash va oy oxirida bitta jadvalda solishtirish. Level Marketing'da biz mijozlarimiz bilan onlayn va oflayn manbalarni bitta hisobotda ko‘rishga harakat qilamiz — shunda byudjet qayerga ketayotgani aniq bo‘ladi.

## Shu mavzuda yana

- [UTM-belgilar: har bir mijoz qayerdan kelganini qanday bilish](/blog/utm-belgilar/)
- [Kabinetdagi lidlar va CRM mos kelmasa: 7 sabab va tekshiruv](/blog/kabinet-va-crm-lidlar/)
- [Reklama hisobotida qanday raqamlar bo‘lishi shart](/blog/reklama-hisoboti/)
