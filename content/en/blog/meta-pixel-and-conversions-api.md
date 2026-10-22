---
title: Meta Pixel and Conversions API: why you need them and how to set them up
description: How Meta Pixel and the Conversions API help your ads, which events to track and the most common setup mistakes.
date: 2026-10-22
slug: meta-pixel-and-conversions-api
type: article
tags: paid ads, meta ads
key: meta-pixel-conversions-api
rubric: target
---

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

## More on this topic

- [Lookalike audiences: how to find people like your customers](/en/blog/lookalike-audiences/)
- [Retargeting: how to bring back people who didn't buy](/en/blog/how-retargeting-works/)
- [How to set up Instagram ads: a step-by-step guide](/en/blog/how-to-set-up-instagram-ads/)
