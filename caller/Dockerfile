FROM python:2.7.11-slim

WORKDIR /

ADD requirements.txt /
ADD caller.py /

RUN pip install -r requirements.txt
EXPOSE 6000
