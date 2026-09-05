import random

class IntelFuzz:
    def __init__(self, engine):
        self.engine = engine
        self.priority = "P4"
        self.level = "Medium"

    def scan(self, target):
        target = self.engine.normalize(target)
        wordlist = [
            "admin", "api", "backup", "config", "debug", "dev", "internal",
            "private", "test", "staging", "prod", "v1", "v2", "v3",
            "auth", "login", "signup", "reset", "forgot", "verify",
            "dashboard", "panel", "console", "monitor", "metrics"
        ]
        found = []
        for path in wordlist[:50]:
            try:
                resp = self.engine.request(f"{target}/{path}")
                if resp.status_code in [200, 403, 500]:
                    found.append({"path": path, "status": resp.status_code})
            except:
                pass
        return {"found": found}
