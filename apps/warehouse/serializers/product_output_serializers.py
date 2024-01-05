from rest_framework import serializers
from apps.warehouse.models.product_output_model import ProductOutput
from master_serv.serializers.dynamic_field_serializer import DynamicFieldsModelSerializer
class ProductOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOutput
        fields = '__all__'

class ProductOutputDynamicResponse(DynamicFieldsModelSerializer):
    class Meta:
        model = ProductOutput
        exclude = ('status', 'modified')

class ProductOutputDynamicRequest(DynamicFieldsModelSerializer):
    class Meta:
        model = ProductOutput
        fields = ('product', 'quantity', 'movement_date', 'reason')

class ProductOutputBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOutput
        fields = ('product', 'quantity', 'movement_date', 'reason')

class ProductOutputCreateRequest(serializers.ModelSerializer):
    class Meta:
        model = ProductOutput
        exclude = ('status', 'modified')

class ProductOutputUpdateRequest(serializers.ModelSerializer):
    class Meta:
        model = ProductOutput
        exclude = ("product_output_id", "status", "modified")