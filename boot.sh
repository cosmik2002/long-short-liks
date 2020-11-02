#!/bin/sh
source venv/bin/activate
python wait_for_it.py
flask db upgrade
py.test
exec gunicorn -b :5000 --access-logfile - --error-logfile - main:app --timeout 30