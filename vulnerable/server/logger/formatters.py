"""Module for handling logging formats"""
import logging


class DebugFormatter(logging.Formatter):
    """Class for debugging log format

    The debugging format includes the time of the log, the log level,
    the name of the logger, and the log message.

    """

    def __init__(self):
        super().__init__("%(asctime)s  |  %(levelno)-2d  |  %(name)s  |  %(message)s")


class StdoutFormatter(logging.Formatter):
    """Class for standard output log format

    The stdout format includes the log message.

    """

    def __init__(self):
        super().__init__("%(message)s")


class StderrFormatter(logging.Formatter):
    """Class for standard error log format

    The debugging format includes the log level's name, and the log message.

    """

    def __init__(self):
        super().__init__("[%(levelname)s] %(message)s")
