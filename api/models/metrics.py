from datetime import datetime

class Metric:
    """
    Representa uma métrica coletada de um serviço.
    """
    def __init__(self, service, healthy, response_time_ms, check_type, error=None):
        self.service = service
        self.healthy = healthy
        self.response_time_ms = response_time_ms
        self.check_type = check_type
        self.error = error
        self.timestamp = datetime.utcnow().isoformat()

    def to_dict(self):
        return {
            "service": self.service,
            "healthy": self.healthy,
            "response_time_ms": self.response_time_ms,
            "type": self.check_type,
            "error": self.error,
            "timestamp": self.timestamp
        }