FROM node:15
WORKDIR /app/server
COPY . .
RUN apt-get update
RUN apt-get install -y openssh-server
RUN echo "PermitRootLogin yes" >> /etc/ssh/sshd_config
RUN echo 'root:pa22word!' | chpasswd
RUN /etc/init.d/ssh restart
RUN npm install
CMD node app.js