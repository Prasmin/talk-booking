# Stage 1: Builder
FROM python:3.11-slim as builder

# Install system deps + Poetry
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/* && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    poetry config virtualenvs.in-project true

WORKDIR /app

# Copy dependency files first for caching
COPY pyproject.toml poetry.lock ./

# Install prod deps only
RUN poetry install --only main --no-interaction --no-ansi

# Stage 2: Runtime
FROM python:3.11-slim

# Create non-root user (github-actions for clarity)
RUN groupadd -r github-actions && \
    useradd -r -g github-actions github-actions && \
    mkdir -p /home/github-actions && \
    chown -R github-actions:github-actions /home/github-actions

WORKDIR /app

# Copy virtualenv from builder
COPY --from=builder --chown=github-actions:github-actions /app/.venv .venv
COPY --chown=github-actions:github-actions . .

# Ensure scripts are executable
RUN chmod +x .venv/bin/*

USER github-actions
ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]