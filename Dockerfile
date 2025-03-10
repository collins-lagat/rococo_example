FROM python:3.12.4-slim-bookworm

# Set the default config file
ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive
ENV PATH=/home/app/.local/bin:$PATH
ARG GROUP_ID=1000
ARG USER_ID=1000

SHELL ["/bin/bash", "-xo", "pipefail", "-c"]

# Install base dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
  vim \
  && rm -rf /var/lib/apt/lists/*

# Create the app user
RUN groupadd -g "${GROUP_ID}" app \
  && useradd -m -l -u "${USER_ID}" -g app app \
  && mkdir -p /app \
  && chown -R app:app /app 

# Set the working directory
WORKDIR /app

# Set the user
USER app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt
