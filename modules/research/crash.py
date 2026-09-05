class Crash:
    def __init__(self, engine):
        self.engine = engine
        self.priority = "P2"
        self.level = "Hard"

    def scan(self, target, param, payloads=None):
        if payloads is None:
            payloads = ["A"*1000, "A"*10000, "%n%n%n", "\\\\x00\\\\x00"]
        results = []
        for p in payloads:
            try:
                resp = self.engine.request(f"{target}?{param}={p}")
                if resp.status_code == 500:
                    results.append({"payload": p, "status": 500, "vulnerable": True})
            except:
                results.append({"payload": p, "status": "timeout", "vulnerable": True})
        return {"crash_findings": results}
