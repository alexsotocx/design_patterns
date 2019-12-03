from http_client import HTTPClient


class HTTPRequestDecorator(HTTPClient):
    def __init__(self, component: HTTPClient):
        self.component = component

    def get(self, path, headers):
        print("Prearing request to {path}".format(path=path))
        response = self.component.get(path, headers)
        print("Request executed with return {res}".format(res=response))
        print("Closing connection")
        return response

