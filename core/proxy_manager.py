import random
import requests

class ProxyManager:
    def __init__(self, proxy_list=None):
        self.proxies = proxy_list or [
            "http://user:pass@proxy1:8080",
            "http://user:pass@proxy2:8080",
            "socks5://proxy3:1080"
        ]
        self.current_index = 0

    def get_next(self):
        proxy = self.proxies[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.proxies)
        return proxy

    def get_random(self):
        return random.choice(self.proxies)
