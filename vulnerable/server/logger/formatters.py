import logging


class DebugFormatter(logging.Formatter):

    def __init__(self):
        super().__init__("%(asctime)s  |  %(levelno)-2d  |  %(name)s  |  %(message)s")


class StdoutFormatter(logging.Formatter):

    def __init__(self):
        super().__init__("%(message)s")


class StderrFormatter(logging.Formatter):

    def __init__(self):
        super().__init__("[%(levelname)s] %(message)s")
