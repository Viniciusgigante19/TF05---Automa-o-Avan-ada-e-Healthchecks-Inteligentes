# Healthchecks

## Tipos Implementados

### HTTP (`http_check.py`)
Verifica se um endpoint HTTP responde com o status esperado.
Configuração: `url`, `timeout`, `expected_status`

### Database (`db_check.py`)
Executa uma query no MySQL e verifica se retorna resultado.
Configuração: `host`, `user`, `password`, `database`, `query`

### Custom/TCP (`custom_check.py`)
Tenta conexão TCP numa porta. Usado para Redis e similares.
Configuração: `host`, `port`, `timeout`

## Configuração (`config/healthchecks.yml`)
Cada serviço define `type` e os parâmetros correspondentes.
O endpoint `/health/status` executa todos e retorna o resultado consolidado.