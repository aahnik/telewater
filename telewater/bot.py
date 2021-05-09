""" This module defines the functions that handle different events.
"""

import logging
import os

from telethon import events

from telewater import conf
from telewater.utils import cleanup, download_image, get_args, stamp
from telewater.watermark import watermark_image, watermark_video


async def start(event):
    await event.respond("Hi! I am alive.")
    raise events.StopPropagation


async def bot_help(event):
    try:
        await event.respond(conf.HELP)
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

        config_dict = conf.config.dict()
        if not key in config_dict.keys():
            raise ValueError(
                f"The key {key} is not a valid key in configuration.")

        config_dict[key] = value
        print(config_dict)

        conf.config = conf.Config(**config_dict)

        print(conf.config)
        if key == "watermark":
            cleanup("image.png")
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
    try:
        key = get_args(event.message.text)
        config_dict = conf.config.dict()
        await event.respond(f"{config_dict.get(key)}")
    except ValueError as err:
        print(err)
        await event.respond(str(err))

    finally:

        raise events.StopPropagation


async def watermarker(event):
    global config
    if event.gif or event.video:
        watermark = watermark_video
    elif event.photo:
        watermark = watermark_image
    else:
        return

    org_file = stamp(await event.download_media(""), user=str(event.sender_id))
    out_file = watermark(org_file)
    await event.client.send_file(event.sender_id, out_file)
    cleanup(org_file, out_file)


ALL_EVENTS = {
    "start": (start, events.NewMessage(pattern="/start")),
    "help": (bot_help, events.NewMessage(pattern="/help")),
    "set": (set_config, events.NewMessage(pattern="/set")),
    "get": (get_config, events.NewMessage(pattern="/get")),
    "watermarker": (watermarker, events.NewMessage()),
}
# this is a dictionary where the keys are the unique string identifier for the events
# the values are a tuple consisting of callback function and event
