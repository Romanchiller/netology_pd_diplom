FROM python:3.10-alpine

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /code/
RUN pip install -r requirements.txt


COPY . /code/

