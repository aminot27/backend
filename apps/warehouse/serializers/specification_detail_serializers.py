from rest_framework.serializers import ModelSerializer
from master_serv.serializers.dynamic_field_serializer import DynamicFieldsModelSerializer
from apps.warehouse.models.specification_detail_model import SpecificationDetail


class SpecificationDetailSerializer(ModelSerializer):
    class Meta:
        model = SpecificationDetail
        fields = "__all__"


class SpecificationDetailDynamicResponse(DynamicFieldsModelSerializer):
    class Meta:
        model = SpecificationDetail
        exclude = ("status", "modified")


class SpecificationDetailCreateRequest(ModelSerializer):
    class Meta:
        model = SpecificationDetail
        exclude = ("status", "modified")


class SpecificationDetailUpdateRequest(ModelSerializer):
    class Meta:
        model = SpecificationDetail
        exclude = ("specification_detail_id", "status", "modified")
