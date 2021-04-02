''' This module implements the command line interface for telewater,
using the modern and robust `typer`.
'''

import os
from typing import Optional
import logging

import typer

from telewater import __version__
from telewater.main import start_bot

from dotenv import load_dotenv

load_dotenv('.env')

FAKE = bool(os.getenv('FAKE'))

app = typer.Typer(add_completion=False)


def version_callback(value: bool):
    if value:
        print(__version__)
        raise typer.Exit()


def verbosity_callback(value: bool):
    if value:
        logging.info(
            'Verbosity turned on. \nThis is suitable for debugging.\n')
        level = logging.INFO
    else:
        level = logging.WARNING
    logging.basicConfig(level=level)


@app.command()
def main(

    API_ID: int = typer.Option(...,
                               '--API_ID',
                               help='API ID obtained from my.telegram.org',
                               envvar='API_ID',
                               prompt='Paste your API ID (input hidden)',
                               hide_input=True),

    API_HASH: str = typer.Option(...,
                                 '--API_HASH',
                                 help='API HASH obtained from my.telegram.org',
                                 envvar='API_HASH',
                                 prompt='Paste your API HASH (input hidden)',
                                 hide_input=True),

    name: str = typer.Option(...,
                             '--name', '-n',
                             help='Name of the bot you are runnning.',
                             envvar='BOT_USERNAME',
                             prompt='Enter the bot name'),

    token: str = typer.Option(...,
                              '--token', '-t',
                              help='Bot Token obtained from @BotFather.',
                              envvar='BOT_TOKEN',
                              prompt='Paste the bot token (input hidden)',
                              hide_input=True,
                              confirmation_prompt=True),

    verbose: Optional[bool] = typer.Option(None,
                                           '--loud', '-l',
                                           callback=verbosity_callback,
                                           envvar='LOUD',
                                           help='Increase output verbosity.'),

    version: Optional[bool] = typer.Option(None,
                                           '--version',
                                           '-v',
                                           callback=version_callback,
                                           help='Show version and exit.')
):
    ''' A telegram bot that applies watermark on images, gifs and videos.

    For detailed docs read : https://github.com/aahnik/telewater
    '''

    if FAKE:
        print(f'name is {name} and token is {token}')
        print(f'API_ID = {API_ID} and API_HASH = {API_HASH}')
        quit(1)

        # when the env var FAKE is truthy, then no real work is done
        # this is for CLI testing purposes

    start_bot(API_ID, API_HASH, name, token)


# AAHNIK 2021
