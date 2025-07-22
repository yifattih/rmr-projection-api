FROM ubuntu:24.04

RUN apt-get update \
  && apt-get install -y \
  git \
  curl \
  python3 \
  python3-pip \
  pipx \
  ca-certificates \
  build-essential \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*
