import socket

class PortProbe:
    def __init__(self, engine):
        self.engine = engine
        self.priority = "P5"
        self.level = "Low"

    def scan(self, target):
        domain = target.replace('https://', '').replace('http://', '').split('/')[0]
        ports = [21, 22, 23, 25, 53, 80, 443, 3306, 5432, 6379, 27017, 8080, 8443]
        open_ports = []
        for port in ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((domain, port))
                if result == 0:
                    open_ports.append({"port": port, "priority": "P5", "level": "Low"})
                sock.close()
            except:
                pass
        return {'open_ports': open_ports, 'priority': self.priority, 'level': self.level}
