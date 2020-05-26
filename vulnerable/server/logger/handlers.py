"""Module for handling logging handlers"""
# pylint: disable=import-error
import logging
from logging.handlers import RotatingFileHandler
import sys
from server.logger.formatters import (
    DebugFormatter, StdoutFormatter, StderrFormatter)
from server.logger.filters import (
    DebugFilter, StdoutFilter, StderrFilter)


class DebugHandler(RotatingFileHandler):
    """Class for debugging log handler"""

    def __init__(self, logpath):
        super().__init__(logpath, maxBytes=100_000, backupCount=5)
        self.setFormatter(DebugFormatter())
        self.addFilter(DebugFilter())


class StdoutHandler(logging.StreamHandler):
    """Class for standard output log handler"""

    def __init__(self):
        super().__init__(sys.stdout)
        self.setFormatter(StdoutFormatter())
        self.addFilter(StdoutFilter())


class StderrHandler(logging.StreamHandler):
    """Class for standard error log handler"""

    def __init__(self):
        super().__init__(sys.stderr)
        self.setFormatter(StderrFormatter())
        self.addFilter(StderrFilter())
