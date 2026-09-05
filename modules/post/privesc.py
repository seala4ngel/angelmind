class Privesc:
    def __init__(self, engine):
        self.engine = engine
        self.priority = "P1"
        self.level = "Critical"

    def scan(self, target):
        target = self.engine.normalize(target)
        checks = ["/etc/passwd", "/etc/shadow", "/etc/sudoers", "/root/.bash_history", "/home/*/.ssh/id_rsa"]
        findings = []
        for file_path in checks:
            try:
                resp = self.engine.request(f"{target}{file_path}")
                if resp.status_code == 200:
                    findings.append({"file": file_path, "accessible": True, "priority": "P1", "level": "Critical"})
            except:
                pass
        return {'findings': findings}
