import os
import json
from datetime import datetime

ALERTS_FILE = os.getenv("ALERTS_FILE", "/app/logs/alerts.json")

def create_alert(service, alert_type, message):
    """
    Grava alerta em arquivo JSON independente do banco.
    """
    # Garante que a pasta existe
    os.makedirs(os.path.dirname(ALERTS_FILE), exist_ok=True)

    # Lê alertas existentes
    if os.path.exists(ALERTS_FILE):
        with open(ALERTS_FILE, 'r') as f:
            alerts = json.load(f)
    else:
        alerts = []

    # Adiciona novo alerta
    alerts.append({
        "service": service,
        "type": alert_type,
        "message": message,
        "timestamp": datetime.now().isoformat()
    })

    # Salva de volta
    with open(ALERTS_FILE, 'w') as f:
        json.dump(alerts, f, indent=2)