from rest_framework import serializers

from apps.warehouse.models.unit_model import Unit
from master_serv.serializers.dynamic_field_serializer import DynamicFieldsModelSerializer


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'


class UnitDynamicResponse(DynamicFieldsModelSerializer):
    class Meta:
        model = Unit
        exclude = ('status', 'modified')


class UnitDynamicRequest(DynamicFieldsModelSerializer):
    class Meta:
        model = Unit
        fields = ('name',)


class UnitBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ('name',)


class UnitCreateRequest(serializers.ModelSerializer):
    class Meta:
        model = Unit
        exclude = ('status', 'modified')


class UnitUpdateRequest(serializers.ModelSerializer):
    class Meta:
        model = Unit
        exclude = ('unit_id', 'status', 'modified')
