from rest_framework import serializers
from apps.warehouse.models.product_model import Product
from master_serv.serializers.dynamic_field_serializer import DynamicFieldsModelSerializer

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductDynamicResponse(DynamicFieldsModelSerializer):
    class Meta:
        model = Product
        exclude = ('status', 'modified')

class ProductDynamicRequest(DynamicFieldsModelSerializer):
    class Meta:
        model = Product
        fields = ('name',)

class ProductBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name',)

class ProductCreateRequest(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=True, required=False)
    class Meta:
        model = Product
        exclude = ('status', 'modified')

class ProductUpdateRequest(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ("product_id", "status", "modified")
