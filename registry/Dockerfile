FROM python:3.7-slim
RUN mkdir /app
WORKDIR /app/
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
ENV FLASK_ENV="docker"
EXPOSE 5000