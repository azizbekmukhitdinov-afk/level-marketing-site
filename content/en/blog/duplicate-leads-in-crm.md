---
title: Duplicate leads in your CRM: when one client applies twice
description: Duplicate leads in a CRM: where they come from, how they distort ad reports and how to merge them. One phone format, 5 merge rules and a clean-up routine.
date: 2026-11-21
slug: duplicate-leads-in-crm
type: article
tags: CRM, leads, sales, reporting
key: crmda-dubllar
rubric: sotuv
---

A client fills in your Instagram form in the evening and, not having heard back by morning, also writes in Direct. Two cards open in the CRM, they land with two sales reps, and both of them call. The client is puzzled, the reps argue, and the report says "two leads". That is how duplicate leads in a CRM appear. This article covers where they come from, how they distort your ad report and the simple rules that keep the database clean.

![What duplicate leads in a CRM are and where they come from](/img/blog/illus/crmda-dubllar-1.jpg 1200x675)

## What duplicate leads in a CRM are and where they come from

A duplicate is two or more records about the same person. One important distinction: a duplicate is not the client's mistake. Most often it is a **repeat enquiry**. If someone writes a second time, they are still interested. The problem is not the enquiry but the CRM treating it as a new person.

| Source | How it happens | Why the CRM misses it |
|---|---|---|
| Form submitted twice | The client did not wait for a reply or applied again from another ad | Every submission opens its own card |
| Two channels | First the form, then Direct, Telegram or a phone call | Direct carries no phone number, only a profile name |
| Phone written differently | +998 90 123 45 67, 901234567, 8 90 123-45-67 | To the CRM these are three different strings |
| Manual entry | A rep created a new contact after a call | Nobody searched the database first |
| File import | An old database or a trade-show list was uploaded | Duplicate checking was off during import |
| Two numbers | The client has two SIM cards or used a spouse's number | The number really is different |

The last two cannot be solved automatically. Only a rep notices them during a conversation. The other four can be closed with settings and a rule.

If leads still reach your CRM by hand, fix that first: [connecting a Meta lead form to your CRM](/en/blog/connect-meta-lead-form-to-crm/) describes 4 ways. Manual downloads produce the most duplicates.

## How duplicates distort your ad report

A duplicate is more than clutter. It skews your two key numbers at once.

**Illustrative example.** A furniture shop in Tashkent spent 600 dollars on ads in a month. The CRM shows 120 leads, 24 of them duplicates. So 96 people actually got in touch. There were 12 sales that month.

| Metric | With duplicates | Without duplicates |
|---|---|---|
| Number of leads | 120 | 96 |
| Cost per lead | 5 dollars | 6.25 dollars |
| Lead-to-sale conversion | 10% | 12.5% |

You get two errors together. First, advertising looks cheaper than it is, because one person was counted twice. Second, the sales team looks worse than it is, because reps were charged with "unsold" people who do not exist. The owner ends up fixing the wrong thing.

Three more consequences:

- **Two reps call the same client.** To the client it signals a disorganised company. To the reps it becomes a dispute over whose sale it is.
- **History is split.** One card holds the quoted price, the other holds the measurements. Nobody sees the whole picture.
- **The source is lost.** You can no longer tell which ad brought the client first.

If the numbers in Ads Manager and in the CRM differ, duplicates are one of the causes worth checking. The rest are in [Ads Manager leads don't match your CRM](/en/blog/ad-leads-vs-crm-mismatch/).

## Phone format: one number, one record

A CRM usually looks for duplicates by phone number. If the number is written in different ways, the search finds nothing. So the first step is a single format.

The most practical choice is the international one: a plus sign, the country code and the number, with no spaces or dashes. This is the E.164 standard, which allows at most 15 digits in a number ([ITU-T E.164](https://www.itu.int/rec/T-REC-E.164)). For Uzbekistan that means +998 followed by 9 digits.

| As received | As stored |
|---|---|
| 90 123 45 67 | +998901234567 |
| 8 (90) 123-45-67 | +998901234567 |
| 998901234567 | +998901234567 |
| +998 90 123-45-67 | +998901234567 |

The format matters beyond the CRM. Meta expects phone numbers in the same shape when matching customer data: symbols, letters and leading zeros removed, and the country code included even if all your customers are in one country ([Meta for Developers](https://developers.facebook.com/docs/marketing-api/conversions-api/parameters/customer-information-parameters)). A tidy database pays off later when you work with [Meta Pixel and the Conversions API](/en/blog/meta-pixel-and-conversions-api/).

Enforce the format in three places:

1. **In the form.** In an instant form the phone field is prefilled from the person's Meta profile, and it usually arrives with the country code. On a website form, add an input mask: "+998" is already there and the client types only 9 digits.
2. **In the integration.** Your connector service or webhook cleans the number before writing it to the CRM: it strips spaces, brackets and dashes and adds the code.
3. **In manual entry.** One rule for reps: a number always starts with +998. If your CRM lets you validate the field format, switch that on.

![The merge rule: 5 decisions](/img/blog/illus/crmda-dubllar-2.jpg 1200x675)

## The merge rule: 5 decisions

What to do with a duplicate should not be decided by each rep in their own way. Answer five questions once and give the team the answers in writing.

| Question | Recommended rule |
|---|---|
| Which card stays as the main one? | The one opened first. It holds the first source and the full history |
| Who is the owner? | The rep who contacted the client first. If nobody has yet, the owner of the first card |
| Which source is recorded? | The source of the first enquiry stays in the main field. Later ones go into a note or a "repeat enquiry" field |
| What happens to the second submission? | It is not deleted. It is added to the main card as an event: date, channel, what was asked |
| What if a closed client comes back? | The contact stays the same and a new deal is opened for it. The old deal remains in the history |

The fourth rule matters most. A repeat submission is not rubbish but a signal: the client is waiting for a reply or has become interested in another product. Delete it and the rep never finds out. That is why we say "merge", not "delete".

Many CRMs have a built-in merge tool, but it does not do everything for you. For example, according to the Bitrix24 help centre, the system merges cards automatically when the values of all fields match, the responsible employee is the same and the leads are at the same stage; if even one field differs, the CRM offers a manual merge instead ([Bitrix24 Helpdesk](https://helpdesk.bitrix24.ru/open/12910200/)). The same page notes that the tool is not available on every plan. Other CRMs have their own conditions, so open the settings and check which field the duplicate search uses. If you are still choosing a system, add this question to your list: [which CRM suits a small business](/en/blog/crm-for-small-business/).

## How to clean up duplicates in a CRM: 6 steps

1. **Make a copy.** Export the database to a file before you start. A merge cannot always be undone.
2. **Bring phone numbers to one format.** Convert the numbers in old records to +998… first. Without this, the search misses half the duplicates.
3. **Find the duplicates.** Use the CRM's own tool, or sort the phone column in the exported file. Identical numbers end up next to each other.
4. **Merge by the rule.** Follow the five decisions above. Do not merge doubtful pairs (different name, same number) until a rep has checked: they may be husband and wife.
5. **Close the entry points.** The form mask, cleaning in the integration, and a "search first, then create" rule. Otherwise it all starts again within a month.
6. **Set a weekly check.** Every Monday one person looks through the list of new duplicates. It takes five minutes.

After that, add one line to the monthly report: "number of repeat enquiries". The figure is useful in its own right: if it jumps, clients are not waiting for your reply. Look for the cause in your [lead response time](/en/blog/lead-response-time/).

![5 common mistakes](/img/blog/illus/crmda-dubllar-3.jpg 1200x675)

## 5 common mistakes

- **Deleting the duplicate.** The chat and the call recording disappear along with the second card.
- **Searching by name only.** A common first name appears in the database dozens of times. The main key is the phone number.
- **Marking a duplicate as a "low-quality lead".** The share of low-quality leads in the ad report then rises artificially. A duplicate needs its own status or tag.
- **Cleaning once and relaxing.** While the entry points stay open, duplicates pile up again.
- **Not telling the agency.** The team running your ads counts leads in Ads Manager. Give them the number of unique clients too, so the cost per lead in your [ad report](/en/blog/what-an-ad-report-should-include/) is the real one.

## Questions and answers

### What share of duplicates is normal?

There is no single benchmark: it depends on how many channels you use and how fast you reply. Count your own figure once and compare it every month. What matters is whether the share is rising or falling.

### What if the client wrote from two different numbers?

An automatic search will not catch this. If a rep notices it in conversation, they add the second number to the main card as an additional phone and merge the cards.

### How do I link an enquiry from Direct that has no phone number?

Ask for the number at the start of the chat and record it on the card. Search the database at that moment: if the number already exists, attach the conversation to that card.

### What should the ad report show, leads or unique clients?

Both. The number of leads is needed to reconcile with Ads Manager. The number of unique clients is needed to calculate the real cost per lead and conversion.

### Does a small shop with 5–10 leads a day need this?

Yes, in a simpler form: a single phone format and a "search first, then create" rule are enough. Order is far easier to establish while the database is small.

## Conclusion

Duplicate leads in a CRM look like a minor technical issue, yet they distort both the cost per lead and the conversion of your sales reps. The fix has three parts: one phone format, a written merge rule and a short weekly check. Do not delete a repeat submission. Add it to the client's history. At Level Marketing, when we prepare a report we reconcile the leads in Ads Manager with the unique enquiries in the client's CRM, so the cost per lead reflects reality rather than paperwork.

## More on this topic

- [Connect a Meta lead form to your CRM: 4 ways and a checklist](/en/blog/connect-meta-lead-form-to-crm/)
- [Ads Manager leads don't match your CRM: 7 causes and a check](/en/blog/ad-leads-vs-crm-mismatch/)
- [Sales rep conversion: who turns leads into sales](/en/blog/sales-rep-conversion/)
