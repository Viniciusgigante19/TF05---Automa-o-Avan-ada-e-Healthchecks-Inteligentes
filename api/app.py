from flask import Flask, jsonify
from flask_cors import CORS
import yaml, os
from healthchecks.http_check import check_http
from healthchecks.db_check import check_database
from healthchecks.custom_check import check_custom
from datetime import datetime
from models.alerts import create_alert
import mysql.connector
import os

app = Flask(__name__)

conn = mysql.connector.connect(
    host=os.getenv("DB_HOST", "db"),
    port=int(os.getenv("DB_PORT", 3306)),
    user=os.getenv("DB_USER", "root"),
    password=os.getenv("DB_PASSWORD", "pass"),
    database=os.getenv("DB_NAME", "app")
)
cursor = conn.cursor()

CORS(app, origins="http://localhost:3000")

def load_config():
    config_path = os.path.join('/app/config', 'healthchecks.yml')
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

def run_checks():
    config = load_config()
    results = []

    for name, cfg in config.get('healthchecks', {}).items():
        check_type = cfg.get('type')

        if check_type == 'http':
            results.append(check_http(name, cfg))
        elif check_type == 'database':
            results.append(check_database(name, cfg))
        elif check_type == 'custom':
            results.append(check_custom(name, cfg))

    return results

@app.route('/health')
def health():
    return jsonify({"status": "ok"})

@app.route('/health/status')
def health_status():
    results = run_checks()
    overall = all(r['healthy'] for r in results)

    for r in results:
        try:
            sql = """
            INSERT INTO metrics (service, healthy, response_time_ms, check_type, error)
            VALUES (%s, %s, %s, %s, %s)
            """
            values = (
                r.get('service'),
                r.get('healthy'),
                r.get('response_time_ms'),
                r.get('type'),
                r.get('error')
            )
            cursor.execute(sql, values)
            conn.commit()
        except mysql.connector.Error as e:
            create_alert(
                service=r.get('service', 'unknown'),
                alert_type='critical',
                message=f"Erro ao salvar métrica: {e}"
            )
            print(f"[DB ERROR] {e}")

        if not r.get('healthy', True):
            create_alert(
                service=r.get('service', 'unknown'),
                alert_type='critical',
                message=r.get('error', 'Falha detectada')
            )

    return jsonify({
        "overall": "healthy" if overall else "degraded",
        "services": results
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)