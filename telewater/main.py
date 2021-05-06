""" This module provides the pythonic entry point for accessing telewater.
"""


import os

from telethon.sync import TelegramClient, functions, types

from telewater.bot import ALL_EVENTS
from telewater.const import COMMANDS, config
from telewater.utils import download_image


def start_bot(API_ID: int, API_HASH: str, name: str, token: str):
    os.makedirs(name, exist_ok=True)
    os.chdir(name)

    if config.watermark:
        download_image(url=config.watermark)

    client = TelegramClient(name, API_ID, API_HASH).start(bot_token=token)

    client(
        functions.bots.SetBotCommandsRequest(
            commands=[
                types.BotCommand(command=key, description=value)
                for key, value in COMMANDS.items()
            ]
        )
    )

    for key, val in ALL_EVENTS.items():
        print(f"Adding event {key}")
        client.add_event_handler(*val)

    print(f"Started bot {name}")
    client.run_until_disconnected()
