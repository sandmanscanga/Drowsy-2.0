"""Module for handling the main logger class"""
# pylint: disable=import-error
import logging
from server.logger.handlers import (
    DebugHandler, StdoutHandler, StderrHandler)


class Logger:
    """Class the defines instances of the logger

    The Logger class contains logic to ensure that only a single logger
    object is configured and all future loggers are children, based on
    the initial object.

    Args:
        alias (str): the logger alias to assign to the logger
        level (:obj:`int`, optional): the logging level to assign
            to the logger, defaults to level 1
        logpath (str): the path to the logfile to rotate,
            defaults to logs/vulnerable.log

    """

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
        """Returns a child logger from the parent

        The get_logger method takes the alias for a desired child logger,
        and joins the parent's alias with the child's alias on a period.
        The newly created Logger objects is then returned.

        Args:
            alias (str): the alias for the child logger

        Returns:
            :obj:`Logger`: the child Logger instance

        """
        return Logger(".".join((self.alias, alias)))

    def initlog(self):
        """Writes a log that should always be the first log

        The initlog method will only be called upon the first instance
        of the class, so it can be easily found and marked as the start
        of a stack of logs in the log file.

        """
        self.logger.log(1, "INITLOG  |  %s", repr(self))

    def debug(self, *args, **kwargs):
        """Overloaded debug log function

        Overloads the default logging module's debug method.

        Args:
            *args: Variable length argument list
            **kwargs: Arbitrary keyword arguments

        """
        self.logger.debug(*args, **kwargs)

    def info(self, *args, **kwargs):
        """Overloaded info log function

        Overloads the default logging module's info method.

        Args:
            *args: Variable length argument list
            **kwargs: Arbitrary keyword arguments

        """
        self.logger.info(*args, **kwargs)

    def warn(self, *args, **kwargs):
        """Overloaded warning log function

        Overloads the default logging module's warning method.

        Args:
            *args: Variable length argument list
            **kwargs: Arbitrary keyword arguments

        """
        self.logger.warning(*args, **kwargs)

    def error(self, *args, **kwargs):
        """Overloaded error log function

        Overloads the default logging module's error method.

        Args:
            *args: Variable length argument list
            **kwargs: Arbitrary keyword arguments

        """
        self.logger.error(*args, **kwargs)

    def fatal(self, *args, **kwargs):
        """Overloaded critical log function

        Overloads the default logging module's critical method.

        Args:
            *args: Variable length argument list
            **kwargs: Arbitrary keyword arguments

        """
        self.logger.critical(*args, **kwargs)


LOGGER = Logger("vulnerable")
