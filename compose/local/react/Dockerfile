# syntax=docker/dockerfile:experimental
FROM node:14.9-alpine

WORKDIR /app/
COPY ./frontend/package.json /app/

RUN yarn install

# Works without the following copy
COPY . /app/

EXPOSE 3000
 
CMD [ "yarn", "start" ]
