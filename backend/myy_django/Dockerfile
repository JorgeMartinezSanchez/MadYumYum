FROM python:latest-slim
WORKDIR /app

COPY ../requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 5000

RUN gunicorn app:app