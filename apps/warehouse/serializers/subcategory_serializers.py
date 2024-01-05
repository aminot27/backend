from rest_framework import serializers
from apps.warehouse.models.subcategory_model import Subcategory
from master_serv.serializers.dynamic_field_serializer import DynamicFieldsModelSerializer

class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = '__all__'

class SubcategoryDynamicResponse(DynamicFieldsModelSerializer):
    class Meta:
        model = Subcategory
        exclude = ('status', 'modified')

class SubcategoryDynamicRequest(DynamicFieldsModelSerializer):
    class Meta:
        model = Subcategory
        fields = ('name',)

class SubcategoryBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ('name',)

class SubcategoryCreateRequest(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        exclude = ('status', 'modified')

class SubcategoryUpdateRequest(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        exclude = ("subcategory_id", "status", "modified")
