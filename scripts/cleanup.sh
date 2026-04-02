#!/bin/bash
echo "🧹 Iniciando limpeza de recursos do TF05..."

# Remove containers parados, redes não utilizadas e imagens suspensas
docker system prune -f

# Limpa logs antigos da aplicação (se houver a pasta logs)
if [ -d "./logs" ]; then
    find ./logs -type f -name "*.log" -mtime +1 -delete
    echo "Logs antigos removidos."
fi

echo "✅ Limpeza concluída."