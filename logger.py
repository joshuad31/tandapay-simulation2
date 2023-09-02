import sys
from io import TextIOWrapper

class Logger:
    def __init__(self, io_stream: TextIOWrapper = sys.stdout):
        self.stream = io_stream

    def log(self, message: str, prefix = "[LOG] "):
        try:
            self.stream.write(f"{prefix}{message}")
            self.stream.flush()
        except Exception as e:
            print(f"Failed to write log message: {e}", file=sys.stderr)

