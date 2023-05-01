import os
import logging
import sys
from logging.handlers import RotatingFileHandler
from settings import ROOT_DIR


LOG_FILE = os.path.join(ROOT_DIR, "tandapay_simulation.log")


class CustomFormatter(logging.Formatter):
    """Logging Formatter to add colors and count warning / errors"""

    grey = "\x1b[38;21m"
    yellow = "\x1b[33;21m"
    red = "\x1b[31;21m"
    bold_red = "\x1b[31a;1m"
    reset = "\x1b[0m"
    _format = "%(asctime)s:: %(name)s :: %(levelname)-4s :: %(message)s [%(filename)s:%(lineno)d]"

    FORMATS = {
        logging.DEBUG: grey + _format + reset,
        logging.INFO: grey + _format + reset,
        logging.WARNING: yellow + _format + reset,
        logging.ERROR: red + _format + reset,
        logging.CRITICAL: bold_red + _format + reset,
    }

    def format(self, record):  # type: ignore
        log_fmt = self.FORMATS.get(record.levelno)
        _formatter = logging.Formatter(log_fmt)
        return _formatter.format(record)


logger = logging.getLogger("TPS")
logger.setLevel(logging.DEBUG)  # better to have too much log than not enough
logger.handlers = []
formatter = CustomFormatter()

# Add console handler
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Add file handlers
f_info_handler = RotatingFileHandler(LOG_FILE, maxBytes=5 * 1024 * 1024, backupCount=4)
f_info_handler.setLevel(logging.DEBUG)
f_info_handler.setFormatter(formatter)
logger.addHandler(f_info_handler)
