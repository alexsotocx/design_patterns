from typing import Optional
from api_gateway import ApiGateway
from endpoint import JSONType

class Client:
    def __init__(self, api_gateway: ApiGateway):
        self._api_gateway = api_gateway

    def request(self, method: str, path: str, body: Optional[JSONType]):
        return self._api_gateway.process_request(method, path, body)
