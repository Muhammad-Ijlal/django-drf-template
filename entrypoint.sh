#!/bin/sh

# Load environment variables from .env file
if [ -f .env ]; then
  source .env
else
  echo "ERROR: .env file not found"
  exit 1
fi

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic

exec "$@"