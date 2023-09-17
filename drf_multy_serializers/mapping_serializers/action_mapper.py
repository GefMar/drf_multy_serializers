__all__ = ("ActionMethodMapper",)
import dataclasses
from collections import defaultdict
from typing import Literal

from rest_framework.serializers import Serializer

from drf_multy_serializers.constants.http import ALL_HTTP_METHODS
from drf_multy_serializers.type_stubs.http import HTTPMethodsT


@dataclasses.dataclass
class ActionMethodMapper:
    serializer_cls: Serializer
    methods: HTTPMethodsT = ALL_HTTP_METHODS
    actions: tuple[str] | Literal["all"] = "all"
    __mapper: defaultdict | None = dataclasses.field(init=False, default=None)

    @property
    def mapper(self):
        if self.__mapper is None:
            self.__mapper = self._make_mapper()
        return self.__mapper

    def _make_mapper(self):
        methods_map = {method.lower(): self.serializer_cls for method in self.methods}
        if self.actions == "all":
            return defaultdict(lambda: methods_map)
        return {action: methods_map for action in self.actions}
