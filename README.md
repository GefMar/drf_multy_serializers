# drf_multy_serializers

The `drf_multy_serializers` library provides tools to create DRF (Django Rest Framework) `ViewSets` with the ability to select serializers based on the current action and HTTP method. This allows for a flexible setup of response formats and incoming data for different operations within the same `ViewSet`.

## Key Features

- **Multiple Serializers**: Utilize different serializers for various actions and HTTP methods.
- **Flexible Configuration**: Map actions, methods, and serializers with the `ActionMethodMapper` class.
- **DRF Integration**: Enhances the standard capabilities of DRF, tailoring it for more complex use cases.

## Installation

*(Add installation instructions if available. E.g., via pip or other means.)*

```bash
pip install drf_multy_serializers
```

## Usage Example

Suppose you have a `Product` model, and you want to employ different serializers for listing products and for creating or editing a product:

```python3
from rest_framework import serializers
from drf_multy_serializers.views import generics
from drf_multy_serializers.mapping_serializers import MultySerializerMapper, ActionMethodMapper
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin
from app import models

class ProductListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()

class ProductDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    price = serializers.DecimalField()

list_mapper = ActionMethodMapper(
    actions=('list',),
    methods=('get',),
    serializer_cls=ProductListSerializer
)

detail_mapper = ActionMethodMapper(
    actions=('create', 'update'),
    methods=('post', 'put', 'patch'),
    serializer_cls=ProductDetailSerializer
)

class ProductViewSet(ListModelMixin, CreateModelMixin, UpdateModelMixin, generics.GenericAPIView):
    multy_serializer = MultySerializerMapper(
        default_serializer=ProductDetailSerializer,
        mappers=(list_mapper, detail_mapper)
    )
    queryset = models.Product.objects.all()
```

## Documentation

---
