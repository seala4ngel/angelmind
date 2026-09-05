import subprocess
import platform

class Lateral:
    def __init__(self, engine):
        self.engine = engine
        self.priority = "P1"
        self.level = "Critical"

    def scan(self, target, method="ssh", username="root", password="root"):
        target = self.engine.normalize(target)
        methods = {
            "ssh": f"sshpass -p '{password}' ssh {username}@{target} 'whoami'",
            "wmi": f"wmic /user:{username} /password:{password} //{target} process call create 'cmd.exe /c whoami'",
            "winrm": f"winrm invoke create wmicimv2/Win32_Process -r:{target} -u:{username} -p:{password} @{{'CommandLine':'whoami'}}",
        }
        results = []
        for m, cmd in methods.items():
            try:
                if platform.system() == "Linux":
                    result = subprocess.check_output(cmd, shell=True).decode()
                else:
                    result = subprocess.check_output(cmd, shell=True).decode(errors='ignore')
                results.append({"method": m, "success": True, "output": result})
            except Exception as e:
                results.append({"method": m, "success": False, "error": str(e)})
        return {"lateral_movement": results}
