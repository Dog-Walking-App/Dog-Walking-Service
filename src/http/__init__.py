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


class HTTPService:
    """Provides methods that register endpoints"""

    items = []

    def _add_item(self, url, func, method):
        self.items.append({
            "url": url,
            "func": func.__name__,
            "method": method,
        })

    def get(self, url: str):
        def decorator(func):
            self._add_item(url, func, "GET")

            def wrapper(self, *args, **kwargs):
                return func(self, *args, **kwargs)
            wrapper.__name__ = func.__name__
            return wrapper
        return decorator

    def post(self, url: str):
        def decorator(func):
            self._add_item(url, func, "POST")

            def wrapper(self, *args, **kwargs):
                return func(self, *args, **kwargs)
            wrapper.__name__ = func.__name__
            return wrapper
        return decorator

    def put(self, url: str):
        def decorator(func):
            self._add_item(url, func, "PUT")

            def wrapper(self, *args, **kwargs):
                return func(self, *args, **kwargs)
            wrapper.__name__ = func.__name__
            return wrapper
        return decorator

    def delete(self, url: str):
        def decorator(func):
            self._add_item(url, func, "DELETE")

            def wrapper(self, *args, **kwargs):
                return func(self, *args, **kwargs)
            wrapper.__name__ = func.__name__
            return wrapper
        return decorator

    def patch(self, url: str):
        def decorator(func):
            self._add_item(url, func, "PATCH")

            def wrapper(self, *args, **kwargs):
                return func(self, *args, **kwargs)
            wrapper.__name__ = func.__name__
            return wrapper
        return decorator

    def build(self, blueprint, controller):
        for item in self.items:
            blueprint.add_url_rule(
                item["url"],
                view_func=getattr(controller, item["func"]),
                methods=[item["method"]]
            )
