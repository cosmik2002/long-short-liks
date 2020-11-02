FROM python:3.7-alpine

RUN adduser -D linksusr

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

WORKDIR /home/linksusr

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY links_transform links_transform
COPY migrations migrations
COPY tests tests
COPY main.py config.py boot.sh conftest.py ./
COPY wait_for_it.py wait_for_it.py
RUN chmod +x boot.sh

ENV FLASK_APP main.py

RUN chown -R linksusr:linksusr ./
USER linksusr

ENTRYPOINT ["./boot.sh"]