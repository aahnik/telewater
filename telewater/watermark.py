""" Watermark is applied here."""

import os

from telewater.const import config


def watermark_video(video_file: str):
    """Apply watermark to video or gifs"""
    output_file = f"watered_{video_file}"
    # TODO: allow time stamping in file names
    # TODO: allow the ffmpeg options to be customized by bot admins
    # TODO: allow standard watermark positions like TOP/MIDDLE/BOTTOM/LEFT/RIGHT in total 9 combinations
    command = f'ffmpeg -i {video_file} \
        -i image.png \
        -an -dn -sn -r {config.frame_rate} \
        -preset {config.preset} \
        -tune zerolatency  -tune fastdecode \
        -filter_complex "overlay={config.x_off}:{config.y_off}" \
        {output_file}'

    print(command)
    os.system(command)
    return output_file


def watermark_image(image_file: str):
    pass
