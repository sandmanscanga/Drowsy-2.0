from server.logger.handlers import *


class Logger(object):

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
        return Logger(".".join((self.alias, alias)))

    def initlog(self):
        self.logger.log(1, "INITLOG  |  %s", repr(self))

    def debug(self, *args, **kwargs):
        self.logger.debug(*args, **kwargs)

    def info(self, *args, **kwargs):
        self.logger.info(*args, **kwargs)

    def warn(self, *args, **kwargs):
        self.logger.warning(*args, **kwargs)

    def error(self, *args, **kwargs):
        self.logger.error(*args, **kwargs)

    def fatal(self, *args, **kwargs):
        self.logger.critical(*args, **kwargs)


LOGGER = Logger("vulnerable")
