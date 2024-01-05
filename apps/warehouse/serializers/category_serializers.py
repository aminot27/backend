from rest_framework import serializers

from apps.warehouse.models.category_model import Category
from master_serv.serializers.dynamic_field_serializer import DynamicFieldsModelSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryDynamicResponse(DynamicFieldsModelSerializer):
    class Meta:
        model = Category
        exclude = ('status', 'modified')


class CategoryCreateRequest(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('status', 'modified')


class CategoryUpdateRequest(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('category_id', 'status', 'modified')
