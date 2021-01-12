FROM node:12.20.0-alpine

COPY . ./app

WORKDIR /app

RUN npm install -g pnpm

RUN pnpm install

EXPOSE 3002
EXPOSE 50051


CMD ["pnpm", "start"]
