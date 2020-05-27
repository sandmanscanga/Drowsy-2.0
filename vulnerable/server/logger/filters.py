"""Module for handling logging filters"""
# pylint: disable=too-few-public-methods
import logging


class DebugFilter(logging.Filter):
    """Class for debugging log filter

    The debug filter will determine which log records will be
    logged to the rotating file.

    """

    def filter(self, record):
        """Logs record numbers greater than zero

        The log record from the incoming log object must have a value
        that is greater than zero.

        """
        return record.levelno > logging.NOTSET


class StdoutFilter(logging.Filter):
    """Class for standard output log filter

    The stdout filter will only record logs to the stdout descriptor.

    """

    def filter(self, record):
        """Logs record numbers between INFO and WARNING

        The log record from the incoming log object must have a value that is
        greater than or equal to twenty, and also must be less than thirty.

        """
        return record.levelno >= logging.INFO and \
            record.levelno < logging.WARNING


class StderrFilter(logging.Filter):
    """Class for standard error log filter

    The stderr filter will only record logs to the stderr descriptor.

    """

    def filter(self, record):
        """Logs record numbers greater than WARNING

        The log record from incoming log object must have a value greater than
        or equal to thirty.

        """
        return record.levelno >= logging.WARNING
