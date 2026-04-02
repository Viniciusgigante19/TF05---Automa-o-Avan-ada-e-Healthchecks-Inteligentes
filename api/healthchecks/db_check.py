import mysql.connector
import time

UPTIME_PERCENT = 100

def check_database(name, config):
    timeout = int(config.get('timeout', '10s').replace('s', ''))

    start = time.time()
    try:
        conn = mysql.connector.connect(
            host=config.get('host', 'db'),
            user=config.get('user', 'root'),
            password=config.get('password', 'pass'),
            database=config.get('database', 'app'),
            connection_timeout=timeout
        )
        cursor = conn.cursor()
        cursor.execute(config.get('query', 'SELECT 1'))
        cursor.fetchone()

        # Contar conexões ativas
        cursor.execute("SHOW STATUS LIKE 'Threads_connected';")
        connections = cursor.fetchone()[1]

        cursor.close()
        conn.close()
        response_time = int((time.time() - start) * 1000)

        return {
            "service": name,
            "type": "database",
            "healthy": True,
            "response_time_ms": response_time,
            "connections": int(connections),
            "uptime": f"{UPTIME_PERCENT}%"
        }

    except mysql.connector.Error as e:
        return {
            "service": name,
            "type": "database",
            "healthy": False,
            "error": str(e),
            "connections": 0,
            "uptime": "0%"
        }