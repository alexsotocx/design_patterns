import requests
from http_client import HTTPClient


class RestHTTPClient(HTTPClient):
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, path, headers):
        print("Not decorated")
        response = requests.get(self.__build_url(path), headers=headers)
        return response.json()

    def __build_url(self, path):
        return self.base_url + path

