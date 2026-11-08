---
title: How to measure offline advertising: QR codes, promo codes, CRM
description: How to measure offline advertising: QR codes, promo codes, a separate phone number and a "how did you hear about us" field in your CRM for signs, banners and flyers.
date: 2026-11-08
slug: measure-offline-advertising
type: article
tags: sales, analytics, offline advertising, crm
key: oflayn-reklama-natijasi
rubric: sotuv
---

A logo on the company car, a banner by the road, flyers at a trade show. The money is spent, but nobody can say for sure whether any of it brought customers. You can measure offline advertising — but you have to plan it **before** the ad goes up. This article covers four simple methods, how to connect them to your CRM, and a table for the monthly tally.

![Why offline advertising is invisible](/img/blog/illus/oflayn-reklama-natijasi-1.jpg 1200x675)

## Why offline advertising is "invisible"

Instagram and Google ads log every click: who tapped, which ad, whether they left a lead afterwards. A banner or a shop sign has no such counter. Someone sees the banner, remembers it, and three days later searches for the brand on Instagram or just walks into the store. In your report, that customer shows up as "organic" or "direct".

So offline ads need their own **trace** — a marker that shows where a customer came from. There are four kinds:

| Method | What it shows | Where it fits |
|---|---|---|
| QR code + UTM | Who scanned and went to the site or bot | Flyers, menus, parcels, trade show stands |
| Promo code | Who mentioned the code when buying | Banners, radio, bloggers, flyers |
| Separate phone number or bot link | Which number got the call | Vehicles, billboards, newspapers |
| "How did you hear about us?" | What the customer remembers | Everywhere, as a cross-check |

No single method shows everything. The best setup is one main trace per ad placement plus one shared question for every customer.

## Method 1: QR code and UTM tag

A QR code doesn't count anything by itself — it just opens a link. To count, you add a UTM tag to that link, the same way as in online ads. Google Analytics Help says every tagged link should include at least three parameters: `utm_source`, `utm_medium` and `utm_campaign` ([Google Analytics Help](https://support.google.com/analytics/answer/10917952)). More on this in [UTM tags](/en/blog/utm-tags/).

Name offline placements consistently:

- `utm_medium=qr` — the same for every QR code;
- `utm_source` — the placement: `flyer-tradeshow`, `menu-table`, `parcel`;
- `utm_campaign` — the period or promotion: `november-2026`.

**Key rules:**

1. A **separate** QR code for every placement. If one code sits on all flyers and banners, you won't know which one worked.
2. A long link makes the QR code dense and tiny. Use a short link and test the code on 2–3 different phones before printing.
3. Give people a reason next to the code: "Scan for the price list" or "Scan for 10% off". Codes without a reason get few scans.
4. Check QR codes in public places now and then to make sure nobody has stuck another code on top. There are reports of scammers in some cities pasting their own codes over real ones ([Sostav](https://www.sostav.ru/blogs/276144/52774)).

No website? The QR code can lead to a Telegram bot. Create a separate link with a start parameter for each placement, and the bot records which link a person came through. More in [Telegram bot for leads](/en/blog/telegram-bot-for-leads/).

## Method 2: promo code

A promo code is a trace that works even if nobody scans anything. The customer says the code at the checkout or on the phone, and you know which ad it came from.

To make promo codes work:

- **One code per placement.** For example, `CHILONZOR` for the banner in Chilanzar and `SERGELI` for the one on the Sergeli road. A single shared code only tells you whether the promotion worked overall.
- **A reason to say it.** A small discount, a gift or free delivery. Without a reason, nobody mentions the code.
- **Easy to say.** One word, no digits or tricky letters. Not "X7QK2", but "BAHOR".
- **A field for the code in the till or CRM.** If the cashier writes codes on a scrap of paper, it'll be gone by the end of the month.

The downside: codes travel. A customer sends the code to a friend on Telegram, and now it looks like a banner result when it's really a referral. Treat promo code numbers as approximate and compare them with other methods.

## Method 3: a separate number or bot link

On a vehicle, a billboard or in a newspaper, people don't scan QR codes or remember promo codes. They see a number and call it. If those placements carry a **separate phone number**, the number of calls is a ready-made result.

In practice it looks like this (illustrative example): a furniture store puts the number of a separate SIM card, not its main line, on the company van. Calls to that number are counted separately for the month, and the manager tags them in the CRM with the source "vehicle".

If customers mostly message on Telegram, use a short link to the bot or channel instead of a number — with its own start parameter for each placement.

This is the most accurate method, but it takes discipline: calls to the separate number need answering just as fast as the main line. A missed call looks like the ad didn't work, when in fact the sales team didn't.

![Method 4: How did you hear about us? in the CRM](/img/blog/illus/oflayn-reklama-natijasi-2.jpg 1200x675)

## Method 4: "How did you hear about us?" in the CRM

This is the cheapest method, and it catches what the others miss: referrals, people walking past, "saw the banner, then found you on Instagram".

But the question has to be asked properly:

- **Pick from a list.** Not free text in the CRM, but fixed options: Instagram, Telegram, Google/maps, banner, vehicle, shop sign, friend's recommendation, other. In free text, "insta", "from instagram" and "IG" end up as three different answers you can't count.
- **A required field.** A manager can't move the lead to the next stage without filling it in.
- **The same wording.** Every manager asks it in the same words. Add it to your [sales script](/en/blog/sales-script/).
- **"Where did you first hear about us?"** and **"What made you get in touch today?"** are two different questions. The first shows which ad introduced you; the second shows which one prompted action. If you keep only one, decide which one you mean.

The downside: people forget, or name the last thing they saw. So use it as a **cross-check** rather than the only source, and compare it with promo codes and calls.

## Pulling it all into one table

If the methods live in separate places, you end the month with numbers from four different sources. Put them in one table — one row per offline placement:

| Placement | Spend | QR visits | Promo code | Calls | "Heard about us" | Sales | Sales value |
|---|---|---|---|---|---|---|---|
| Banner in Chilanzar | 4M UZS | — | 9 | — | 14 | 6 | 21M UZS |
| Company vehicle | 1M UZS | — | — | 11 | 5 | 2 | 7M UZS |
| Trade show flyers | 2M UZS | 38 | 4 | — | 3 | 1 | 3M UZS |

*Illustrative example: the numbers only show how to fill in the table.*

Look at two things:

1. **Cost per sale** — spend divided by the number of sales. Compare it with your customer acquisition cost from online ads.
2. **Did it pay off** — compare the profit from those sales with the spend. How to do it: [ROMI: is your marketing paying off](/en/blog/how-to-calculate-romi/).

Offline ads work slowly: someone sees a banner today and comes in two weeks later. So judge results over at least a month, ideally two or three — not a week.

## Seeing the effect of offline on online

Many people who see a banner don't scan anything — they search for the brand name later. You can see that effect indirectly:

- **Branded searches.** Your Google Business Profile and Yandex Business listing show searches and direction requests. Did they grow in the month the banner was up? More in [add your business to maps](/en/blog/add-your-business-to-maps/).
- **Instagram profile visits.** Did profile visits and follower growth change during the banner period?
- **Leads from the area.** If the banner is in one district, watch the share of CRM leads from that district.

None of this is hard proof, since other things can change at the same time. But when several signals move in the same direction, you can draw a conclusion.

![A one-month plan, step by step](/img/blog/illus/oflayn-reklama-natijasi-3.jpg 1200x675)

## A one-month plan, step by step

1. **Before launch:** choose a trace for each offline placement — QR, promo code or number.
2. **Prepare the CRM:** add offline options to the "Source" field, create a promo code field, make the source field required.
3. **Train managers:** one question, one way of recording it.
4. **Check before printing:** do the QR codes open, are the UTMs correct, does the promo code work at the till.
5. **Every week:** copy QR visits, calls and promo codes into the table.
6. **At month end:** add sales and amounts, calculate cost per sale, and decide which placements to keep and which to stop.

## Questions and answers

**Isn't this too complicated for a small shop?**
No. The simplest version is a "How did you hear about us?" column in your CRM — or even in Google Sheets — plus one promo code per banner. That's a day's work.

**Where do I see how many times a QR code was scanned?**
If the UTM-tagged link leads to a website, in Google Analytics by source and medium. If it leads to a bot, in the bot itself by start parameter. Some QR services show scan counts too, but that data stays on their servers.

**The customer says "Instagram", but actually saw the banner. What now?**
That's normal. Don't rely on one question: compare with promo codes, the separate number and growth in branded searches. When several sources point the same way, you can trust the picture more.

**If results are poor, should I stop the ad right away?**
Check first: did the trace work, did managers ask the question, were calls answered? Offline ads are slow, so give them at least a month.

## Conclusion

Measuring offline advertising doesn't require a complex system. A trace for every placement — QR, promo code or number — plus a required "How did you hear about us?" field in the CRM is enough. What matters is planning it before the ad goes live and comparing everything in one table at month end. At Level Marketing we try to look at online and offline sources in a single report with our clients, so it's clear where the budget actually goes.

## More on this topic

- [UTM tags: how to know where every customer came from](/en/blog/utm-tags/)
- [Ads Manager leads don't match your CRM: 7 causes and a check](/en/blog/ad-leads-vs-crm-mismatch/)
- [What an advertising report should include](/en/blog/what-an-ad-report-should-include/)
