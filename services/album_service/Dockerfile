FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ./requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./app /app/app

COPY ./alembic /app/alembic

COPY ./entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
