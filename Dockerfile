FROM python:3.11 as base

ENV C_FORCE_ROOT=True
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/code

WORKDIR /code

RUN /usr/local/bin/python -m pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir poetry==1.3.2

COPY pyproject.toml poetry.lock requirements.txt /code/

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --without dev

COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

COPY scripts/web/startup.sh /code/scripts/web/startup.sh
RUN chmod +x /code/scripts/web/startup.sh

# tests image
FROM base AS test

RUN poetry install --no-interaction --no-ansi --with dev

USER 1001