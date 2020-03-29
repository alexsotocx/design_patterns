from typing import List
from endpoint import Endpoint

class UserEndpoint(Endpoint):
    def __init__(self, userRepository: List[str]):
        super().__init__('GET', '/users')
        self._userRepo = userRepository

    def execute(self, jsonBody):
        return 200, self._userRepo
