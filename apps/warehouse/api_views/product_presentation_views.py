from django.core.exceptions import FieldError
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from apps.warehouse.models.presentation_model import Presentation
from apps.warehouse.models.product_model import Product
from apps.warehouse.repositories.product_presentation_repository import ProductPresentationRepository
from apps.warehouse.serializers.product_presentation_serializers import ProductPresentationSerializer, ProductPresentationDynamicResponse, ProductPresentationCreateRequest, \
    ProductPresentationUpdateRequest
from master_serv.serializers.filter_request_format_serializer import FilterRequestFormatSerializer
from master_serv.utils.success_response import SuccessResponse
from master_serv.views.base_view import BaseAPIView
from rest_framework.exceptions import APIException, NotFound, ValidationError


class ProductPresentationsView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    product_presentation_repository = ProductPresentationRepository()

    """
    Get all records view
    """

    @swagger_auto_schema(responses={status.HTTP_200_OK: ProductPresentationSerializer(many=True)})
    def get(self, request):
        try:
            product_presentations = self.product_presentation_repository.get_product_presentations()
            return SuccessResponse(data_=ProductPresentationSerializer(product_presentations, many=True).data).send()
        except:
            raise APIException()

    """
    Get all filtered records by params and return the given values
    """

    @swagger_auto_schema(request_body=FilterRequestFormatSerializer,
                         responses={status.HTTP_200_OK: ProductPresentationDynamicResponse(many=True)})
    def post(self, request):
        params, values = super().get_filter_request_data(request)
        product_presentations = self.product_presentation_repository.post_product_presentations(*values, **params)
        if type(product_presentations) is FieldError:
            raise ValidationError(product_presentations)
        else:
            return SuccessResponse(data_=ProductPresentationDynamicResponse(product_presentations, many=True, fields=values).data).send()
class ProductPresentationView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    product_presentation_repository = ProductPresentationRepository()

    @swagger_auto_schema(request_body=ProductPresentationCreateRequest, responses={status.HTTP_200_OK: ProductPresentationSerializer()})
    def post(self, request):
        create_data = super().get_request_data(ProductPresentationCreateRequest(data=request.data))

        presentation_id = create_data.get('presentation')
        try:
            presentation = Presentation.objects.get(pk=presentation_id)
        except Presentation.DoesNotExist:
            raise NotFound(detail="Presentation not found")

        create_data['presentation'] = presentation

        product_id = create_data.get('product')
        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            raise NotFound(detail="Product not found")

        create_data['product'] = product

        try:
            product_presentation = self.product_presentation_repository.create_product_presentation(create_data)
            return SuccessResponse(data_=ProductPresentationSerializer(product_presentation).data).send()
        except:
            raise APIException(detail="Error creating product presentation")


class ProductPresentationDetailView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    product_presentation_repository = ProductPresentationRepository()

    """
    Filter a record by id
    """

    @swagger_auto_schema(responses={status.HTTP_200_OK: ProductPresentationSerializer()})
    def get(self, request, pk):
        product_presentation = self.product_presentation_repository.get_product_presentation(product_presentation_id=pk)
        if product_presentation is None:
            raise NotFound(detail="Product Presentation not found")
        else:
            return SuccessResponse(data_=ProductPresentationSerializer(product_presentation).data).send()

    @swagger_auto_schema(request_body=ProductPresentationUpdateRequest, responses={status.HTTP_200_OK: ProductPresentationSerializer()})
    def put(self, request, pk):
        try:
            update_data = super().get_request_data(serialized_request=ProductPresentationUpdateRequest(data=request.data))
            product_presentation = self.product_presentation_repository.update_product_presentation(product_presentation_id=pk, product_presentation=update_data)
            if product_presentation is None:
                raise NotFound(detail="Product Presentation not found")
            else:
                return SuccessResponse(data_=ProductPresentationSerializer(product_presentation).data).send()
        except:
            raise APIException()

    def delete(self, request, pk):
        product_presentation = self.product_presentation_repository.get_product_presentation(
            product_presentation_id=pk)
        deleted = self.product_presentation_repository.soft_delete_product_presentation(product_presentation_id=pk)
        if deleted is None:
            raise NotFound(detail="Product Presentation not found")
        else:
            return SuccessResponse(data_=ProductPresentationSerializer(product_presentation).data).send()
