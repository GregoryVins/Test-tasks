FROM node:12.18.4
RUN mkdir client/
COPY client/ /client/
WORKDIR ./client
RUN npm i
RUN npm run build
CMD npm run start
