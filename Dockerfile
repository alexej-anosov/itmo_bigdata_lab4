FROM python:3.10

ENV PYTHONUNBUFFERED=1

ARG BUCKET_KEY_ID
ARG BUCKET_KEY
ARG REGION
ARG DB_URL

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && pip install -r requirements.txt

RUN aws configure set aws_access_key_id ${BUCKET_KEY_ID}
RUN aws configure set aws_secret_access_key ${BUCKET_KEY}
RUN aws configure set region ${REGION}

COPY . /app

WORKDIR /app
RUN dvc pull data/weights.joblib

WORKDIR src

ENV DB_URL = ${DB_URL}