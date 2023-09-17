__all__ = ("GenericAPIView",)

from rest_framework import generics

from drf_multy_serializers.mapping_serializers.multy_mapper import MultySerializerMapper


class GenericAPIView(generics.GenericAPIView):
    multy_serializer: MultySerializerMapper

    def get_serializer_class(self):
        return self.multy_serializer.get_serializer(self.request)
