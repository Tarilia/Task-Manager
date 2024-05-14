FROM python:3.10 as base

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWEITEBYTECODE 1

WORKDIR /task-manager

RUN pip install --upgrade pip --no-cache-dir && \
    pip install poetry --no-cache-dir && \
    poetry config virtualenvs.create false && \
    poetry config installer.max-workers 1

COPY pyproject.toml poetry.lock ./

COPY . .

FROM base as dev

RUN poetry install --no-interaction --no-ansi


FROM base as prod

RUN poetry install --without dev --no-interaction --no-ansi
