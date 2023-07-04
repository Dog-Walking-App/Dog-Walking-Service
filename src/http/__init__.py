from .request import IRequest, Request, RequestMock
from .response import IResponse, Response, ResponseMock


class Http:
    def __init__(
        self,
        request: IRequest,
        response: IResponse,
    ):
        self.request = request
        self.response = response


class HttpMock:
    def __init__(
        self,
        request: IRequest,
        response: IResponse,
    ):
        self.request = request
        self.response = response


class Controller:
    def __init__(
        self,
        http: Http,
    ):
        self.request = http.request
        self.response = http.response
