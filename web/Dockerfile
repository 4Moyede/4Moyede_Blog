FROM node:15
WORKDIR /app/server
COPY . .
RUN apt-get update
RUN apt-get install -y vim
RUN npm install
CMD node app.js