FROM python:3.9

WORKDIR /app

RUN apt-get update && apt-get upgrade -y

RUN apt-get install ffmpeg screen -y

RUN pip install --upgrade pip poetry

ENV POETRY_VIRTUALENVS_IN_PROJECT true

COPY telewater telewater

COPY README.md LICENSE pyproject.toml poetry.lock entrypoint.py ./

RUN poetry install

CMD poetry run python -u entrypoint.py
