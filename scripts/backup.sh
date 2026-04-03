#!/bin/sh

# Cria pasta de backup com timestamp
BACKUP_DIR="./backups/$(date +%Y%m%d_%H%M%S)"
mkdir -p "$BACKUP_DIR"

echo "Salvando em $BACKUP_DIR..."

# 1. Backup das configurações
cp -r ./config "$BACKUP_DIR/config"
echo "Configs salvas"

# 2. Backup do banco de dados
docker compose exec -T db mysqldump \
  -u root -ppass app > "$BACKUP_DIR/database.sql"
echo "Banco salvo"

echo "Backup concluído em $BACKUP_DIR"