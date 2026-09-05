import random

class ProxyManager:
    def __init__(self):
        self.proxies = [
            "http://proxy1:8080",
            "http://proxy2:8080",
            "http://proxy3:8080",
            "socks5://proxy4:1080",
            "socks5://proxy5:1080",
        ]

    def get_random(self):
        return random.choice(self.proxies)

    def get_rotating(self, count=5):
        for _ in range(count):
            yield self.get_random()
