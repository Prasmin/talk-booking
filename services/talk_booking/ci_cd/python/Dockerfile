FROM python:3.11-slim

# Create github user and set up home directory
RUN mkdir -p /home/github && \
    addgroup github && \
    useradd -d /home/github -g github github && \
    chown github:github /home/github

# Install curl (as root)
RUN apt-get update && apt-get install -y curl

# Switch to github user
USER github
WORKDIR /home/github

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to PATH and configure virtualenvs
ENV PATH=/home/github/.local/bin:$PATH
RUN poetry config virtualenvs.in-project true