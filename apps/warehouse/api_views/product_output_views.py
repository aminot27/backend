from django.core.exceptions import FieldError
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from apps.warehouse.models.product_model import Product
from apps.warehouse.repositories.product_output_repository import ProductOutputRepository
from apps.warehouse.serializers.product_output_serializers import ProductOutputSerializer, ProductOutputDynamicResponse, \
    ProductOutputBasicSerializer, ProductOutputDynamicRequest
from master_serv.serializers.filter_request_format_serializer import FilterRequestFormatSerializer
from master_serv.utils.success_response import SuccessResponse
from master_serv.views.base_view import BaseAPIView
from rest_framework.exceptions import APIException, NotFound, ValidationError

class ProductOutputsView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    product_output_repository = ProductOutputRepository()

    @swagger_auto_schema(responses={status.HTTP_200_OK: ProductOutputSerializer(many=True)})
    def get(self, request):
        try:
            product_outputs = self.product_output_repository.get_product_outputs()
            return SuccessResponse(data_=ProductOutputSerializer(product_outputs, many=True).data).send()
        except:
            raise APIException()

    @swagger_auto_schema(request_body=FilterRequestFormatSerializer,
                         responses={status.HTTP_200_OK: ProductOutputDynamicResponse(many=True)})
    def post(self, request):
        params, values = super().get_filter_request_data(request)
        product_outputs = self.product_output_repository.post_product_outputs(*values, **params)
        if type(product_outputs) is FieldError:
            raise ValidationError(product_outputs)
        else:
            return SuccessResponse(
                data_=ProductOutputDynamicResponse(product_outputs, many=True, fields=values).data).send()


class ProductOutputView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    product_output_repository = ProductOutputRepository()

    @swagger_auto_schema(request_body=ProductOutputDynamicRequest,
                         responses={status.HTTP_200_OK: ProductOutputSerializer()})
    def post(self, request):
        create_data = super().get_request_data(ProductOutputDynamicRequest(data=request.data))


        product_id = create_data.get('product')
        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            raise NotFound(detail="Product not found")

        create_data['product'] = product

        try:
            product_output = self.product_output_repository.create_product_output(create_data)
            return SuccessResponse(data_=ProductOutputSerializer(product_output).data).send()
        except:
            raise APIException(detail="Error creating product output")



class ProductOutputDetailView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    product_output_repository = ProductOutputRepository()

    @swagger_auto_schema(responses={status.HTTP_200_OK: ProductOutputSerializer()})
    def get(self, request, pk):
        product_output = self.product_output_repository.get_product_output(product_output_id=pk)
        if product_output is None:
            raise NotFound(detail="Product Output not found")
        else:
            return SuccessResponse(data_=ProductOutputSerializer(product_output).data).send()

    @swagger_auto_schema(request_body=ProductOutputDynamicRequest,
                         responses={status.HTTP_200_OK: ProductOutputSerializer()})
    def put(self, request, pk):
        try:
            update_data = super().get_request_data(serialized_request=ProductOutputDynamicRequest(data=request.data))
            product_output = self.product_output_repository.update_product_output(product_output_id=pk,
                                                                                 product_output=update_data)

            if product_output is None:
                raise NotFound(detail="Product Output not found")
            else:
                return SuccessResponse(data_=ProductOutputSerializer(product_output).data).send()
        except:
            raise APIException()

    def delete(self, request, pk):
        product_output = self.product_output_repository.get_product_output(product_output_id=pk)
        deleted = self.product_output_repository.soft_delete_product_output(product_output_id=pk)
        if deleted is None:
            raise NotFound(detail="Product Output not found")
        else:
            return SuccessResponse(data_=ProductOutputSerializer(product_output).data).send()
