"""Module for handling logging formats"""
import logging


class DebugFormatter(logging.Formatter):
    """Class for debugging log format"""

    def __init__(self):
        super().__init__("%(asctime)s  |  %(levelno)-2d  |  %(name)s  |  %(message)s")


class StdoutFormatter(logging.Formatter):
    """Class for standard output log format"""

    def __init__(self):
        super().__init__("%(message)s")


class StderrFormatter(logging.Formatter):
    """Class for standard error log format"""

    def __init__(self):
        super().__init__("[%(levelname)s] %(message)s")
