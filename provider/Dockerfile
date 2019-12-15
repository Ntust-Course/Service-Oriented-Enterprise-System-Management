FROM python:3.7-slim
RUN mkdir /app
WORKDIR /app/
COPY . /app
RUN apt update && apt install -y git
RUN pip install --no-cache-dir -r requirements.txt
ENV FLASK_ENV="docker"
EXPOSE 8001 8002