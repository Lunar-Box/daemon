# --------------------------------
# Lunar Box
# Ubuntu Container
# --------------------------------

FROM python:3.8-buster

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y software-properties-common curl git tar bash
RUN addgroup --gid 998 server
RUN useradd -r -u 999 -d /home/server -g server -m server

USER root
ENV USER root
ENV HOME /home/server

WORKDIR /home/server
