FROM node:alpine

WORKDIR /astack-authentication

COPY ./main/package.json /astack-authentication/package.json

COPY ./main/package-lock.json /astack-authentication/package-lock.json

RUN npm i

COPY ./main /astack-authentication/

CMD ["npm", "start"]
