""" Various utility functions are defined in this module.
"""


import shutil

import requests

# TODO: make file download using asynchronous method
# import aiohttp
# import aiofiles

# async def download_image(url: str, filename: str) -> bool:
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as resp:
#             if resp.status == 200:
#                 f = await aiofiles.open(filename, mode='wb')
#                 await f.write(await resp.read())
#                 await f.close()


def download_image(url: str, filename: str = "image.png") -> bool:
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
        raise ValueError(f"No args provided to command.")
    else:
        prefix, args = splitted
    print(prefix)
    args = args.strip()
    print(args)
    return args
