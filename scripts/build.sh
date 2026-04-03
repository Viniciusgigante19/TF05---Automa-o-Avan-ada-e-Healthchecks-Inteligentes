#!/bin/sh

# 1. Valida Docker
if ! docker info > /dev/null 2>&1; then
  echo "Docker não está rodando"
  exit 1
fi

# 2. Build das imagens
echo "Construindo imagens..."
docker compose build --no-cache

# 3. Sobe os containers
echo "Subindo containers..."
docker compose up -d

# 4. Valida se TODOS estão running
echo "Validando containers..."
sleep 10  # aguarda estabilizar

ALL_OK=true
for c in $(docker compose ps -q); do
  STATUS=$(docker inspect --format='{{.State.Status}}' $c)
  if [ "$STATUS" != "running" ]; then
    ALL_OK=false
    break
  fi
done

# 5. Decisão final
if [ "$ALL_OK" = true ]; then
  echo "OK: todos os containers estão UP"
else
  echo "ERRO: containers com problema:"
  for c in $(docker compose ps -q); do
    STATUS=$(docker inspect --format='{{.State.Status}}' $c)
    if [ "$STATUS" != "running" ]; then
      echo "- $c (status: $STATUS)"
    fi
  done
  exit 1
fi