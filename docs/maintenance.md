# Manutenção

## Limpeza de recursos
```sh
./scripts/cleanup.sh
```
Remove containers parados, redes órfãs e logs com mais de 1 dia.

## Backup
```sh
./scripts/backup.sh
```
Gera pasta `./backups/YYYYMMDD_HHMMSS/` com configs e dump SQL.

## Restore do banco
```sh
docker compose exec -T db mysql -u root -ppass app < ./backups/PASTA/database.sql
```

## Monitoramento manual
```sh
./scripts/health-monitor.sh
```

## Verificar logs de um serviço
```sh
docker compose logs api
docker compose logs db
```