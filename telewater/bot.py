''' This module defines the functions that handle different events.
'''

import os
import logging

from telethon import TelegramClient, events

from telewater.const import HELP, X_OFF, Y_OFF
from telewater.watermark import watermark_video
from telewater.utils import download_image, get_args


# TODO: (optional) send logs to attached logs channel


async def start(event):
    # TODO: authentication for admins and users via deep linking, or "enter your access code"
    await event.respond('Hi! I am alive.')
    raise events.StopPropagation


async def bot_help(event):
    try:
        await event.respond(HELP)
    finally:
        raise events.StopPropagation


async def set_image(event):
    # TODO: accept images directly besides urls
    # TODO: show preview on different sizes
    # TODO: allow image resize / compress/ transparent bkrnd

    try:
        image_url = get_args(event.message.text)
        # TODO: if args are empty, ask follow up question to get user-input
        download_image(image_url, 'image.png')
        await event.respond('Done')
    finally:
        raise events.StopPropagation


async def set_pos(event):
    try:
        pos_arg = get_args(event.message.text)
        # TODO: if the pos args are empty, ask follow up question to get user-input of standard postions (TOP/BOTTOM ...)
        #  specific pos must be supplied thru args
        global X_OFF, Y_OFF
        X_OFF, Y_OFF = pos_arg.split('*')
        await event.respond(f'X_OFF = {X_OFF} and Y_OFF = {Y_OFF}')
    finally:
        raise events.StopPropagation


async def watermarker(event):
    # TODO: reject large files (above certain file limit)
    # TODO: also watermark photos
    if event.gif or event.video:

        mp4_file = await event.download_media('')
        # TODO: suffix the downloaded media with time-stamp and user id

        outf = watermark_video(mp4_file, X_OFF, Y_OFF)
        print(outf)
        await event.client.send_file(event.sender_id, outf)
        os.remove(mp4_file)
        os.remove(outf)


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
    'start': (start, events.NewMessage(pattern='/start')),
    'help': (bot_help, events.NewMessage(pattern='/help')),
    'set_image': (set_image, events.NewMessage(pattern='/setimg')),
    'set_pos': (set_pos, events.NewMessage(pattern='/setpos')),
    'watermarker': (watermarker, events.NewMessage())
}
# this is a dictionary where the keys are the unique string identifier for the events
# the values are a tuple consisting of callback function and event
