""" This module defines the constants or default values.
"""
from pydantic import BaseModel, validator
from watermark import Position


class Config(BaseModel):
    watermark: str = "https://raw.githubusercontent.com/Mahesh1414/image/main/20210903_221413.png"
    frame_rate: int = 15
    preset: str = "ultrafast"
    position: Position = Position.center

    @validator("preset")
    def validate_preset(val):
        allowed = ["ultrafast", "fast", "medium", "slow"]
        if not val in allowed:
            raise ValueError(f"Choose preset from {allowed}")
        return val


START = """I am alive!"""

HELP = """
Using the bot is very simple. Just send a photo, video or gif to the bot. The bot will reply with the watermarked media.

The bot commands `/set` and `/get` can set and get the value of the configuration variables. The commands are simple and intuitive. The bot will show you the usage if you send an incorrect argument.

Syntax for `/set` ➜  `/set key: value`
Syntax for `/get` ➜  `/get key`

"""

COMMANDS = {
    "start": "start the bot or check if alive",
    "set": "set the value for a config variable",
    "get": "know the value of a config variable",
    "help": "learn how to use the bot",
}

config = Config()
