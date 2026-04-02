import time, yaml, socket, requests
from flask import Flask, jsonify

app = Flask(__name__)

def load_config():
    try:
        with open('config/healthchecks.yml', 'r') as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"Erro ao ler config: {e}")
        return {"healthchecks": {}}

def check_http(conf):
    try:
        start = time.time()
        # Se for a própria API, usa 127.0.0.1 para evitar loop de rede externa
        url = conf['url']
        if "api:5000" in url:
            url = url.replace("api", "127.0.0.1")
            
        r = requests.get(url, timeout=conf['timeout'])
        ms = round((time.time() - start) * 1000, 2)
        status = "healthy" if r.status_code == conf.get('expected_status', 200) else "unhealthy"
        return {"status": status, "response_time": ms}
    except Exception as e:
        print(f"Erro HTTP em {conf.get('url')}: {e}")
        return {"status": "unhealthy", "response_time": 0}

def check_tcp(conf):
    try:
        start = time.time()
        # Tenta resolver o nome do host antes de conectar
        host = socket.gethostbyname(conf['host'])
        with socket.create_connection((host, conf['port']), timeout=conf['timeout']):
            ms = round((time.time() - start) * 1000, 2)
            return {"status": "healthy", "response_time": ms}
    except Exception as e:
        print(f"Erro TCP em {conf.get('host')}: {e}")
        return {"status": "unhealthy", "response_time": 0}

@app.route('/health/status')
def status():
    config = load_config()
    results = {}
    if not config or 'healthchecks' not in config:
        return jsonify({"error": "Config não carregada"}), 500

    for name, data in config['healthchecks'].items():
        if data['type'] == 'http':
            results[name] = check_http(data)
        elif data['type'] == 'tcp':
            results[name] = check_tcp(data)
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)