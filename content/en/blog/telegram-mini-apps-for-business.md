---
title: Telegram Mini Apps for business: catalogs, booking, payments
description: What a Telegram Mini App is, how to use it for catalogs, booking and loyalty, the payment rules for Telegram Stars and physical goods, cost estimates and when a bot is enough.
date: 2026-11-28
slug: telegram-mini-apps-for-business
type: article
tags: Telegram Mini App, Telegram bot, Telegram Stars, online sales
key: telegram-mini-app
rubric: smm
---

Your customers already message you, read your channel and place orders in Telegram. But browsing a catalog or picking a time slot in an ordinary bot, through buttons and messages, is clumsy. A Telegram Mini App fixes that: a full website-like interface opens right inside Telegram. This article explains what a Mini App is, where it helps a business, what the payment rules are and when a plain bot is enough.

## What a Telegram Mini App is

A Mini App is a web app that opens inside Telegram. According to [Telegram's official documentation](https://core.telegram.org/bots/webapps), it is built with JavaScript, attached to a bot, and gives a flexible interface that can replace any website. For the user it is simple: open the bot, tap a button, and a catalog, booking page or personal account appears without leaving for a browser.

A Mini App can be opened from several places:

- the main app button on the bot's profile, or a `t.me/botname?startapp` link;
- the menu button in the chat;
- an inline button under a message, or a keyboard button;
- a direct link in the form `t.me/botname/appname`.

Per the documentation, a Mini App receives the user's Telegram theme (day or night colours), automatically knows basic data such as name and language, can open full screen and can be added to the phone's home screen as a shortcut. With the user's permission, geolocation and a QR code scanner also work. The main benefit for a business: the customer doesn't register or type a password, because Telegram already knows who they are.

A Mini App sits on top of a bot, so you need a bot first. How to create one from scratch is covered in [how to create a Telegram bot](/en/blog/create-a-telegram-bot/).

## Bot, Mini App or website: the difference

| Criterion | Plain bot | Mini App | Website |
|---|---|---|---|
| Interface | Messages and buttons | Pages, photos, filters, cart | Anything |
| Sign-up | Not needed | Not needed, Telegram knows the user | Usually needed, or a form |
| Follow-up contact | Bot can message | Messages via the bot | Email, SMS or ads |
| Traffic from Google | No | No | Yes (SEO) |
| Development effort | Small | Medium | Medium to large |
| Best job | Leads, answers, reminders | Catalog, booking, personal account | Customers from search, trust |

One important point: a Mini App does not fully replace a website. It won't show up in Google search. It works best for an audience you already have in Telegram: channel subscribers, bot users and people arriving from Telegram ads.

## Four use cases for business

**1. Catalog and ordering.** Shops, cafes, flower delivery, building materials: filters, photos, a cart and an address. Instead of writing "how much is it?", the customer chooses on their own and the manager receives a ready order. For online store marketing in general, see [online store marketing](/en/blog/marketing-an-online-store/).

**2. Booking and appointments.** Beauty salons, clinics, car services, training centres: pick a service, a specialist and a free slot. The bot then sends reminders automatically. This is where a Mini App pays back fastest, because agreeing on a time in chat takes many messages.

**3. Loyalty card.** Instead of a plastic card, a bonus balance and a QR code inside Telegram. The cashier scans the code and the bot reminds the customer: "you have 35,000 soums in bonuses." How to design the bonus mechanics is covered in [loyalty programmes](/en/blog/loyalty-program/).

**4. Calculator, quiz or selection helper.** A renovation cost calculator, a "which course suits you" quiz, an instalment payment calculator. At the end the customer leaves their contact, and it's a high-quality lead because the person has already defined what they need. On collecting leads with a bot, see [collecting leads with a Telegram bot](/en/blog/telegram-bot-for-leads/).

## Payments: rules for digital and physical goods

This is where most mistakes happen. Telegram treats digital and physical goods differently.

| What you sell | How to take payment | Source |
|---|---|---|
| Digital goods and services (online course, subscription, e-book, in-app features) | Telegram Stars only | [Telegram Stars rules](https://core.telegram.org/bots/payments-stars) |
| Physical goods and offline services (clothes, food, salon services) | Various currencies and payment providers | [Bot Payments rules](https://core.telegram.org/bots/payments) |

Telegram's [Stars page](https://core.telegram.org/bots/payments-stars) says it plainly: payments for digital goods and services must be made exclusively in Telegram Stars. The reason is App Store and Google Play rules. If the rule is broken, Telegram may not show the bot or Mini App to mobile users. So a business selling online courses should not plan to take card payments inside a Mini App.

For physical goods and services you may use other currencies and providers. A provider is connected through the payment settings in BotFather, and the currency table in the [Bot Payments documentation](https://core.telegram.org/bots/payments) includes the Uzbek soum (UZS). Check BotFather's current list to see which local providers are available, and follow the rules of the provider you choose. Many businesses have a simpler option too: take the order in the Mini App and collect payment on delivery or through your own payment system. Agree this with your developer and payment provider in advance.

## How to estimate the cost

A Mini App's price depends on its scope. Rather than guessing market prices, it's more useful to estimate the work in hours. The figures below are an illustrative example, not a quote:

| Option | Rough effort (illustrative) | What's included |
|---|---|---|
| Plain bot | 20–40 hours | Leads, answers to questions, manager alerts |
| Catalog or booking Mini App | 80–200 hours | Design, pages, admin panel, connection to the bot |
| + payments and CRM integration | +40–80 hours | Provider, writing orders to the CRM, status messages |
| Support | 5–15 hours a month | Bugs, price and catalog updates |

Final price = hours × the hourly rate of your developer or team. Don't forget support: catalogs and prices change, and Telegram keeps adding features.

## Illustrative example: a booking Mini App for a salon

The numbers below are an illustrative example. A salon gets 400 people a month writing to it on Telegram.

**Now (in chat):** 25% of the 400 conversations end in a booking — 100 bookings. The administrator spends an average of 4 minutes per conversation: 400 × 4 = 1,600 minutes, about 27 hours.

**With a Mini App:** 30% of the 400 people book on their own — 120 bookings. The administrator only talks to the 100 people who have questions: 100 × 4 = 400 minutes, about 7 hours.

With an average ticket of 250,000 soums, the extra 20 bookings bring 5,000,000 soums of revenue a month. At a 40% gross margin, that is 2,000,000 soums of profit. If development took 120 hours at an illustrative rate of 150,000 soums an hour, the cost is 18,000,000 soums. Calculate payback on profit, not revenue: 18,000,000 ÷ 2,000,000 = 9 months, not counting the administrator's saved time. If that's too long for you, try booking through a plain bot first.

## When a plain bot is enough

Before spending on a Mini App, answer these questions:

- **Fewer than 10–15 products?** A bot with buttons or a channel post is enough.
- **Does the customer want to talk before choosing anyway?** Renovation or real estate, for example. Then a lead bot and a fast reply matter more.
- **No audience in Telegram yet?** A Mini App doesn't bring traffic. Build your channel and bot audience first; how to move subscribers into a bot is covered in [moving Telegram channel subscribers into your bot](/en/blog/move-channel-subscribers-to-telegram-bot/).
- **Who will update the catalog?** If prices change daily and nobody is responsible, the Mini App will go stale fast.

A Mini App makes sense when you have many products or time slots, an active Telegram audience, frequent repeat orders and a named person who maintains the catalog.

## Common mistakes

- **Simply embedding the website in a Mini App.** A site that isn't adapted for mobile screens is just as awkward inside Telegram.
- **Not using bot messages.** A Mini App's strength is reminders and status updates through the bot. Going silent after an order wastes that.
- **Card payments for a digital product.** This goes against Telegram's rules and risks the app being hidden from mobile users.
- **Not measuring sources.** Use a separate `startapp` parameter for each post and ad so you can see which source produced orders.
- **Forgetting it after launch.** Once a month, review opens, orders and abandoned carts.

## Questions and answers

### Do users need to download a separate app?

No. A Mini App opens inside Telegram. Users only need Telegram, and according to the documentation they can even add the Mini App to their home screen as a shortcut.

### Can I use Telegram Stars for physical goods?

In Telegram's rules, Stars are mandatory for digital goods and services. Other providers and currencies are allowed for physical goods. Local customers usually find paying in soums more convenient.

### How do I promote a Mini App?

Through a button in a channel post, the bot's menu button, and ad links in Telegram and on other platforms. Use a separate link parameter for each source so you can measure results.

### Can I build a Mini App with a no-code builder?

Builders exist for simple catalogs or booking, and they launch faster. But if you need custom logic, deep CRM integration or a non-standard design, you'll need custom development.

## Conclusion

A Telegram Mini App is a tool for catalogs, booking, loyalty and calculators for businesses that already have an audience in Telegram. Digital goods can only be sold for Telegram Stars; physical goods and services may use other providers. Decide based on development hours and payback calculated on profit, and if your catalog is small or your sales depend on conversation, start with a plain bot.

Whether your Telegram sales funnel needs a Mini App or a bot will do — Level Marketing can work through that with you during a free audit.

## More on this topic

- [Telegram bot broadcasts: 7 rules so customers don't block you](/en/blog/telegram-bot-broadcast-rules/)
- [Telegram channel post with a button: bot setup and click counts](/en/blog/telegram-channel-post-with-button/)
- [A Telegram AI assistant: replying to leads 24/7](/en/blog/telegram-ai-assistant/)
