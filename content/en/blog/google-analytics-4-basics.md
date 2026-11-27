---
title: Google Analytics 4 basics: setup for a small business website
description: Google Analytics 4 for a small business website: setup, key events, UTM tags, linking Google Ads, which reports to watch and the most common setup mistakes.
date: 2026-11-27
slug: google-analytics-4-basics
type: article
tags: Google Analytics 4, GA4, web analytics, website
key: google-analytics-4
rubric: target
---

Ads are sending people to your website, but nobody can say for sure which channel brings in leads — it's a very common situation. **Google Analytics 4** (GA4) answers exactly that question: where people came from, what they did on the site and which of them left an enquiry. This guide covers setting up GA4 from scratch for a small business website, the reports you need and the mistakes to avoid.

## What GA4 is and what it gives a business

GA4 is Google's free web analytics service. It records every action on your site as an "event": a page opened, a button clicked, a form submitted. For a business owner that means three practical benefits:

- **traffic sources** — Google, Instagram, Telegram, ads or direct visits;
- **key events** — how many enquiries, phone taps and Telegram clicks each channel produced;
- **pages** — which ones work and which ones people leave straight away.

GA4 doesn't show sales on its own — it shows actions on the site. Whether an enquiry became a real customer is something your CRM knows. That's why GA4 and CRM numbers sometimes differ, which is normal; the reasons are explained in [Ads Manager leads don't match your CRM](/en/blog/ad-leads-vs-crm-mismatch/).

## Step 1: account, property and data stream

The setup order:

1. Go to analytics.google.com with a company Google account (not an employee's personal email).
2. Create an **Account** — the company name.
3. Create a **Property** — the site name, time zone "Uzbekistan", currency "UZS" or whichever you work in.
4. Add a **Data stream** — "Web", then enter your site's address.
5. Copy the Measurement ID (it starts with G-).

The company should own the account, with the developer or agency added as users. Otherwise your statistics leave when the partnership ends.

## Step 2: installing it on the site

There are three ways; choose based on your site:

| Method | Best for | Difficulty |
|---|---|---|
| A field in your site builder (Tilda, a WordPress plugin, etc.) | Sites on a ready-made platform | Easy |
| Google tag (gtag.js) code on the pages | A simple site with a developer | Medium |
| Google Tag Manager | Many buttons, forms and ad pixels | Medium, but flexible |

If the site also has a Meta Pixel, it's easier to manage everything in one place through Tag Manager. A link to our pixel setup guide is at the end of this page.

After installing, check it: open the site on your phone and look for yourself in **Reports → Realtime**. If you don't show up, the code is in the wrong place or uses a different ID.

## Step 3: first settings

Do these four things on day one — later is too late.

**Data retention.** According to Google's help page, user-level data can be kept for 2 or 14 months ([Google Analytics Help](https://support.google.com/analytics/answer/7667196)). Many properties start at 2 months — switch it to 14 under Admin → Data collection and modification → Data retention. The change only applies going forward; deleted data doesn't come back.

**Enhanced measurement.** Make sure it's on in the data stream settings: without extra code it records page views, scrolls, outbound clicks, site search, file downloads and form interactions.

**Exclude internal traffic.** Define your office IP as "internal traffic" and activate the filter. Otherwise staff visits will skew the numbers.

**Access rights.** Write down who is an administrator and who only views.

## Step 4: key events

What GA4 used to call "conversions" are now called **key events**. Google explains the change as a way to avoid confusion with conversions in Google Ads, which keeps the word "conversion" ([Google Analytics Help](https://support.google.com/analytics/answer/13965727)).

A small business website usually needs 3–5 key events:

| Event | What it is | How to set it up |
|---|---|---|
| generate_lead | Enquiry form submitted | Via the "Thank you" page view or the form submission |
| Phone tap | Click on a tel: link | A separate event via Tag Manager |
| Telegram click | Click on a t.me link | A new event based on click with the condition link_domain = t.me |
| WhatsApp click | Click on a wa.me link | Same, with wa.me |
| purchase | Online payment (if any) | Via the site or platform |

To mark an event as key: Admin → Events (or Key events) → switch on the toggle next to the event.

Illustrative example: a dental clinic in Tashkent tracks three key events on its site: the form, the call button and Telegram. A month later it can see that visitors from Google tend to call, while visitors from Instagram message on Telegram. The numbers here are illustrative, but the lesson is practical: you can put a different contact button first for each channel.

Don't make every page view or 10 seconds on site a key event — the metric becomes meaningless. The rule from [What is conversion rate?](/en/blog/what-is-conversion-rate/) applies: a conversion is an action close to money.

## Step 5: UTM tags and linking Google Ads

**UTM tags.** GA4 detects sources on its own, but it often gets it wrong for links in an Instagram bio, Telegram posts or SMS — visits from messaging apps, for example, can end up as "direct". Add utm_source, utm_medium and utm_campaign to every ad and post link. The full rules are in [UTM tags](/en/blog/utm-tags/). One important point: use standard utm_medium values such as "cpc", "social" or "email", otherwise GA4 drops the traffic into the "Unassigned" group.

**Linking Google Ads.** Admin → Product links → Google Ads links. Once linked:

- Google Ads campaigns show up separately in GA4 reports;
- GA4 key events can be imported into Google Ads as conversions;
- remarketing audiences are built from site visitors.

**Linking Search Console.** In the same section, connect Search Console so organic search queries and pages appear inside GA4.

## Which reports to watch

GA4 has a lot of reports, but a business owner needs four:

1. **Acquisition → Traffic acquisition.** How many sessions and key events each channel produced (Organic Search, Paid Search, Organic Social, Direct, Referral).
2. **Engagement → Landing page.** Which page people landed on first and whether it led to an enquiry. A weak ad landing page shows up here.
3. **Engagement → Events / Key events.** The count and trend of each key event.
4. **Realtime.** To check straight away whether traffic is arriving after a campaign or post goes live.

Visits from AI services such as ChatGPT and Gemini can also appear under Referral — worth tracking separately, as discussed in [Google AI Mode and AI Overviews](/en/blog/google-ai-mode-for-business/).

Fifteen minutes a week is enough: key events by channel, the best and worst landing page, and the change from last week. Add these GA4 numbers to your monthly [advertising report](/en/blog/what-an-ad-report-should-include/).

## Common mistakes

- **The account belongs to an employee or agency** — when the partnership ends, the history is gone.
- **Retention left at 2 months** — no way to compare with last year.
- **No key events** — you see traffic but not results.
- **Everything is a key event** — scrolls and page views have become "conversions".
- **Code installed twice** — the builder field and Tag Manager at once, so every number is doubled.
- **No UTM tags** — Instagram and Telegram traffic disappears into "direct".
- **Internal traffic not filtered** — on a small site, staff can make up a noticeable share of visits.

## Checklist: is GA4 ready?

- The account owner is a company Google account
- Time zone set to Tashkent, correct currency
- Code installed one way only, your visit shows in Realtime
- Retention set to 14 months
- Internal traffic filter active
- 3–5 key events marked and checked with a test enquiry
- UTM tags on every ad and post link
- Google Ads and Search Console linked
- A weekly 15-minute review in the calendar

Don't skip the test enquiry: fill in the form yourself and, a few minutes later, check in Realtime that the generate_lead event appeared.

## Questions and answers

### Is GA4 paid?

No, standard GA4 is free for small and medium businesses. There is a paid Google Analytics 360 for large companies, but a small site doesn't need it.

### Why don't leads in GA4 match my CRM?

There are many reasons: someone submits the form twice, an ad blocker stops the GA4 code, cookie consent isn't given, or the enquiry comes in by phone. Use GA4 for trends and comparing channels; your CRM is the source of truth for the exact lead count.

### Isn't my site builder's analytics enough?

Tilda's or another builder's statistics show the basics, but channels, key events and the Google Ads link are far more complete in GA4. The two don't interfere with each other.

### When will I see data?

In the Realtime report — immediately. Standard reports can lag by a few hours up to a day. Collect at least 2–4 weeks of data before drawing conclusions.

## Conclusion

Setting up Google Analytics 4 is a one-day job: a company-owned account, correctly installed code, 14-month retention, an internal traffic filter and 3–5 key events. Then add UTM tags, link Google Ads and Search Console, and spend 15 minutes a week on four reports. That way you answer "which ads are working?" with numbers, not guesses.

During a free audit, Level Marketing can check your site's GA4 setup and whether key events are being recorded correctly.

## More on this topic

- [How to set up Google Ads: a step-by-step search campaign](/en/blog/how-to-set-up-google-ads/)
- [Meta Pixel and Conversions API: 2026 setup guide and changes](/en/blog/meta-pixel-and-conversions-api/)
- [A landing page that converts: the structure, block by block](/en/blog/landing-page-that-converts/)
