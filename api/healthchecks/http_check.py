import requests
import time

def check_http(name, config):
    url = config.get('url')
    timeout = int(config.get('timeout', '10s').replace('s', ''))
    expected_status = config.get('expected_status', 200)

    start = time.time()
    try:
        response = requests.get(url, timeout=timeout)
        response_time = int((time.time() - start) * 1000)

        healthy = response.status_code == expected_status

        return {
            "service": name,
            "type": "http",
            "healthy": healthy,
            "status_code": response.status_code,
            "response_time_ms": response_time
        }

    except requests.exceptions.ConnectionError:
        return {"service": name, "type": "http", "healthy": False, "error": "Conexão recusada"}
    except requests.exceptions.Timeout:
        return {"service": name, "type": "http", "healthy": False, "error": "Timeout"}