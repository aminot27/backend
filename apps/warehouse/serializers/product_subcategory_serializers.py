from rest_framework import serializers

from apps.warehouse.models.product_subcategory_model import ProductSubcategory  # Asegúrate de tener el import correcto
from master_serv.serializers.dynamic_field_serializer import DynamicFieldsModelSerializer


class ProductSubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSubcategory
        fields = '__all__'


class ProductSubcategoryDynamicResponse(DynamicFieldsModelSerializer):
    class Meta:
        model = ProductSubcategory
        exclude = ('status', 'modified')


class ProductSubcategoryDynamicRequest(DynamicFieldsModelSerializer):
    class Meta:
        model = ProductSubcategory
        fields = ('name',)


class ProductSubcategoryBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSubcategory
        fields = ('name',)


class ProductSubcategoryCreateRequest(serializers.ModelSerializer):
    class Meta:
        model = ProductSubcategory
        exclude = ('status', 'modified')


class ProductSubcategoryUpdateRequest(serializers.ModelSerializer):
    class Meta:
        model = ProductSubcategory
        exclude = ("product_subcategory_id", "status", "modified")
