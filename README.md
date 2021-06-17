# telewater

A telegram bot that applies watermark on images, gifs and videos.

## Features

- **Fast** because it is made using async libraries.
- **Simple** to use.
- Any one who uses an instance of the bot will have to use the same watermark and position. This is meant to be used by **single person/organization** (by only you or your team), as configuration is stored at a global level instead of per user basis.
- **No database** connection required.
- It **does not store media** (photos/videos/gifs) on the server. Media is deleted immediately after the watermarked version is sent to the user.

Watch this [video on YouTube](https://www.youtube.com/watch?v=M-ouyCPdZw0) to learn how to use and deploy this bot.

## Usage

Using the bot is very simple. Just send a photo, video or gif to the bot. The bot will reply with the watermarked media.

The bot commands `/set` and `/get` can set and get the value of the configuration variables. The commands are simple and intuitive. The bot will show you the usage if you send an incorrect argument.

## Deploy

Click on [this link](https://m.do.co/c/98b725055148) and get **free 100$**
on Digital Ocean.

[![DigitalOcean Referral Badge](https://web-platforms.sfo2.digitaloceanspaces.com/WWW/Badge%203.svg)](https://www.digitalocean.com/?refcode=98b725055148&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge)

> **NOTE** You will get nothing if you directly sign up from Digital Ocean Home Page.
> **Use the link** above, or **click on the big fat button** above to get free 100$.

Read the **[Guide to Deploy to Digital Ocean](https://github.com/aahnik/telewater/wiki/Deploy-to-Digital-Ocean)**.

------

This application can also be easily deployed to Heroku, which is extremely good if you want to enjoy a free tier.

You may [read further](#further-reading) to learn about more more deployment options.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/aahnik/telewater)

Click on the above button. A form will appear, where you need to enter the credentials for the bot. After the app is deployed sucessfully, [turn on the woker dyno](https://user-images.githubusercontent.com/66209958/117938593-d6de0080-b324-11eb-9c0f-9bcc6d975808.png) to start the bot.

## Installation

The following is the guide to install `telewater` on your computer, or VPS.

If you are a beginner, don't bother yourself with these. Just go ahead with the heroku method described abvoe.

If you are familiar with **Docker** then [click here](https://github.com/aahnik/telewater/wiki/Install-and-run-using-docker) otherwise, continue reading.

#### Requirements

Make sure to have these installed in your system.

- [python3.9+](https://www.python.org/) and [pip](https://pip.pypa.io/en/stable/installing/) (the bot is built with the telethon library)
- [ffmpeg](https://ffmpeg.org/) (used by the bot for applying watermark)

#### Verification

Open you terminal to check if you have all basic requirements properly installed.

1. Run `python --version` and you should get something like this `Python 3.9.2` (or above).
2. Run `pip --version` and you should get `pip 20.2.2` (or above).

    > Some systems may require to use `python3` and `pip3` instead of the above.

3. Run `ffmpeg -h` and it should display a help message and version above `4.2.4`.

#### Install via pip

```shell
pip install telewater
```

#### Starting `telewater`

Telewater has a simple command line interface to start the bot.

Simply open your terminal and run `telewater`. It will prompt you to enter the required information.

## Further reading

- [Environment Variables](https://github.com/aahnik/telewater/wiki/Environment-Variables)
- [Telewater CLI usage](https://github.com/aahnik/telewater/wiki/Telewater-CLI-usage)
- [Install and run using docker](https://github.com/aahnik/telewater/wiki/Install-and-run-using-docker)
- [Deploy to Digital Ocean](https://github.com/aahnik/telewater/wiki/Deploy-to-Digital-Ocean)
- [Run multiple instances](https://github.com/aahnik/telewater/wiki/Run-multiple-instances)

For any further help, feel free to [create an issue](https://github.com/aahnik/telewater/issues) in the GitHub repo.

<!-- AAHNIK 2021 -->
