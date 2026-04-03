#!/bin/sh

echo "Iniciando rollback..."

# 1. Para só os containers deste projeto
docker compose down

# 2. Restaura o backup da config
if [ -f config/healthchecks.yml.bak ]; then
  mv config/healthchecks.yml.bak config/healthchecks.yml
  echo "Config restaurada"
else
  echo "ERRO: backup não encontrado"
  exit 1
fi

# 3. Sobe novamente com a config anterior
docker compose up -d

echo "Rollback concluído"