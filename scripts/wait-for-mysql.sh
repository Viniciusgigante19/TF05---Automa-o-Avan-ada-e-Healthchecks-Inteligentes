#!/bin/bash
# /tf05/scripts/wait-for-mysql.sh

DB_HOST=${DB_HOST:-db}

echo "Aguardando socket TCP em $DB_HOST:3306..."

while ! timeout 1 bash -c "cat < /dev/null > /dev/tcp/$DB_HOST/3306" 2>/dev/null; do
    sleep 1
done

echo "Conexão aceita! Liberando API..."

# CRITICAL: Esta linha executa o "python app.py" (o CMD do Dockerfile)
exec "$@"