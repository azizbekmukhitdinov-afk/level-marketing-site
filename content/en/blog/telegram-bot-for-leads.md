---
title: Collecting leads with a Telegram bot: a guide for business
description: How to collect leads with a Telegram bot: which questions to ask, where leads should go, how to track the ad source and the new SMS ad rules from 1 November.
date: 2026-10-23
slug: telegram-bot-for-leads
type: article
tags: telegram, sales, automation, CRM
key: telegram-bot-orqali-arizalar
rubric: sotuv
---

In Uzbekistan, customers message on Telegram first. That makes collecting leads with a Telegram bot the most natural channel after a website or a lead form: the customer stays in a familiar app, and you get a ready name, phone number and request. Below, step by step: what the bot should ask, where the lead goes and how a manager should handle it.

![Why a Telegram bot](/img/blog/illus/telegram-bot-orqali-arizalar-1.jpg 1200x675)

## Why a Telegram bot

After visiting Tashkent in June 2024, Telegram founder Pavel Durov wrote that more than 70% of Uzbekistan's population is on Telegram ([Spot](https://www.spot.uz/oz/2024/06/30/pavel-durov/)). That is the company's own figure, but everyday experience points the same way: customers of shops, clinics and training centres would rather write than call.

A plain "Message us on Telegram" button has a problem: everyone writes differently. One asks "how much?", another sends a voice note, a third never leaves a number. The manager has to pull the details out of each person again. A bot instead:

- asks the right questions **in the same order**;
- gets the phone number **with one tap**;
- sends the lead to a manager or group **instantly**;
- **replies** at night and on weekends;
- records **which ad** the lead came from.

It tidies up the "interest → lead" stage of your [sales funnel](/en/blog/what-is-a-sales-funnel/) and frees the manager's time for actual selling.

## What a lead bot should ask

The main rule: **fewer questions, more leads**. Ask only what the manager needs for the first call. Everything else can be clarified in conversation.

A sample flow for a furniture store in Tashkent:

1. **Greeting and language** — "Hello! Choose a language: O‘zbekcha / Русский".
2. **What is needed** — buttons: "Kitchen", "Wardrobe", "Bedroom", "Other".
3. **Rough timing** — "This month", "Within 1–3 months", "Just looking".
4. **Name** — free text.
5. **Phone number** — a "Share my number" button.
6. **Closing** — "Thank you! Our designer will call within 15 minutes" (working hours) or "We'll call you at 9:00 tomorrow" (after hours).

A few practical tips:

- **Buttons beat typing.** Customers tap instead of type, so there are fewer mistakes and drop-offs.
- **Get the number via a button.** Telegram has a button that shares the user's contact with the bot: one tap and the number arrives in the right format. It only works in a private chat with the bot.
- **Don't hide the price.** If customers ask about price first, add a "Prices" section: a rough range plus "leave your number for an exact quote".
- **Save the long questionnaire for later.** Room sizes, colours and materials belong in the conversation with the designer.

> The bot's job is to start the conversation, not to replace the manager.

## Where the lead goes: three options

The bot has collected a lead; now it must not get lost. Depending on the size of the business, there are three routes:

| Option | Fits | Pros | Cons |
|---|---|---|---|
| A Telegram group for managers | 1–3 managers, dozens of leads a day | Fast and free to set up | No statuses or history; leads get lost in the feed |
| A Google Sheet | Small team, simple reporting | All leads in one place, filters and totals | No reminders or tasks |
| A CRM | Ongoing ads, several managers | Every lead becomes a task, with a pipeline and reports | Setup and a monthly fee |

The best option is usually a **mix**: the lead lands in the CRM and the manager also gets a Telegram notification. How to choose a system: [what a CRM is and which one suits a small business](/en/blog/crm-for-small-business/).

The group message should be short and easy to read:

- New lead: Kitchen
- Name: Dilnoza
- Phone: +998 ...
- Timing: this month
- Source: instagram_kitchen_october

The manager reads it and can call straight away, with no extra questions.

## How to handle leads from a Telegram bot

The bot collects leads, but the manager brings in the money. The most common problem is a lead that arrives in the bot and sits unanswered for hours. So write the handling rules in advance:

1. **Owner.** Every shift has a clear person responsible for leads.
2. **Response time.** During working hours, a few minutes. Why it matters: [lead response time](/en/blog/lead-response-time/).
3. **First contact.** A call or a private Telegram message. The bot can ask which the customer prefers.
4. **Status.** Every lead goes "new" → "contacted" → "meeting/measurement" → "sale" or "declined (reason)".
5. **Script.** The manager knows what to say in the first minute; see the structure in [sales script](/en/blog/sales-script/).

A simple rule in the managers' group also helps: whoever takes a lead reacts to the message or replies "mine". That way two people never call the same customer, and no lead is left unanswered.

![How to track the ad source](/img/blog/illus/telegram-bot-orqali-arizalar-2.jpg 1200x675)

## How to track the ad source

A big advantage of a bot is that you can see which ad each lead came from. Telegram supports a start parameter for this: you add a tag to the bot link, for example `t.me/your_bot?start=insta_kitchen`. When a customer opens the bot through that link, the bot sees the tag and saves it with the lead.

Make a separate link for every channel and ad:

| Where | Link tag |
|---|---|
| Instagram profile (bio) | `start=insta_bio` |
| Kitchen ad on Instagram | `start=insta_kitchen` |
| Post in a Telegram channel | `start=tg_channel` |
| QR code in the store | `start=qr_store` |

At the end of the month, group leads by tag and see which ad brought more leads at a lower cost. It's the same logic as UTM tags for a website; details in [UTM tags](/en/blog/utm-tags/). Then divide ad spend by the number of leads to get your [cost per lead (CPL)](/en/blog/cost-per-lead-cpl-how-to-lower/).

## SMS ad rules and bots: what to know

Many businesses send promotions to their customer base by SMS. According to Anhor.uz, new requirements for advertising over mobile networks take effect on 1 November 2026: promotional SMS only with the recipient's written or electronic consent, and promotional calls and messages banned from 18:00 to 09:00 ([Anhor](https://anhor.uz/news/v-uzbekistane-zapretyat-reklamnye-zvonki-i-sms-po-vecheram-i-nochyu/)). Check the exact details against the official text with a lawyer.

A Telegram bot approaches this from the other side: **the customer starts the bot themselves**. Still, a bot shouldn't spam either:

- **Ask for permission first.** At the end of the lead flow: "Would you like to get offers and news? Yes / No".
- **Write rarely and usefully.** Send ads every day and customers will block the bot.
- **Protect personal data.** Names and phone numbers are personal data. Give access only to the staff who need it, and don't hand the base to outside services.

## Who builds the bot, and how

You don't need to be a programmer to make a Telegram bot. You register it through @BotFather in a few minutes; after that it needs a "brain". There are three routes:

- **No-code builders** — ready-made services where you assemble questions and buttons with a mouse. Enough for a simple lead bot. Watch the monthly fee.
- **A freelancer or studio** — built around your process, with CRM integration. The price depends on features, so compare several offers.
- **A bot inside your CRM** — some CRMs have a Telegram integration, so a lead immediately becomes a customer card.

Whichever route you choose, check before launch:

- the bot works in Uzbek and Russian;
- there are no more than 5–6 questions;
- the number is collected with a button;
- the lead reaches a manager within a minute;
- there is an after-hours auto-reply;
- every ad has its own start link;
- you have left a test lead yourself or through a friend.

![Common mistakes](/img/blog/illus/telegram-bot-orqali-arizalar-3.jpg 1200x675)

## Common mistakes

- **A maze of a bot.** Dozens of menus and sections; the customer can't find the lead button.
- **No human.** If the bot can't answer, a "Contact a manager" button is a must.
- **Leads reach no one.** Notifications are off or a manager left the group. Leave a test lead every week.
- **No source tag.** One link across all ads, so you can't tell what works.
- **The bot doesn't match the ad.** The ad promises a "free measurement" and the bot never mentions it. The customer gets confused.

## Conclusion

Collecting leads with a Telegram bot is convenient for customers and orderly for the business. Few questions, a button for the number, instant notifications, a start link for every ad and clear handling rules: these five things turn a bot into a real sales tool. The bot collects leads; a manager who replies fast makes the sale.

At Level Marketing, when we launch ads we agree in advance where leads will go and who answers them: when ads, the bot and the sales team work as one chain, every lead is accounted for.

## More on this topic

- [Lead response time: how it affects sales](/en/blog/lead-response-time/)
- [What a CRM is and which one suits a small business](/en/blog/crm-for-small-business/)
- [UTM tags: how to know where every customer came from](/en/blog/utm-tags/)
