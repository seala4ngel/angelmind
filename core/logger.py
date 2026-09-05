import datetime

class Logger:
    def __init__(self, logfile="arsenal.log"):
        self.logfile = logfile

    def log(self, message, level="INFO"):
        timestamp = datetime.datetime.now().isoformat()
        with open(self.logfile, "a") as f:
            f.write(f"[{timestamp}] [{level}] {message}\n")
        print(f"[{timestamp}] [{level}] {message}")
