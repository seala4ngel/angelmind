import json
import datetime

class Report:
    def __init__(self, findings):
        self.findings = findings

    def to_markdown(self):
        report = f"# Security Assessment Report\n\n"
        report += f"**Date:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        report += "## Findings\n\n"
        for f in self.findings:
            if isinstance(f, dict):
                module = f.get('module', f.get('target', 'unknown'))
                priority = f.get('priority', 'N/A')
                level = f.get('level', 'N/A')
                report += f"- **{module}** — Priority: {priority} — Level: {level}\n"
            else:
                report += f"- {str(f)}\n"
        return report

    def to_json(self):
        return json.dumps({"findings": self.findings, "generated": str(datetime.datetime.now())}, indent=2)
