FROM python:3.10-slim-bullseye

# Configure environment
ENV DEBIAN_FRONTEND=noninteractive \
    PIP_PREFER_BINARY=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    git


COPY requirements.txt /
RUN pip3 install -U --no-cache-dir -r \
    /requirements.txt && \
    rm /requirements.txt
