---
title: Google Tag Manager basics: tags, triggers and clean setup
description: Google Tag Manager basics: container, tags, triggers and variables, installing GA4 and the Meta Pixel, testing in Preview mode and the most common mistakes.
date: 2026-11-28
slug: google-tag-manager-basics
type: article
tags: Google Tag Manager, GTM, web analytics, GA4, Meta Pixel
key: google-tag-manager
rubric: target
---

Your site needs GA4, Yandex Metrica and a Meta Pixel, then you also want to count taps on the call button and jumps to Telegram, and every time you message the developer and wait a week. **Google Tag Manager** (GTM) solves this: one code goes on the site, and every other tag is managed from the GTM interface. This guide covers the core concepts, installing GA4 and the Meta Pixel, Preview mode and the typical mistakes.

## What GTM is and when you need it

GTM is a free "tag manager". A tag is any snippet of code on your site: analytics, a pixel, a chat widget. GTM lets you add, change and remove them without touching the site's code.

| Situation | Do you need GTM |
|---|---|
| Only GA4, and your site builder has a ready-made field | Not necessarily |
| GA4 + Metrica + Meta Pixel | Yes, everything in one place |
| You need to count button, phone and Telegram clicks | Yes |
| Ads change often and the developer is always busy | Yes |
| The site owner has no access to the code at all | Sort out access first |

The rule is simple: with more than two tags, or any button tracking, GTM saves time.

## Three core concepts

Everything in GTM is built around three elements:

| Element | What it is | Example |
|---|---|---|
| Tag | What fires | Google tag (GA4), Meta Pixel, Metrica code |
| Trigger | When it fires | All pages, the "Thank you" page, a click on a t.me link |
| Variable | Which value is used | The clicked link's URL, the page URL, an ID |

Remember the formula: **tag + trigger = action**. For example, "send the generate_lead event to GA4" (tag) "when the user opens the /thank-you/ page" (trigger).

## Step 1: account and container

1. Go to tagmanager.google.com with the **company's** Google account.
2. Create an account (the company name) and add a container.
3. Choose the container type. According to Google's help, Web is the most common for websites; there are also iOS, Android, AMP and Server types. Google suggests naming the container after your site's top-level URL, and you don't need a separate container for each page ([Tag Manager Help](https://support.google.com/tagmanager/answer/6103696)).
4. Install the two code snippets: the first as high as possible inside `<head>`, the second (noscript) immediately after the opening `<body>` tag ([installation guide](https://support.google.com/tagmanager/answer/14847097)).

The container ID starts with GTM-. Many site builders and CMSs have a dedicated field for it.

## Step 2: connect GA4 through GTM

Google's help gives this order ([set up the Google tag](https://support.google.com/analytics/answer/15756616)):

1. Tags → New.
2. Tag type: **Google tag**.
3. In the Tag ID field, enter your GA4 data stream ID (it starts with G-).
4. Trigger: **Initialization – All Pages**, so the tag fires before other triggers.
5. Save and click Submit to publish. According to the help, data collection can take up to 30 minutes to start.

Important: if GA4 code is already on the site directly and you add it through GTM as well, page views can be recorded twice. Pick one method and remove the other. For GA4 reports and key events, see [Google Analytics 4 basics: setup for a small business website](/en/blog/google-analytics-4-basics/).

## Step 3: track enquiries and buttons

This is the most useful part of GTM. A small business site usually needs four triggers:

| What we count | Trigger type | Condition |
|---|---|---|
| Enquiry sent | Page View | Page Path = /thank-you/ |
| Call button | Click – Just Links | Click URL starts with "tel:" |
| Telegram | Click – Just Links | Click URL contains "t.me" |
| WhatsApp | Click – Just Links | Click URL contains "wa.me" |

Click variables such as Click URL are filled in by click triggers ([built-in variables](https://support.google.com/tagmanager/answer/7182738)). If you don't see them in the list, turn them on under Variables by configuring the built-in variables.

For each trigger, create a GA4 event tag (for example generate_lead, click_phone, click_telegram) and mark them as key events in GA4. The same triggers can feed the Meta Pixel and Yandex Metrica goals too: one trigger, three systems. On Metrica goals, see [How to set up Yandex Metrica: counter, goals and Webvisor](/en/blog/how-to-set-up-yandex-metrica/).

**A tip on forms:** the most reliable approach is to send people to a separate "Thank you" page after they submit. GTM's form submission trigger can be unreliable with some form builders, so always test it in Preview.

## Step 4: the Meta Pixel

GTM has no official Google tag for the Meta Pixel. Meta's documentation describes two routes: a Custom HTML tag, or a GTM template provided by Meta ([Meta documentation](https://developers.facebook.com/documentation/ads-commerce/gateway-products/signals-gateway/pixel-setup-google-tag-manager)).

The basic order:

- the base pixel code on all pages;
- the standard "Lead" event on the "Thank you" page or on the enquiry trigger;
- store the Pixel ID in a variable, so you change it in one place.

A browser pixel doesn't see every event because of cookies and blockers, so you need the Conversions API as well. Details are in [Meta Pixel and Conversions API: 2026 setup guide and changes](/en/blog/meta-pixel-and-conversions-api/).

## Step 5: Preview mode and publishing

In GTM, changes don't go live straight away: first a draft (workspace), then testing, then publishing.

**Preview.** According to Google's help, the Preview button shows your site as if the current draft were published, and Tag Assistant shows which tags and triggers fired. The mode is visible only in the browser where preview was enabled, or to people you share the link with; regular visitors don't see it ([preview and debug](https://support.google.com/tagmanager/answer/6107056)).

Pre-publishing checklist:

- open the home page: did the Google tag fire once;
- tap the phone button: did the click_phone tag fire;
- submit the form: did generate_lead and Lead fire on the "Thank you" page;
- check that the enquiry tag does **not** fire on other pages.

**Publishing.** When you click Submit, give the version a clear name: "Telegram and phone clicks, 28.11". If something breaks, you can roll back to a previous version under Versions.

## Access rights

There are five permission levels at container level ([user permissions](https://support.google.com/tagmanager/answer/6107011)):

| Permission | What they can do | Who gets it |
|---|---|---|
| No access | Can't see the container | — |
| Read | View only | Owner, analyst |
| Edit | Makes changes, can't publish | Junior specialist |
| Approve | Creates versions, can't publish | Reviewer |
| Publish | Full rights | Lead specialist or agency |

Keep Admin rights at account level with the company.

## Illustrative example: how cost per lead changes after GTM

Illustrative example. A clinic spends 6,000,000 soums a month on ads. Before GTM only site forms were counted: 40 enquiries, a cost per lead of 150,000 soums. The ads look "expensive" and someone suggests cutting the budget.

Phone and Telegram clicks were added through GTM:

| Channel | Per month |
|---|---|
| Forms | 40 |
| Call button | 35 |
| Telegram | 25 |
| Total contacts | 100 |
| Cost per contact | 6,000,000 / 100 = 60,000 soums |

The numbers are illustrative, but the lesson is practical: with incomplete tracking you risk switching off ads that actually work. Ad algorithms also learn from all contacts, not just forms. The next step is reconciling those 100 contacts with your CRM, because a click isn't yet an enquiry; why the numbers differ is explained in [Ads Manager leads don't match your CRM: 7 causes and a check](/en/blog/ad-leads-vs-crm-mismatch/).

## Common mistakes

- **The container sits in the agency's or developer's account.** The partnership ends and access goes with it.
- **Code installed twice** (directly on the site and through GTM). Page views and conversions double.
- **Publishing without Preview.** The enquiry tag fires on every page: more "leads" in the ad account, none in the CRM.
- **No naming convention.** "Tag 1", "New trigger": in six months nobody will understand them. Use a format like "GA4 – generate_lead", "Click – Telegram".
- **Old tags never removed.** Dead pixels slow the site down.
- **Unnamed versions.** It's hard to find which change broke what.

## Questions and answers

### Does GTM slow the site down?

GTM itself is a single script. Slowness usually comes from the number and weight of the tags you add to it, so remove unneeded tags regularly.

### Can I set up GTM without a developer?

Installing the container code needs one-time access to the site, and many site builders let you do it yourself. After that, tags and triggers are configured in the GTM interface without writing code.

### What's the difference between GTM and Google Analytics?

GA4 collects data and shows reports. GTM only delivers code to the site and shows no reports at all. GTM is the pipe; GA4 is the tank.

### Can I install Yandex Metrica through GTM?

Yes, you can place the Metrica code on all pages with a Custom HTML tag. After installing, check in Preview and in the Metrica report that the visit was recorded.

## Conclusion

Google Tag Manager is a way to manage all your site's code from one place. One container in the company account, a Google tag with the Initialization trigger, four core triggers (form, phone, Telegram, WhatsApp), the Meta Pixel, and a Preview check before every publish. Then your ad results are fully visible, and you don't wait for a developer for every small change.

During a free audit, Level Marketing can check whether GTM, GA4 and the Meta Pixel on your site work correctly and whether every contact is being counted.

## More on this topic

- [Google Analytics 4 basics: setup for a small business website](/en/blog/google-analytics-4-basics/)
- [Meta Pixel and Conversions API: 2026 setup guide and changes](/en/blog/meta-pixel-and-conversions-api/)
- [UTM tags: how to know where every customer came from](/en/blog/utm-tags/)
