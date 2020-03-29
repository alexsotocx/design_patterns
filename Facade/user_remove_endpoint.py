from typing import List
from endpoint import Endpoint

class UserRemoveEndpoint(Endpoint):
    def __init__(self, userRepository: List[str]):
        super().__init__('DELETE', '/users')
        self._userRepo = userRepository

    def execute(self, jsonBody):
        self._userRepo.remove(jsonBody['id'])
        return 204, None
