import json
import datetime

class Reporter:
    def __init__(self):
        self.findings = []

    def add(self, finding):
        self.findings.append(finding)

    def generate_html(self):
        html = f"""
        <html>
        <head><title>Arsenal Apik Report</title></head>
        <body>
        <h1>Security Assessment Report</h1>
        <p>Generated: {datetime.datetime.now()}</p>
        <ul>
        """
        for f in self.findings:
            html += f"<li>{f.get('type')} — {f.get('priority')} — {f.get('level')}</li>"
        html += "</ul></body></html>"
        return html

    def generate_json(self):
        return json.dumps({'findings': self.findings, 'generated': str(datetime.datetime.now())}, indent=2)
