FROM python:3.12

ENV PYTHONPATH=/app

WORKDIR /app

COPY requirements.txt /app/

RUN apt-get update && apt-get install -y netcat-openbsd

RUN pip install --no-cache-dir -r requirements.txt

COPY app /app/app
COPY alembic.ini /app/alembic.ini
RUN ls -al

EXPOSE 8075

