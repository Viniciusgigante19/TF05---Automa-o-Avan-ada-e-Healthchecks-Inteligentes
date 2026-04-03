from datetime import datetime

class Alert:
    """
    Representa um alerta gerado quando um serviço falha
    ou ultrapassa um threshold.
    """
    def __init__(self, service, level, message):
        self.service = service
        self.level = level 
        self.message = message
        self.timestamp = datetime.utcnow().isoformat()

    def to_dict(self):
        return {
            "service": self.service,
            "level": self.level,
            "message": self.message,
            "timestamp": self.timestamp
        }


def evaluate_alerts(results, thresholds):
    """
    Recebe os resultados dos healthchecks e os thresholds,
    retorna lista de alertas gerados.
    """
    alerts = []
    rt_warning = thresholds.get('response_time', {}).get('warning', 1000)
    rt_critical = thresholds.get('response_time', {}).get('critical', 5000)

    for r in results:
        if not r.get('healthy'):
            alerts.append(Alert(
                service=r['service'],
                level='critical',
                message=f"Serviço {r['service']} está DOWN. Erro: {r.get('error', 'desconhecido')}"
            ).to_dict())

        elif r.get('response_time_ms', 0) >= rt_critical:
            alerts.append(Alert(
                service=r['service'],
                level='critical',
                message=f"Tempo de resposta crítico: {r['response_time_ms']}ms"
            ).to_dict())

        elif r.get('response_time_ms', 0) >= rt_warning:
            alerts.append(Alert(
                service=r['service'],
                level='warning',
                message=f"Tempo de resposta alto: {r['response_time_ms']}ms"
            ).to_dict())

    return alerts