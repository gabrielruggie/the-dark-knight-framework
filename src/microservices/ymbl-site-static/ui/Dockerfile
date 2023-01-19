FROM node:alpine

WORKDIR /ymbl-site-static

COPY ./main/package.json /ymbl-site-static/package.json

COPY ./main/package-lock.json /ymbl-site-static/package-lock.json

RUN npm i

COPY ./main /ymbl-site-static/

CMD ["npm", "start"]


