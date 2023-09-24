from abc import ABC, abstractmethod
from flask import jsonify, Response as TResponse


def _get_status_code(**kwargs):
    return (kwargs and kwargs["status_code"] or 200) or 200


class IResponse(ABC):
    @abstractmethod
    def send(self, *args, **kwargs) -> TResponse:
        pass


class Response(IResponse):
    def send(self, *args, **kwargs):
        return jsonify(*args, **kwargs), _get_status_code(**kwargs)


class TResponseMock:
    def __init__(self, *args, **kwargs):
        self.data = args and args[0] or None
        self.kwargs = kwargs.copy()
        if "status_code" in self.kwargs:
            del self.kwargs["status_code"]
        self.status_code = _get_status_code(**kwargs)

    def get_json(self):
        return self.data or self.kwargs


class ResponseMock(IResponse):
    def send(self, *args, **kwargs):
        return TResponseMock(*args, **kwargs)
