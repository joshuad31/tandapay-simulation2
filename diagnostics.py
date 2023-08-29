# diagnostics.py

class Diagnostics:
    def __init__(self):
        self.strings = []

    def addStr(self, s: str) -> None:
        self.strings.append(s)

    def getOutput(self) -> str:
        return '\n'.join(self.strings)

