---
title: Meta Pixel and Conversions API: why you need them and how to set them up
description: How Meta Pixel and the Conversions API help your ads, which events to track and the most common setup mistakes.
date: 2026-10-22
updated: 2026-10-23
slug: meta-pixel-and-conversions-api
type: article
tags: paid ads, meta ads
key: meta-pixel-conversions-api
rubric: target
---

Are your ads bringing sales, or just clicks? Only tracking can answer that precisely. Meta advertising has two tracking tools for it: **Meta Pixel** and the **Conversions API**. Here is why you need them, which events to track and which setup mistakes to avoid.

![What Meta Pixel is](/img/blog/illus/meta-pixel-conversions-api-1.jpg 1200x675)

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

![What if you don't have a website](/img/blog/illus/meta-pixel-conversions-api-2.jpg 1200x675)

## What if you don't have a website

Many businesses sell through Instagram Direct or Telegram. Then you don't need the Pixel, but you still have to record sales: mark leads in a CRM or spreadsheet and compare which ads bring sales. For calculating cost per lead, see our [CPL guide](/en/blog/cost-per-lead-cpl-how-to-lower/).

## How to check your events

- **Events Manager → Test Events.** Open your site, submit a form and watch whether the event appears in real time.
- **Meta Pixel Helper.** A Chrome extension that shows which events fire on a page.
- **Duplicates.** If the Pixel and Conversions API run together, an event needs the same event_id in both so it isn't counted twice.
- **Match quality.** Events Manager shows a score for how well events are matched to users. If it's low, send extra data through the Conversions API — for example, a hashed phone number.

## Event parameters

Add **value** and **currency** to Purchase and Lead events. Meta can then see which ads bring in more money and optimise towards higher-value customers. Stores with a catalogue also need product IDs (content_ids) — they power dynamic retargeting.

## Privacy and consent

Tell your website users about data collection in your privacy policy. Don't send sensitive data through events: medical conditions, financial circumstances and the like. Clinics need to be especially careful — a page URL or event name must not reveal a condition. Clinic marketing is covered in [Marketing a clinic](/en/blog/marketing-a-clinic/).

![How to use Pixel data](/img/blog/illus/meta-pixel-conversions-api-3.jpg 1200x675)

## How to use Pixel data

- Optimise campaigns for the **Lead** or **Purchase** event, not for clicks.
- Build [retargeting](/en/blog/how-retargeting-works/) audiences from website visitors.
- Create [lookalike audiences](/en/blog/lookalike-audiences/) from leads and buyers.
- See in reports which creative brings in leads.

## Questions and answers

### Do you need a developer to install the Pixel?

Many website builders and CMSs have a ready-made Meta integration — entering the Pixel ID is enough. The Conversions API can often be connected through partner integrations as well. For a complex site or your own server, you'll need a developer.

### Can you put several Pixels on one site?

Technically yes, but it muddles the data. One Pixel per business is better; give your agency access through Business Manager instead.

### How long are Pixel audiences kept?

The maximum retention for a website visitor audience is 180 days. So install the Pixel well before your ads start, so data begins to build up.

### Can you work without the Conversions API?

To start, yes. But browser restrictions and ad blockers mean some data gets lost. Add the Conversions API as your budget grows.

### What if events don't show up in the account?

Check that the code is on every page, the correct Pixel ID is used and your ad blocker is off. Send the event again through Test Events — events can appear with a slight delay.

### Will ads improve as soon as the Pixel is installed?

Not immediately. The algorithm needs enough events to learn from — a new campaign usually spends several days in the "learning phase". Don't change the settings too often during this period, or learning starts over. Judge the results after at least a week.

## Conclusion

The Pixel and the Conversions API are your advertising's eyes. Without them the algorithm works blind and you pay for cheap leads that never turn into sales. At Level Marketing we set up tracking in the first week of every project.

## More on this topic

- [Lookalike audiences: how to find people like your customers](/en/blog/lookalike-audiences/)
- [Retargeting: how to bring back people who didn't buy](/en/blog/how-retargeting-works/)
- [How to set up Instagram ads: a step-by-step guide](/en/blog/how-to-set-up-instagram-ads/)
