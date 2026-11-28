---
title: Google Search Console guide for business owners
description: Google Search Console for business owners: verifying your site, submitting a sitemap, the Performance report, the page indexing report and URL Inspection.
date: 2026-11-28
slug: google-search-console-guide
type: article
tags: Google Search Console, SEO, website, indexing
key: google-search-console
rubric: target
---

Which searches your site appears for in Google, how many people see it and how many click, which pages never made it into search at all: only one free tool shows this precisely, and that's **Google Search Console**. This guide covers what a business owner actually needs: verification, the sitemap, the Performance report, indexing, URL Inspection and a 20-minute monthly check.

## What Search Console is and what it doesn't show

Search Console is data from Google itself: how your site looks in search and how Google "reads" it. Unlike analytics tools, it shows the stage **before** a person lands on your site.

| Question | Search Console | GA4 / Yandex Metrica |
|---|---|---|
| Which search did we appear for | Yes | No (almost) |
| How many saw it, how many clicked | Yes | Only those who arrived |
| Is the page indexed | Yes | No |
| What they did on site, did they enquire | No | Yes |

So Search Console doesn't replace analytics; it complements it. For on-site actions you need [Google Analytics 4 basics: setup for a small business website](/en/blog/google-analytics-4-basics/) or [How to set up Yandex Metrica: counter, goals and Webvisor](/en/blog/how-to-set-up-yandex-metrica/). The general logic of SEO is in [What is SEO? How to rank a website in Google and Yandex](/en/blog/what-is-seo/).

## Step 1: verify your site

Search Console has two property types:

| Property type | What it covers | Verification method |
|---|---|---|
| Domain | The whole domain: http and https, www and subdomains | DNS record only |
| URL-prefix | Only the given address (for example https://sayt.uz/) | HTML file, meta tag, Google Analytics, Tag Manager or DNS |

According to Google's help, a Domain property can only be verified through DNS, and a manually added DNS record can take up to two or three days to take effect. To stay verified, don't remove the record ([Google Search Console Help](https://support.google.com/webmasters/answer/9008080)).

**Decision rule:** if you have access to the domain's DNS settings, choose a Domain property; it shows every version of your site in one report. If you don't, or you need it today, use a URL-prefix property and verify with a meta tag or Google Analytics.

Important: the **company's** Google account should own the property, with the developer or agency added as users. Otherwise the history leaves when the partnership ends.

## Step 2: submit a sitemap

A sitemap is a list of your site's important pages (usually sayt.uz/sitemap.xml). Most site builders and CMSs generate one automatically. In the Sitemaps section you enter the address and submit it.

Key facts from Google's help ([Sitemaps report](https://support.google.com/webmasters/answer/7451001)):

- one sitemap can hold up to 50,000 URLs and 50 MB uncompressed; anything larger gets split into several files;
- statuses: success, has errors, couldn't fetch;
- submitting a sitemap doesn't guarantee the pages will be crawled or indexed.

A sitemap is a map for Google, not an order. A thin or duplicate page may stay out of the index even if it's listed.

## Step 3: the Performance report

This is the most useful part for a business. Four metrics ([Google Help](https://support.google.com/webmasters/answer/7576553)):

- **Clicks**: how many times people clicked through to your site from search results;
- **Impressions**: how many times your site appeared in results;
- **CTR**: clicks divided by impressions;
- **Average position**: the average position of your site's topmost result.

Limits worth knowing:

- Search Console keeps data for the last **16 months** ([Google Analytics Help](https://support.google.com/analytics/answer/13682862)); if you want a longer history, save a monthly export yourself;
- the interface exports up to 1,000 rows; rare queries are anonymised for privacy and get no row of their own, so the rows add up to less than the chart total ([Google Search Central blog](https://developers.google.com/search/blog/2022/10/performance-data-deep-dive));
- the newest data can be preliminary and may change over the next few hours.

A decision table for the report:

| Situation | What it means | What to do |
|---|---|---|
| Many impressions, low CTR | The page is seen, but the title doesn't pull | Rewrite title and description, add price or benefit |
| Position 8–20 | Close to page one | Strengthen the text, answer questions, add internal links |
| Lots of brand queries, few service queries | People who know you find you; new customers don't | Service pages and articles |
| Clicks dropped sharply | Technical problem or competition | Check the indexing report |

How to choose which queries to work on is covered in [Keyword research: building a keyword list for Google Ads and SEO](/en/blog/keyword-research/).

## Illustrative example: from CTR to enquiries

Illustrative example. A Tashkent dental clinic's "implant price" page gets 12,000 impressions a month at an average position of 6, with 180 clicks, so a CTR of 1.5%.

The title was "Dental implants — Clinic name". It was changed to "Implant prices in Tashkent: 2026 prices and instalments", and the description now mentions the free consultation. The next month, at the same position, CTR rose to, say, 3%.

| Metric | Before | After |
|---|---|---|
| Impressions | 12,000 | 12,000 |
| CTR | 1.5% | 3% |
| Clicks | 180 | 360 |
| Site conversion (illustrative 4%) | 7 enquiries | 14 enquiries |

That's 7 extra enquiries a month with no ad budget. The numbers are illustrative, but the logic is real: Search Console shows you where clicks are being lost. After changing titles, wait at least 2–4 weeks for results, because daily swings are large.

## Step 4: the page indexing report

The Page indexing report shows which pages are in Google's index, which aren't, and why. The main reasons ([Google Help](https://support.google.com/webmasters/answer/7440203)):

| Reason | What it means | Usual action |
|---|---|---|
| Crawled, currently not indexed | Google saw it but didn't index it | Make the page more valuable, merge duplicates |
| Discovered, currently not indexed | Google knows the page but hasn't crawled it yet | Internal links, sitemap |
| Duplicate without user-selected canonical | A copy of another page | Set the canonical page |
| Excluded by "noindex" | The page tells Google not to index it | Check it wasn't added by accident |
| Not found (404) | The page doesn't exist | Redirect if it mattered |
| Page with redirect | Points to another URL | Usually fine |
| Blocked by robots.txt | Crawling is disallowed | Check whether the block is needed |

As Google itself says, don't expect every URL on your site to be indexed, but all your important pages should be. So don't look at the count of "not indexed" pages; look at your list of **important pages**: home, services, prices, contacts, key articles.

The most dangerous case: after launching a new site, the developer forgets to remove the "noindex" left from test mode. Put this check on your launch checklist; more on that in [How to build a business website: site builder, AI or developer](/en/blog/how-to-build-a-business-website/).

## Step 5: URL Inspection

Enter a page address in the search bar at the top and Search Console shows its status. According to Google's help ([URL Inspection tool](https://support.google.com/webmasters/answer/9012289)):

- it first shows the indexed version, which may be out of date;
- the live test checks the page right now, but a passing test doesn't guarantee indexing;
- there's a "Request indexing" button, but requests have a daily limit and don't guarantee the page gets indexed;
- for many new or updated pages, Google recommends submitting a sitemap.

Practical rule: a new service page or an important change gets one request for that URL. Resubmitting the same page every day doesn't speed anything up.

## The 20-minute monthly check

| Every month | What to look at |
|---|---|
| Performance | Clicks and impressions vs last month and last year |
| Queries | New queries, top-10 pages with low CTR |
| Indexing | Important pages indexed, any new errors |
| Sitemap | Status "Success" |
| Export | Save the month's data to a spreadsheet (because of the 16-month limit) |

You can also link Search Console to Google Analytics 4, so search queries and on-site actions show up in one place.

## Questions and answers

### Do I need Search Console for advertising?

Not directly: it shows organic search. But organic queries are a good source of keywords for Google Ads, and the reverse works too: queries that performed well in ads can get their own SEO pages.

### Why don't clicks in Search Console and Analytics match?

Search Console counts clicks in search results; analytics counts visits on the site. If someone clicks and leaves before the page loads, or rejects cookies, analytics won't record the visit.

### When will a new site appear in Google?

There's no fixed timeline. In its URL Inspection help, Google says indexing typically takes about a day but can take much longer. Submit a sitemap, add internal links to important pages and make sure there's no "noindex".

### Is there a tool like this for Yandex?

Yes, Yandex has its own webmaster panel with similar logic: site verification, sitemap, indexing, queries. If your customers also search on Yandex, set up both.

## Conclusion

Search Console is free data straight from Google. Set it up once: a Domain property in the company account, a submitted sitemap, a link to GA4. Then 20 minutes a month: find pages with low CTR, confirm important pages are indexed and export the data. It's one of the cheapest ways to win extra enquiries without an ad budget.

During a free audit, Level Marketing can look at how your site appears in Search Console and which pages have dropped out of the index.

## More on this topic

- [What is SEO? How to rank a website in Google and Yandex](/en/blog/what-is-seo/)
- [Keyword research: building a keyword list for Google Ads and SEO](/en/blog/keyword-research/)
- [Types of website traffic: organic, paid, direct and AI referrals](/en/blog/types-of-website-traffic/)
