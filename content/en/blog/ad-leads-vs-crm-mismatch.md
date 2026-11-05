---
title: Ads Manager leads don't match your CRM: 7 causes and a check
description: Leads in Ads Manager don't match your CRM? Here are 7 causes of the gap, a 5-step weekly reconciliation, a table of gap types and a simple checklist.
date: 2026-11-05
slug: ad-leads-vs-crm-mismatch
type: article
tags: sales, analytics, crm, meta ads
key: kabinet-va-crm-lidlar
rubric: sotuv
weight: 1
---

Ads Manager shows 120 leads for the month, the CRM shows 90 (illustrative example). The agency says the ads are working, the sales team says there aren't enough leads, and the owner doesn't know whom to believe. When leads in Ads Manager don't match the CRM, it rarely means someone is lying — usually the two systems simply count different things. Below are the 7 most common causes and a reconciliation routine that takes about half an hour a week.

![Why the two numbers will never be identical](/img/blog/illus/kabinet-va-crm-lidlar-1.jpg 1200x675)

## Why the two numbers will never be identical

Ads Manager counts an **action** tied to an ad: a form was submitted, a conversation started, a "lead" event fired on the website. The CRM counts a **customer** that a sales rep accepted: there is a phone number, a name, a note on who talked to them.

So the goal is not to make the numbers equal but to **understand** the gap and keep it under control. If you can explain every part of it — "duplicate", "spam", "never reached the CRM" — you're fine. If the unexplained part is large, leads are probably getting lost, and that is money.

## 7 reasons Ads Manager leads don't match the CRM

### 1. "Lead" means different things on each side

With a Messages objective, Ads Manager counts a started conversation as a result. But a person may ask "how much?" and never read the reply, and the sales rep won't log that as a lead. With an instant form, every submission is a lead, even with a wrong number. More on that difference in [Lead form or Direct messages](/en/blog/lead-form-or-messages/).

### 2. Duplicates

Someone submits the form twice, or submits a form and then also writes in Direct. Two results in Ads Manager, one customer in the CRM (if contacts are merged by phone number). That's a normal gap; just count it.

### 3. Leads never reach the CRM

The most dangerous cause. The integration (Zapier, Make, the CRM's own connector) breaks, Page access permissions change, or a new question is added to the form and never mapped to a CRM field. With manual transfer, leads simply sit there on the day the rep is off sick. One important fact: Meta keeps lead data for 90 days from submission, after which it can no longer be downloaded ([Meta Business Help](https://www.facebook.com/business/help/734933888443065)). If you don't find a lost lead quickly, it is gone for good.

### 4. Spam, tests and empty leads

Wrong numbers, "test", accidental taps — Ads Manager counts them all. The rep either doesn't log them or closes them straight away as junk. If there are many, the problem is the form itself; we covered the causes in [Leads don't answer the phone](/en/blog/leads-dont-answer-the-phone/).

### 5. Attribution window (for website leads)

When leads come from your website, Ads Manager sees them through the Pixel and Conversions API and credits them to an ad within an **attribution window**. Meta's default setting is 7-day click or 1-day view ([Meta Business Help](https://www.facebook.com/business/help/460276478298895)). So if someone saw the ad without clicking, then came to the site from Google the next day and left a request, Ads Manager may claim it while the CRM records the source as "Google". How the Pixel works: [Meta Pixel and Conversions API](/en/blog/meta-pixel-and-conversions-api/).

### 6. The CRM source is logged wrong

In a hurry, the rep picks "other" or "referral" instead of "Instagram". As a result, the CRM shows fewer ad leads than there really are. For website forms, the fix is [UTM tags](/en/blog/utm-tags/) and automatic source capture; for manually entered leads, a required "source" field.

### 7. Dates and time zones

Your ad account has its own time zone. If it isn't set to Tashkent time, late-evening leads land on one day in Ads Manager and on another in the CRM. At month boundaries that's a gap of a few leads. And if a rep logs a lead the next day, the CRM date shifts too.

## Weekly reconciliation in 5 steps

One person does this once a week, say every Monday. It usually takes 20–40 minutes.

**Step 1. Agree on one definition.** Write it down with the agency and the sales team: for us, a "lead" is an enquiry from ads with a phone number. Conversations and forms are counted separately.

**Step 2. Export the list from Meta.** For instant forms, download last week's leads as a CSV from Leads Center (Meta Business Suite). For conversations, take the results count in Ads Manager and the list of Direct threads. Use the same date range in both systems.

**Step 3. Pull the same period from the CRM.** Filter leads with the source "Instagram/Facebook ads". If you don't have a CRM yet, read [which CRM suits a small business](/en/blog/crm-for-small-business/) first — in a spreadsheet this check quickly turns into chaos.

**Step 4. Match by phone number.** Put both lists in one sheet and match them by number — a basic Excel or Google Sheets lookup is enough. Put every number that is in Ads Manager but not in the CRM into a category: duplicate, spam/test, never reached the CRM, source logged differently.

**Step 5. Fix the cause and write it down.** Hand "never reached the CRM" leads to a rep immediately and check the integration. Record the result in one line every week, so you notice right away when the gap starts to grow.

![Types of gaps and what to do](/img/blog/illus/kabinet-va-crm-lidlar-2.jpg 1200x675)

## Types of gaps and what to do

| Gap type | What it looks like | What to do |
|---|---|---|
| Duplicate | Same number twice in Ads Manager | Count it, merge contacts by number in the CRM |
| Spam and tests | Wrong number, "test", empty field | Number confirmation or an extra question in the form |
| Never reached the CRM | In Ads Manager, not in the CRM at all | Check integration and permissions, work the lead now |
| Different source | In the CRM, but as "other" or "referral" | Required "source" field, UTM, a short rule for reps |
| Date shift | Leads fell on the neighbouring day | Check the time zone, reconcile by week |
| Attribution | Website lead in Ads Manager, "Google" in the CRM | View click and view results separately in reports |

## Illustrative example: a furniture store in Tashkent

*Illustrative example, numbers for clarity.* The store runs Instagram ads with an instant form. In one week Ads Manager shows 40 leads, the CRM 29. Matching by phone number showed:

- 4 duplicates (one person submitted twice);
- 3 wrong numbers or "test";
- 1 in the CRM, but with the source "referral";
- 3 never reached the CRM: a new question added to the form had broken the integration that day.

Those last three are the key finding. Without a weekly check they would have turned into dozens of lost enquiries over a month. The integration was fixed, and all three people got a call the same day.

![Weekly checklist](/img/blog/illus/kabinet-va-crm-lidlar-3.jpg 1200x675)

## Weekly checklist

- [ ] The definition of a "lead" is written down and agreed with the agency
- [ ] Leads are exported from Leads Center every week, well before the 90-day limit
- [ ] Ads Manager and the CRM are compared for the same period
- [ ] Matching is done by phone number
- [ ] Every gap is put into a category
- [ ] "Never reached the CRM" leads are worked the same day
- [ ] The CRM "source" field is required
- [ ] The weekly result is recorded in one line

## Questions and answers

**How big a gap is normal?**
There's no single right number — it depends on the ad type: conversations show a bigger gap than forms. What matters is not the percentage but what the gap consists of: the unexplained part should be close to zero.

**Which numbers should I trust — Ads Manager or the CRM?**
Both, for different questions. Ads Manager to compare which ads and creatives perform better. The CRM to know how many real customers and sales you had. Your monthly [advertising report](/en/blog/what-an-ad-report-should-include/) should include both.

**Can we transfer leads manually?**
If you get a few a day, yes — with a named owner and a deadline. As volume grows, set up an integration: manual transfer delays leads, and a delayed lead goes cold.

**Does the agency need CRM access?**
Full access isn't required. But the agency should know every week or month which leads were good and which turned into sales — otherwise it will optimise for cheap leads rather than for sales.

## Conclusion

Ads Manager and CRM numbers will never match exactly, and that's fine. What's not fine is nobody knowing what the gap is made of. One shared definition, a weekly export and matching by phone number help you find lost leads within a week. At Level Marketing we review ad results together with the client's sales data, so the numbers in the report are about real customers.

## More on this topic

- [What an advertising report should include](/en/blog/what-an-ad-report-should-include/)
- [UTM tags: how to know where every customer came from](/en/blog/utm-tags/)
- [What a CRM is and which one suits a small business](/en/blog/crm-for-small-business/)
