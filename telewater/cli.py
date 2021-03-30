''' This module implements the command line interface for telewater,
using the modern and robust `typer`.
'''


from typing import Optional
import logging

import typer

from telewater import __version__
from telewater.main import start_bot
from telewater.settings import FAKE


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
        name: str = typer.Option(...,
                                 '--name', '-n',
                                 help='Name of the bot you are runnning.',
                                 envvar='BOT_USERNAME',
                                 prompt='Please enter the bot name'),

        token: str = typer.Option(...,
                                  '--token', '-t',
                                  help='Bot Token obtained from @BotFather.',
                                  envvar='BOT_TOKEN',
                                  prompt='Please paste the bot token \
                                (your input will be invisible)',
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
    ''' Run the bot with the username and token obtained from @BotFather.
    '''

    if not FAKE:
        start_bot(name, token)
    else:
        # when the env var FAKE_TELEWATER is truthy, then no real work is done
        # this is for CLI testing purposes
        print(f'name is {name} and token is {token}')

# AAHNIK 2021
