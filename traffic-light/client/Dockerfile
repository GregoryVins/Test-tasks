FROM node
RUN mkdir client/
COPY ../ /client/
WORKDIR /client
RUN npm install -g @angular/cli
RUN npm install
RUN npm start
