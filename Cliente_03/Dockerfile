
# Usar a imagem base do Ubuntu mais recente
FROM ubuntu:latest

# Evita que o apt-get peça interação durante o build
ENV DEBIAN_FRONTEND=noninteractive

# Atualiza os pacotes e instala o python3
RUN apt-get update && apt-get install -y python3

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o script do cliente para o diretório de trabalho
COPY cliente_03.py .

# Comando que será executado quando o container iniciar
CMD ["python3", "./cliente_03.py"]