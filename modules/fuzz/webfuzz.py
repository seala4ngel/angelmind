class WebFuzz:
    def __init__(self, engine):
        self.engine = engine
        self.priority = "P4"
        self.level = "Medium"

    def scan(self, target):
        target = self.engine.normalize(target)
        try:
            with open("payloads/paths.txt", "r") as f:
                paths = [line.strip() for line in f if line.strip()]
        except:
            paths = ["admin", "login", "api", ".env"]

        found = []
        for path in paths[:10]:  # ← UBAH 100 JADI 10
            try:
                resp = self.engine.request(f"{target}/{path}")
                if resp.status_code == 200:
                    found.append({"path": path, "status": 200, "priority": "P4", "level": "Medium"})
                elif resp.status_code == 403:
                    found.append({"path": path, "status": 403, "priority": "P4", "level": "Medium"})
            except:
                pass
        return {'found': found}
