BODIES = {
"meta-pixel-conversions-api": {
"uz": """
Reklama sotuv olib kelyaptimi yoki shunchaki bosishlarmi? Bu savolga aniq javobni faqat kuzatuv beradi. Meta reklamasida kuzatuvning ikki vositasi bor: **Meta Pixel** va **Conversions API**. Ushbu maqolada ular nima uchun kerakligini, qaysi hodisalarni kuzatish va o‘rnatishda qanday xatolardan qochish kerakligini ko‘rib chiqamiz.

## Meta Pixel nima

Pixel — saytingizga qo‘yiladigan kichik kod. U tashrif buyuruvchi saytda nima qilganini — sahifani ko‘rgani, formani yuborgani, xarid qilganini — Meta'ga yuboradi. Natijada:

- reklama kabinetida qaysi reklama ariza va sotuv olib kelganini ko‘rasiz;
- algoritm aynan shu harakatni qiladigan odamlarni qidirishni o‘rganadi;
- saytga kirgan, lekin sotib olmaganlar uchun [retargeting](/blog/retargeting-qanday-ishlaydi/) auditoriyasini yaratasiz.

## Conversions API nima va nega Pixel yetmaydi

Pixel brauzer orqali ishlaydi. Reklama blokerlari, iOS cheklovlari va cookie sozlamalari tufayli hodisalarning bir qismi Meta'ga yetib bormaydi. **Conversions API (CAPI)** xuddi shu hodisalarni sizning serveringizdan yuboradi. Ikkalasi birga ishlaganda Meta ma'lumotni to‘liqroq oladi, bir xil hodisaning ikki nusxasi esa `event_id` orqali birlashtiriladi (deduplikatsiya).

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

1. **Events Manager**'da (business.facebook.com) yangi ma'lumot manbai — Pixel yarating.
2. Kodni saytga qo‘shing. Tilda, WordPress yoki Shopify kabi konstruktorlarda tayyor integratsiya bor; o‘zingiz yozgan saytda kod sahifa boshiga yoki Google Tag Manager orqali qo‘yiladi.
3. Asosiy hodisalarni sozlang: kamida Lead yoki Purchase, kichik biznes uchun Contact ham.
4. **Conversions API**'ni ulang: platformaning tayyor integratsiyasi, Google Tag Manager server konteyneri yoki dasturchi yordamida.
5. **Test Events** bo‘limida tekshiring: har bir hodisa kelyaptimi va moslik sifati (Event Match Quality) qanday.

## Ko‘p uchraydigan xatolar

- Pixel saytga ikki marta o‘rnatilgan — hodisalar ikki baravar hisoblanadi.
- Lead hodisasi «Rahmat» sahifasida emas, forma sahifasining o‘zida ishga tushadi — har bir tashrif ariza bo‘lib ko‘rinadi.
- Domen Business Manager'da tasdiqlanmagan.
- Kampaniya maqsadi bilan optimallashtirish hodisasi mos kelmaydi.

## Saytingiz bo‘lmasa-chi

Ko‘p bizneslar Instagram Direct yoki Telegram orqali sotadi. Bunda Pixel kerak emas, lekin sotuvni qayd qilish baribir zarur: arizalarni CRM yoki jadvalda belgilang va qaysi reklama sotuv olib kelganini solishtiring. Ariza narxini qanday hisoblash haqida — [CPL bo‘yicha qo‘llanmamizda](/blog/lid-narxi-cpl-qanday-kamaytirish/).

## Xulosa

Pixel va Conversions API — reklamaning «ko‘zi». Ularsiz algoritm qorong‘ida ishlaydi, siz esa arzon, lekin sotuvga aylanmaydigan arizalar uchun pul to‘laysiz. Level Marketing har bir loyihada kuzatuvni birinchi haftada sozlaydi.
""",
"ru": """
Приносит ли реклама продажи или только клики? Точно ответить на этот вопрос может только отслеживание. В рекламе Meta для этого есть два инструмента: **Meta Pixel** и **Conversions API**. Разберём, зачем они нужны, какие события отслеживать и каких ошибок избегать при установке.

## Что такое Meta Pixel

Pixel — небольшой код, который устанавливается на сайт. Он передаёт в Meta, что посетитель сделал на сайте: посмотрел страницу, отправил форму, совершил покупку. В результате:

- в рекламном кабинете видно, какая реклама принесла заявки и продажи;
- алгоритм учится искать людей, которые совершают именно это действие;
- можно собрать аудиторию для [ретаргетинга](/ru/blog/retargeting-kak-rabotaet/) из тех, кто был на сайте, но не купил.

## Что такое Conversions API и почему одного Pixel мало

Pixel работает через браузер. Из-за блокировщиков рекламы, ограничений iOS и настроек cookie часть событий до Meta не доходит. **Conversions API (CAPI)** передаёт те же события с вашего сервера. Вместе они дают Meta более полные данные, а дубли одного события объединяются по `event_id` (дедупликация).

## Какие события отслеживать

| Событие | Когда срабатывает | Кому важно |
|---|---|---|
| PageView | При открытии любой страницы | Всем |
| ViewContent | Страница товара или услуги | Магазинам, услугам |
| Lead | Отправка формы | Бизнесу услуг |
| Contact | Нажатие кнопки Telegram или звонка | Малому бизнесу |
| InitiateCheckout | Начало оформления заказа | Интернет-магазину |
| Purchase | Завершённая покупка | Интернет-магазину |

## Как установить: 5 шагов

1. В **Events Manager** (business.facebook.com) создайте источник данных — Pixel.
2. Добавьте код на сайт. В конструкторах вроде Tilda, WordPress или Shopify есть готовая интеграция; на самописном сайте код ставится в начало страницы или через Google Tag Manager.
3. Настройте ключевые события: минимум Lead или Purchase, для малого бизнеса ещё Contact.
4. Подключите **Conversions API**: через готовую интеграцию платформы, серверный контейнер Google Tag Manager или с помощью разработчика.
5. Проверьте в разделе **Test Events**: приходит ли каждое событие и какое у него качество совпадения (Event Match Quality).

## Частые ошибки

- Pixel установлен на сайт дважды — события считаются в двойном размере.
- Событие Lead срабатывает не на странице «Спасибо», а на самой странице формы — каждый визит выглядит как заявка.
- Домен не подтверждён в Business Manager.
- Цель кампании не совпадает с событием оптимизации.

## А если сайта нет

Многие бизнесы продают через Instagram Direct или Telegram. Тогда Pixel не нужен, но фиксировать продажи всё равно обязательно: отмечайте заявки в CRM или таблице и сравнивайте, какая реклама приносит продажи. Как считать цену заявки — в нашем [гиде по CPL](/ru/blog/tsena-lida-cpl-kak-snizit/).

## Вывод

Pixel и Conversions API — «глаза» рекламы. Без них алгоритм работает вслепую, а вы платите за дешёвые заявки, которые не превращаются в продажи. В Level Marketing мы настраиваем отслеживание в первую же неделю каждого проекта.
""",
"en": """
Are your ads bringing sales, or just clicks? Only tracking can answer that precisely. Meta advertising has two tracking tools for it: **Meta Pixel** and the **Conversions API**. Here is why you need them, which events to track and which setup mistakes to avoid.

## What Meta Pixel is

The Pixel is a small piece of code you add to your website. It tells Meta what a visitor did on your site: viewed a page, submitted a form, completed a purchase. As a result:

- you can see in Ads Manager which ads brought leads and sales;
- the algorithm learns to look for people who take exactly that action;
- you can build a [retargeting](/en/blog/how-retargeting-works/) audience of people who visited but didn't buy.

## What the Conversions API is, and why the Pixel isn't enough

The Pixel works through the browser. Because of ad blockers, iOS restrictions and cookie settings, some events never reach Meta. The **Conversions API (CAPI)** sends the same events from your server. Together they give Meta fuller data, and duplicates of the same event are merged using an `event_id` (deduplication).

## Which events to track

| Event | When it fires | Who it matters for |
|---|---|---|
| PageView | Any page load | Everyone |
| ViewContent | Product or service page | Shops, services |
| Lead | Form submitted | Service businesses |
| Contact | Telegram or call button clicked | Small businesses |
| InitiateCheckout | Checkout started | Online stores |
| Purchase | Purchase completed | Online stores |

## How to set it up: 5 steps

1. In **Events Manager** (business.facebook.com), create a new data source — a Pixel.
2. Add the code to your site. Builders like Tilda, WordPress or Shopify have ready integrations; on a custom site the code goes into the page header or through Google Tag Manager.
3. Set up the key events: at least Lead or Purchase, plus Contact for small businesses.
4. Connect the **Conversions API**: via your platform's integration, a Google Tag Manager server container or a developer.
5. Check in **Test Events** that every event arrives and what its Event Match Quality score is.

## Common mistakes

- The Pixel is installed twice, so every event is counted double.
- The Lead event fires on the form page itself rather than the "Thank you" page, so every visit looks like a lead.
- The domain isn't verified in Business Manager.
- The campaign objective doesn't match the optimisation event.

## What if you don't have a website

Many businesses sell through Instagram Direct or Telegram. Then you don't need the Pixel, but you still have to record sales: mark leads in a CRM or spreadsheet and compare which ads bring sales. For calculating cost per lead, see our [CPL guide](/en/blog/cost-per-lead-cpl-how-to-lower/).

## Conclusion

The Pixel and the Conversions API are your advertising's eyes. Without them the algorithm works blind and you pay for cheap leads that never turn into sales. At Level Marketing we set up tracking in the first week of every project.
""",
},
"lookalike-auditoriya": {
"uz": """
Eng yaxshi mijozlaringizga o‘xshash odamlarni qayerdan topish mumkin? Meta'da buning uchun **lookalike (o‘xshash) auditoriya** bor: siz algoritmga namuna berasiz, u esa shu namunaga o‘xshash yangi odamlarni topadi. Bu maqolada lookalike qanday ishlashini, qaysi manbadan yaratish kerakligini va qanday xatolardan qochishni ko‘rib chiqamiz.

## Lookalike qanday ishlaydi

Siz **manba auditoriya** (source) beraysiz — masalan, xaridorlaringiz ro‘yxati. Meta bu odamlarning umumiy belgilarini — qiziqishlari, xatti-harakati, demografiyasini — tahlil qiladi va tanlangan mamlakatda ularga eng o‘xshash odamlarni yig‘adi. Natijada siz qiziqishlarni taxmin qilib o‘tirmasdan, haqiqiy mijozlaringizga yaqin auditoriyaga reklama berasiz.

## Qaysi manbadan yaratish kerak

| Manba | Sifati | Izoh |
|---|---|---|
| Xaridorlar ro‘yxati (telefon, email) | Eng yuqori | CRM'dan eksport qiling |
| Pixel: Purchase yoki Lead | Yuqori | Saytda kuzatuv bo‘lsa |
| Direct'ga yozganlar | O‘rtacha-yuqori | Xabarlar kampaniyalari uchun yaxshi |
| Instagram profil bilan faol bo‘lganlar | O‘rtacha | Katta, lekin «iliqroq» |
| Videoni 75% ko‘rganlar | O‘rtacha | Kontent kuchli bo‘lsa |

Qoida oddiy: manba qanchalik sotuvga yaqin bo‘lsa, lookalike shunchalik yaxshi ishlaydi. Manba kamida bir mamlakatdan 100 kishidan iborat bo‘lishi kerak, lekin bir necha yuz yoki ming kishi bo‘lsa, natija barqarorroq.

## Qanday foiz tanlash kerak

Lookalike hajmi mamlakat auditoriyasining 1% dan 10% gacha bo‘ladi. 1% — eng o‘xshash, lekin kichik guruh; 10% — keng, ammo o‘xshashligi pastroq. O‘zbekistonda Meta auditoriyasi yirik mamlakatlarga qaraganda kichikroq, shuning uchun 1% ba'zan juda tor bo‘lib qoladi. Amaliy yondashuv: 1–3% bilan boshlang, keyin 3–5% va kengroq variantlarni alohida test qiling.

## Qadamma-qadam

1. Auditoriyalar bo‘limida manba auditoriyani yarating yoki mijozlar ro‘yxatini yuklang.
2. «Lookalike auditoriya yaratish»ni tanlang, mamlakat sifatida O‘zbekistonni belgilang.
3. Foizni tanlang (masalan, 1%, 3% va 5% — uchta alohida auditoriya).
4. Har birini alohida reklama to‘plamida bir xil kreativ bilan sinang.
5. Mavjud mijozlarni istisno qiling — ularga yangi mijoz sifatida reklama ko‘rsatish shart emas.

## Ko‘p uchraydigan xatolar

- **Sifatsiz manba.** «Barcha arizalar» o‘rniga «sotib olganlar»dan yarating.
- **Eskirgan ro‘yxat.** Manbani har 1–2 oyda yangilang.
- **Bir-birini qoplaydigan auditoriyalar.** Bir xil odamlarga bir nechta to‘plam raqobatlashib, narxni oshiradi.
- **Kreativni e'tiborsiz qoldirish.** Auditoriya qanchalik yaxshi bo‘lmasin, kuchsiz kreativ baribir ishlamaydi.

Meta bugun ko‘pincha algoritmga ko‘proq erkinlik beradigan Advantage+ auditoriyani tavsiya qiladi. Bunday kampaniyalarda lookalike'ni «tavsiya» sifatida qo‘shish mumkin — algoritm undan boshlang‘ich nuqta sifatida foydalanadi. Qaysi variant yaxshiroqligini faqat [A/B test](/blog/kreativlar-ab-test/) ko‘rsatadi.

## Xulosa

Lookalike — mavjud mijozlar bazangizni yangi mijozlar oqimiga aylantirishning tez yo‘li. Sifatli manba, bir nechta foizni test qilish va mijozlarni istisno qilish — asosiy uch qoida. Level Marketing CRM'dagi xaridorlar asosida auditoriyalar yaratib, ariza narxini pasaytiradi.
""",
"ru": """
Где найти людей, похожих на ваших лучших клиентов? Для этого в Meta есть **lookalike-аудитории (похожие аудитории)**: вы даёте алгоритму образец, а он находит новых людей, похожих на него. Разберём, как работают lookalike, из какого источника их создавать и каких ошибок избегать.

## Как работает lookalike

Вы задаёте **исходную аудиторию** (source) — например, список покупателей. Meta анализирует общие признаки этих людей — интересы, поведение, демографию — и собирает в выбранной стране тех, кто больше всего на них похож. В итоге вы показываете рекламу аудитории, близкой к реальным клиентам, не угадывая интересы вручную.

## Из какого источника создавать

| Источник | Качество | Комментарий |
|---|---|---|
| Список покупателей (телефоны, email) | Самое высокое | Выгрузите из CRM |
| Pixel: Purchase или Lead | Высокое | Если на сайте есть отслеживание |
| Те, кто писал в Direct | Среднее–высокое | Хорошо для кампаний на сообщения |
| Активные в профиле Instagram | Среднее | Большая, но «тёплая» аудитория |
| Досмотревшие видео на 75% | Среднее | Если контент сильный |

Правило простое: чем ближе источник к продаже, тем лучше работает lookalike. В источнике должно быть минимум 100 человек из одной страны, но с несколькими сотнями или тысячами результат стабильнее.

## Какой процент выбирать

Размер lookalike — от 1% до 10% аудитории страны. 1% — самые похожие, но маленькая группа; 10% — широкая, но менее похожая. В Узбекистане аудитория Meta меньше, чем в крупных странах, поэтому 1% иногда оказывается слишком узким. Практический подход: начните с 1–3%, затем отдельно протестируйте 3–5% и шире.

## Пошагово

1. В разделе «Аудитории» создайте исходную аудиторию или загрузите список клиентов.
2. Выберите «Создать похожую аудиторию», страна — Узбекистан.
3. Задайте процент (например, 1%, 3% и 5% — три отдельные аудитории).
4. Протестируйте каждую в отдельной группе объявлений с одинаковым креативом.
5. Исключите текущих клиентов — показывать им рекламу как новым не нужно.

## Частые ошибки

- **Слабый источник.** Создавайте не из «всех заявок», а из «купивших».
- **Устаревший список.** Обновляйте источник раз в 1–2 месяца.
- **Пересекающиеся аудитории.** Несколько групп конкурируют за одних и тех же людей и поднимают цену.
- **Игнорирование креатива.** Даже лучшая аудитория не спасёт слабый креатив.

Сейчас Meta часто рекомендует Advantage+ аудиторию, которая даёт алгоритму больше свободы. В таких кампаниях lookalike можно добавить как «подсказку» — алгоритм использует её как отправную точку. Какой вариант лучше, покажет только [A/B-тест](/ru/blog/ab-test-kreativov/).

## Вывод

Lookalike — быстрый способ превратить базу текущих клиентов в поток новых. Качественный источник, тест нескольких процентов и исключение клиентов — три главных правила. В Level Marketing мы строим аудитории на основе покупателей из CRM и снижаем цену заявки.
""",
"en": """
Where can you find people who look like your best customers? Meta's answer is **lookalike audiences**: you give the algorithm a sample, and it finds new people similar to it. Here is how lookalikes work, which source to build them from and which mistakes to avoid.

## How lookalikes work

You provide a **source audience** — for example, your list of buyers. Meta analyses what these people have in common — interests, behaviour, demographics — and gathers the people in your chosen country who resemble them most. You end up advertising to an audience close to your real customers without guessing interests by hand.

## Which source to use

| Source | Quality | Notes |
|---|---|---|
| Buyer list (phones, emails) | Highest | Export it from your CRM |
| Pixel: Purchase or Lead | High | If your site has tracking |
| People who messaged you in Direct | Medium–high | Good for message campaigns |
| People engaged with your Instagram profile | Medium | Large but "warmer" |
| People who watched 75% of a video | Medium | If your content is strong |

The rule is simple: the closer the source is to a sale, the better the lookalike works. The source needs at least 100 people from one country, but results are more stable with hundreds or thousands.

## Which percentage to choose

A lookalike covers 1% to 10% of a country's audience. 1% is the most similar but small; 10% is broad but less similar. Meta's audience in Uzbekistan is smaller than in large markets, so 1% is sometimes too narrow. A practical approach: start with 1–3%, then test 3–5% and broader separately.

## Step by step

1. In Audiences, create a source audience or upload a customer list.
2. Choose "Create lookalike audience" and set Uzbekistan as the country.
3. Pick the percentage — for example, 1%, 3% and 5% as three separate audiences.
4. Test each in its own ad set with the same creative.
5. Exclude existing customers — there's no need to advertise to them as if they were new.

## Common mistakes

- **A weak source.** Build from "buyers", not "all leads".
- **An outdated list.** Refresh the source every 1–2 months.
- **Overlapping audiences.** Several ad sets compete for the same people and push up costs.
- **Ignoring the creative.** Even the best audience won't save a weak creative.

Meta now often recommends Advantage+ audience, which gives the algorithm more freedom. In those campaigns you can add a lookalike as a "suggestion" the algorithm uses as a starting point. Only an [A/B test](/en/blog/ab-testing-ad-creatives/) will show which approach works better for you.

## Conclusion

Lookalikes are a fast way to turn your existing customer base into a flow of new customers. A quality source, testing several percentages and excluding current customers are the three main rules. At Level Marketing we build audiences from the buyers in your CRM to bring cost per lead down.
""",
},
"retargeting-qanday-ishlaydi": {
"uz": """
Odamlarning ko‘pchiligi birinchi ko‘rishdayoq sotib olmaydi: profilga kiradi, narxni ko‘radi, o‘ylab ko‘rish uchun chiqib ketadi. **Retargeting** — aynan shu odamlarga qayta reklama ko‘rsatib, ularni qarorga qaytarish. Bu maqolada retargeting kimlarga ko‘rsatilishini, qanday kreativ ishlashini va uni qanday qilib bezor qiluvchi reklamaga aylantirmaslikni ko‘rib chiqamiz.

## Retargeting nima

Retargeting (yoki remarketing) — biznesingiz bilan allaqachon aloqada bo‘lgan odamlarga reklama ko‘rsatish. Ular sizni taniydi, shuning uchun bunday reklama odatda yangi auditoriyaga qaraganda arzonroq ariza olib keladi. Lekin auditoriya kichik bo‘lgani uchun u yangi mijozlar oqimini almashtirmaydi — uni to‘ldiradi.

## Kimlarga qayta ko‘rsatish kerak

| Auditoriya | Manba | Muddat |
|---|---|---|
| Saytga kirganlar | Meta Pixel | 7–30 kun |
| Mahsulot sahifasini ko‘rganlar | Pixel: ViewContent | 7–14 kun |
| Instagram profil bilan faol bo‘lganlar | Instagram akkaunt | 30–90 kun |
| Videoni 50–75% ko‘rganlar | Video ko‘rishlar | 30 kun |
| Direct'ga yozib, sotib olmaganlar | Xabarlar | 14–30 kun |
| Lid-formani ochib, yubormaganlar | Instant forma | 7–30 kun |

Saytdagi hodisalar uchun [Meta Pixel va Conversions API](/blog/meta-pixel-conversions-api/) sozlangan bo‘lishi kerak.

## Qanday kreativ ishlaydi

Retargeting auditoriyasi sizni allaqachon biladi, shuning uchun ularga birinchi reklamani takrorlash foydasiz. Ishlaydigan yondashuvlar:

- **Sharhlar va natijalar** — «boshqalar sotib oldi va mamnun».
- **E'tirozlarga javob** — narx, yetkazib berish, kafolat, muddatli to‘lov.
- **Muddatli taklif** — «shu hafta ichida o‘lchov bepul».
- **Eslatma** — ko‘rgan mahsulotini yoki xizmatini ko‘rsatish.

## Chastotani nazorat qiling

Kichik auditoriyaga katta byudjet berilsa, bitta odam reklamani kuniga bir necha marta ko‘radi va bezor bo‘ladi. Chastota ko‘rsatkichini kuzating: u tez o‘sib, CTR tushsa — byudjetni kamaytiring yoki kreativni yangilang. Odatda retargetingga umumiy byudjetning kichik qismi, masalan, 10–20% yetadi.

## Kimni istisno qilish kerak

- Allaqachon sotib olganlarni (agar takroriy sotuv maqsadi bo‘lmasa).
- Ishga qabul qilish yoki hamkorlik bo‘yicha yozganlarni.
- Juda eski tashrifchilarni — 90 kundan oshganlar odatda «sovib» qoladi.

## Xulosa

Retargeting qiziqqan, lekin qaror qilmagan odamlarni sotuvga qaytaradi. To‘g‘ri auditoriya, e'tirozlarga javob beradigan kreativ va chastota nazorati — muvaffaqiyatning uch sharti. Yangi auditoriyani topish uchun esa [lookalike auditoriyalardan](/blog/lookalike-auditoriya/) foydalaning.
""",
"ru": """
Большинство людей не покупает с первого касания: заходят в профиль, смотрят цену и уходят «подумать». **Ретаргетинг** — повторный показ рекламы именно этим людям, чтобы вернуть их к решению. Разберём, кому показывать ретаргетинг, какие креативы работают и как не превратить его в навязчивую рекламу.

## Что такое ретаргетинг

Ретаргетинг (или ремаркетинг) — показ рекламы людям, которые уже взаимодействовали с вашим бизнесом. Они вас знают, поэтому такая реклама обычно приносит заявки дешевле, чем холодная аудитория. Но аудитория небольшая, поэтому ретаргетинг не заменяет поток новых клиентов, а дополняет его.

## Кому показывать повторно

| Аудитория | Источник | Срок |
|---|---|---|
| Посетители сайта | Meta Pixel | 7–30 дней |
| Смотревшие страницу товара | Pixel: ViewContent | 7–14 дней |
| Активные в профиле Instagram | Аккаунт Instagram | 30–90 дней |
| Досмотревшие видео на 50–75% | Просмотры видео | 30 дней |
| Писавшие в Direct, но не купившие | Сообщения | 14–30 дней |
| Открывшие лид-форму, но не отправившие | Моментальная форма | 7–30 дней |

Для событий на сайте должны быть настроены [Meta Pixel и Conversions API](/ru/blog/meta-pixel-i-conversions-api/).

## Какие креативы работают

Аудитория ретаргетинга вас уже знает, поэтому повторять первую рекламу бесполезно. Работают:

- **Отзывы и результаты** — «другие купили и довольны».
- **Ответы на возражения** — цена, доставка, гарантия, рассрочка.
- **Ограниченное предложение** — «замер бесплатно до конца недели».
- **Напоминание** — показать тот товар или услугу, которые человек смотрел.

## Контролируйте частоту

Если маленькой аудитории дать большой бюджет, один человек будет видеть рекламу по несколько раз в день и раздражаться. Следите за частотой: если она быстро растёт, а CTR падает — уменьшите бюджет или обновите креатив. Обычно на ретаргетинг хватает небольшой части общего бюджета, например 10–20%.

## Кого исключать

- Тех, кто уже купил (если цель — не повторные продажи).
- Тех, кто писал по вакансиям или сотрудничеству.
- Слишком старых посетителей — после 90 дней интерес обычно «остывает».

## Вывод

Ретаргетинг возвращает к покупке тех, кто заинтересовался, но не решился. Правильная аудитория, креативы с ответами на возражения и контроль частоты — три условия успеха. А чтобы находить новых людей, используйте [lookalike-аудитории](/ru/blog/lookalike-auditoriya/).
""",
"en": """
Most people don't buy on first contact: they visit your profile, check the price and leave "to think about it". **Retargeting** means showing ads again to exactly these people to bring them back to a decision. Here is who to retarget, which creatives work and how to keep it from becoming annoying.

## What retargeting is

Retargeting (or remarketing) is advertising to people who have already interacted with your business. They know you, so these ads usually bring leads more cheaply than a cold audience. But the audience is small, so retargeting doesn't replace a flow of new customers — it complements it.

## Who to show ads to again

| Audience | Source | Window |
|---|---|---|
| Website visitors | Meta Pixel | 7–30 days |
| People who viewed a product page | Pixel: ViewContent | 7–14 days |
| People engaged with your Instagram profile | Instagram account | 30–90 days |
| People who watched 50–75% of a video | Video views | 30 days |
| People who messaged in Direct but didn't buy | Messages | 14–30 days |
| People who opened a lead form but didn't submit | Instant form | 7–30 days |

For website events, you need [Meta Pixel and the Conversions API](/en/blog/meta-pixel-and-conversions-api/) set up.

## Which creatives work

Your retargeting audience already knows you, so repeating the first ad is pointless. What works:

- **Reviews and results** — "others bought and are happy".
- **Answers to objections** — price, delivery, warranty, instalments.
- **A time-limited offer** — "free measurement until the end of the week".
- **A reminder** — showing the product or service they looked at.

## Keep frequency under control

Give a small audience a big budget and one person sees your ad several times a day and gets irritated. Watch frequency: if it climbs fast while CTR drops, cut the budget or refresh the creative. Retargeting usually needs only a small share of the total budget, for example 10–20%.

## Who to exclude

- People who already bought (unless your goal is repeat sales).
- People who wrote about jobs or partnerships.
- Very old visitors — interest usually cools after 90 days.

## Conclusion

Retargeting brings back people who were interested but didn't decide. The right audience, creatives that answer objections and controlled frequency are the three conditions for success. To find new people, use [lookalike audiences](/en/blog/lookalike-audiences/).
""",
},
"tiktok-ads-ozbekistonda": {
"uz": """
TikTok — qisqa videolar platformasi, u yerda reklama Instagram'dan boshqacha ishlaydi: odamlar ko‘ngilochar kontent uchun keladi va reklama ham shunday ko‘rinishi kerak. Bu maqolada TikTok Ads qaysi bizneslarga mos kelishini, boshlashdan oldin nimani tekshirish kerakligini va qanday kreativ ishlashini ko‘rib chiqamiz.

## Avval tekshiring: auditoriyangiz TikTok'dami

O‘zbekistonda TikTok'ning ishlashi turli davrlarda cheklangan. Shuning uchun byudjet ajratishdan oldin ikki narsani tekshiring:

1. Mijozlaringiz hozir ilovadan faol foydalanyaptimi — ulardan so‘rang, raqobatchilarning TikTok faolligiga qarang.
2. TikTok Ads Manager sizning akkauntingiz uchun O‘zbekistonni target qilishga ruxsat beradimi va to‘lov qabul qiladimi.

Agar javob «yo‘q» bo‘lsa, xuddi shu vertikal videolarni Instagram Reels va YouTube Shorts'da ishlatish mumkin.

## Kimga ayniqsa mos keladi

- Yosh auditoriyaga mo‘ljallangan mahsulotlar: kiyim, kosmetika, gadjetlar.
- Ovqat, kafe va yetkazib berish xizmatlari.
- Ta'lim: til kurslari, IT, onlayn darslar.
- Ko‘rgazmali natijasi bor xizmatlar: go‘zallik, ta'mir, avtomobil detailing.

## Boshlash: 5 qadam

1. **TikTok Ads Manager**'da (ads.tiktok.com) biznes akkaunti oching va kompaniya ma'lumotlarini kiriting.
2. To‘lov usulini qo‘shing.
3. Saytingiz bo‘lsa, TikTok Pixel'ni o‘rnating va asosiy hodisalarni sozlang.
4. Kampaniya maqsadini tanlang: trafik, ariza yoki konversiya.
5. 3–5 ta turli video bilan kichik byudjetda test kampaniya ishga tushiring.

## TikTok'da qanday kreativ ishlaydi

- **Reklamaga o‘xshamasin.** Professional rolik emas, telefonda olingan jonli video yaxshiroq ishlaydi.
- **Birinchi 2 soniya — hook.** Muammo, natija yoki kutilmagan harakat. Batafsil — [Reels uchun hooklar](/blog/reels-uchun-hooklar/) maqolasida.
- **Ovoz va subtitr.** TikTok'da ko‘pchilik ovoz bilan ko‘radi, lekin subtitr baribir kerak.
- **Odam kameraga gapiradi.** Asoschi, sotuvchi yoki mijoz — yuz ishonch uyg‘otadi.
- **Spark Ads.** Yaxshi organik videoni reklama sifatida ko‘tarish — u layk va izohlarini saqlab qoladi.

## Natijani qanday baholash

TikTok'da bosishlar arzon bo‘lishi mumkin, lekin asosiy ko‘rsatkich — ariza va sotuv narxi. Ularni Meta reklamasi bilan bir xil usulda solishtiring: sarf, arizalar, CPL va sotuvga konversiya. Kreativlarni qanday solishtirish haqida — [A/B test](/blog/kreativlar-ab-test/) maqolasida.

## Xulosa

TikTok Ads — yosh va faol auditoriyaga chiqishning kuchli kanali, lekin avval auditoriyangiz u yerdaligini va platforma O‘zbekistonda ishlashini tekshiring. Videolar esa har qanday holatda Reels va Shorts uchun ham yaraydi. Level Marketing videograflari bitta suratga olishdan bir nechta platforma uchun kreativ tayyorlaydi.
""",
"ru": """
TikTok — платформа коротких видео, и реклама в нём работает иначе, чем в Instagram: люди приходят за развлекательным контентом, и реклама должна выглядеть так же. Разберём, каким бизнесам подходит TikTok Ads, что проверить перед стартом и какие креативы работают.

## Сначала проверьте: есть ли ваша аудитория в TikTok

Работа TikTok в Узбекистане в разные периоды ограничивалась. Поэтому прежде чем выделять бюджет, проверьте две вещи:

1. Пользуются ли ваши клиенты приложением активно сейчас — спросите их, посмотрите на активность конкурентов в TikTok.
2. Позволяет ли TikTok Ads Manager вашему аккаунту таргетироваться на Узбекистан и принимает ли оплату.

Если ответ «нет», те же вертикальные видео можно использовать в Instagram Reels и YouTube Shorts.

## Кому особенно подходит

- Товары для молодой аудитории: одежда, косметика, гаджеты.
- Еда, кафе и доставка.
- Образование: языковые курсы, IT, онлайн-уроки.
- Услуги с наглядным результатом: бьюти, ремонт, автодетейлинг.

## Как начать: 5 шагов

1. В **TikTok Ads Manager** (ads.tiktok.com) создайте бизнес-аккаунт и заполните данные компании.
2. Добавьте способ оплаты.
3. Если есть сайт, установите TikTok Pixel и настройте ключевые события.
4. Выберите цель кампании: трафик, лиды или конверсии.
5. Запустите тестовую кампанию на небольшой бюджет с 3–5 разными видео.

## Какие креативы работают в TikTok

- **Не похоже на рекламу.** Живое видео на телефон работает лучше профессионального ролика.
- **Первые 2 секунды — хук.** Проблема, результат или неожиданное действие. Подробнее — в [статье о хуках для Reels](/ru/blog/huki-dlya-reels/).
- **Звук и субтитры.** В TikTok многие смотрят со звуком, но субтитры всё равно нужны.
- **Человек говорит в камеру.** Основатель, продавец или клиент — лицо вызывает доверие.
- **Spark Ads.** Продвижение удачного органического видео как рекламы — оно сохраняет лайки и комментарии.

## Как оценивать результат

Клики в TikTok могут быть дешёвыми, но главный показатель — цена заявки и продажи. Сравнивайте их так же, как рекламу в Meta: расход, заявки, CPL и конверсия в продажу. Как сравнивать креативы — в статье про [A/B-тесты](/ru/blog/ab-test-kreativov/).

## Вывод

TikTok Ads — сильный канал выхода на молодую активную аудиторию, но сначала убедитесь, что ваша аудитория там есть и платформа работает в Узбекистане. Видео в любом случае пригодятся для Reels и Shorts. Видеографы Level Marketing делают из одной съёмки креативы сразу под несколько площадок.
""",
"en": """
TikTok is a short-video platform, and advertising there works differently from Instagram: people come for entertainment, and your ads have to look the same way. Here is which businesses TikTok Ads suit, what to check before you start and which creatives work.

## Check first: is your audience on TikTok

TikTok's availability in Uzbekistan has been restricted at different times. So before committing a budget, check two things:

1. Are your customers actively using the app right now? Ask them and look at competitors' TikTok activity.
2. Does TikTok Ads Manager let your account target Uzbekistan and accept your payment?

If the answer is no, the same vertical videos can run on Instagram Reels and YouTube Shorts.

## Who it suits best

- Products for a young audience: clothing, cosmetics, gadgets.
- Food, cafés and delivery.
- Education: language courses, IT, online lessons.
- Services with visible results: beauty, renovation, car detailing.

## Getting started: 5 steps

1. In **TikTok Ads Manager** (ads.tiktok.com), open a business account and fill in your company details.
2. Add a payment method.
3. If you have a website, install the TikTok Pixel and set up key events.
4. Choose a campaign objective: traffic, leads or conversions.
5. Launch a small-budget test campaign with 3–5 different videos.

## Which creatives work on TikTok

- **Don't look like an ad.** A lively phone-shot video beats a polished commercial.
- **The first 2 seconds are the hook.** A problem, a result or an unexpected action. More in our [Reels hooks](/en/blog/reels-hooks/) article.
- **Sound and captions.** Many TikTok users watch with sound, but captions are still a must.
- **A person talking to camera.** A founder, seller or customer — a face builds trust.
- **Spark Ads.** Boosting a strong organic video as an ad keeps its likes and comments.

## How to judge results

Clicks on TikTok can be cheap, but what matters is cost per lead and per sale. Compare them the same way as your Meta ads: spend, leads, CPL and conversion to sale. For comparing creatives, see our [A/B testing](/en/blog/ab-testing-ad-creatives/) guide.

## Conclusion

TikTok Ads is a strong channel for reaching a young, active audience, but first make sure your audience is there and the platform works in Uzbekistan. Either way, the videos will serve you on Reels and Shorts. Level Marketing's videographers turn one shoot into creatives for several platforms at once.
""",
},
"kreativlar-ab-test": {
"uz": """
Qaysi reklama yaxshiroq ishlashini oldindan bilib bo‘lmaydi — tajribali targetolog ham taxmin qiladi. Shuning uchun professional reklama **A/B test** orqali boshqariladi: bir nechta variant bir vaqtda ishga tushadi va raqamlar g‘olibni aniqlaydi. Bu maqolada nimani, qanday va qancha vaqt test qilish kerakligini ko‘rib chiqamiz.

## A/B test nima

A/B test — ikki yoki undan ortiq variantni bir xil sharoitda solishtirish, bunda **faqat bitta element** farq qiladi. Masalan, bir xil auditoriya va byudjet, lekin videoning birinchi soniyalari har xil. Shunda natijadagi farq aynan shu elementga bog‘liq ekanini bilasiz.

## Nimani test qilish kerak

| Element | Misol | Ta'siri |
|---|---|---|
| Hook (boshlanish) | Muammo bilan yoki natija bilan | Juda katta |
| Taklif | «Chegirma 10%» yoki «O‘lchov bepul» | Juda katta |
| Format | Video yoki karusel | Katta |
| Matn | Qisqa yoki batafsil | O‘rtacha |
| Auditoriya | Qiziqishlar yoki Advantage+ | O‘rtacha |
| Tugma | «Batafsil» yoki «Xabar yuborish» | Kichik |

Avval eng katta ta'sirga ega elementlardan boshlang: hook va taklif.

## Qanday o‘tkaziladi: 5 qadam

1. **Gipoteza yozing.** «Natijadan boshlangan video ariza narxini pasaytiradi».
2. **Bitta o‘zgaruvchi tanlang.** Qolgan hamma narsa bir xil bo‘lsin.
3. **Ishga tushiring.** Meta'da A/B test (Experiments) vositasidan foydalanish yoki alohida reklama to‘plamlarini teng byudjet bilan ishga tushirish mumkin.
4. **Yetarli ma'lumot to‘plang.** Har bir variant bir necha o‘nlab natija (bosish, xabar yoki ariza) to‘plaguncha va kamida 4–7 kun kuting.
5. **Xulosa qiling va yozib qo‘ying.** G‘olibni qoldiring, yutqazganini o‘chiring va natijani test jurnaliga yozing.

## G‘olibni qanday aniqlash

Asosiy ko‘rsatkich — **ariza narxi (CPL)** va iloji bo‘lsa, sotuvga konversiya. CTR va bitta bosish narxi yordamchi ko‘rsatkichlar: arzon bosish ko‘p, lekin ariza yo‘q bo‘lsa, kreativ «qiziqarli», ammo sotmaydi. CPL nima ekanligi haqida — [CPL bo‘yicha qo‘llanmamizda](/blog/lid-narxi-cpl-qanday-kamaytirish/).

## Test jurnali

Har bir testni oddiy jadvalda qayd eting:

| Sana | Gipoteza | Variantlar | Natija (CPL) | Xulosa |
|---|---|---|---|---|
| 1-hafta | Hook: muammo va natija | A / B | A arzonroq | Muammodan boshlash ishlaydi |

Bir necha oydan keyin bu jadval sizning auditoriyangiz uchun nima ishlashini ko‘rsatadigan qimmatli bilim bazasiga aylanadi.

## Ko‘p uchraydigan xatolar

- Bir vaqtda bir nechta narsani o‘zgartirish.
- Testni 1–2 kundan keyin to‘xtatish.
- Juda kichik byudjet — hech qaysi variant yetarli natija to‘plamaydi.
- G‘olibni topib, yangi testni boshlamaslik — kreativlar vaqt o‘tib «charchaydi».

## Xulosa

A/B test reklamani taxmindan raqamlarga o‘tkazadi. Har hafta kamida bitta test — reklamani doimiy yaxshilab borishning eng oddiy usuli. Kreativlar uchun g‘oyalar — [video reklama turlari](/blog/video-reklama-turlari/) maqolasida.
""",
"ru": """
Заранее узнать, какая реклама сработает лучше, невозможно — даже опытный таргетолог лишь предполагает. Поэтому профессиональная реклама управляется через **A/B-тесты**: несколько вариантов запускаются одновременно, и победителя определяют цифры. Разберём, что, как и сколько тестировать.

## Что такое A/B-тест

A/B-тест — сравнение двух или более вариантов в одинаковых условиях, когда отличается **только один элемент**. Например, одинаковые аудитория и бюджет, но разные первые секунды видео. Тогда разница в результате объясняется именно этим элементом.

## Что тестировать

| Элемент | Пример | Влияние |
|---|---|---|
| Хук (начало) | С проблемы или с результата | Очень большое |
| Оффер | «Скидка 10%» или «Замер бесплатно» | Очень большое |
| Формат | Видео или карусель | Большое |
| Текст | Короткий или подробный | Среднее |
| Аудитория | Интересы или Advantage+ | Среднее |
| Кнопка | «Подробнее» или «Отправить сообщение» | Небольшое |

Начинайте с элементов с наибольшим влиянием: хука и оффера.

## Как провести: 5 шагов

1. **Сформулируйте гипотезу.** «Видео, начинающееся с результата, снизит цену заявки».
2. **Выберите одну переменную.** Всё остальное одинаково.
3. **Запустите.** В Meta можно использовать инструмент A/B-тестов (Experiments) или запустить отдельные группы объявлений с равным бюджетом.
4. **Наберите достаточно данных.** Подождите, пока каждый вариант наберёт несколько десятков результатов (кликов, сообщений или заявок), и минимум 4–7 дней.
5. **Сделайте вывод и запишите.** Победителя оставьте, проигравшего отключите, результат внесите в журнал тестов.

## Как определить победителя

Главный показатель — **цена заявки (CPL)** и, если возможно, конверсия в продажу. CTR и цена клика — вспомогательные: если кликов много и они дешёвые, а заявок нет, креатив «интересный», но не продающий. Что такое CPL — в нашем [гиде по CPL](/ru/blog/tsena-lida-cpl-kak-snizit/).

## Журнал тестов

Фиксируйте каждый тест в простой таблице:

| Дата | Гипотеза | Варианты | Результат (CPL) | Вывод |
|---|---|---|---|---|
| 1-я неделя | Хук: проблема против результата | A / B | A дешевле | Начинать с проблемы работает |

Через несколько месяцев эта таблица превращается в ценную базу знаний о том, что работает именно на вашу аудиторию.

## Частые ошибки

- Менять несколько вещей одновременно.
- Останавливать тест через 1–2 дня.
- Слишком маленький бюджет — ни один вариант не набирает достаточно результатов.
- Найти победителя и не запускать новый тест — креативы со временем «выгорают».

## Вывод

A/B-тесты переводят рекламу из догадок в цифры. Минимум один тест в неделю — самый простой способ постоянно улучшать рекламу. Идеи для креативов — в статье о [видах видеорекламы](/ru/blog/vidy-videoreklamy/).
""",
"en": """
You can't know in advance which ad will perform best — even an experienced specialist is only guessing. That's why professional advertising runs on **A/B tests**: several versions launch at once and the numbers pick the winner. Here is what to test, how and for how long.

## What an A/B test is

An A/B test compares two or more versions under the same conditions, with **only one element** different. For example, the same audience and budget but a different opening for the video. Then any difference in results comes down to that element.

## What to test

| Element | Example | Impact |
|---|---|---|
| Hook (opening) | Start with a problem or a result | Very high |
| Offer | "10% off" or "Free measurement" | Very high |
| Format | Video or carousel | High |
| Copy | Short or detailed | Medium |
| Audience | Interests or Advantage+ | Medium |
| Button | "Learn more" or "Send message" | Low |

Start with the elements that matter most: the hook and the offer.

## How to run it: 5 steps

1. **Write a hypothesis.** "A video that opens with the result will lower cost per lead."
2. **Pick one variable.** Keep everything else identical.
3. **Launch.** In Meta you can use the A/B test (Experiments) tool or run separate ad sets with equal budgets.
4. **Collect enough data.** Wait until each version has a few dozen results (clicks, messages or leads) and at least 4–7 days have passed.
5. **Conclude and record.** Keep the winner, switch off the loser and log the result.

## How to pick the winner

The main metric is **cost per lead (CPL)** and, where possible, conversion to sale. CTR and cost per click are secondary: lots of cheap clicks with no leads means the creative is "interesting" but doesn't sell. More on CPL in our [CPL guide](/en/blog/cost-per-lead-cpl-how-to-lower/).

## A test log

Record every test in a simple table:

| Date | Hypothesis | Versions | Result (CPL) | Conclusion |
|---|---|---|---|---|
| Week 1 | Hook: problem vs result | A / B | A cheaper | Opening with the problem works |

After a few months this table becomes a valuable knowledge base about what works for your audience.

## Common mistakes

- Changing several things at once.
- Stopping a test after 1–2 days.
- A budget too small for any version to collect enough results.
- Finding a winner and not starting the next test — creatives wear out over time.

## Conclusion

A/B testing moves your advertising from guesswork to numbers. At least one test a week is the simplest way to keep improving. For creative ideas, see [7 types of video ads](/en/blog/types-of-video-ads/).
""",
},
}
