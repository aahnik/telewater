""" This module defines the constants or default values.
"""
from pydantic import BaseModel, validator


class Config(BaseModel):
    watermark: str = "https://user-images.githubusercontent.com/66209958/109513526-35883200-7acb-11eb-97ed-c0b2ca72119a.png"
    x_off: int = 10
    y_off: int = 10
    frame_rate: int = 15
    preset: str = "ultrafast"

    @validator("preset")
    def validate_preset(val):
        allowed = ["ultrafast", "fast", "medium", "slow"]
        if not val in allowed:
            raise ValueError(f"Choose preset from {allowed}")
        return val


HELP = """
This bot is made with free and open source code.

Please star on GitHub

https://github.com/aahnik/telewater

"""

COMMANDS = {
    "start": "start the bot or check if alive",
    "set": "set the value for a config variable",
    "get": "know the value of a config variable",
    "help": "learn how to use the bot",
}

config = Config()
