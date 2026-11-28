---
title: Water delivery marketing: subscriptions, bots and repeat orders
description: Marketing a drinking water delivery business: a first-order offer, repeat orders through a Telegram bot, office contracts and customer retention, with an illustrative example.
date: 2026-11-28
slug: water-delivery-marketing
type: article
tags: water delivery, repeat sales, Telegram bot, B2B
key: suv-yetkazib-berish-marketing
rubric: biznes
---

Water delivery is a habit business. A family or an office picks a supplier once and then calls the same number for months, often years, without thinking about it. So marketing has two jobs: win the first order, and make the repeat order so easy that the customer never has a reason to look elsewhere. Let's go through both, with numbers, using a supplier of water in 19-litre bottles as the example.

## Why retention, not advertising, makes the money here

The profit on a single bottle is small. A customer acquired through ads almost never pays back on the first order; they start making you money in month three or four, sometimes later. That is why the key question in this niche is not "what did the lead cost?" but "how many months does the customer stay?"

The calculation below is an illustrative example. The figures are made up, but the logic holds in any city:

| Metric | Illustrative value |
|---|---|
| Price of one bottle to the customer | 18,000 soums |
| Water, bottle washing, delivery | 11,000 soums |
| Gross profit per bottle | 7,000 soums |
| Bottles per family per month | 3 |
| Monthly gross profit per family | 21,000 soums |
| Cost per lead from ads | 25,000 soums |
| Lead to first order | 40% |
| Cost to acquire one customer | 62,500 soums |

In this example a new customer pays back only at the end of month three. If half of your customers leave after the first month, your advertising loses money. If a customer stays 12 months, they bring 252,000 soums of gross profit, four times the acquisition cost. The takeaway: fix retention before you raise the ad budget. The method is explained in [repeat sales and LTV](/en/blog/repeat-sales-and-ltv/), and how to measure customers leaving in [customer churn](/en/blog/customer-churn-rate/).

## The first-order offer: who are you inviting?

The most common mistake is advertising "first bottle free". That offer pulls in freebie hunters: they order once and disappear. A good entry offer should carry the customer into a second and a third order.

Options that work:

- **Start without a bottle deposit.** What stops many people is not the price of water but the deposit on the bottle. Skip the deposit on the first order, or split it over three months, on the condition of at least two bottles.
- **A pump or dispenser with a subscription.** A free pump for customers who take at least N bottles a month, a rented dispenser for offices. Your equipment sitting in their home is the strongest retention tool you have.
- **A first-month bundle.** "Four bottles plus a pump" at a fixed price. In a month the customer gets used to your service.

The rule: however cheap the offer, it should cover at least a month of consumption. One free bottle does not create a habit. How to build an entry offer is covered in [the entry offer](/en/blog/entry-offer/).

## Repeat orders: a Telegram bot with one button

When does a customer switch to a competitor? The moment the water runs out and nobody answers your phone. So the repeat-order channel must be faster than a phone call.

A minimal bot flow:

1. On first use, the bot asks for the phone number with a button. The Telegram Bot API has exactly this: a button that sends the user's number as a contact, available in private chats only ([Bot API, KeyboardButton](https://core.telegram.org/bots/api#keyboardbutton)).
2. The address, floor and intercom code are saved once.
3. Next time the customer just taps "Two more bottles" and picks a delivery slot.
4. The bot confirms the order and tells the customer when the courier leaves.
5. The bot asks how many empty bottles there are, so the courier knows how many to collect.

Building the bot from scratch is covered in [how to create a Telegram bot](/en/blog/create-a-telegram-bot/).

### Reminders: a sale cheaper than any ad

Every customer has their own interval: one family takes a bottle every 10 days, another every 5. Calculate the days between the last two orders in your CRM or bot, and the day before the water should run out, send a personal reminder: "You usually order around now. Shall we bring it tomorrow morning?" with two buttons, "Yes" and "Later".

This is not a broadcast; it is a message that reaches each customer at their own time, which is why people do not block it. Mass broadcasts also have technical limits on Telegram: on the free tier a bot cannot broadcast more than about 30 messages per second ([Telegram Bots FAQ](https://core.telegram.org/bots/faq)). Broadcast etiquette is covered in [Telegram bot broadcasts](/en/blog/telegram-bot-broadcast-rules/).

## Subscription models: what suits whom

| Model | For | Upside | Risk |
|---|---|---|---|
| On request | Low-consumption families | Simple for the customer | Easy to switch to a competitor |
| Fixed schedule (e.g. every Tuesday) | Offices, large families | Courier routes known in advance | Water piles up and the customer cancels |
| Prepaid bundle (10 to 20 bottles) | Regular customers | Cash up front, customer committed | Discount eats the margin |
| Office contract | Companies | Large, stable volume | Paperwork and payment terms |

A practical rule: start ordinary customers on request with the bot, and offer a bundle or a schedule after the third order. Nobody agrees to a subscription before trying the service.

## Offices: a separate channel and a separate offer

An office means dozens of bottles a month and a customer for years. But someone else makes the decision: the office manager or administrator, whose concerns differ from a family's:

- a contract and invoices, payment by bank transfer;
- delivery on the same weekday without having to remind anyone;
- a dispenser and its regular sanitising;
- one named contact, a specific manager rather than a call centre.

Offices come from direct outreach, not Instagram ads: a list of business centres, calls to administrators, a free one-week dispenser trial. If you serve one office in a building, offer the neighbours too, since the courier is going there anyway. More on the B2B approach in [B2B marketing](/en/blog/b2b-marketing-uzbekistan/).

## Geography: density decides profit

Delivery cost depends less on distance than on route density. A courier covers 20 customers on one street in an hour; 20 customers spread across the city take a whole day.

So:

- run ads by radius in districts where you already have routes first;
- before opening a new district, gather enough customers there for at least one daily route;
- create listings on Google and Yandex Maps, because someone searching "water delivery" picks a nearby service. Here is how: [add your business to maps](/en/blog/add-your-business-to-maps/).

## Trust in quality: what to show

Until they drink it, customers don't know where your water comes from. Build trust with specifics:

- where the water comes from and how it is purified, in a short video from the plant;
- how bottles are washed and checked;
- laboratory test results, real documents only, with dates;
- courier uniforms, a clean van, bottles carried in and installed.

Avoid unprovable claims like "the purest water" in ads: comparative and superlative claims need evidence.

## Measuring retention: five numbers

| Number | How to calculate | Why it matters |
|---|---|---|
| Active customers | Ordered in the last 30 days | The real size of your base |
| Second-order rate | Reordered within the first month / new customers | Shows the quality of the entry offer |
| Monthly churn | No order for more than twice their usual interval | Early warning |
| Bottles in circulation | Bottles held by customers | Deposit and stock accounting |
| Share of orders via bot | Bot orders / all orders | Operator load and speed |

When a customer goes twice their usual interval without ordering, have an operator call them, not the bot, and ask why: price, a late delivery, a move. Winning back a lost customer is almost always cheaper than finding a new one.

## Common mistakes

- A one-off free promotion with no system behind it.
- Customer addresses and consumption kept only in the courier's head.
- Promising "delivery in 2 hours" and arriving the next day.
- Advertising to every district at once, so couriers criss-cross the city.
- Sending offices the same offer as families.

## Questions and answers

### Does a water delivery business need Instagram?

Yes, but not as the main sales channel. Instagram builds trust: the plant, the purification, the couriers. Orders come from maps, search, district-level targeted ads and referrals.

### Won't a discounted bundle kill the margin?

The bundle discount is what you pay for cash up front and for the customer staying several months. Keep the discount below half the profit on one bottle, and offer bundles only after the third order.

### A customer says a competitor is cheaper. Should I cut the price?

First find out why they are leaving. More often the cause is late deliveries or unanswered calls, not price. If it really is price, offer a bundle or a pump instead of a discount.

### Do referral programmes work?

Yes, because neighbours and colleagues ask each other. A simple mechanic: one free bottle for the referrer and one for the new customer, released after the new customer's second order.

## Conclusion

In water delivery the winner is not whoever advertises most, but whoever keeps customers longest. Let the entry offer build a month-long habit, the bot turn repeat orders into one tap, the reminder arrive before the water runs out, and offices get their own contract and manager. In a free audit, Level Marketing reviews your ads, funnel and repeat-order system and shows you where money is leaking.

## More on this topic

- [Loyalty programmes: bonuses and cashback that bring people back](/en/blog/loyalty-program/)
- [Unit economics: how to know how much you can pay for ads](/en/blog/unit-economics-for-small-business/)
- [Lead response time: how it affects sales](/en/blog/lead-response-time/)
