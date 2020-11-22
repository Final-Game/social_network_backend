FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1

# RUN echo http://mirror.yandex.ru/mirrors/alpine/v3.8/main > /etc/apk/repositories; \
#     echo http://mirror.yandex.ru/mirrors/alpine/v3.8/community >> /etc/apk/repositories

RUN apk update && apk upgrade
RUN apk add --no-cache bash \
    pkgconfig \
    git \
    gcc \
    openldap \
    libcurl \
    python3-dev \
    gpgme-dev \
    libc-dev \
    && rm -rf /var/cache/apk/*
RUN wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py
RUN pip install setuptools==30.1.0


RUN mkdir /code
WORKDIR /code

COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

ADD . /code

RUN python manage.py collectstatic --noinput
EXPOSE 8000