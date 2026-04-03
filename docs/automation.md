# Automação

## Scripts

### build.sh
Valida o Docker, builda as imagens e verifica se todos os containers subiram.
```sh
./scripts/build.sh
```

### deploy.sh
Faz backup das configs, sobe os containers e valida os healthchecks.
Em caso de falha, executa rollback automático.
```sh
./scripts/deploy.sh
```

### rollback.sh
Para os containers, restaura o backup de configuração e sobe novamente.
```sh
./scripts/rollback.sh
```

### backup.sh
Salva configs e dump do banco em `./backups/TIMESTAMP/`.
```sh
./scripts/backup.sh
```

### cleanup.sh
Remove containers parados, redes e imagens não utilizadas. Apaga logs antigos.
```sh
./scripts/cleanup.sh
```

### health-monitor.sh
Consulta o endpoint `/health/status` e exibe o resultado no terminal.
```sh
./scripts/health-monitor.sh
```