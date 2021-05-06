""" This module defines the functions that handle different events.
"""

import logging
import os

from telethon import TelegramClient, events

from telewater.const import HELP, Config, config
from telewater.utils import download_image, get_args
from telewater.watermark import watermark_video


async def start(event):
    await event.respond("Hi! I am alive.")
    raise events.StopPropagation


async def bot_help(event):
    try:
        await event.respond(HELP)
    finally:
        raise events.StopPropagation


async def set_config(event):
    """usage /set KEY: VAL"""
    global config
    try:
        pos_arg = get_args(event.message.text)
        splitted = pos_arg.split(":", 1)

        if not len(splitted) == 2:
            raise ValueError("Incorrect argument format")

        key, value = [item.strip() for item in splitted]

        config_dict = config.dict()
        if not key in config_dict.keys():
            raise ValueError(f"The key {key} is not a valid key in configuration.")

        config_dict[key] = value
        print(config_dict)

        config = Config(**config_dict)

        print(config)
        if key == "watermark":
            download_image(url=value)
        await event.respond(f"The value of {key} was set to {value}")

    except ValueError as err:
        print(err)
        await event.respond(str(err))
    except Exception as err:
        print(err)

    finally:
        raise events.StopPropagation


async def get_config(event):
    """usage /get KEY"""
    global config
    try:
        key = get_args(event.message.text)
        config_dict = config.dict()
        await event.respond(f"{config_dict.get(key)}")
    except ValueError as err:
        print(err)
        await event.respond(str(err))

    finally:

        raise events.StopPropagation


async def watermarker(event):
    # TODO: reject large files (above certain file limit)
    # TODO: also watermark photos
    global config
    if event.gif or event.video:

        mp4_file = await event.download_media("")
        # TODO: suffix the downloaded media with time-stamp and user id

        outf = watermark_video(mp4_file)
        print(outf)
        await event.client.send_file(event.sender_id, outf)
        os.remove(mp4_file)
        os.remove(outf)
    elif event.photo:
        await event.respond("Photos are currently not supported")


# TODO: fetch information about bot name
# TODO:set the bot commands

# client(functions.bots.SetBotCommandsRequest(
#     commands=[types.BotCommand(
#         command='some string here',
#         description='some string here'
#     )]
# ))
# client.run_until_disconnected()


ALL_EVENTS = {
    "start": (start, events.NewMessage(pattern="/start")),
    "help": (bot_help, events.NewMessage(pattern="/help")),
    "set": (set_config, events.NewMessage(pattern="/set")),
    "get": (get_config, events.NewMessage(pattern="/get")),
    "watermarker": (watermarker, events.NewMessage()),
}
# this is a dictionary where the keys are the unique string identifier for the events
# the values are a tuple consisting of callback function and event
