FROM python:3.10

ARG BUCKET_KEY_ID
ARG BUCKET_KEY
ARG REGION

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app/

RUN aws configure set aws_access_key_id ${BUCKET_KEY_ID}
RUN aws configure set aws_secret_access_key ${BUCKET_KEY}
RUN aws configure set region ${REGION}

RUN dvc pull src/data/weights.joblib

ENV PYTHONUNBUFFERED=1

