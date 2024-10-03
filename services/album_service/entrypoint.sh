#!/bin/bash

set -e

function wait_for_db() {
  echo "Waiting for PostgreSQL to start..."
  while ! nc -z db 5432; do
    sleep 0.1

  done
  echo "PostgreSQL started."
}

wait_for_db

echo "Running Alembic migrations..."

alembic upgrade head

echo "Starting FastAPI server..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000