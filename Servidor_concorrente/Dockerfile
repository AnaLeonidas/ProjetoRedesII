# servidor/Dockerfile
FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y python3

WORKDIR /app

COPY servidor_concorrente.py .

COPY filmes.json .

CMD ["python3", "./servidor_concorrente.py"]