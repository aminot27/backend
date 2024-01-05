from django.core.exceptions import FieldError
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from apps.warehouse.models.product_model import Product
from apps.warehouse.repositories.product_input_repository import ProductInputRepository
from apps.warehouse.serializers.product_input_serializers import ProductInputSerializer, ProductInputDynamicResponse, \
    ProductInputBasicSerializer, ProductInputDynamicRequest
from master_serv.serializers.filter_request_format_serializer import FilterRequestFormatSerializer
from master_serv.utils.success_response import SuccessResponse
from master_serv.views.base_view import BaseAPIView
from rest_framework.exceptions import APIException, NotFound, ValidationError


class ProductInputsView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    product_input_repository = ProductInputRepository()

    @swagger_auto_schema(responses={status.HTTP_200_OK: ProductInputSerializer(many=True)})
    def get(self, request):
        try:
            product_inputs = self.product_input_repository.get_product_inputs()
            return SuccessResponse(data_=ProductInputSerializer(product_inputs, many=True).data).send()
        except:
            raise APIException()

    @swagger_auto_schema(request_body=FilterRequestFormatSerializer,
                         responses={status.HTTP_200_OK: ProductInputDynamicResponse(many=True)})
    def post(self, request):
        params, values = super().get_filter_request_data(request)
        product_inputs = self.product_input_repository.post_product_inputs(*values, **params)
        if type(product_inputs) is FieldError:
            raise ValidationError(product_inputs)
        else:
            return SuccessResponse(
                data_=ProductInputDynamicResponse(product_inputs, many=True, fields=values).data).send()


class ProductInputView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    product_input_repository = ProductInputRepository()

    @swagger_auto_schema(request_body=ProductInputDynamicRequest,
                         responses={status.HTTP_200_OK: ProductInputSerializer()})
    def post(self, request):
        create_data = super().get_request_data(ProductInputDynamicRequest(data=request.data))

        product_id = create_data.get('product')
        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            raise NotFound(detail="Product not found")

        create_data['product'] = product

        try:
            product_input = self.product_input_repository.create_product_input(create_data)
            return SuccessResponse(data_=ProductInputSerializer(product_input).data).send()
        except:
            raise APIException(detail="Error creating product input")


class ProductInputDetailView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    product_input_repository = ProductInputRepository()

    @swagger_auto_schema(responses={status.HTTP_200_OK: ProductInputSerializer()})
    def get(self, request, pk):
        product_input = self.product_input_repository.get_product_input(product_input_id=pk)
        if product_input is None:
            raise NotFound(detail="Product Input not found")
        else:
            return SuccessResponse(data_=ProductInputSerializer(product_input).data).send()

    @swagger_auto_schema(request_body=ProductInputDynamicRequest,
                         responses={status.HTTP_200_OK: ProductInputSerializer()})
    def put(self, request, pk):
        try:
            update_data = super().get_request_data(serialized_request=ProductInputDynamicRequest(data=request.data))
            product_input = self.product_input_repository.update_product_input(product_input_id=pk,
                                                                               product_input=update_data)
            if product_input is None:
                raise NotFound(detail="Product Input not found")
            else:
                return SuccessResponse(data_=ProductInputSerializer(product_input).data).send()
        except:
            raise APIException()

    def delete(self, request, pk):
        product_input = self.product_input_repository.get_product_input(product_input_id=pk)
        deleted = self.product_input_repository.soft_delete_product_input(product_input_id=pk)
        if deleted is None:
            raise NotFound(detail="Product Input not found")
        else:
            return SuccessResponse(data_=ProductInputSerializer(product_input).data).send()
