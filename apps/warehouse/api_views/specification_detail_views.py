import traceback

from django.core.exceptions import FieldError
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from apps.warehouse.models.specification_model import Specification
from apps.warehouse.repositories.specification_detail_repository import SpecificationDetailRepository
from apps.warehouse.serializers.specification_detail_serializers import SpecificationDetailSerializer, SpecificationDetailDynamicResponse, SpecificationDetailCreateRequest, \
    SpecificationDetailUpdateRequest
from master_serv.serializers.filter_request_format_serializer import FilterRequestFormatSerializer
from master_serv.utils.success_response import SuccessResponse
from master_serv.views.base_view import BaseAPIView
from rest_framework.exceptions import APIException, NotFound, ValidationError

class SpecificationDetailsView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    specification_detail_repository = SpecificationDetailRepository()

    """
    Get all records view
    """

    @swagger_auto_schema(responses={status.HTTP_200_OK: SpecificationDetailSerializer(many=True)})
    def get(self, request):
        try:
            specification_details = self.specification_detail_repository.get_specification_details()
            return SuccessResponse(data_=SpecificationDetailSerializer(specification_details, many=True).data).send()
        except:
            raise APIException()

    """
    Get all filtered records by params and return the given values
    """

    @swagger_auto_schema(request_body=FilterRequestFormatSerializer,
                         responses={status.HTTP_200_OK: SpecificationDetailDynamicResponse(many=True)})
    def post(self, request):
        params, values = super().get_filter_request_data(request)
        specification_details = self.specification_detail_repository.post_specification_details(*values, **params)
        if type(specification_details) is FieldError:
            raise ValidationError(specification_details)
        else:
            return SuccessResponse(
                data_=SpecificationDetailDynamicResponse(specification_details, many=True, fields=values).data).send()

class SpecificationDetailView_2(BaseAPIView):
    permission_classes = [IsAuthenticated]
    specification_detail_repository = SpecificationDetailRepository()

    @swagger_auto_schema(request_body=SpecificationDetailCreateRequest,
                         responses={status.HTTP_200_OK: SpecificationDetailSerializer()})
    def post(self, request):
        create_data = super().get_request_data(SpecificationDetailCreateRequest(data=request.data))

        specification_id = create_data.get('specification')
        try:
            specification = Specification.objects.get(pk=specification_id)
        except Specification.DoesNotExist:
            tb = traceback.format_exc()
            print(tb)
            raise NotFound(detail="Especification not found")

        create_data['specification'] = specification

        try:
            specification_detail = self.specification_detail_repository.create_specification_detail(create_data)
            return SuccessResponse(data_=SpecificationDetailSerializer(specification_detail).data).send()
        except:
            raise APIException(detail="Error creating specification detail")

class SpecificationDetailDetailView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    specification_detail_repository = SpecificationDetailRepository()

    """
    Filter a record by id
    """

    @swagger_auto_schema(responses={status.HTTP_200_OK: SpecificationDetailSerializer()})
    def get(self, request, pk):
        specification_detail = self.specification_detail_repository.get_specification_detail(specification_detail_id=pk)
        if specification_detail is None:
            raise NotFound(detail="Specification Detail not found")
        else:
            return SuccessResponse(data_=SpecificationDetailSerializer(specification_detail).data).send()

    @swagger_auto_schema(request_body=SpecificationDetailUpdateRequest, responses={status.HTTP_200_OK: SpecificationDetailSerializer()})
    def put(self, request, pk):
        try:
            update_data = super().get_request_data(serialized_request=SpecificationDetailUpdateRequest(data=request.data))
            specification_detail = self.specification_detail_repository.update_specification_detail(
                specification_detail_id=pk, specification_detail=update_data)
            if specification_detail is None:
                raise NotFound(detail="Specification Detail not found")
            else:
                return SuccessResponse(data_=SpecificationDetailSerializer(specification_detail).data).send()
        except:
            raise APIException()

    def delete(self, request, pk):
        specification_detail = self.specification_detail_repository.get_specification_detail(
            specification_detail_id=pk)
        deleted = self.specification_detail_repository.soft_delete_specification_detail(specification_detail_id=pk)
        if deleted is None:
            raise NotFound(detail="Specification Detail not found")
        else:
            return SuccessResponse(data_=SpecificationDetailSerializer(specification_detail).data).send()
