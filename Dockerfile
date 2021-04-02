FROM python:3.9

WORKDIR /app

RUN apt-get update && apt-get upgrade -y

RUN apt-get install ffmpeg -y

RUN pip install telewater

CMD ["telewater"]
