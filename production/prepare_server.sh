#!/bin/bash

# Prepares the server

echo "Preparing database..."
python3 manage.py makemigrations
python3 manage.py migrate
echo "Collecting static files"
python3 manage.py collectstatic --noinput

echo "Creating new horilla user..."
python3 manage.py createhorillauser \
  --first_name $HORILLA_INIT_FIRST_NAME \
  --last_name $HORILLA_INIT_LAST_NAME \
  --username $HORILLA_INIT_USERNAME \
  --password $HORILLA_INIT_PASSWORD \
  --email $HORILLA_INIT_EMAIL \
  --phone $HORILLA_INIT_PHONE \
  --no-color
