---
title: Meta Pixel and Conversions API: 2026 setup guide and changes
description: How to set up Meta Pixel and the Conversions API, which events to track and what changes in your reports from 12 November: a practical 2026 guide.
date: 2026-10-22
updated: 2026-11-09
slug: meta-pixel-and-conversions-api
type: article
tags: paid ads, meta ads
key: meta-pixel-conversions-api
rubric: target
---

Are your ads bringing sales, or just clicks? Only tracking can answer that precisely. Meta advertising has two tracking tools for it: **Meta Pixel** and the **Conversions API**. Here is why you need them, which events to track and what changes in your reports from November 2026.

![What Meta Pixel is](/img/blog/illus/meta-pixel-conversions-api-1.jpg 1200x675)

## What Meta Pixel is

The Pixel is a small piece of code you add to your website. It tells Meta what a visitor did on your site: viewed a page, submitted a form, completed a purchase. As a result:

- you can see in Ads Manager which ads brought leads and sales;
- the algorithm learns to look for people who take exactly that action;
- you can build a [retargeting](/en/blog/how-retargeting-works/) audience of people who visited but didn't buy.

## What the Conversions API is, and why the Pixel isn't enough

The Pixel works through the browser. Because of ad blockers, iOS restrictions and cookie settings, some events never reach Meta. The **Conversions API (CAPI)** sends the same events from your server. Together they give Meta fuller data, and duplicates of the same event are merged using an `event_id` (deduplication).

## What changed in Meta Pixel and the Conversions API in 2026

Three changes in 2026 directly affect tracking. The first is the most urgent.

**1. Measuring conversions on the customer's device.** Pixel settings now include a toggle called **Measure conversions on customer devices**. It matches an ad view to a purchase on the customer's own device, using details the customer already gave the business (an email, for example) and temporary device data. Meta explains it in its [help centre](https://www.facebook.com/business/help/4237575203200036). The setting is on by default for eligible Pixels. It is not active for people in the EU or UK, and Uzbekistan is not part of that exclusion. Events Manager shows [12 November 2026](https://ppc.land/meta-pixel-will-count-more-conversions-from-nov-12-unless-advertisers-opt-out/) as the measurement start date, while Meta's help pages give no date, so check your own account.

**2. One-click Conversions API.** In April 2026 Meta [announced a no-developer option](https://www.facebook.com/business/news/pixel-conversionsapi-updates): the events your Pixel sends are automatically mirrored from the server, and duplicates are merged.

**3. An AI feature in the Pixel.** The Pixel can add page and product details to events on its own: names, availability, business information. You can turn it off in Events Manager or choose which categories to share.

### Does the new setting apply to your site

According to reviews based on Meta's help articles, the feature needs two things: the Pixel sits directly on the page (not in an iframe and not as an image-only pixel), and the site requires login with an email or mobile number.

| Site type | Does the setting work | What to do |
|---|---|---|
| Landing page or form, no accounts | No | Reports won't change; connect the Conversions API |
| Store with guest checkout | Condition not met | Check the status in Settings |
| Store requiring login by email or phone | Yes, by default | Follow the 4 steps below |
| Pixel in an iframe or image-only | No | Place the code directly on the page if you want the feature |
| No website, only Direct and Telegram | No | Record sales in a CRM or spreadsheet |

### 4 steps before 12 November

1. **Check the status.** Events Manager → Data sources → your Pixel → Settings. Is the setting there, and is it on?
2. **Record a baseline.** For the last 2–4 weeks: purchases in Ads Manager, cost per purchase, ROAS and actual sales in your CRM.
3. **Mark the date in your report.** Note when measurement started, so that when someone says "the ads got better" you can check against it.
4. **Compare Ads Manager with your CRM.** If Ads Manager shows more purchases but your CRM and till don't, the measurement changed, not the ads. For how to reconcile them, see [why ad leads and CRM numbers differ](/en/blog/ad-leads-vs-crm-mismatch/).

The attribution window and model don't change; what changes is the set of conversions that can be measured. Knowing how the [attribution window](/en/blog/meta-attribution-window/) works helps you read the report correctly. Cost per purchase may look lower and ROAS higher, even if real sales haven't grown.

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

1. In **Events Manager** (business.facebook.com), use **Connect Data → Web** to create a Pixel or pick an existing one.
2. Add the code to your site. Builders like Tilda, WordPress or Shopify have ready integrations; on a custom site the code goes into the page header or through Google Tag Manager.
3. Set up the key events: at least Lead or Purchase, plus Contact for small businesses.
4. Connect the **Conversions API**. The simplest route is Connect Data → Web → choose your Pixel → See other ways to setup → **Set up with Meta**: free, no developer needed. If you want to choose events yourself, use your platform's integration, a Google Tag Manager server container or a developer.
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
- **Duplicates.** If the Pixel and Conversions API run together, an event needs the same event_id and event name in both so it isn't counted twice. Meta merges them [within 48 hours](https://developers.facebook.com/docs/marketing-api/conversions-api/deduplicate-pixel-and-server-events/) of receiving the first event. With the one-click option, Meta handles this itself.
- **Match quality.** Events Manager shows a score for how well events are matched to users. If it's low, send extra data through the Conversions API — for example, a hashed phone number.

## Event parameters

Add **value** and **currency** to Purchase and Lead events. Meta can then see which ads bring in more money and optimise towards higher-value customers. Stores with a catalogue also need product IDs (content_ids) — they power dynamic retargeting.

## Privacy and consent

Tell your website users about data collection in your privacy policy. Don't send sensitive data through events: medical conditions, financial circumstances and the like. Clinics need to be especially careful — a page URL or event name must not reveal a condition. The one-click Conversions API mirrors everything the Pixel sends with no separate filter, and the Pixel's AI feature adds page data. So clinics and financial sites should check exactly what is being sent before turning them on. That responsibility stays with the advertiser. Clinic marketing is covered in [Marketing a clinic](/en/blog/marketing-a-clinic/).

![How to use Pixel data](/img/blog/illus/meta-pixel-conversions-api-3.jpg 1200x675)

## How to use Pixel data

- Optimise campaigns for the **Lead** or **Purchase** event, not for clicks.
- Build [retargeting](/en/blog/how-retargeting-works/) audiences from website visitors.
- Create [lookalike audiences](/en/blog/lookalike-audiences/) from leads and buyers.
- See in reports which creative brings in leads.

## Questions and answers

### Do you need a developer to install the Pixel?

Many website builders and CMSs have a ready-made Meta integration — entering the Pixel ID is enough. The Conversions API can now be connected without a developer through **Set up with Meta** in Events Manager. You only need a developer to choose individual events or send app and offline events.

### Can you put several Pixels on one site?

Technically yes, but it muddles the data. One Pixel per business is better; give your agency access through Business Manager instead.

### How long are Pixel audiences kept?

The maximum retention for a website visitor audience is 180 days. So install the Pixel well before your ads start, so data begins to build up.

### Can you work without the Conversions API?

To start, yes. But browser restrictions and ad blockers mean some data gets lost. Connecting it is now free and takes minutes, so there is little reason to wait. By Meta's own figures, advertisers using the Conversions API for web events had a [17.8% lower cost per result on average](https://www.facebook.com/business/news/pixel-conversionsapi-updates) — an average, not a guarantee.

### What if events don't show up in the account?

Check that the code is on every page, the correct Pixel ID is used and your ad blocker is off. Send the event again through Test Events — events can appear with a slight delay.

### Should you turn off on-device measurement?

Not necessarily. Meta recommends keeping it on to see more conversions and strengthen the signal. But if your reporting depends on ROAS and comparisons during a sale period matter, you can turn it off for a while — the toggle is per Pixel and can be changed at any time. Whichever you choose, note the date in your [report](/en/blog/what-an-ad-report-should-include/).

### If the Conversions API is already connected, should you switch to the one-click option?

No. Meta says advertisers with an existing partner or server integration don't need to change anything. The new setting doesn't replace the Pixel or Conversions API either; it works alongside them.

### Will ads improve as soon as the Pixel is installed?

Not immediately. The algorithm needs enough events to learn from — a new campaign usually spends several days in the "learning phase". Don't change the settings too often during this period, or learning starts over. Judge the results after at least a week.

## Conclusion

The Pixel and the Conversions API are your advertising's eyes. Without them the algorithm works blind and you pay for cheap leads that never turn into sales. From November, comparing Ads Manager numbers with your CRM matters even more: a higher number doesn't always mean higher sales. At Level Marketing we set up tracking in the first week of every project.

## More on this topic

- [Meta attribution window: how to read results in your report](/en/blog/meta-attribution-window/)
- [Retargeting: how to bring back people who didn't buy](/en/blog/how-retargeting-works/)
- [How to set up Instagram ads: a step-by-step guide](/en/blog/how-to-set-up-instagram-ads/)
