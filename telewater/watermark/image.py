import logging

from PIL import Image

from telewater import conf
from telewater.utils import cleanup


def to_png(file: str) -> str:
    im = Image.open(file)
    if not file.endswith(".png"):
        png_file = f"{file}.png"
        im.save(png_file)
    else:
        png_file = file

    return png_file


def _open_image(file: str):
    im = Image.open(file)
    logging.info(
        f"""Opened Image {file}
        Image format {im.format}
        Mode {im.mode}
        Size {im.size}
            Height {im.height}
            Width {im.width}
    """
    )
    im = im.convert("RGBA")

    return im


def watermark_image(image_file: str, watermark_file: str = "image.png"):
    png = to_png(image_file)
    im = _open_image(png)
    wt = _open_image(watermark_file)
    im.alpha_composite(im=wt, dest=(conf.config.x_off, conf.config.y_off))
    output_file = f"watered_{png}"
    im.save(output_file)
    cleanup(png)
    return output_file
