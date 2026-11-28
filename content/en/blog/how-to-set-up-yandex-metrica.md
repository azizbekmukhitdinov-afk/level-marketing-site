---
title: How to set up Yandex Metrica: counter, goals and Webvisor
description: Setting up Yandex Metrica from scratch: installing the counter, goals, Webvisor, UTM tags and linking Yandex Direct. With an illustrative calculation and common mistakes.
date: 2026-11-28
slug: how-to-set-up-yandex-metrica
type: article
tags: Yandex Metrica, web analytics, Yandex Direct, website
key: yandex-metrika-sozlash
rubric: target
---

Money is going into Yandex Direct, people are landing on the site, yet nobody can say for sure which keyword brought in an enquiry. **Yandex Metrica** is a free web analytics service: it records visits, traffic sources and on-site actions, and its Webvisor feature replays a visit almost like a video. This guide covers the setup order from installing the counter to linking Direct, the decision rules and the typical mistakes.

## What Metrica gives you and how it differs from GA4

A common line is "we already have Google Analytics, we don't need Metrica". If you run Yandex Direct, Metrica is close to mandatory: Direct's strategies and reports rely on its data. Running both services side by side is normal; they don't interfere with each other.

| Question | Yandex Metrica | Google Analytics 4 |
|---|---|---|
| Works best with | Yandex Direct | Google Ads |
| Visit recordings (like a video) | Yes, Webvisor | Not built in |
| Target action | "Goals" | "Key events" |
| Quick start | Many ready-made goal types | Events often need manual setup |

For GA4 details see [Google Analytics 4 basics: setup for a small business website](/en/blog/google-analytics-4-basics/). Small differences between the two systems' numbers are normal, because they count visits differently.

## Step 1: create the counter

The counter is the code you put on your site. The order:

1. Go to metrika.yandex.ru with the **company's** Yandex account, not an employee's or developer's. When the partnership ends, the statistics would leave with them.
2. Add a counter: name, site domain, time zone (Tashkent).
3. In the main settings, switch on the **Webvisor, scroll map and form analytics** option. According to Yandex's help, you can enable it when creating the counter or later in the counter settings ([Yandex Metrica help, in Russian](https://yandex.ru/support/metrika/general/creating-counter.html)).
4. Install the code: on a ready-made platform (CMS) through a dedicated field or plugin; on a custom site on every page; through Tag Manager if you use it.

If your site has many buttons and forms, or a Meta Pixel as well, it's easier to manage all the codes in one place. That's covered in [Google Tag Manager basics: tags, triggers and clean setup](/en/blog/google-tag-manager-basics/).

**Check.** After installing, open the site on your phone and a few minutes later look for the visit in today's report. If it isn't there, the code is missing from some pages or carries another counter's number.

## Step 2: goals

A goal is an action that matters to you: an enquiry, a tap on the phone number, a jump to Telegram. Without goals Metrica only shows "how many people came", which is half the picture for a business.

Yandex's help lists 16 goal types, including page visits, form submission, click on a phone number, jump to a messenger, button click, JavaScript event and composite (multi-step) goals ([goal types](https://yandex.ru/support/metrika/general/goals.html)). A small business site usually needs these:

| Goal | Type | Why |
|---|---|---|
| Enquiry sent | Form submission or "Thank you" page visit | Main goal, CPL is calculated on it |
| Call button | Click on a phone number | Common in mobile traffic |
| Telegram / WhatsApp | Jump to a messenger | For people who write instead of filling the form |
| Prices page | Page visit | A sign of interest, not a main goal |

Rules worth knowing (source: [Yandex Metrica help](https://yandex.com/support/metrica/ru/general/multi)):

- one counter can hold **up to 200 goals**;
- statistics for a new goal start within a few minutes, with nothing backfilled, so create goals **before** launching ads;
- editing a goal doesn't change data already collected;
- if you delete a goal, its data disappears from reports.

**Auto-goals.** Metrica can automatically record clicks on phone numbers, email addresses and messenger links. According to the help, automatic goals don't count towards the overall limit and can't be used inside a composite goal ([auto-goals](https://yandex.com/support/metrica/ru/general/auto-goals)). They're handy to start with, but set up your main goal, the enquiry, yourself and precisely.

**Decision rule:** one main goal (the action closest to money) and 2–4 supporting ones. Don't make "30 seconds on site" or "viewed 2 pages" the main goal for a Direct strategy: the algorithm will start chasing cheap visits from people who don't buy. Why that happens is explained in [What is conversion rate? How to calculate and improve it](/en/blog/what-is-conversion-rate/).

## Step 3: Webvisor

Webvisor records a visit: mouse movement, scrolling, clicks, form filling. Numbers tell you "what" happened; Webvisor shows you "why".

According to Yandex's help, recordings are kept for **15 days** including the current day, and the number of recordings per day is set by a special algorithm ([Webvisor requirements and limits](https://yandex.ru/support/metrica/webvisor/requirements.html)). So Webvisor isn't an archive: review problems within two weeks.

Recordings worth watching:

- **came from ads and didn't reach a goal**: where did they stop;
- **left an enquiry**: which blocks did they read, did they go back to prices;
- **mobile visits**: does the button fit on screen, does the keyboard hide the form.

Twenty to thirty recordings a week is enough. If the same problem shows up five or six times, it isn't chance and needs fixing. On page structure, see [A landing page that converts: the structure, block by block](/en/blog/landing-page-that-converts/).

## Step 4: UTM tags

Metrica separates traffic from Direct, organic search and social networks on its own, but for accurate data on Instagram ads, Telegram posts or partner sites, add UTM tags to your links. Naming rules and a template are in [UTM tags: how to know where every customer came from](/en/blog/utm-tags/). In Metrica you'll find the results in the UTM tags report in the sources section.

The core rule stays the same: lowercase only, one channel always gets the same name, and all names live in one spreadsheet.

## Step 5: link Yandex Direct

People often skip this step and end up with confusing reports.

**Attach the counter to the campaign.** In Direct, choose your Metrica counter in the campaign settings. According to the help, if the counter isn't attached, ad clicks show up in Metrica under a "third-party campaigns" source ([connecting Direct reports](https://yandex.ru/support/metrika/general/direct.html)).

**The yclid tag.** Direct automatically adds yclid, a unique click ID, to the link, and the counter uses it to tie a visit to a specific click. If you use redirects, make sure yclid reaches the final URL.

**Dynamic parameters.** Direct fills in parameters such as {keyword}, {campaign_id}, {source} and {device_type} in your link ([URL parameters](https://yandex.ru/support/direct/statistics/url-tags.html)). For example:

`https://sayt.uz/?utm_source=yandex&utm_medium=cpc&utm_campaign={campaign_id}&utm_term={keyword}`

The keyword then reaches your CRM together with the enquiry, and you can see which search phrase produced a sale.

**Connect the goal to the strategy.** Direct's automatic strategies optimise for Metrica goals, so pick your main goal, the enquiry, in the strategy. Whether Direct makes sense for you at all is covered in [Yandex Direct in Uzbekistan: when it helps and how to start](/en/blog/yandex-direct-in-uzbekistan/).

## Illustrative example: one month in numbers

Illustrative example. A furniture store spent 4,000,000 soums on Direct in a month. Metrica shows:

| Metric | Value |
|---|---|
| Visits from Direct | 1,600 |
| "Enquiry sent" goal | 48 |
| "Call button" | 32 |
| "Jump to Telegram" | 20 |
| Total contacts | 100 |
| Cost per contact | 4,000,000 / 100 = 40,000 soums |

Now Webvisor: most mobile visits stop at the form and leave; the form has 7 fields. The fields are cut to 3, and next month, on the same budget, enquiries rise from 48 to, say, 70 (also an illustrative figure). Cost per contact drops to roughly 32,000 soums.

The next step is reconciling with the CRM. Metrica may show 100 contacts while the CRM holds 76 real leads: repeat clicks, unanswered calls, one person writing through two channels. That gap is normal, and the reasons are covered in [Ads Manager leads don't match your CRM: 7 causes and a check](/en/blog/ad-leads-vs-crm-mismatch/).

## Common mistakes

- **The counter sits in the developer's account.** The partnership ends and the history goes with it.
- **Two counters on one site** (old and new). Numbers get split or double-counted.
- **Goals created after ads launched.** The first week has no conversions, so the strategy learns blind.
- **A "light" action as the main goal.** Direct brings cheap visits, but enquiries don't grow.
- **Counter not attached to the campaign.** Ad traffic lands in the wrong source in reports.
- **Webvisor switched off, or nobody watches it.** Recordings disappear after 15 days.
- **Office staff visits.** On a small site your own team noticeably skews the numbers, so filter them out.

## Questions and answers

### The site already has Google Analytics. Do I need Metrica too?

If you run Yandex Direct, yes: Direct's strategies and reports rely on Metrica goals. If you only use Google Ads and Meta, Metrica isn't required, but it's worth installing for Webvisor alone.

### Does Webvisor slow the site down?

Any extra script adds some load to a page. In practice, the main speed problems on small business sites are heavy images and unnecessary scripts. Measure speed before and after installing and compare.

### Why do Direct and Metrica show different click numbers?

Direct counts clicks; Metrica counts visits. If someone clicks and leaves before the page loads, Direct has a click and Metrica has no visit. Direct also counts only clicks that passed its click-fraud filter ([Direct help, in Russian](https://yandex.ru/support/direct/ru/statistics/metrika)).

### When should I test my goals?

Right after creating them: fill in the form yourself, tap the button and a few minutes later check that the goal shows up in the report. After that, reconcile Metrica enquiries with the CRM once a month.

## Conclusion

Setting up Yandex Metrica properly is a one-day job: one counter in the company account, 3–5 goals created before ads go live, Webvisor switched on, UTM tags, and the counter attached to your Direct campaigns. After that, half an hour a week: goal trends, 20–30 Webvisor recordings and a monthly CRM check. That's how you manage an ad budget by numbers instead of gut feeling.

During a free audit, Level Marketing can check whether the Metrica counter, goals and Direct link on your site are working correctly.

## More on this topic

- [Yandex Direct in Uzbekistan: when it helps and how to start](/en/blog/yandex-direct-in-uzbekistan/)
- [UTM tags: how to know where every customer came from](/en/blog/utm-tags/)
- [Google Analytics 4 basics: setup for a small business website](/en/blog/google-analytics-4-basics/)
