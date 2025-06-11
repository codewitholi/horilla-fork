#!/bin/bash


# Wait until postgres is ready
while ! pg_isready -q -h $DB_HOST -p $DB_PORT -U $DB_USER -d $DB_NAME
do
echo "$(date) - Waiting for postgres database to be ready"
sleep 2
done

echo "$(date) - Postgres database is ready"
