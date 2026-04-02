#!/bin/bash
echo "🚀 Iniciando Deploy Automatizado..."

# Backup (Requisito 0,1 pt)
cp config/healthchecks.yml config/healthchecks.yml.bak

# Build e Up
docker-compose up -d --build

echo "⏳ Aguardando serviços estabilizarem..."
sleep 10

# Validação do Healthcheck (0,2 pts)
# Verifica se a API está retornando 'healthy' para os serviços
if curl -s http://localhost:5000/health/status | grep -q "unhealthy"; then
    echo "❌ Falha detectada nos Healthchecks! Iniciando Rollback..."
    docker-compose down
    mv config/healthchecks.yml.bak config/healthchecks.yml
    docker-compose up -d
    exit 1
else
    echo "✅ Deploy concluído com sucesso e serviços saudáveis!"
fi