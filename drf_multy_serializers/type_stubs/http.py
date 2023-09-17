from typing import Literal

GetLiteral = Literal["get"]
PostLiteral = Literal["post"]
PutLiteral = Literal["put"]
PatchLiteral = Literal["patch"]
DeleteLiteral = Literal["delete"]

HTTPMethodsT = tuple[GetLiteral | PostLiteral | PutLiteral | PatchLiteral | DeleteLiteral, ...]
