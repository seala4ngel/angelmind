class CVSS:
    @staticmethod
    def calculate(priority):
        mapping = {"P1": 9.8, "P2": 7.5, "P3": 5.3, "P4": 3.1, "P5": 1.0}
        return mapping.get(priority, 0.0)
