FROM node:16.10.0-alpine

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

# Create app directory
RUN mkdir -p /usr/local/app

# Move to the app directory
WORKDIR /usr/local/app

# Copy package.json first to check if an npm install is needed

COPY ./package.json ./
COPY ./yarn.lock ./
RUN yarn install --no-cache
COPY . .
EXPOSE 3000
ENTRYPOINT ["yarn", "producer"]