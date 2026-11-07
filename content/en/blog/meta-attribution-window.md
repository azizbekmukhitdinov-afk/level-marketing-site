---
title: Meta attribution window: how to read results in your report
description: The Meta attribution window explained: 7-day click, 1-day view and engage-through, what changed in 2026, and how to read your ad report without mistakes.
date: 2026-11-07
slug: meta-attribution-window
type: article
tags: paid social, meta ads, attribution, ad reporting
key: meta-atributsiya-oynasi
rubric: target
weight: 1
---

Ads Manager says «32 purchases», but the till shows fewer customers from ads this week. Usually nobody is lying — the answer is the **attribution window**, the rule Meta uses to credit a sale to an ad. Here is how the attribution window works in Meta, what changed in 2026, and how to read your report without drawing the wrong conclusions.

## What attribution is and where the «window» comes from

Attribution means linking a result (a purchase, a sign-up, an add-to-cart) to a specific ad. Someone sees your ad today, visits your site on their own tomorrow and buys three days later. Was that sale caused by the ad? Meta answers with a rule: if the person interacted with the ad within a certain **time span**, the result is credited to the ad. That time span is the attribution window.

A window has two parts:

- **Type of interaction** — the person clicked the ad, engaged with it in some other way (a like, a save, watching a video) or only saw it.
- **Length** — how many days after the interaction a result still counts.

One key point: the attribution window matters mostly for **website conversions** — purchases and leads that arrive through the Pixel and the Conversions API. We covered the setup in our article on [Meta Pixel and the Conversions API](/en/blog/meta-pixel-and-conversions-api/). A lead from an instant form or a Direct message is recorded inside Meta, so there the real question is different: do Ads Manager and your CRM agree?

## Three windows in Meta: click, engage-through and view

In ad set settings (Ads Manager → ad set → «Conversion» section → attribution setting) Meta shows three window types. Exact names and options vary with your account language and campaign type, so check your own account.

| Window | What counts | Length options |
|---|---|---|
| Click-through | The person clicked a link in the ad and then converted | 1 day or 7 days |
| Engage-through | A non-link interaction: like, comment, save, share, watching a video for a few seconds | 1 day or off |
| View-through | The person only saw the ad, did not click, then converted | 1 day or off |

For website conversions the default is usually **7-day click, 1-day engage-through and 1-day view**. In other words, a purchase within a week of a click and a purchase within a day of a simple impression are both credited to the ad.

## What changed in 2026

If your numbers look lower than last year's reports, two changes may explain it.

**1. Long view windows are gone.** As Meta announced on its developer blog in October 2025, [from 12 January 2026 the Ads Insights API no longer returns the 7-day and 28-day view windows](https://developers.facebook.com/blog/post/2025/10/16/ads-insights-api-metric-availability-updates/). The longest view window is now 1 day. If you used to report with 28-day view, old and new numbers are not directly comparable.

**2. «Click» got narrower.** In March 2026 Meta [announced that click-through attribution only counts link clicks](https://searchengineland.com/meta-introduces-click-and-engage-through-attribution-updates-470629): likes, saves and shares no longer count as a click. Link clicks include website visits, calls, messages, lead forms and similar buttons. Everything else moved into the new **engage-through** type, which replaced the old «engaged-view» (video views) and now applies to all formats.

The practical takeaway: last year's and this year's «sales after click» do not measure the same thing. When you compare periods, note these dates in your report.

## How to read your report: 5 steps

### 1. Check which window is set

The «Results» column in Ads Manager follows the ad set's attribution setting. Before reading a report, open the ad set editor and check the setting. If different ad sets use different windows, comparing them in one table is a mistake.

### 2. Add the «Compare attribution settings» columns

When customising columns in Ads Manager there is a **Compare attribution settings** section. It splits the same result by window: 1-day click, 7-day click, 1-day view and others. In one table you see how much came after a click and how much came only after an impression.

### 3. Look at the view-through share

If a large share of results comes from **views only**, be careful. These people saw the ad but might have bought anyway — regular customers who already know you, for example. In [retargeting](/en/blog/how-retargeting-works/) especially, the view window can inflate results, because that audience returns to your site regardless.

### 4. Reconcile with your CRM and till

Ads Manager is the ad platform grading its own work. Real money lives in your CRM and at the till. Every week compare purchases in Ads Manager with ad-sourced sales in your CRM. [UTM tags](/en/blog/utm-tags/) and a «how did you hear about us» question help identify the source. There will always be a gap; what matters is that it stays roughly the same week to week. If it suddenly widens, use our [Ads Manager vs CRM check](/en/blog/ad-leads-vs-crm-mismatch/) to find the cause.

### 5. Stick to one window

Pick one main window for reporting and keep it for months. If you do change it, write down the date: numbers before and after are not comparable. An agency report should also state which window was used — more on that in [what an advertising report should include](/en/blog/what-an-ad-report-should-include/).

## Which window to choose: by business type

There is no single right answer — the window should match how fast your customer decides.

| Business | Decision speed | Sensible starting point |
|---|---|---|
| Online store: clothing, cosmetics, accessories | A day or two | 1-day click + 1-day view; watch 7-day click in the comparison columns |
| Furniture, home appliances | A few days to a week | 7-day click + 1-day view |
| Real estate, cars, courses | Weeks | 7-day click; the main result is a lead, track sales in the CRM |
| Leads via instant form or Direct | Lead happens inside Meta | The window matters little; check lead quality in the CRM |

*Illustrative example:* a furniture store in Tashkent advertises website purchases. With «7-day click + 1-day view», Ads Manager shows 30 purchases in a week. The comparison columns show 18 within a day of a click, 7 within 2–7 days of a click and 5 after a view only. So 25 purchases can be credited to ads with confidence, and 5 belong to the «ads may have helped» bucket. When [calculating ROMI](/en/blog/how-to-calculate-romi/), use 25 for the cautious scenario and 30 for the optimistic one.

## 5 common mistakes

1. **Comparing numbers with different windows.** One ad set on 7-day click, another on 1-day — that table cannot tell you which is better.
2. **Treating the Ads Manager number as real sales.** Meta, Google Analytics and your CRM count by different rules. The same purchase can be claimed «by ads» in two systems at once.
3. **Ignoring the view window completely.** View-through results are not «fake»: in video and awareness campaigns they show part of the effect. Keep them on a separate line, but do not make them your main KPI.
4. **Changing the window because results look «bad».** A wider window inflates the number, not the sales. If results drop, check creatives, audience and the [learning phase](/en/blog/meta-learning-limited/) first.
5. **Forgetting the 2026 changes.** Comparing with the period before the January and March changes makes it easy to conclude, wrongly, that «ads got worse».

## Questions and answers

**Will changing the attribution window make my ads perform better?**
The window does not add sales; it only changes which sales are credited to ads. But in conversion-optimised campaigns Meta learns from results inside that window, so it is best to match it to how quickly your buyers decide.

**Is the 28-day window gone entirely?**
The 7-day and 28-day view windows are no longer returned in reports since January 2026. 28-day click is not available as an optimisation setting; it may still appear in some reporting and comparison tools — check your own account.

**Does the window matter if I use instant forms?**
Less. The form is filled in inside Meta and the lead is credited to the ad straight away. The key questions there are lead quality and making sure every lead reaches your CRM.

**Google Analytics shows a different number. Which is right?**
Both are right by their own rules. Google Analytics usually ignores views and gives the sale to the last source. Make one system your primary source and use the other as a check.

## Conclusion

The attribution window is the ruler your ad results are measured with. If you do not know the ruler, the numbers mislead: 30 sales in one report, 20 in another, for the very same week. Check which window is set, look at clicks and views separately, reconcile Ads Manager with your CRM and flag the 2026 changes in your reports.

If the numbers in Ads Manager and at the till do not add up, the Level Marketing team can review your ad report and explain which window fits your business.

## More on this topic

- [Learning limited in Meta ads: why results are unstable](/en/blog/meta-learning-limited/)
- [Retargeting: how to bring back people who didn't buy](/en/blog/how-retargeting-works/)
- [Lead form or Direct messages: which brings more sales](/en/blog/lead-form-or-messages/)
