from django.core.exceptions import FieldError
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from apps.warehouse.repositories.unit_repository import UnitRepository
from apps.warehouse.serializers.unit_serializers import UnitSerializer, UnitDynamicResponse, UnitCreateRequest, \
    UnitUpdateRequest
from master_serv.serializers.filter_request_format_serializer import FilterRequestFormatSerializer
from master_serv.utils.success_response import SuccessResponse
from master_serv.views.base_view import BaseAPIView
from rest_framework.exceptions import APIException, NotFound, ValidationError

class UnitsView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    unit_repository = UnitRepository()

    @swagger_auto_schema(responses={status.HTTP_200_OK: UnitSerializer(many=True)})
    def get(self, request):
        try:
            units = self.unit_repository.get_units()
            return SuccessResponse(data_=UnitSerializer(units, many=True).data).send()
        except:
            raise APIException()

    @swagger_auto_schema(request_body=FilterRequestFormatSerializer, responses={status.HTTP_200_OK: UnitDynamicResponse(many=True)})
    def post(self, request):
        params, values = super().get_filter_request_data(request)
        units = self.unit_repository.get_units(*values, **params)
        if type(units) is FieldError:
            raise ValidationError(units)
        else:
            return SuccessResponse(data_=UnitDynamicResponse(units, many=True, fields=values).data).send()


class UnitView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    unit_repository = UnitRepository()

    @swagger_auto_schema(request_body=UnitCreateRequest, responses={status.HTTP_200_OK: UnitSerializer()})
    def post(self, request):
        create_data = super().get_request_data(UnitCreateRequest(data=request.data))
        try:
            unit = self.unit_repository.create_unit(create_data)
            return SuccessResponse(data_=UnitSerializer(unit).data).send()
        except:
            raise APIException(detail="Error creating unit")


class UnitDetailView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    unit_repository = UnitRepository()

    @swagger_auto_schema(responses={status.HTTP_200_OK: UnitSerializer()})
    def get(self, request, pk):
        unit = self.unit_repository.get_unit(unit_id=pk)
        if unit is None:
            raise NotFound(detail="Unit not found")
        else:
            return SuccessResponse(data_=UnitSerializer(unit).data).send()

    @swagger_auto_schema(request_body=UnitUpdateRequest, responses={status.HTTP_200_OK: UnitSerializer()})
    def put(self, request, pk):
        try:
            update_data = super().get_request_data(serialized_request=UnitUpdateRequest(data=request.data))
            unit = self.unit_repository.update_unit(unit_id=pk, unit=update_data)
            if unit is None:
                raise NotFound(detail="Unit not found")
            else:
                return SuccessResponse(data_=UnitSerializer(unit).data).send()
        except:
            raise APIException()

    def delete(self, request, pk):
        deleted = self.unit_repository.soft_delete_unit(unit_id=pk)
        unit = self.unit_repository.get_unit(unit_id=pk)
        if deleted is None:
            raise NotFound(detail="Unit not found")
        else:
            return SuccessResponse(data_=UnitSerializer(unit).data).send()