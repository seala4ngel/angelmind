import random

class WAFBypass:
    def __init__(self):
        self.encodings = [
            lambda s: s.replace("'", "%27"),
            lambda s: s.replace(" ", "/**/"),
            lambda s: s.replace("=", "!="),
            lambda s: s.replace("AND", "&&"),
            lambda s: s.replace("OR", "||"),
            lambda s: s.upper(),
        ]

    def bypass(self, payload):
        if random.random() < 0.3:
            return random.choice(self.encodings)(payload)
        return payload
