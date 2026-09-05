class Fingerprint:
    def __init__(self, engine):
        self.engine = engine
        self.priority = "P5"
        self.level = "Low"

    def scan(self, target):
        target = self.engine.normalize(target)
        try:
            resp = self.engine.request(target)
            tech = {
                "server": resp.headers.get('Server', 'Unknown'),
                "powered_by": resp.headers.get('X-Powered-By', 'Unknown'),
                "cf_ray": 'Cloudflare' if 'cf-ray' in resp.headers else None,
            }
            return {'technology': tech, 'priority': self.priority, 'level': self.level}
        except:
            return {'technology': {}, 'priority': self.priority, 'level': self.level}
