from typing import List, Optional
from endpoint import Endpoint, JSONType, HTTPResponse

## This is the facade
class ApiGateway:
    def __init__(self):
        self._endpoints: List[Endpoint] = []

    def add_endpoint(self, endpoint: Endpoint):
        self._endpoints.append(endpoint)

    def process_request(self, method: str, path: str, body: Optional[JSONType]) -> HTTPResponse:
        for endpoint in self._endpoints:
            if endpoint.match(method, path):
                return endpoint.execute(body)
        return 404, {'message': 'Endpoint not found'}
