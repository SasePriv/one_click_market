FROM node:20.11.0 AS builder

ARG PROJECT_NAME
ARG PROJECT_EXTERNAL_PATH=frontend/

WORKDIR /temp

COPY ${PROJECT_EXTERNAL_PATH} .

RUN npm install

RUN npm run build

FROM node:20.11.0 AS server

ARG PROJECT_NAME

RUN mkdir ${PROJECT_NAME}
COPY .env .

WORKDIR ${PROJECT_NAME}

COPY --from=builder /temp/next.config.js ./
COPY --from=builder /temp/public ./public
COPY --from=builder /temp/.next ./.next
COPY --from=builder /temp/node_modules ./node_modules
COPY --from=builder /temp/package.json ./package.json


CMD [ "npm", "run", "start" ]


