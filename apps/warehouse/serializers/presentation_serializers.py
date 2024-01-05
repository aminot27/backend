from rest_framework import serializers

from apps.warehouse.models.presentation_model import Presentation
from master_serv.serializers.dynamic_field_serializer import DynamicFieldsModelSerializer


class PresentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presentation
        fields = '__all__'


class PresentationDynamicResponse(DynamicFieldsModelSerializer):
    class Meta:
        model = Presentation
        exclude = ('status', 'modified')


class PresentationDynamicRequest(DynamicFieldsModelSerializer):
    class Meta:
        model = Presentation
        fields = ('name',)


class PresentationBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presentation
        fields = ('name',)


class PresentationCreateRequest(serializers.ModelSerializer):
    class Meta:
        model = Presentation
        exclude = ('status', 'modified')


class PresentationUpdateRequest(serializers.ModelSerializer):
    class Meta:
        model = Presentation
        exclude = ("presentation_id", "status", "modified")
