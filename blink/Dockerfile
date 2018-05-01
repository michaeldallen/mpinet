FROM alpine

RUN apk update

RUN apk add \
    gcc	\
    musl-dev \
    py2-pip \
    python \
    python-dev 

RUN pip install --upgrade pip

RUN pip install \
    RPi.GPIO \
    readchar

WORKDIR /root/blink

COPY blink.py .
