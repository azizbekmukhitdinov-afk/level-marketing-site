---
title: Telegram channel post with a button: bot setup and click counts
description: A Telegram channel post with a button, step by step: connecting a bot, button types, what to write on the button and three ways to count clicks, with tables.
date: 2026-11-22
slug: telegram-channel-post-with-button
type: article
tags: Telegram, channel, bot, button
key: kanalda-tugmali-post
rubric: smm
weight: 1
---

When a channel post has a "Get the price" or "Book a visit" button under it, nobody has to hunt for a link in the text — they tap once. But the regular post composer has no such button: a Telegram channel post with a button is published through a bot. Below is how to connect one, what to write on the button and, most importantly, how to count the clicks.

![What a Telegram channel post with a button is and when you need one](/img/blog/illus/kanalda-tugmali-post-1.jpg 1200x675)

## What a Telegram channel post with a button is and when you need one

It is an ordinary channel post with one or more buttons under it. Telegram calls this an inline keyboard: it is attached to the message itself and shown together with it. Only a bot can add it, so the post is sent to the channel by your bot, not by you.

A button helps when:

- the post has one clear goal: a booking, a price request, a catalogue;
- you want to move people from the channel into a bot or onto your site;
- you need to know how many people each post brought.

If the post is just news or a useful tip, you can skip the button. When every post has one, subscribers get used to it and stop tapping.

## Button types: which ones work in a channel

The [Telegram Bot API documentation](https://core.telegram.org/bots/api#inlinekeyboardbutton) says each button does exactly one thing: it opens a link, sends a signal to the bot, or copies text. One button cannot do two jobs. The types a business needs are in the table.

| Button type | What happens on tap | In a channel | When to use it |
|---|---|---|---|
| Link (url) | A website or a link inside Telegram opens | Works | Sending people to a bot, a site, a catalogue |
| Signal (callback) | The bot is told about the tap, the person stays in the channel | Works | A poll, "I want this too", counting taps |
| Copy (copy_text) | Text is copied to the clipboard | Works | A promo code, an address, a phone number |
| Mini app (web_app) | An app opens inside the bot | Only in a private chat with the bot | Not suitable for a channel post |

A few limits are stated there as well:

- the data a signal button sends to the bot is 1 to 64 bytes, so a short tag (`price_sofa`), not a long text;
- copied text is up to 256 characters;
- a text post is up to 4096 characters, a photo caption up to 1024;
- a button can have a colour: a red, green or blue style.

Buttons are arranged in rows. You can put two or three in a row, but long labels get cut off on a phone. Give the main button a row of its own.

## Connecting a bot to your channel: 5 steps

You do not have to be a developer, but you should know the sequence — then you can check the work whoever does it.

1. **Create a bot.** Open @BotFather in Telegram, create a new bot and get its token. The token is the key to the bot. Do not show it to anyone, not even in a screenshot.
2. **Make the bot a channel administrator.** In the channel settings, add the bot to the administrators and grant only the right it needs: posting messages. If you plan to edit posts later, add the editing right too. The other rights (adding administrators, removing subscribers) are not needed.
3. **Prepare the post.** Text, image and buttons: a label and a link or a signal tag for each. Always add a tag to the link — more on that below.
4. **Send it to a test channel first.** Create a private test channel and add the bot there as well. Check how the post looks on a phone, whether the label is cut off and whether the link opens correctly.
5. **Publish to the main channel.** The bot posts on behalf of the channel — to a subscriber it looks like any other post, only with a button under it.

There are two ways to send the post. The first is a ready-made "post bot" service where you type the text and the button in a normal chat. The second is your own bot, set up once by a developer. A ready-made service is faster, but it also gets administrator rights in your channel, so check who you are trusting. With your own bot, the database and the statistics stay with you. If a bot already collects enquiries for you (see [collecting leads with a Telegram bot](/en/blog/telegram-bot-for-leads/)), it makes sense for the same bot to publish the posts.

Good news: the button can be changed after the post is out. The Bot API has a separate method that replaces only the keyboard and leaves the text alone. The promotion is over — you change the button to "Promotion ended, open the catalogue" and keep the post.

![Button text: 6 rules](/img/blog/illus/kanalda-tugmali-post-2.jpg 1200x675)

## Button text: 6 rules

The button is the shortest and most important text in the post. People may not read the whole post, but they will see the button.

1. **Start with a verb.** Not "Catalogue" but "Open the catalogue". People should know what happens after the tap.
2. **Two to four words.** Long labels get cut off on a phone. Always check in the test channel.
3. **One post, one main button.** With three equal buttons people cannot choose and tap none.
4. **Promise the result, not the process.** "Go to the bot" is a process. "Calculate the price" is a result.
5. **The post and the button are about the same thing.** A post about a sofa with an "All products" button confuses people.
6. **Keep the promise after the tap.** Someone tapped "Get the price" — the bot shows the price straight away instead of asking five questions first.

| Weak button | Strong button | Why |
|---|---|---|
| More | Get the price | People know what they will get |
| Bot | Pick a time | It has a verb and a result |
| Tap here | Open the catalogue | A specific action |
| Get in touch with us | Message a manager | Short, not cut off |

## How to count clicks: 3 ways

This is where most people go wrong. When someone taps a link button, Telegram tells the bot nothing: the person simply follows the link. There is no ready-made "button clicks" number. You have to measure it yourself.

| Method | What you see | What you need |
|---|---|---|
| A start link to the bot | How many people started the bot from each post | A separate parameter for each post: `?start=post_2211` |
| A site link with UTM tags | How many people came to the site from each post | UTM in the link and site analytics |
| A signal (callback) button | Every tap and who tapped | Your own bot that records the taps |

**Start link.** The link on the button looks like `https://t.me/your_bot?start=post_2211`. When someone starts the bot, the bot receives that tag and records which post they came from. The rules for the tag and examples are in the article on [moving channel subscribers into your bot](/en/blog/move-channel-subscribers-to-telegram-bot/). Note that this method counts bot starts, not taps. People who tapped and left without pressing "Start" stay invisible.

**UTM tags.** If the button leads to your site, add UTM to the link: the source is telegram, the campaign is the post name. How to build them is explained in the article on [UTM tags](/en/blog/utm-tags/).

**Signal button.** Each tap sends the bot a message that includes who tapped. The bot can show the person a short notification (up to 200 characters according to the documentation), for example: "Got it, a manager will message you". The documentation describes one more option: in response to a tap, the bot can open a link like `t.me/your_bot?start=...`. So the tap is counted and the person lands in the bot — two things at once. This needs your own bot.

Put the numbers into one table every week. The table below is an **illustrative example** for a furniture shop's channel; the numbers only show how the calculation works.

| Post | Views | Started the bot | Share | Enquiries |
|---|---|---|---|---|
| Sofa, "Calculate the price" | 2,000 | 60 | 3% | 9 |
| Kitchen, "Open the catalogue" | 1,800 | 27 | 1.5% | 2 |
| Promotion, "Get the discount" | 2,400 | 96 | 4% | 6 |

Two conclusions follow. First, compare the share between your own posts and do not look for a universal "norm" — it differs from channel to channel. Second, look at the last column. The promotion post brought more people into the bot, but the sofa post produced more enquiries. The goal is an enquiry, not a tap.

![6 mistakes in posts with a button](/img/blog/illus/kanalda-tugmali-post-3.jpg 1200x675)

## 6 mistakes in posts with a button

1. **The same link in every post.** Without a tag you cannot tell which post worked. Give each post its own parameter.
2. **Too many rights for the bot.** A bot that publishes posts does not need the right to add administrators or manage subscribers.
3. **The token in a group chat.** Whoever has the token can post to the channel as the bot. If the token has leaked, get a new one from @BotFather.
4. **An empty bot behind the button.** Someone taps "Get the price" and the bot says "Hello!" and goes silent. Build the path inside the bot first, then publish the post.
5. **Too many buttons.** Five or six buttons are a menu, not a post. Keep the menu inside the bot.
6. **Not checking the button in a paid post.** When you [place an ad in someone else's channel](/en/blog/telegram-advertising/), give that link its own parameter too, and tap the button yourself once the post is live.

## Questions and answers

**Can I make a post with a button without a bot, like a regular post?**
The button under a post is a bot keyboard, and a bot adds it. The option without a bot is a plain link in the text. It works too, but it is less visible.

**If a bot publishes the post, will the channel show "bot"?**
No, the post goes out on behalf of the channel. Subscribers see it as a regular post.

**Can I see who tapped the button?**
With a link button, no — you only see those who started the bot. With a signal button, the bot receives information about the person who tapped. But that does not give you the right to message them with ads: until a person starts the bot themselves, the bot cannot write to them. For later messages, follow the [broadcast rules](/en/blog/telegram-bot-broadcast-rules/).

**Can I add a button to an old post?**
If the bot published the post, yes — the bot can change the keyboard later. For posts you wrote by hand, the bot needs the editing right; test this in the test channel first.

**How many buttons should one post have?**
One main button and at most one supporting button. For example: "Calculate the price" with "Copy the address" under it.

A channel post with a button is not complicated: the bot becomes an administrator, the post gets one clear button, and every link gets its own tag. The rest is comparing the numbers every week and repeating the posts that brought enquiries. When Level Marketing works with clients, it connects channel posts, the bot and the CRM into one chain, so every enquiry shows which post it came from.

## More on this topic

- [Moving Telegram channel subscribers into your bot: step by step](/en/blog/move-channel-subscribers-to-telegram-bot/)
- [How to grow a Telegram channel from zero](/en/blog/grow-a-telegram-channel/)
- [Telegram bot broadcasts: 7 rules so customers don't block you](/en/blog/telegram-bot-broadcast-rules/)
