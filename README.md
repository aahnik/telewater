# telewater

A telegram bot that applies watermark on images, gifs and videos.

## Features

- **Fast** because it is made using async libraries.
- **Simple** to use.
- Any one who uses an instance of the bot will have to use the same watermark and position. This is meant to be used by **single person/organization** (by only you or your team), as configuration is global.
- **No database** connection required.
- It **does not store media** (photos/videos/gifs) on the server. Media is deleted immediately after the watermarked version is sent to the user.


## Installation

If you are familiar with **Docker** then [click here](https://github.com/aahnik/telewater/wiki/Install-and-run-using-docker) otherwise, continue reading.

### Requirements

Make sure to have these installed in your system.

- [python3.9+](https://www.python.org/) and [pip](https://pip.pypa.io/en/stable/installing/) (the bot is built with the telethon library)
- [ffmpeg](https://ffmpeg.org/) (used by the bot for applying watermark)

### Verification

Open you terminal to check if you have all basic requirements properly installed.

1. Run `python --version` and you should get something like this `Python 3.9.2` (or above).
2. Run `pip --version` and you should get `pip 20.2.2` (or above).

    > Some systems may require to use `python3` and `pip3` instead of the above.

3. Run `ffmpeg -h` and it should display a help message and version above `4.2.4`.

### Install via pip

```shell
$ pip install telewater
```


## Usage

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
