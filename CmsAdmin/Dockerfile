FROM python:3.7.9

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

ADD . /code

RUN python manage.py collectstatic --noinput
EXPOSE 8000

CMD [ "./start_uwsgi.sh" ]