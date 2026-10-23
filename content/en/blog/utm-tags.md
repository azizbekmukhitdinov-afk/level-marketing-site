---
title: UTM tags: how to know where every customer came from
description: What UTM is, the parameters, how to build a link, naming rules and where to see results.
date: 2026-10-22
updated: 2026-10-23
slug: utm-tags
type: article
tags: sales, analytics
key: utm-belgilar
rubric: sotuv
---

People arrive at your website from Instagram, Telegram, Google and partner channels — but which of them bring leads and sales? **UTM tags** answer that: small "labels" added to a link that show the source of every visit in your analytics. Here is what UTM is, how to build a link and where to see the results.

## UTM parameters

| Parameter | What it means | Example |
|---|---|---|
| utm_source | Source | instagram, telegram, google |
| utm_medium | Channel type | cpc, post, stories, email |
| utm_campaign | Campaign | sofa_october |
| utm_content | Creative or variant | video_a, banner_b |
| utm_term | Keyword (for search ads) | sofa_tashkent |

An example link:

`https://levelm.uz/en/?utm_source=instagram&utm_medium=cpc&utm_campaign=audit_october&utm_content=video_a`

## How to build the link

- Google's **Campaign URL Builder** — fill in the fields and the link is ready.
- A spreadsheet template: parameters in columns, the final column assembling the link with a formula, so the whole team uses the same names.

## Naming rules

1. Lowercase only: "Instagram" and "instagram" are two different sources in analytics.
2. Underscores or hyphens instead of spaces.
3. The same thing always gets the same name.
4. Write all names down in one document.

## Where to see results

- **Google Analytics 4** — in the traffic acquisition report by source, medium and campaign.
- **Yandex Metrica** — UTM reports.
- **Your CRM** — if you store UTM values with leads from website forms, each sale links to its exact source. For choosing a CRM, see our [separate article](/en/blog/crm-for-small-business/).

## What if you don't have a website

UTM doesn't work inside Instagram and Telegram. Instead:

- For a Telegram channel, create a separate named invite link for each source — more in our [Telegram advertising](/en/blog/telegram-advertising/) article.
- For shops, a separate promo code per channel.
- A "Where did you hear about us?" question on the lead.

## Common mistakes

- Different names for the same campaign.
- UTM tags on internal site links — they overwrite the real source.
- Typos from typing links by hand — always test them.

## A ready-made UTM table (example)

| Channel | utm_source | utm_medium | utm_campaign |
|---|---|---|---|
| Instagram ads | instagram | cpc | sofa_october |
| Instagram bio link | instagram | bio | evergreen |
| Telegram channel post | telegram | post | sofa_october |
| Telegram Ads | telegram | cpc | sofa_october |
| Google search | google | cpc | sofa_october |
| Email newsletter | email | newsletter | november_promo |

Give one campaign the same utm_campaign name across all channels — then its total result shows up in a single row.

## How to read UTM results

In GA4's traffic acquisition report, look at leads (conversions) alongside visits. Judging channels by visits alone leads to the wrong conclusions.

**An example (illustrative numbers):** Instagram ads bring 1,000 visits and 20 leads; a Telegram post brings 300 visits and 15 leads. The first channel brings more people, but the Telegram visitors are much "warmer": 5% versus 2%. A comparison like this shows where to add budget.

## Carrying UTM tags through to the lead

Analytics shows where a visit came from, but to see sales, the UTM values must be stored with the lead itself. A simple way is hidden fields in your website form: when the page opens, the utm_source, utm_medium and utm_campaign values from the link are written into them and go to the CRM together with the lead. After that, your report answers not "which campaign brought how many visits" but "which campaign brought how many sales and how much revenue". Many website builders and CRM integrations already include such fields — check before you set them up.

## Questions and answers

### Do UTM tags hurt your search rankings?

No, as long as UTM tags are only on external links. Don't put them on internal site links, and make sure your pages declare their main address (canonical) correctly.

### Can you shorten a UTM link?

Yes. The short link still opens the full one, and the tags are kept. Just click it once after shortening to check.

### Should the Instagram bio link have UTM tags?

Yes — that separates profile visits from ad traffic. For example: utm_source=instagram and utm_medium=bio.

### When do you need utm_content?

When one campaign has several creatives or one post has several links. For example, video_a and video_b, or "button" and "link in text" — then you can see which variant brought more leads.

## Conclusion

UTM tags are the simplest way to know where each customer came from. Without them you can't calculate [ROMI](/en/blog/how-to-calculate-romi/) or channel performance correctly. Build one template, follow the naming rules and review the results every month.

## More on this topic

- [Repeat sales and LTV: more revenue from existing customers](/en/blog/repeat-sales-and-ltv/)
- [How to collect customer feedback and what to do with it](/en/blog/collecting-customer-feedback/)
- [Cost per lead (CPL): what it is and how to lower it](/en/blog/cost-per-lead-cpl-how-to-lower/)
