---
title: Marketing experiments: hypotheses, ICE scoring and a test log
description: How to write a marketing hypothesis, rank ideas with ICE, build a test plan, sanity-check sample size and keep an experiment log, with worked illustrative examples.
date: 2026-11-28
slug: marketing-experiments-ice
type: article
tags: hypotheses, ICE scoring, experiments, A/B testing, marketing analytics
key: marketing-gipotezalari
rubric: biznes
---

"Let's try Reels", "maybe a discount?", "we need a new website". In many businesses, marketing decisions happen exactly like this: an idea appears, money is spent, and a month later nobody can say for sure what happened. Working with hypotheses changes the order: every idea is written down in advance as a measurable prediction, ranked, tested and logged. This article covers the format, ICE scoring, the test plan and a simple sample size sanity check.

## How a hypothesis differs from an idea

An idea is "what to do". A hypothesis is "if we do this, which metric will change, by how much, and why". The difference looks small, but it is what lets you answer "did it work?" at the end of a test.

A hypothesis has four required parts:

- **The change**: what exactly we will do.
- **The audience or place**: for whom, or at which funnel stage.
- **The metric and expected change**: which number, and by how much.
- **The reason**: why we think so, and what data we rely on.

## The hypothesis format

A one-sentence template:

**"If we [change], then [metric] for [audience] will change by [amount], because [reason]. We will test it over [period] using [method]."**

| Poorly written | Well written (illustrative example) |
|---|---|
| We should do Reels | If we launch 3 Reels creatives showing the product in use, cost per lead for our Tashkent audience will fall by 20%, because in reviews customers write "I didn't believe it until I saw it live" |
| Improve the website | If we cut the enquiry form from 6 fields to 3, page-to-enquiry conversion will rise from 4% to 5%, because analytics shows people leaving halfway through the form |
| Reply faster | If we reply to enquiries within 30 minutes, enquiry-to-meeting conversion will rise from 25% to 35%, because in the CRM late-reply enquiries reached a meeting less often |

In a good hypothesis the metric is one of the numbers in your [KPI](/en/blog/what-is-kpi/) system, so the result connects to the overall business goal.

## Where hypotheses come from

Strong hypotheses come from data, not imagination:

- **CRM and analytics**: which funnel stage loses the most.
- **Customer conversations**: in what situation and why people buy; see [Jobs to be Done](/en/blog/jobs-to-be-done/).
- **Reviews and call recordings**: recurring objections and phrases.
- **Ad reports**: which creative holds attention and which burns out quickly.
- **Unit economics**: which metric has the biggest effect on profit; see [unit economics](/en/blog/unit-economics-for-small-business/).

## ICE: how to rank ideas

There are always more ideas than resources. ICE is a quick way to rank them. The letters stand for **Impact**, **Confidence** and **Ease**. The method is credited to growth marketer Sean Ellis, as stated for example in [Itamar Gilad's article](https://itamargilad.com/the-tool-that-will-help-you-choose-better-product-ideas/). Each factor is scored from 1 to 10 and the scores are multiplied. Some teams average them instead; what matters is picking one method and sticking to it.

| Score | Impact | Confidence | Ease |
|---|---|---|---|
| 1–3 | Barely moves the main metric | Gut feeling only, no data | More than a month of work, high cost |
| 4–6 | Noticeable, but at one stage | One or two signals: a review, a call | One or two weeks, moderate cost |
| 7–10 | Big effect on revenue or cost per lead | Our own numbers or a previous test | A few days, almost free |

Scoring Confidence honestly is the hardest part. A rule of thumb: "I believe it" is 2–3, "customers say so" is 4–5, "it shows in our data" is 6–8, "we have tested it before" is 9–10.

### ICE example: a furniture store (illustrative example)

| Hypothesis | I | C | E | ICE |
|---|---|---|---|---|
| H1. Showing a price range in the creative lowers cost per lead | 8 | 6 | 9 | 432 |
| H2. Replying to enquiries within 30 minutes raises order conversion | 7 | 8 | 7 | 392 |
| H3. A free 3D design offer increases lead volume | 8 | 5 | 4 | 160 |
| H4. A blogger partnership brings a new audience | 7 | 3 | 5 | 105 |
| H5. A new website raises conversion | 6 | 4 | 2 | 48 |

Order: H1 → H2 → H3. The new website (H5) looks like the "biggest" idea, but confidence is low and effort is high, so it goes last. ICE is not an exact science: it speeds up team debates and reduces the "loudest voice wins" effect.

## The test plan: what to write before launch

A plan written before the start prevents you from interpreting the result "whichever way suits us" later.

| Item | Example for H1 (illustrative example) |
|---|---|
| Primary metric | Cost per lead (CPL) |
| Secondary metric | Lead → home measurement visit conversion |
| Current value | CPL 45,000 soums |
| Expected result | CPL 36,000 soums or lower |
| Variants | A: current creative, B: with a price range |
| Budget | 1,500,000 soums per variant |
| Duration | At least 7 days, in full weeks |
| Stopping rule | No stopping on results before the end date |
| Decision rule | If B is cheaper and lead quality holds, B becomes the default |

The secondary metric matters: if leads get cheaper but nobody books a measurement visit, it is not a win. The final verdict in money terms comes from [ROMI](/en/blog/how-to-calculate-romi/).

## Sample size: a simple sanity check

Many tests are doomed from the start because there is too little data. The volume you need depends on two things: your current conversion rate and how small a difference you want to detect. Under standard settings (95% significance, 80% power), a rough calculation:

| Current conversion | Result you want to detect | Needed per variant (approx.) |
|---|---|---|
| 3% | 3.6% (+20%) | about 14,000 visits |
| 10% | 15% (+50%) | about 700 visits |

These figures use the standard formula; check your own case with a tool such as [Evan Miller's sample size calculator](https://www.evanmiller.org/ab-testing/sample-size.html).

Practical takeaway (illustrative example): if a click costs 1,500 soums, the test in the first row needs about 21 million soums per variant. For a small business that is often unrealistic. So:

- **On a small budget, test big changes.** Not button colours, but the offer, how you show the price, or the whole creative idea.
- **Pick a metric higher up the funnel.** There are more clicks and leads than sales, so data accumulates faster.
- **Treat a small test as directional.** In the H1 example each variant gets about 33 leads, which only reveals a large difference. Confirm the result with a repeat test.
- **Do not stop early.** In the first days the "winner" often flips. Wait for the planned end date and use full weeks: weekday and weekend audiences differ.

For testing content ideas without your followers, Instagram has a dedicated tool: [Instagram Trial Reels](/en/blog/instagram-trial-reels/).

## The experiment log

The log is the team's memory. Without it, the same tests get repeated a year later and lessons leave with the specialist. A simple table is enough:

| # | Date | Hypothesis | ICE | Metric: before → after | Decision | Lesson |
|---|---|---|---|---|---|---|
| 1 | 03.11 | Price range in creative | 432 | CPL 45,000 → 37,000 soums | Adopted | When the price is visible, fewer empty "how much?" leads |
| 2 | 10.11 | Reply within 30 minutes | 392 | Orders 18% → 24% | Adopted | Reply standard added to the CRM |
| 3 | 17.11 | Free 3D design | 160 | Leads +10%, quality dropped | Rejected | The free offer attracted browsers |

All figures are an illustrative example. What matters is that "Rejected" rows get logged too. A failed test is knowledge you have already paid for.

## Common mistakes

- **Changing several things at once.** If the creative, audience and page all change, you cannot tell what worked.
- **Choosing the metric after the test.** CPL got worse, but a win is declared because "reach went up".
- **Logging only winning tests.** Half a log means half the lessons.
- **Massaging ICE scores.** Inflating the score of a favourite idea makes the method pointless.
- **Ignoring seasonality.** Comparing a pre-holiday week with an ordinary one leads to false conclusions.

## Questions and answers

### Does a small business need hypotheses, or is this for big companies?

A small business needs it even more, because every soum counts. You do not need complex tools: a Google Sheets table, two to four tests a month and a weekly 15-minute review are enough.

### Are there alternatives to ICE?

Yes, for example models that score reach separately. But for a small team ICE is the fastest: three questions and one number. The key is to apply it consistently.

### What if the test result is unclear?

That is a result too: the difference is smaller than you expected. Either repeat the test with more data or try a bolder change. Do not accept a result on the basis that it "almost worked".

### How many tests can I run per week?

It depends on budget and traffic. Each test must collect enough data, so on a small budget one or two tests at a time usually beat several half-finished ones.

## Conclusion

Working with hypotheses means writing ideas as predictions, ranking them with ICE, planning before launch, checking that you will have enough data, and logging every result. Within a few months the log becomes the most valuable document about what works in your particular business.

If you want to know which hypothesis in your ads and funnel to test first, Level Marketing can suggest a few priority ideas as part of a free audit.

## More on this topic

- [A/B testing ad creatives: how to run it](/en/blog/ab-testing-ad-creatives/)
- [What is an MVP: testing an idea for the least money](/en/blog/what-is-an-mvp/)
- [How to validate a business idea before you advertise](/en/blog/validate-a-business-idea/)
