from http_client import HTTPClient
from rest_http_client import RestHTTPClient
from http_request_decorator import HTTPRequestDecorator


def make_request(client: HTTPClient, path, headers):
    client.get(path, headers)


rest_client = RestHTTPClient("https://jsonplaceholder.typicode.com")
http_client_logger = HTTPRequestDecorator(rest_client)

make_request(rest_client, "/todos/1", {})
make_request(http_client_logger, "/todos/1", {})

