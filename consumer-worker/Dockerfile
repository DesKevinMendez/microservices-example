FROM node:16.10.0-alpine as CONSUMER-WORKER

RUN apk --no-cache add \
      bash \
      g++ \
      ca-certificates \
      lz4-dev \
      musl-dev \
      cyrus-sasl-dev \
      openssl-dev \
      make \
      python3

RUN apk add --no-cache --virtual .build-deps gcc zlib-dev libc-dev bsd-compat-headers py-setuptools bash

COPY ./package.json /home/

COPY . /home/

WORKDIR /home/

RUN yarn install
