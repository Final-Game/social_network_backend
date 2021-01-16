FROM nginx:1.15.11

COPY nginx.conf /etc/nginx/nginx.conf
COPY configs/* /etc/nginx/configs/

RUN rm -rf /etc/nginx/conf.d/*
COPY services/* /etc/nginx/conf.d/

EXPOSE 80