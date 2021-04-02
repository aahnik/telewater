''' Watermark is applied here.
'''

import os


def watermark_video(video_file: str, X_OFF: int = 10, Y_OFF: int = 10):
    output_file = f'watered_{video_file}'
    # TODO: allow time stamping in file names
    # TODO: allow the ffmpeg options to be customized by bot admins
    # TODO: allow standard watermark positions like TOP/MIDDLE/BOTTOM/LEFT/RIGHT in total 9 combinations
    command = f'ffmpeg -i {video_file} \
        -i image.png \
        -an -dn -sn -r 10 \
        -preset ultrafast \
        -tune zerolatency  -tune fastdecode \
        -filter_complex "overlay={X_OFF}:{Y_OFF}" \
        {output_file}'

    print(command)
    os.system(command)
    return output_file
