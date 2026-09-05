import subprocess
import platform

class Lateral:
    def __init__(self, engine):
        self.engine = engine
        self.priority = "P1"
        self.level = "Critical"

    def scan(self, target, username="root", password="root"):
        cmd = f"sshpass -p '{password}' ssh -o StrictHostKeyChecking=no {username}@{target} 'whoami'"
        try:
            result = subprocess.check_output(cmd, shell=True).decode()
            return {"success": True, "output": result, "method": "ssh"}
        except Exception as e:
            return {"success": False, "error": str(e), "method": "ssh"}
