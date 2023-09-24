from abc import ABC, abstractmethod
from flask import request


class IRequest(ABC):
    @abstractmethod
    def get_json(self):
        pass


class Request(IRequest):
    def get_json(self):
        return request.get_json()


class RequestMock(IRequest):
    def get_json(self):
        pass
