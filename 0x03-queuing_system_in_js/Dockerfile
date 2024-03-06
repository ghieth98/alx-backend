FROM node:latest as build
WORKDIR .
COPY package*.json .
RUN npm install
COPY . .

EXPOSE 3000

CMD node index.js