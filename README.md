# Merch Notify

## Description

This script checks a webpage to see if they have added new merch since the last time this script checked.

This began because I want to buy a limited edition hat and I don't know when it will go on sale.

In the future, myself or others could reuse this code to set up other notifications based on changes on other websites.

## Problem

This is a simple project to solve a simple problem:

* Two comedians, whose podcast I listen to, are making available a limited edition run of a hat that I want to buy.
* It will sell out quickly.
* It is set to drop sometime this month, but I don't know when.

## Solution

Write a script to notify me when the hats go on sale!

### Explanation

This project uses a bash script to make a `curl` request to retrieve their merch page (sorted by most recent) and saves the source to `source.html`.

It then runs a Python script that does the following:

* Uses Beautiful Soup to parse the HTML
* Checks the list of product names against a list of product names previously saved locally
* If there are any product names not already in my local product list, it adds the product to my local list, and it uses `notify-send` to send me a desktop notification with the name of the new product and a link to the merch page

## Why the Git Repo?

The function this project performs is pretty specific, and I will stop using it as soon as I buy the hat that I want.

So why bother creating a Git repo?

As you might have guessed, it wouldn't be too hard to tweak the code and use it for other purposes. 

Maybe you'd like to be notified when concert tickets go on sale for a band you like?

Maybe you just want to be notified any time a specific webpage changes?

There are lot's of reasons you might want a personal notification if a site changes.

It wouldn't be hard to do this all from scratch, but hey, this might provide a scaffold that saves you some setup time.

## Usage

You'll have to review the code and make a few changes to get this to work.

I've changed the real URL out of courtesy to the site owner.

You will need to change the local path to your appropriate directory.

You will have to experiment to find the selector that retrieves the data you want. For context, the site this was built for uses Shopify. I haven't tested it, but there's a good chance this selector, or something similar, will work with other Shopify stores.

For more information on parsing HTML with Beatiful Soup, see their documentation here:
[Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

Once configured and working, I use a simple `watch -n [seconds] ./hat` command to run my bash script every N seconds. I recommend you check at most every few minutes. 

I run it in a tmux session so it can run in the background.

## Future Feature Ideas

* Connect with Twilio API and run on a VPS to send you text messages instead of desktop notifications. Then you wouldn't have to be at your computer to get the notification.

## Legal Disclaimer

This is for personal, non-commercial use only.
Use this at your own risk.
I'm not responsible for your behavior.

As far as I am aware, as of this writing, web scraping of publicly available information is generally accepted as perfectly legal in the US, though it may be against terms of service of individual websites.

If in doubt, check the site's `/robots.txt` file. 

If you use this code, please don't spam the server with requests every second. It can get your IP address blocked, which would defeat the purpose, and it's not good karma because it costs the server unnecessary bandwidth.

In other words, be nice :)
