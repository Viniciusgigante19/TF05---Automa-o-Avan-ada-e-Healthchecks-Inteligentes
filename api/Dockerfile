FROM python:3.9-slim

# Instala curl para o healthcheck do Docker e dependências do sistema
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Instala as bibliotecas necessárias diretamente para ganhar tempo
RUN pip install --no-cache-dir \
    flask \
    requests \
    pyyaml \
    mysql-connector-python \
    flask-cors

# Copia o código da API
COPY . .

# Expõe a porta 5000
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "app.py"]