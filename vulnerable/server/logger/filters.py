import logging


class DebugFilter(logging.Filter):

    def filter(self, record):
        return record.levelno > logging.NOTSET


class StdoutFilter(logging.Filter):

    def filter(self, record):
        return record.levelno >= logging.INFO and record.levelno < logging.WARNING


class StderrFilter(logging.Filter):

    def filter(self, record):
        return record.levelno >= logging.WARNING
