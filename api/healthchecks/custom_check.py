import socket
import time

def check_custom(name, config):
    host = config.get('host')
    port = int(config.get('port'))
    timeout = int(config.get('timeout', '5s').replace('s', ''))

    start = time.time()
    try:
        sock = socket.create_connection((host, port), timeout=timeout)
        sock.close()
        response_time = int((time.time() - start) * 1000)

        return {
            "service": name,
            "type": "custom",
            "healthy": True,
            "response_time_ms": response_time
        }

    except (socket.timeout, ConnectionRefusedError) as e:
        return {"service": name, "type": "custom", "healthy": False, "error": str(e)}