#!/bin/sh

URL="http://localhost:5000/health/status"

echo "Verificando $URL..."

STATUS=$(curl -s -o /dev/null -w "%{http_code}" "$URL")

if [ "$STATUS" -eq 200 ]; then
  RESULTADO=$(curl -s "$URL")
  echo "OK: endpoint respondeu 200"
  echo "$RESULTADO"
else
  echo "ERRO: endpoint respondeu $STATUS"
  exit 1
fi