---
title: Telegram bot broadcasts: 7 rules so customers don't block you
description: How to run Telegram bot broadcasts: consent, segments, frequency, timing, Telegram limits and 5 common mistakes. Practical rules for shops and services.
date: 2026-11-11
slug: telegram-bot-broadcast-rules
type: article
tags: Telegram, bot, broadcast, customer database
key: telegram-bot-rassilka-qoidalari
rubric: smm
weight: 1
---

A Telegram bot broadcast is the cheapest way to bring a new offer to past customers: one message reaches thousands of people in a few minutes. But a badly sent broadcast pushes customers not towards a purchase but towards the "Block" button — and after that the bot can never message them again. This article covers 7 rules for Telegram bot broadcasts, Telegram's limits, what the law in Uzbekistan says and the 5 most common mistakes.

## How a bot broadcast differs from a channel post

Many business owners treat a bot as a "second channel". In fact it is a different tool: people open a channel post whenever they like, while a bot message lands in their private chats, next to conversations with friends and family. That is why the bar is higher.

| | Telegram channel | Bot broadcast |
|---|---|---|
| Where it lands | In the channel list, often muted | In a private chat, with a notification |
| Who receives it | Every channel subscriber | People who started the bot, or a chosen segment |
| Personalisation | None, one post for all | By name, purchase history, branch, language |
| Response | Comment or reaction | Button tap, order, question right in the chat |
| Cost of a mistake | The subscriber leaves the channel | The customer blocks the bot and you can no longer write to them |

The takeaway is simple: a channel is media, a bot is a personal conversation. We covered channel growth in a [separate article](/en/blog/grow-a-telegram-channel/); here we only talk about bots.

## Telegram and the law: 4 things to know before a broadcast

**1. A bot cannot write first.** As Telegram's official page puts it, bots can't start conversations: a user must message the bot first or add it to a group ([core.telegram.org/bots](https://core.telegram.org/bots)). So your broadcast list is only the people who pressed "Start" in your bot. You cannot "upload" a list of phone numbers into a bot and message them.

**2. There is a speed limit.** According to the Telegram Bots FAQ, a bot cannot broadcast more than about 30 messages per second, and it should avoid sending more than one message per second to a single chat ([Telegram Bots FAQ](https://core.telegram.org/bots/faq)). Paid broadcasts raise the limit to 1,000 messages per second, but only for bots with at least 100,000 Stars on balance and at least 100,000 monthly active users. For a small business this is not a problem: a 5,000-person list goes out in a few minutes within the free limit. Your developer just needs to queue the messages, otherwise Telegram starts returning errors.

**3. Consent for advertising is the safest route.** Article 30 of Uzbekistan's Law "On Advertising" allows advertising in telecommunication services only with the subscriber's prior consent ([lex.uz](https://lex.uz/ru/docs/6052633)). Since 1 November 2026, written or electronic consent is mandatory for advertising SMS — see our [article on the new SMS rules](/en/blog/sms-advertising-rules-uzbekistan/). Whether a Telegram bot broadcast falls under these exact rules, we could not find a clear answer in open sources. The practical advice: send promotional messages only to people who gave explicit consent, and talk to a lawyer in complex cases.

**4. Your database holds personal data.** If the bot stores names, phone numbers and purchase history, personal data law applies. We walked through storage and consent step by step in our [customer database article](/en/blog/customer-database-personal-data-uzbekistan/).

> This article is not legal advice. We explain the law and Telegram's rules in plain language.

## 7 rules for Telegram bot broadcasts

### 1. Say what you will send at sign-up

When a customer opens the bot for the first time, make a clear promise: "Once a week we send the new collection and subscriber-only offers. I agree / Order updates only". Two buttons, two separate lists. Store the date and time of the "I agree" tap: that is your consent record.

### 2. Split the list into segments

The same message to everyone is the fastest road to blocks. The simplest segments:

- **Buyers and non-buyers.** Accessories and repeat purchases for the first group, a reason for a first purchase for the second.
- **Language.** If the bot offers a language choice, send separate Uzbek and Russian texts.
- **Branch or city.** A promotion in Chilanzar is useless to a customer in Samarkand.
- **Interest.** Whatever menu section someone opened most — send a message on that topic.

If the bot also collects leads (how to set that up is in [collecting leads with a Telegram bot](/en/blog/telegram-bot-for-leads/)), the segment data builds up on its own.

### 3. Decide the frequency in advance

There is no fixed number, but there is a rule: send as often as you promised at sign-up. For most businesses, 1–2 promotional messages a week are enough. If you want to write more often during the holiday season, say so upfront: "Until the end of December — a new offer every Monday and Thursday".

### 4. Choose the time carefully

For SMS, advertising between 18:00 and 09:00 is banned. We found no such rule for Telegram, but the logic is the same: a notification at night annoys people. Send during the day and compare results by hour. Given the limit of about 30 messages per second, you can spread a large list over several hours — Telegram's FAQ suggests the same.

### 5. One message, one goal, one button

The message should fit on a phone screen: the benefit in the first line, then 2–3 short sentences and a single button at the end ("Open catalogue", "Message a manager"). Three offers, five links and a long text go unread. You can add a photo or a short video, but the text should make sense without it.

### 6. Show the way out

Under every promotional message put an "I don't need offers" button. It is not a paradox: without it, people block the bot and you can no longer send them order updates or warranty reminders. With it, they leave only the promotional list, while service messages keep reaching them.

### 7. Measure every broadcast

Track at least four numbers:

| Metric | What it shows |
|---|---|
| Delivered | How much of the list is still "alive" |
| Blocked | Users for whom sending returned an error — your annoyance level |
| Button taps | Whether the offer was interesting |
| Orders or leads | Whether the broadcast made money |

Add [UTM tags](/en/blog/utm-tags/) to links so broadcast purchases show up separately in your website analytics. If blocks rise two broadcasts in a row, reduce the frequency or narrow the segment.

## 5 common mistakes

1. **Buying a phone list or copying one from elsewhere.** The bot can't message them anyway, and sending SMS would breach the consent requirement.
2. **Mixing service messages with advertising.** "Your order is on its way. By the way, −20% today!" is no longer a service message — it is an ad. Keep them apart.
3. **Writing several times a day.** Especially a string of "last chance" messages. One reminder is enough.
4. **One text for everyone.** Sending a "first purchase discount" to someone who has already bought damages trust.
5. **Not measuring results.** "We sent a broadcast, there seem to have been sales" is not a report. Record blocks and orders every time.

## Illustrative example: a furniture shop's monthly broadcast plan

*Illustrative example — the numbers and situation are made up for clarity.* A furniture shop in Tashkent has 3,000 bot subscribers; 1,200 of them tapped "I agree to offers" and 700 have bought at least once.

| Week | Audience | Message | Button |
|---|---|---|---|
| 1 | Consented, not yet bought | New sofa collection, 3 photos | "Catalogue" |
| 2 | Buyers (with consent) | A coffee table and cushions to match the sofa | "Message a manager" |
| 3 | Everyone (service message) | Opening hours and the new branch address | "Open in maps" |
| 4 | Everyone who consented | Weekend offer with a clear deadline | "Reserve" |

At the end of each week the shop records four numbers: delivered, blocked, taps and orders. The week 3 message is not advertising, so it also goes to people who did not consent. How to turn such a list into steady repeat sales is shown in our [article on LTV](/en/blog/repeat-sales-and-ltv/).

## Questions and answers

### Can I send ads to every bot subscriber?

Technically yes — Telegram lets a bot message anyone who started it. But the law requires prior consent for advertising by SMS and in telecom services, and there is no clear answer for bots. The safe route is to send advertising only to people who tapped "I agree".

### What service do I need for broadcasts?

If the bot is your own, a developer can add a broadcast feature. Ready-made bot builders usually include one too. What matters is that it shows segments, the consent flag and block statistics.

### Can I win back a customer who blocked the bot?

The bot cannot message them. Contact resumes only if the customer starts the bot again. That is why preventing blocks is much easier than winning people back.

### If I have a channel, do I need bot broadcasts?

They complement each other. The channel carries useful content for everyone; the bot carries personal offers and messages close to an order. We compared the options in [Telegram or Instagram](/en/blog/telegram-or-instagram-for-business/).

### How many times a week should I send?

As many as you promised at sign-up. If blocks start to rise, cut back.

## Conclusion

A Telegram bot broadcast is a direct line to your warmest audience. To keep it open, get consent, segment your list, write at the promised frequency, keep one goal and an opt-out button in every message, and measure the result every time. At Level Marketing we connect leads from ads to a bot and a CRM with our clients and plan repeat sales through the same system.

## More on this topic

- [How to grow a Telegram channel from zero](/en/blog/grow-a-telegram-channel/)
- [Telegram channel or Instagram: where should a business invest?](/en/blog/telegram-or-instagram-for-business/)
- [New Year content plan: 8 weeks from November to January](/en/blog/new-year-content-plan/)
