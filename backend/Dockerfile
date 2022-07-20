FROM python:3.8-alpine
ENV PYTHONBUFFERED 1
WORKDIR /alpine
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .