"""Module for handling logging filters"""
# pylint: disable=too-few-public-methods
import logging


class DebugFilter(logging.Filter):
    """Class for debugging log filter"""

    def filter(self, record):
        """Logs record numbers greater than zero"""
        return record.levelno > logging.NOTSET


class StdoutFilter(logging.Filter):
    """Class for standard output log filter"""

    def filter(self, record):
        """Logs record numbers between INFO and WARNING"""
        return record.levelno >= logging.INFO and record.levelno < logging.WARNING


class StderrFilter(logging.Filter):
    """Class for standard error log filter"""

    def filter(self, record):
        """Logs record numbers greater than WARNING"""
        return record.levelno >= logging.WARNING
