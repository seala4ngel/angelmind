import os
import platform

class Persist:
    def __init__(self, engine):
        self.engine = engine
        self.priority = "P1"
        self.level = "Critical"

    def generate_linux(self, script_path, cron="*/5 * * * *"):
        return f"{cron} /usr/bin/python3 {script_path}"

    def generate_windows(self, script_path, task_name="SystemUpdate"):
        return f"schtasks /create /tn {task_name} /tr {script_path} /sc minute /mo 5 /ru SYSTEM"

    def scan(self, target, script_path, os_type="linux"):
        if os_type == "linux":
            persistence = self.generate_linux(script_path)
        elif os_type == "windows":
            persistence = self.generate_windows(script_path)
        else:
            persistence = "echo 'Unsupported OS'"
        return {'persistence': persistence, 'os_type': os_type}
