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
    """Class for debugging log handler

    The DebugHandler will assign a rotating log file every 100,000 bytes.
    There can be up to five rotated backups for the log path.  The
    DebugFormatter and the DebugFilter are also added to the handler instance.

    Args:
        logpath (str): the fullpath to the logfile to rotate

    """

    def __init__(self, logpath):
        super().__init__(logpath, maxBytes=100_000, backupCount=5)
        self.setFormatter(DebugFormatter())
        self.addFilter(DebugFilter())


class StdoutHandler(logging.StreamHandler):
    """Class for standard output log handler

    The StdoutHandler will assign the sys.stdout descriptor and any
    logs that are passed as info level, will be printed to the console.
    The formatter and filter are also added to the handler configuration.

    """

    def __init__(self):
        super().__init__(sys.stdout)
        self.setFormatter(StdoutFormatter())
        self.addFilter(StdoutFilter())


class StderrHandler(logging.StreamHandler):
    """Class for standard error log handler

    The StderrHandler will assign the sys.stderr descriptor and any
    logs that are passed as warning level or higher, will be printed to the
    console as an error stream. The formatter and filter are also added to
    the handler configuration.

    """

    def __init__(self):
        super().__init__(sys.stderr)
        self.setFormatter(StderrFormatter())
        self.addFilter(StderrFilter())
