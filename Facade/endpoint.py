from typing import List, Dict, Union, Tuple, Optional
from dataclasses import dataclass

JSONType = Dict[str, Union[str, int, bool, None]]
HTTPResponse = Tuple[int, Union[JSONType, None]]


@dataclass
class Endpoint:
    method: str
    path: str

    def execute(self, jsonBody: Optional[JSONType]) -> HTTPResponse:
        raise NotImplementedError

    def match(self, method: str, path: str) -> bool:
        return path == self.path and method == self.method
