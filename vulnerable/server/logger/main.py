"""Module for handling the main logger class"""
# pylint: disable=import-error
import logging
from server.logger.handlers import (
    DebugHandler, StdoutHandler, StderrHandler)


class Logger:
    """Class the defines instances of the logger"""

    _RUNNING = None

    def __init__(self, alias, level=1, logpath="logs/vulnerable.log"):
        self.alias = alias
        self.level = level
        self.logger = logging.getLogger(self.alias)
        self.logger.setLevel(self.level)
        if not self._RUNNING:
            Logger._RUNNING = True
            self.logger.addHandler(DebugHandler(logpath))
            self.logger.addHandler(StdoutHandler())
            self.logger.addHandler(StderrHandler())
            self.initlog()

    def __repr__(self):
        return repr(self.alias)

    def __str__(self):
        return self.alias

    def __int__(self):
        return self.level

    def get_logger(self, alias):
        """Returns a child logger from the parent"""
        return Logger(".".join((self.alias, alias)))

    def initlog(self):
        """Writes a log that should always be the first log"""
        self.logger.log(1, "INITLOG  |  %s", repr(self))

    def debug(self, *args, **kwargs):
        """Overloaded debug log function"""
        self.logger.debug(*args, **kwargs)

    def info(self, *args, **kwargs):
        """Overloaded info log function"""
        self.logger.info(*args, **kwargs)

    def warn(self, *args, **kwargs):
        """Overloaded warning log function"""
        self.logger.warning(*args, **kwargs)

    def error(self, *args, **kwargs):
        """Overloaded error log function"""
        self.logger.error(*args, **kwargs)

    def fatal(self, *args, **kwargs):
        """Overloaded critical log function"""
        self.logger.critical(*args, **kwargs)


LOGGER = Logger("vulnerable")
