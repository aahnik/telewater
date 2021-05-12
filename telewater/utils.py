""" Various utility functions are defined in this module.
"""


import logging
import os
import re
import shutil
from datetime import datetime

import requests

from telewater import conf


def download_image(url: str, filename: str = "image.png") -> bool:
    if filename in os.listdir():
        print("Image exists")
        return True
    try:
        print("Downloading image ... ")
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            print("Got file response")
            with open(filename, "wb") as file:
                response.raw.decode_content = True
                shutil.copyfileobj(response.raw, file)
    except Exception as err:
        print(err)
        return False
    else:
        print("File created image")
        return True


def get_args(text: str):
    splitted = text.split(" ", 1)
    if not len(splitted) == 2:
        return ""
    else:
        prefix, args = splitted
    print(prefix)
    args = args.strip()
    print(args)
    return args


def cleanup(*files):
    for file in files:
        try:
            os.remove(file)
        except FileNotFoundError:
            logging.info(f"File {file} does not exist.")


def stamp(file: str, user: str):

    now = str(datetime.now())
    outf = safe_name(f"{user} {now} {file}")
    try:
        os.rename(file, outf)
        return outf
    except Exception as err:
        logging.warning(f"Stamping file name failed for {file} to {outf}")


def safe_name(file_name: str):
    return re.sub(pattern="[-!@#$%^&*()\s]", repl="_", string=file_name)


def gen_kv_str():
    kv_string = "\n**Below is your current configuration**\n\n"
    for k, v in conf.config.dict().items():
        kv_string += f"`{k} : {v}`\n"
    return kv_string
