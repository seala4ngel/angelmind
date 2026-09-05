import smtplib
from email.mime.text import MIMEText

class Phishing:
    def __init__(self, engine):
        self.engine = engine
        self.priority = "P1"
        self.level = "Critical"

    def scan(self, target, email_list, smtp_config):
        results = []
        for email in email_list:
            msg = MIMEText(f"Click here: {target}")
            msg['Subject'] = "Urgent: Action Required"
            msg['From'] = smtp_config.get('from')
            msg['To'] = email
            try:
                server = smtplib.SMTP(smtp_config.get('server'), smtp_config.get('port'))
                server.starttls()
                server.login(smtp_config.get('username'), smtp_config.get('password'))
                server.sendmail(smtp_config.get('from'), [email], msg.as_string())
                server.quit()
                results.append({"email": email, "status": "sent"})
            except Exception as e:
                results.append({"email": email, "status": "failed", "error": str(e)})
        return {"results": results}
