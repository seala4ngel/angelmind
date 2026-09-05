import random, time, requests
from fake_useragent import UserAgent
class AngelOPSEC:
    def __init__(self):
        self.ua = UserAgent()
        self.session = requests.Session()
        self.session.verify = False
        self.jitter = (0.3, 1.8)
    def headers(self):
        return {
            'User-Agent': self.ua.random,
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9',
            'X-Forwarded-For': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
        }
    def request(self, url, method='GET', **kwargs):
        time.sleep(random.uniform(*self.jitter))
        headers = self.headers()
        if 'headers' in kwargs:
            kwargs['headers'].update(headers)
        else:
            kwargs['headers'] = headers
        return self.session.request(method, url, **kwargs)
