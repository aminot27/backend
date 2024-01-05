from rest_framework import serializers

from apps.warehouse.models.product_detail_model import ProductDetail
from master_serv.serializers.dynamic_field_serializer import DynamicFieldsModelSerializer

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetail
        fields = '__all__'

class ProductDetailDynamicResponse(DynamicFieldsModelSerializer):
    class Meta:
        model = ProductDetail
        exclude = ('status', 'modified')

class ProductDetailDynamicRequest(DynamicFieldsModelSerializer):
    class Meta:
        model = ProductDetail
        fields = ('product', 'serial_number')

class ProductDetailBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetail
        fields = ('product', 'serial_number')

class ProductDetailCreateRequest(serializers.ModelSerializer):
    class Meta:
        model = ProductDetail
        exclude = ('status', 'modified')

class ProductDetailUpdateRequest(serializers.ModelSerializer):
    class Meta:
        model = ProductDetail
        exclude = ("product_detail_id", "status", "modified")
