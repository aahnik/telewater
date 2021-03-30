# telewater

A telegram bot that applies watermark on images, gifs and videos.

## Features

- **Fast** because it is made using async libraries.
- **Simple** to use.
- Any one who uses an instance of the bot will have to use the same watermark and position. This is meant to be used by **single person/organization** (by only you or your team), as configuration is global.
- **No database** connection required.
- It **does not store media** (photos/videos/gifs) on the server. Media is deleted immediately after the watermarked version is sent to the user.


## Where to Deploy

- It is recommended to run this on a **Linux VPS**.
- [Heroku](https://www.heroku.com/) made me cry. Don't be seduced by "free" and "one-click" deploys.
- [Digital Ocean](https://www.digitalocean.com/) Ubuntu Droplet is a good choice for high performance.


## Requirements

Make sure to have these installed in your system.

- [python3.9+](https://www.python.org/) and [pip](https://pip.pypa.io/en/stable/installing/) (the bot is built with the telethon library)
- [ffmpeg](https://ffmpeg.org/) (used by the bot for applying watermark)

### Verification

Open you terminal to check if you have all basic requirements properly installed.

1. Run `python --version` and you should get something like this `Python 3.9.2` (or above).
2. Run `pip --version` and you should get `pip 20.2.2` (or above).

    > Some systems may require to use `python3` and `pip3` instead of the above.

3. Run `ffmpeg -h` and it should display a help message and version above `4.2.4`.

## Installation

```shell
pip install telewater
```


## Configuration

Create a file named `.env` inside your current directory (or the directory from which you desire to run the `telewater` command.)

Fill the file with your `API_ID` and `API_HASH`

Example:

```txt
API_ID=12345
API_HASH=102837:kjfjfk9r9JOIJOIjoi_jf9wr0w
```

Replace the above values with the actual values. Learn [how to get them](https://docs.telethon.dev/en/latest/basic/signing-in.html) for your telegram account.


## Usage

Telewater has a simple command line interface to start the bot.

Simply open your terminal and run `telewater`.


> **Note:**
> - It will prompt you to input the bot name and token.

For more advanced options, run `telewater --help`.

```shell
Usage: telewater [OPTIONS]

  Run the bot with the username and token obtained from @BotFather.

Options:
  -n, --name TEXT   Name of the bot you are runnning.  [env var: BOT_USERNAME;
                    required]

  -t, --token TEXT  Bot Token obtained from @BotFather.  [env var: BOT_TOKEN;
                    required]

  -l, --loud        Increase output verbosity.  [env var: LOUD]
  -v, --version     Show version and exit.
  --help            Show this message and exit.
```



> **Note:**
> - In the above help text, you see `env var` specified for some options. The value of those options can be set by using an environment variable (of the specified name), instead of passing as a command line argument.
> - You can write your enviroment variables for telewater inside a file called `.env` which lies in the same directory from which `telewater` command is invoked.

For any furthur help, feel free to create an issue.
