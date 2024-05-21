FROM python:3.11-slim-bookworm

# Configure environment
ENV DEBIAN_FRONTEND=noninteractive \
    PIP_PREFER_BINARY=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    git && \
    rm -rf /var/lib/apt/lists/*

# Install Python packages
COPY requirements.txt /
RUN pip3 install -U --no-cache-dir -r \
    /requirements.txt && \
    rm /requirements.txt

# Use a non-root user
RUN useradd -m appuser
USER appuser
