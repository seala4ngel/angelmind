import random

class MailCraft:
    def __init__(self, engine):
        self.engine = engine
        self.priority = "P2"
        self.level = "Hard"

    def generate(self, target, template_type="invoice"):
        templates = {
            "invoice": f"""
            Subject: Invoice #{random.randint(1000,9999)} - Payment Due

            Dear Customer,

            Your invoice #{random.randint(1000,9999)} is now due.
            Please click here to pay: {target}/pay

            Regards,
            Billing Team
            """,
            "security": f"""
            Subject: Security Alert - Suspicious Login

            Dear User,

            We detected a suspicious login to your account.
            Please verify your identity here: {target}/verify

            Regards,
            Security Team
            """,
            "social": f"""
            Subject: You've been mentioned!

            Hey,

            Someone mentioned you in a post.
            Check it out: {target}/notification

            Regards,
            Social Team
            """,
        }
        return {"template": templates.get(template_type, templates["invoice"])}
