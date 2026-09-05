class Diff:
    def __init__(self, engine):
        self.engine = engine
        self.priority = "P3"
        self.level = "Medium-Hard"

    def scan(self, target, before_hash, after_hash):
        return {
            "module": "diff",
            "target": target,
            "before": before_hash,
            "after": after_hash,
            "diff": f"Changes detected between {before_hash[:8]} and {after_hash[:8]}",
            "priority": "P3",
            "level": "Medium-Hard"
        }
