from rest_framework import serializers

from apps.warehouse.models.product_input_model import ProductInput
from master_serv.serializers.dynamic_field_serializer import DynamicFieldsModelSerializer

class ProductInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInput
        fields = '__all__'

class ProductInputDynamicResponse(DynamicFieldsModelSerializer):
    class Meta:
        model = ProductInput
        exclude = ('status', 'modified')

class ProductInputDynamicRequest(DynamicFieldsModelSerializer):
    class Meta:
        model = ProductInput
        fields = ('product', 'quantity', 'movement_date', 'reason')

class ProductInputBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInput
        fields = ('product', 'quantity', 'movement_date', 'reason')

class ProductInputCreateRequest(serializers.ModelSerializer):
    class Meta:
        model = ProductInput
        exclude = ('status', 'modified')

class ProductInputUpdateRequest(serializers.ModelSerializer):
    class Meta:
        model = ProductInput
        exclude = ("product_input_id", "status", "modified")
