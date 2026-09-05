from urllib.parse import quote
class AngelXSS:
    def __init__(self, opsec):
        self.op = opsec
    def test_reflected(self, url, param):
        payloads = ['<script>alert(1)</script>','<img src=x onerror=alert(1)>','<svg onload=alert(1)>']
        for payload in payloads:
            try:
                resp = self.op.request(f"{url}?{param}={quote(payload)}")
                if resp and payload in resp.text:
                    return {'vulnerable': True, 'type': 'reflected'}
            except:
                continue
        return {'vulnerable': False}
    def full_scan(self, url, param):
        return {'target': url, 'param': param, 'reflected': self.test_reflected(url, param)}
