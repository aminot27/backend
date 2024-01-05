from django.core.exceptions import FieldError
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from apps.warehouse.models.product_model import Product
from apps.warehouse.repositories.specification_repository import SpecificationRepository
from apps.warehouse.serializers.specification_serializers import SpecificationSerializer, \
    SpecificationDynamicResponse, SpecificationCreateRequest, SpecificationUpdateRequest
from master_serv.serializers.filter_request_format_serializer import FilterRequestFormatSerializer
from master_serv.utils.success_response import SuccessResponse
from master_serv.views.base_view import BaseAPIView
from rest_framework.exceptions import APIException, NotFound, ValidationError


class SpecificationsView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    specification_repository = SpecificationRepository()

    @swagger_auto_schema(responses={status.HTTP_200_OK: SpecificationSerializer(many=True)})
    def get(self, request):
        try:
            specifications = self.specification_repository.get_specifications()
            return SuccessResponse(data_=SpecificationSerializer(specifications, many=True).data).send()
        except:
            raise APIException()

    @swagger_auto_schema(request_body=FilterRequestFormatSerializer,
                         responses={status.HTTP_200_OK: SpecificationDynamicResponse(many=True)})
    def post(self, request):
        params, values = super().get_filter_request_data(request)
        specifications = self.specification_repository.post_specifications(*values, **params)
        if type(specifications) is FieldError:
            raise ValidationError(specifications)
        else:
            return SuccessResponse(
                data_=SpecificationDynamicResponse(specifications, many=True, fields=values).data).send()


class SpecificationView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    specification_repository = SpecificationRepository()

    @swagger_auto_schema(request_body=SpecificationCreateRequest,
                         responses={status.HTTP_200_OK: SpecificationSerializer()})
    def post(self, request):
        create_data = super().get_request_data(SpecificationCreateRequest(data=request.data))

        product_id = create_data.get('product')
        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            raise NotFound(detail="Product not found")

        create_data['product'] = product

        try:
            specification = self.specification_repository.create_specification(create_data)
            return SuccessResponse(data_=SpecificationSerializer(specification).data).send()
        except:
            raise APIException(detail="Error creating specification")


class SpecificationDetailView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    specification_repository = SpecificationRepository()

    @swagger_auto_schema(responses={status.HTTP_200_OK: SpecificationSerializer()})
    def get(self, request, pk):
        specification = self.specification_repository.get_specification(specification_id=pk)
        if specification is None:
            raise NotFound(detail="Specification not found")
        else:
            return SuccessResponse(data_=SpecificationSerializer(specification).data).send()

    @swagger_auto_schema(request_body=SpecificationUpdateRequest,
                         responses={status.HTTP_200_OK: SpecificationSerializer()})
    def put(self, request, pk):
        try:
            update_data = super().get_request_data(serialized_request=SpecificationUpdateRequest(data=request.data))
            specification = self.specification_repository.update_specification(specification_id=pk,
                                                                               specification=update_data)
            if specification is None:
                raise NotFound(detail="Specification not found")
            else:
                return SuccessResponse(data_=SpecificationSerializer(specification).data).send()
        except:
            raise APIException()

    def delete(self, request, pk):
        specification = self.specification_repository.get_specification(specification_id=pk)
        deleted = self.specification_repository.soft_delete_specification(specification_id=pk)
        if deleted is None:
            raise NotFound(detail="Specification not found")
        else:
            return SuccessResponse(data_=SpecificationSerializer(specification).data).send()
