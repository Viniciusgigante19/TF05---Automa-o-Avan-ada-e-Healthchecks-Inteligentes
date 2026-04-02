from flask import Flask, jsonify
import yaml, os
from healthchecks.http_check import check_http
from healthchecks.db_check import check_database
from healthchecks.custom_check import check_custom

app = Flask(__name__)

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
    return jsonify({
        "overall": "healthy" if overall else "degraded",
        "services": results
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)