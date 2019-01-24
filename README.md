# Zulip Kudos Bot

A [Zulip](https://zulipchat.com/) bot for giving kudos to your community.

## What is Kudos

**Praise and honour received for an achievement.**

> Kudos comes from Greek and means ‘praise’. Despite appearances, it is not a plural form. This means that there is no singular form kudo and that the use of kudos as a plural, as in the following sentence, is incorrect: he received many kudos for his work (correct use is he received much kudos for his work)  
-- Oxford Dictionary



## How to use this on RC Community

### 1. Setup  
Recurse Center zulip already have a Kudos Bot, so no need to setup of the bot.

### 2. Send Kudos  
In any stream, topic or private message @mention Kudos, the person or persons you want to honour and write your message with any markdown style.

```
@Kudos @Terry O'Shea (W2'19) @Meredith Finkelstein (W2'19) @Michelle Torres (W2'19)
Great job during the Hack RC event!
This bot is amazing :parrot:
```

**Important Note**  
We trust in your good sense, so we do not filter the content of your message.
Please use it wizely.

### 3. Anonymous
You can do anonymous so the person will receive Kudos but will not know you are the sender.

Use `--anon` on the content of the message


### 4. Where the Kudo appears  
You can find all Kudos on #Kudos stream and there are topics for each person that receive kudos!

## How to use this project on my own Zulip instance

### 1. Create the bot
  1. From your desktop, click on the gear :gear: in the upper right corner.
  2. Select Settings.
  3. On the left, click Your bots.
  4. Click Add a new bot.
  5. Select 'Generic Bot'
  5. Fill out the fields, and click Create bot.


### 2. Get bot details
Copy the details from your bot for api key, email, etc.

### 3. Deploy
Run now with environment variables using the ones from step 2.

### 4. Cronjob
Configure an account on cron-job.org to ping your url every minute.


## :busts_in_silhouette: Contributors
- [Terry](https://github.com/TerryOShea)
- [Meredith](https://github.com/msrobot0)
- [Michelle](https://github.com/nmicht)

## About this bot

We created this bot as part of Hack RC (Recurse Center) event on 2019.

[Recurse Center](https://www.recurse.com/) (before Hacker School) is a self-directed, community-driven educational retreat for programmers in New York City.
