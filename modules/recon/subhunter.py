import re
import dns.resolver

class SubHunter:
    def __init__(self, engine):
        self.engine = engine
        self.priority = "P5"
        self.level = "Low"

    def passive(self, domain):
        subdomains = set()
        try:
            resp = self.engine.request(f"https://crt.sh/?q=%25.{domain}&output=json")
            if resp.status_code == 200:
                for entry in resp.json():
                    name = entry.get('name_value', '')
                    if name.endswith(f'.{domain}'):
                        subdomains.add(name)
        except:
            pass
        try:
            resp = self.engine.request(f"http://web.archive.org/cdx/search/cdx?url=*.{domain}/*&output=json&fl=original&collapse=urlkey")
            if resp.status_code == 200:
                for line in resp.json():
                    if isinstance(line, list) and line:
                        url = line[0]
                        match = re.search(rf'(?:https?://)?([a-zA-Z0-9.-]+\.{domain})', url)
                        if match:
                            subdomains.add(match.group(1))
        except:
            pass
        return list(subdomains)

    def active(self, subdomains):
        results = []
        for sub in subdomains:
            try:
                answers = dns.resolver.resolve(sub, 'A')
                ip = answers[0].address if answers else None
                alive = False
                techs = []
                for proto in ['https', 'http']:
                    try:
                        resp = self.engine.request(f"{proto}://{sub}", timeout=5)
                        if resp.status_code < 500:
                            alive = True
                            if 'Server' in resp.headers:
                                techs.append(resp.headers['Server'])
                            if 'cf-ray' in resp.headers:
                                techs.append('Cloudflare')
                            break
                    except:
                        continue
                results.append({'domain': sub, 'ip': ip, 'alive': alive, 'technologies': techs})
            except:
                results.append({'domain': sub, 'ip': None, 'alive': False, 'technologies': []})
        return results

    def scan(self, target):
        domain = target.replace('https://', '').replace('http://', '').split('/')[0]
        subdomains = self.passive(domain)
        results = self.active(subdomains)
        return {
            'module': 'subhunter',
            'target': domain,
            'total': len(results),
            'alive': [r for r in results if r['alive']],
            'dead': [r for r in results if not r['alive']],
            'all': results,
            'priority': self.priority,
            'level': self.level
        }
