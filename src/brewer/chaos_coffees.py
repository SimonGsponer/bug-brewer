from random import randint

from .bean_bag import BasicBean
from utils.dynamic_logger import Logger
from .faulty_beans import (
    error_5066,
    error_1000,
    error_2033,
    error_2034,
    error_2035,
    error_3310,
    error_5057
)


class EspressoError(BasicBean):
    """Error where wrong value in config file leads to error."""
    error_types = [error_2034]

    def __init__(self, n_calls, error_proc, logger: Logger):
        super().__init__(n_calls, error_proc, logger)

    def error_node(self):
        random_node = randint(10, 200)
        self.logger.log.info(f"Invoking node {random_node}...")
        try:
            raise self.error_types[0].error

        except Exception as e:
            self.logger.log_error(exception_to_log=e)

        self.error_occurred = True


class DoppioDisruptor(BasicBean):
    """Missing environmental variable leads to faulty function call."""
    error_types = [error_2034, error_2033]

    def __init__(self, n_calls, error_proc, logger: Logger):
        super().__init__(n_calls, error_proc, logger)

    def error_node(self):
        random_node = randint(10, 200)
        self.logger.log.info(f"Invoking node {random_node}...")
        try:
            raise self.error_types[0].error from self.error_types[1].error

        except Exception as e:
            self.logger.log_error(exception_to_log=e)

        self.error_occurred = True


class MacchiatoMalfunction(BasicBean):
    """Missing read-write access rights."""
    error_types = [error_5057]

    def __init__(self, n_calls, error_proc, logger: Logger):
        super().__init__(n_calls, error_proc, logger)

    def error_node(self):
        random_node = randint(10, 200)
        self.logger.log.info(f"Invoking node {random_node}...")
        try:
            raise self.error_types[0].error

        except Exception as e:
            self.logger.log_error(exception_to_log=e)

        self.error_occurred = True
    

class FrappeFrenzy(BasicBean):
    """VPC misconfigured"""
    error_types = [error_5066]

    def __init__(self, n_calls, error_proc, logger: Logger):
        super().__init__(n_calls, error_proc, logger)

    def error_node(self):
        random_node = randint(10, 200)
        self.logger.log.info(f"Invoking node {random_node}...")
        try:
            raise self.error_types[0].error

        except Exception as e:
            self.logger.log_error(exception_to_log=e)

        self.error_occurred = True


class CorruptedCortado(BasicBean):
    """VPC misconfigured"""
    error_types = [error_5057, error_2033]

    def __init__(self, n_calls, error_proc, logger: Logger):
        super().__init__(n_calls, error_proc, logger)

    def error_node(self):
        random_node = randint(10, 200)
        self.logger.log.info(f"Invoking node {random_node}...")
        try:
            raise self.error_types[0].error from self.error_types[1].error

        except Exception as e:
            self.logger.log_error(exception_to_log=e)

        self.error_occurred = True


class AnomalousAmericano(BasicBean):
    """Unsupported value in function call due to typo in configuration."""
    error_types = [error_2035, error_2034]

    def __init__(self, n_calls, error_proc, logger: Logger):
        super().__init__(n_calls, error_proc, logger)

    def error_node(self):
        random_node = randint(10, 200)
        self.logger.log.info(f"Invoking node {random_node}...")
        try:
            raise self.error_types[0].error from self.error_types[1].error

        except Exception as e:
            self.logger.log_error(exception_to_log=e)

        self.error_occurred = True


class RogueRistretto(BasicBean):
    """Out of memory"""
    error_types = [error_1000]

    def __init__(self, n_calls, error_proc, logger: Logger):
        super().__init__(n_calls, error_proc, logger)

    def error_node(self):
        random_node = randint(10, 200)
        self.logger.log.info(f"Invoking node {random_node}...")
        try:
            raise self.error_types[0].error

        except Exception as e:
            self.logger.log_error(exception_to_log=e)

        self.error_occurred = True

class MochaMayhem(BasicBean):
    """Feature not supported."""
    error_types = [error_3310]

    def __init__(self, n_calls, error_proc, logger: Logger):
        super().__init__(n_calls, error_proc, logger)

    def error_node(self):
        random_node = randint(10, 200)
        self.logger.log.info(f"Invoking node {random_node}...")
        try:
            raise self.error_types[0].error

        except Exception as e:
            self.logger.log_error(exception_to_log=e)

        self.error_occurred = True


class LeakyLatte(BasicBean):
    """Feature not supported on platform."""
    error_types = [error_3310, error_2033]

    def __init__(self, n_calls, error_proc, logger: Logger):
        super().__init__(n_calls, error_proc, logger)

    def error_node(self):
        random_node = randint(10, 200)
        self.logger.log.info(f"Invoking node {random_node}...")
        try:
            raise self.error_types[0].error from self.error_types[1].error

        except Exception as e:
            self.logger.log_error(exception_to_log=e)

        self.error_occurred = True


class PerturbedPocillo(BasicBean):
    """Wrong database credentials."""
    error_types = [error_5066, error_2034]

    def __init__(self, n_calls, error_proc, logger: Logger):
        super().__init__(n_calls, error_proc, logger)

    def error_node(self):
        random_node = randint(10, 200)
        self.logger.log.info(f"Invoking node {random_node}...")
        try:
            raise self.error_types[0].error from self.error_types[1].error

        except Exception as e:
            self.logger.log_error(exception_to_log=e)

        self.error_occurred = True
