FROM python:3.10 as base

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWEITEBYTECODE 1

WORKDIR /task-manager

RUN pip install "poetry==1.5.1"

COPY . .

RUN poetry config virtualenvs.create false
RUN poetry config installer.max-workers 1


FROM base as dev

RUN poetry install --no-interaction --no-ansi


FROM base as prod

RUN poetry install --without dev --no-interaction --no-ansi
