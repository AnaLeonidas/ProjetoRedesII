FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y python3

WORKDIR /app

COPY cliente_03.py .

CMD ["python3", "./cliente_03.py"]