from rest_framework import serializers

from apps.warehouse.models.specification_model import Specification
from master_serv.serializers.dynamic_field_serializer import DynamicFieldsModelSerializer

class SpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specification
        fields = '__all__'

class SpecificationDynamicResponse(DynamicFieldsModelSerializer):
    class Meta:
        model = Specification
        exclude = ('status', 'modified')

class SpecificationDynamicRequest(DynamicFieldsModelSerializer):
    class Meta:
        model = Specification
        fields = ('name',)

class SpecificationBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specification
        fields = ('name',)

class SpecificationCreateRequest(serializers.ModelSerializer):
    class Meta:
        model = Specification
        exclude = ('status', 'modified')

class SpecificationUpdateRequest(serializers.ModelSerializer):
    class Meta:
        model = Specification
        exclude = ("specification_id", "status", "modified")
