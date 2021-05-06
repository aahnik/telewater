FROM python:3.9

WORKDIR /app

RUN apt-get update && apt-get upgrade -y

RUN apt-get install ffmpeg screen -y

RUN pip install --upgrade pip poetry

COPY telewater telewater

COPY README.md LICENSE pyproject.toml poetry.lock entrypoint ./

RUN chmod +x entrypoint

RUN poetry install

CMD poetry run ./entrypoint
