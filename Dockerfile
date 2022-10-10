FROM python:latest
WORKDIR /bot
COPY ./bot/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt