import time
import schedule
import subprocess

class Scheduler:
    def __init__(self, target, module):
        self.target = target
        self.module = module

    def run(self):
        print(f"[SCHEDULER] Running {self.module} on {self.target}")
        subprocess.run(["python3", "run.py", "--module", self.module, "--target", self.target])

    def schedule_daily(self):
        schedule.every().day.at("02:00").do(self.run)
        while True:
            schedule.run_pending()
            time.sleep(60)

if __name__ == "__main__":
    s = Scheduler("example.com", "subhunter")
    s.schedule_daily()
