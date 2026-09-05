import re

class LeakScan:
    def __init__(self, engine):
        self.engine = engine
        self.priority = "P4"
        self.level = "Medium"

    def scan(self, target):
        target = self.engine.normalize(target)
        patterns = {
            'AWS_KEY': r'AKIA[0-9A-Z]{16}',
            'GITHUB_TOKEN': r'ghp_[A-Za-z0-9]{36}',
            'API_KEY': r'[a-zA-Z0-9]{32}',
            'JWT': r'eyJ[A-Za-z0-9-_]+\.[A-Za-z0-9-_]+\.[A-Za-z0-9-_]+'
        }
        leaks = []
        try:
            resp = self.engine.request(target)
            for name, pattern in patterns.items():
                if re.search(pattern, resp.text):
                    leaks.append(name)
            return {'leaks': leaks, 'priority': self.priority, 'level': self.level}
        except:
            return {'leaks': []}
