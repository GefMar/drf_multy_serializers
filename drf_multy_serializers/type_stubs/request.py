from typing import Literal, Protocol


class RequestProtocol(Protocol):
    action: str
    method: Literal["get", "post", "put", "patch", "delete"]
