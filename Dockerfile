FROM python:3.12-rc-slim-buster
WORKDIR /bot
COPY ./bot/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt