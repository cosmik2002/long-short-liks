FROM python:3.7-alpine

RUN adduser -D linksusr

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

WORKDIR /home/linksusr

COPY ../requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY ../links_transform links_transform
COPY ../migrations migrations
COPY ../main.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP main.py

RUN chown -R linksusr:linksusr ./
USER linksusr

ENTRYPOINT ["./boot.sh"]