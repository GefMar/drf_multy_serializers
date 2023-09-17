__all__ = ("MultySerializerMapper",)

import dataclasses

from rest_framework.serializers import Serializer

from drf_multy_serializers.type_stubs.request import RequestProtocol

from .action_mapper import ActionMethodMapper


@dataclasses.dataclass
class MultySerializerMapper:
    mappers: tuple[ActionMethodMapper, ...] = dataclasses.field(kw_only=True)
    default_serializer: type[Serializer] | None = dataclasses.field(default=None, kw_only=True)
    __mapper: dict = dataclasses.field(init=False)

    def __post_init__(self):
        self.__mapper = {}
        self.load_serializers()

    def load_serializers(self):
        for mapper in self.mappers:
            self.validate(mapper)
            self.__mapper.update(mapper.mapper)

    def validate(self, mapper: ActionMethodMapper, *, raise_exception: bool = True) -> bool:
        intersection = set(self.__mapper).intersection(mapper.mapper)
        if raise_exception and intersection:
            msg = f"actions: {intersection} already exist"
            raise ValueError(msg)
        return bool(intersection)

    def get_serializer(self, request: RequestProtocol) -> Serializer:
        try:
            return self.__mapper[request.action][request.method.lower()]
        except KeyError:
            if self.default_serializer is None:
                raise
            return self.default_serializer
