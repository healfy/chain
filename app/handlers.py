import os
import typing
from abc import ABC, abstractmethod

import app
from .shared import Logger


BASE_DIR: str = os.path.dirname(os.path.abspath(app.__file__))


class Handler(ABC):

    @abstractmethod
    def set_next(self, handler: 'Handler') -> 'Handler':
        pass

    @abstractmethod
    def handle(self, request: typing.AnyStr):
        pass


class AbstractHandler(Handler):

    _next_handler: Handler = None
    logger: Logger
    result_file: str = os.path.join(BASE_DIR, 'result.txt')

    def __init__(self, logger: Logger):
        self.logger = logger

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: typing.AnyStr) -> typing.Optional[str]:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None

    def log_result(self, request: typing.AnyStr):
        with open(os.path.join(BASE_DIR, request), 'r') as f:
            with open(self.result_file, 'a+') as f2:
                f2.write('\n\n')
                f2.write(f.read())


class XMLHandler(AbstractHandler):
    _name: str = 'XML'

    def handle(self, request: typing.AnyStr):
        if request.endswith('xml'):
            self.logger.log(f'Oбработчик {self._name} получил файл {request}')
            return self.log_result(request)
        return super().handle(request)


class JSONHandler(AbstractHandler):
    _name: str = 'JSON'

    def handle(self, request: typing.AnyStr):
        if request.endswith('json'):
            self.logger.log(f'Oбработчик {self._name} получил файл {request}')
            return self.log_result(request)
        return super().handle(request)


class CSVHandler(AbstractHandler):
    _name: str = 'CSV'

    def handle(self, request: typing.AnyStr):
        if request.endswith('csv'):
            self.logger.log(f'Oбработчик {self._name} получил файл {request}')
            return self.log_result(request)
        return super().handle(request)


class TXTHandler(AbstractHandler):
    _name: str = 'TXT'

    def handle(self, request: typing.AnyStr):
        if request.endswith('txt'):
            self.logger.log(f'Oбработчик {self._name} получил файл {request}')
            return self.log_result(request)
        return super().handle(request)
