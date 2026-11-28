---
title: Marketing dashboard: a one-page panel for business owners
description: How to build a marketing dashboard: metrics by funnel stage, a breakdown by source, a weekly and monthly rhythm, and assembling it in Google Sheets and Looker Studio.
date: 2026-11-28
slug: marketing-dashboard
type: article
tags: dashboard, analytics, Looker Studio, Google Sheets, KPI
key: marketing-dashboard
rubric: biznes
---

Owners usually get their numbers from three places: the ad account, the CRM and a manager's verbal "it was a good week." The three never match, and decisions get made on gut feeling. A marketing dashboard is a panel that shows the path from ad to payment on a single page. This article covers which metrics belong on it, how often to look at them and how to assemble it in Google Sheets and Looker Studio.

## How a dashboard differs from a report

A report explains a past period: what happened, why, and what we do next month. A dashboard shows the current state and answers one question quickly: "are we on plan, and where is the problem?" A report is read once a month; a dashboard is opened every day or every week.

That's why a dashboard has to be short. With 40 metrics on it, the owner will stop opening it. A good panel has 8–12 numbers, each compared with the plan, and each with a clear owner. The structure of a report is covered in [what an advertising report should include](/en/blog/what-an-ad-report-should-include/), and metrics in general in [what is a KPI](/en/blog/what-is-kpi/).

## Metrics by funnel stage

The easiest way to build a dashboard is along the funnel: top to bottom, from money to money. One main number and one ratio per stage is enough.

| Stage | Main number | Ratio | Source |
|---|---|---|---|
| Advertising | Spend | CPM or CPC | Ad account |
| Interest | Number of leads | CPL = spend ÷ leads | Ad account and CRM |
| Quality | Qualified leads | Qualified share, % | CRM |
| Contact | Leads that got a reply | Reply time, minutes | CRM |
| Meeting or consultation | Meetings | Lead to meeting, % | CRM |
| Sale | Sales and revenue | CAC = spend ÷ sales | CRM or till |
| Profit | Gross profit | ROMI | Calculation |

The key rule: **take the lead count from the CRM, not from the ad account**, and keep the ad account figure next to it for comparison. If they differ by more than a few percent, something is wrong with the integration — look for the causes in [Ads Manager leads don't match your CRM](/en/blog/ad-leads-vs-crm-mismatch/). How to calculate ROMI is explained in [ROMI: is your marketing paying off](/en/blog/how-to-calculate-romi/).

## Breakdown by source

Even when the totals look fine, one channel can be eating the others' money. So the dashboard needs a second table: a breakdown by source. For every lead to reach the CRM with its source, add [UTM tags](/en/blog/utm-tags/) to your ad links and keep the campaign name in lead form data.

Five columns are enough: spend, leads, CPL, sales, CAC. The main insight usually appears when you compare CPL with CAC: the cheapest lead is not always the cheapest sale.

## How often to look

You don't need to check every number daily. In fact, reacting to daily swings often does harm: ad algorithms need time to learn.

| Rhythm | Who looks | What they look at | Decision |
|---|---|---|---|
| Daily, 5 minutes | Head of sales | New leads, unanswered leads, reply time | Who calls whom |
| Weekly, 30 minutes | Owner + marketer | Spend, CPL, qualified share, meetings, % of plan | Swap creatives, move budget |
| Monthly, 1–2 hours | Owner + team | Sales, CAC, ROMI, source breakdown, plan vs actual | Next month's plan and budget |

At Level Marketing the monthly results are presented in the client's office: plan and actual are shown side by side, and next month's plan is agreed on the basis of those numbers. The weekly dashboard exists so that the end of the month brings no surprises.

## Where to build it: Google Sheets and Looker Studio

For a small business a two-layer setup is enough: data in Google Sheets, visuals in Looker Studio. Looker Studio has a [no-cost version](https://docs.cloud.google.com/looker/docs/studio/about-looker-studio-pro-content), while the paid Pro edition mainly adds company-level ownership and team features.

**Spreadsheet structure.** Create three tabs:

- **"Raw data"** — each row is one day and one source: date, source, spend, leads, qualified leads, meetings, sales, revenue. Data lands here manually or automatically.
- **"Plan"** — a monthly target for each metric.
- **"Panel"** — formulas with weekly and monthly totals and the percentage of plan.

To connect it to Looker Studio, Google's [guide to the Sheets connector](https://docs.cloud.google.com/looker/docs/studio/connect-to-google-sheets) requires data in tabular form, with a single header row and consistent value types in each column. So the "Raw data" tab must not contain merged cells, subtotals or comments.

**Refresh rate.** According to [Google's documentation](https://docs.cloud.google.com/looker/docs/studio/manage-data-freshness), Looker Studio refreshes Sheets data every 15 minutes by default and Google Analytics data every 12 hours. That means Analytics figures suit weekly analysis, not daily control. Setting up Analytics on your site is covered in [Google Analytics 4 basics](/en/blog/google-analytics-4-basics/).

The simplest way to bring in Meta ad numbers is a weekly export from Ads Manager into the "Raw data" tab. You can automate that later — see [marketing automation](/en/blog/marketing-automation/).

## Illustrative example: a one-week panel

The numbers below are an illustrative example, not a real company. The business sells through a consultation, the average order is 3,000,000 soums, and the gross margin is 30%.

| Metric | Actual | Plan | vs plan |
|---|---|---|---|
| Spend | 6,000,000 soums | 6,000,000 soums | 100% |
| Leads | 400 | 380 | 105% |
| CPL | 15,000 soums | 15,800 soums | good |
| Qualified leads | 240 (60%) | 65% | below |
| Consultations | 60 | 70 | 86% |
| Sales | 18 | 20 | 90% |
| Revenue | 54,000,000 soums | 60,000,000 soums | 90% |

CAC = 6,000,000 ÷ 18 ≈ 333,000 soums. Gross profit = 54,000,000 × 0.3 = 16,200,000 soums. ROMI = (16,200,000 − 6,000,000) ÷ 6,000,000 = 170%.

Breakdown by source:

| Source | Spend | Leads | CPL | Sales | CAC |
|---|---|---|---|---|---|
| Meta | 4,000,000 | 320 | 12,500 | 11 | ~364,000 |
| Google Search | 2,000,000 | 80 | 25,000 | 7 | ~286,000 |

Looking only at CPL, Google seems twice as expensive. Yet a sale costs less on Google. The panel's main takeaway: the problem isn't the number of leads but the qualified share (60% against a 65% plan) and bookings for consultations. So next week the answer is not a bigger budget but stronger questions in the Meta form and a check of the booking script.

## Signal rules

For a dashboard to drive decisions, write down "if …, then …" rules in advance. An illustrative template:

- CPL above plan by 20% two weeks in a row — swap the creatives.
- Qualified share drops below 50% — review the form questions and the audience.
- Average reply time above 30 minutes — the head of sales rebalances the queue.
- One source's CAC is 1.5 times the average — cut its budget by 20–30% and move the money to another source.

Set the thresholds from your own unit economics: the CAC at which a sale starts losing money is your limit.

## Common mistakes

- **Ad metrics only.** Reach, CTR and likes, but no sales — that's a copy of the ad account, not a dashboard.
- **No plan column.** Without a plan you can't tell whether 400 leads is good or bad.
- **Different numbers in different places.** Pick one source per metric and label it on the panel.
- **Too many charts.** If a chart isn't tied to a decision, remove it.
- **No owner.** If it's unclear who updates and who checks the panel, it will be out of date within two weeks.

## Questions and answers

### Do I need a developer for a dashboard?

No. A simple panel in Google Sheets and Looker Studio can be built in a day or two. A developer or a paid connector helps when you want data pulled automatically, but a weekly manual export is enough to start.

### Aren't the CRM's own reports enough?

A CRM shows the sales side well, but it usually doesn't know your ad spend. A dashboard is needed because it brings spend and sales together in one place, which is what makes CAC and ROMI visible.

### Which metrics should I start with?

Three: spend, leads in the CRM and sales. From those you get CPL and CAC. Then add qualified share and reply time.

### Can I share the dashboard with my agency?

Yes, and it helps: the agency and the sales team see the same numbers. Give view-only access and leave editing rights with the panel's owner.

## Conclusion

A good marketing dashboard is one page, 8–12 numbers, a comparison with plan and one source per metric. Build it along the funnel stages, add a breakdown by source, set a daily, weekly and monthly rhythm and write your signal rules in advance. Google Sheets and Looker Studio are enough to start.

If you'd like help bringing your numbers into one panel, Level Marketing can review your ad data and CRM during a free audit.

## More on this topic

- [Unit economics: how to know how much you can pay for ads](/en/blog/unit-economics-for-small-business/)
- [Sales rep conversion: who turns leads into sales](/en/blog/sales-rep-conversion/)
- [Cost per lead (CPL): what it is and how to lower it](/en/blog/cost-per-lead-cpl-how-to-lower/)
