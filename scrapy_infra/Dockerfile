
FROM python:3.12-slim

WORKDIR /scrapy_service
COPY . .
RUN apt update && apt -y upgrade && apt install lsof
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt --no-cache-dir
RUN mkdir /etc/scrapyd/
RUN cp ./scrapy_infra/scrapyd.conf /etc/scrapyd/