""" Watermark to videos is applied here."""

import logging
import os

from telewater import conf


def watermark_video(video_file: str, watermark_file: str = "image.png"):
    """Apply watermark to video or gifs"""
    output_file = f"watered_{video_file}"
    command = f'ffmpeg -i {video_file} \
        -i {watermark_file} \
        -an -dn -sn -r {conf.config.frame_rate} \
        -preset {conf.config.preset} \
        -tune zerolatency  -tune fastdecode \
        -filter_complex "overlay={conf.config.x_off}:{conf.config.y_off}" \
        {output_file}'

    logging.info(f"Running command {command}")
    os.system(command)
    return output_file
