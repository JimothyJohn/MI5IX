FROM python:3.11-slim-bookworm

# Configure environment
ENV DEBIAN_FRONTEND=noninteractive \
    PIP_PREFER_BINARY=1

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git && \
    rm -rf /var/lib/apt/lists/*

# Install Python packages
COPY requirements.txt /
RUN pip3 install --no-cache-dir -r \
    /requirements.txt && \
    rm /requirements.txt

COPY agency/ /app/agency/

# Use a non-root user
RUN useradd -m appuser
USER appuser
