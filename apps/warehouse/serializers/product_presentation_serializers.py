from rest_framework.serializers import ModelSerializer
from apps.warehouse.models.product_presentation import ProductPresentation
from master_serv.serializers.dynamic_field_serializer import DynamicFieldsModelSerializer


class ProductPresentationSerializer(ModelSerializer):
    class Meta:
        model = ProductPresentation
        fields = "__all__"


class ProductPresentationDynamicResponse(DynamicFieldsModelSerializer):
    class Meta:
        model = ProductPresentation
        exclude = ("status", "modified")


class ProductPresentationCreateRequest(ModelSerializer):
    class Meta:
        model = ProductPresentation
        exclude = ("status", "modified")


class ProductPresentationUpdateRequest(ModelSerializer):
    class Meta:
        model = ProductPresentation
        exclude = ("product_presentation_id", "status", "modified")
