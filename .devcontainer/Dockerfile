FROM python:3.13-slim as service

ENV DIR=/workspace

WORKDIR ${DIR}
COPY . ${DIR}

RUN apt-get -y update \
    && apt-get -y install git
RUN git config --global --add safe.directory ${DIR}

# Install dev dependencies
RUN pip install -e ".[dev]"

# Install production dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pre-commit ruff mypy
