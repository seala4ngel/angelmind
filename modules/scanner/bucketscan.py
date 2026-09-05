class BucketScan:
    def __init__(self, engine):
        self.engine = engine
        self.priority = "P4"
        self.level = "Medium"

    def scan(self, target):
        target = self.engine.normalize(target)
        domain = target.replace('https://', '').replace('http://', '').split('/')[0]
        buckets = [f"{domain}-backup", f"{domain}-assets", f"{domain}-data", f"{domain}-logs"]
        results = []
        for bucket in buckets:
            url = f"https://{bucket}.s3.amazonaws.com"
            try:
                resp = self.engine.request(url)
                if resp.status_code == 200:
                    results.append({"bucket": bucket, "public": True, "priority": "P4", "level": "Medium"})
            except:
                pass
        return {'public_buckets': results, 'priority': self.priority, 'level': self.level}
