class Misconfig:
    def __init__(self, engine):
        self.engine = engine
        self.priority = "P4"
        self.level = "Medium"

    def scan(self, target):
        target = self.engine.normalize(target)
        try:
            resp = self.engine.request(target)
            issues = []
            if 'X-Frame-Options' not in resp.headers:
                issues.append("X-Frame-Options missing (clickjacking)")
            if 'X-Content-Type-Options' not in resp.headers:
                issues.append("X-Content-Type-Options missing")
            if 'Strict-Transport-Security' not in resp.headers:
                issues.append("HSTS missing")
            return {'vulnerable': len(issues) > 0, 'issues': issues, 'priority': self.priority, 'level': self.level}
        except:
            return {'vulnerable': False}
