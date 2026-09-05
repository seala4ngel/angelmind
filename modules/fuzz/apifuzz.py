class APIFuzz:
    def __init__(self, engine):
        self.engine = engine
        self.priority = "P4"
        self.level = "Medium"

    def scan(self, target):
        target = self.engine.normalize(target)
        params = ["id", "user", "email", "password", "token", "key", "debug", "file", "path", "url"]
        results = []
        for param in params:
            try:
                resp = self.engine.request(f"{target}?{param}=test")
                if resp.status_code == 200 and "test" in resp.text:
                    results.append({"param": param, "reflected": True, "priority": "P4", "level": "Medium"})
            except:
                pass
        return {'results': results}
