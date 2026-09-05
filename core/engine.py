import random
import time
import requests
from fake_useragent import UserAgent
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class ArsenalEngine:
    def __init__(self, config=None):
        self.config = config or {}
        self.proxies = self.config.get('proxies', [])
        self.ua = UserAgent()
        self.jitter_min = self.config.get('jitter_min', 0.5)
        self.jitter_max = self.config.get('jitter_max', 3.0)
        self.retry_count = self.config.get('retry_count', 3)
        self.timeout = self.config.get('timeout', 30)
        self.session = requests.Session()
        self.session.verify = False

    def _get_proxy(self):
        return random.choice(self.proxies) if self.proxies else None

    def _get_headers(self):
        return {
            'User-Agent': self.ua.random,
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive'
        }

    def _sleep(self):
        time.sleep(random.uniform(self.jitter_min, self.jitter_max))

    def request(self, url, method='GET', params=None, data=None, json_data=None, headers=None):
        self._sleep()
        proxy = self._get_proxy()
        proxies = {'http': proxy, 'https': proxy} if proxy else None
        final_headers = self._get_headers()
        if headers:
            final_headers.update(headers)

        for attempt in range(self.retry_count):
            try:
                return self.session.request(
                    method, url, params=params, data=data, json=json_data,
                    headers=final_headers, proxies=proxies, timeout=self.timeout
                )
            except Exception:
                if attempt == self.retry_count - 1:
                    raise
                time.sleep(2 ** attempt)

    def normalize(self, target):
        if not target.startswith(('http://', 'https://')):
            target = 'https://' + target
        return target.rstrip('/')
