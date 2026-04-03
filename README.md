# TF05 - Sistema de Monitoramento com Docker

## Estrutura do Projeto
- **API**: Flask (Python) realizando healthchecks HTTP e TCP.
- **Dashboard**: Nginx servindo interface estática.
- **DB**: MySQL 8.0 para persistência de métricas.
- **Cache**: Redis para validação de conectividade TCP.

## Como Executar
1. Execute o script de deploy:
   `./scripts/deploy.sh`
2. Acesse o Dashboard: `http://localhost:3000`
3. Endpoint de Métricas: `http://localhost:5000/health/status`

## Automação
O script `deploy.sh` realiza o backup das configurações, build das imagens e validação de healthcheck com suporte a rollback automático.

Dashboard
Interface de Visualização (Frontend): Servido via Nginx, ele é o ponto final do consumo de dados. Sua função é realizar requisições assíncronas para a API e plotar os gráficos de performance e status em tempo real para o administrador.

API de Métricas
Orquestrador de Saúde (Backend): O "cérebro" do sistema. Ele lê as configurações de healthchecks.yml, executa as rotinas de teste (HTTP, TCP, SQL), processa os alertas baseados nos thresholds e expõe os dados formatados para o Dashboard via JSON.


Banco de Dados
Persistência de Telemetria (MySQL): Armazena o histórico de todas as verificações. É fundamental para o requisito de "Análise de Tendências", permitindo que o Dashboard exiba gráficos de uptime e tempo de resposta das últimas 24h.

Redis Cache
Alvo de Conectividade (TCP): Atua como o serviço de infraestrutura para validar o sistema de alertas e o critério de verificação via protocolo TCP. No ecossistema, simula a camada de cache que deve estar sempre disponível.