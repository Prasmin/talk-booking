FROM python:3.11-slim

RUN mkdir -p /home/github && \
    addgroup github && \
    useradd -d /home/github -g github github && \
    chown github:github /home/github

USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl build-essential gcc \
    && rm -rf /var/lib/apt/lists/*
USER github 
# Install Poetry
# Using the official installation script from Poetry's documentation

WORKDIR /home/github

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH=/home/github/.local/bin:$PATH
RUN poetry config virtualenvs.in-project true

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY --chown=github:github pyproject.toml poetry.lock* ./
RUN poetry install --no-interaction --no-ansi --only main

COPY --chown=github:github . .

CMD ["poetry", "run", "uvicorn", "web_app.main:app", "--host", "0.0.0.0", "--port", "8000"]