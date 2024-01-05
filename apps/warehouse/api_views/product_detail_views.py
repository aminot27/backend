from django.core.exceptions import FieldError
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import APIException, NotFound, ValidationError

from apps.warehouse.models.product_detail_model import ProductDetail
from apps.warehouse.models.product_model import Product
from apps.warehouse.repositories.product_detail_repository import ProductDetailRepository
from apps.warehouse.serializers.product_detail_serializers import ProductDetailSerializer, \
    ProductDetailDynamicRequest, ProductDetailDynamicResponse, ProductDetailCreateRequest
from master_serv.serializers.filter_request_format_serializer import FilterRequestFormatSerializer
from master_serv.utils.success_response import SuccessResponse
from master_serv.views.base_view import BaseAPIView


class ProductDetailsView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    product_detail_repository = ProductDetailRepository()

    @swagger_auto_schema(responses={status.HTTP_200_OK: ProductDetailSerializer(many=True)})
    def get(self, request):
        try:
            product_details = self.product_detail_repository.get_product_details()
            return SuccessResponse(data_=ProductDetailSerializer(product_details, many=True).data).send()
        except:
            raise APIException()

    @swagger_auto_schema(request_body=FilterRequestFormatSerializer,
                         responses={status.HTTP_200_OK: ProductDetailDynamicResponse(many=True)})
    def post(self, request):
        params, values = super().get_filter_request_data(request)
        product_details = self.product_detail_repository.post_product_details(*values, **params)
        if type(product_details) is FieldError:
            raise ValidationError(product_details)
        else:
            return SuccessResponse(
                data_=ProductDetailDynamicResponse(product_details, many=True, fields=values).data).send()

class ProductDetailView_2(BaseAPIView):
    permission_classes = [IsAuthenticated]
    product_detail_repository = ProductDetailRepository()

    @swagger_auto_schema(request_body=ProductDetailCreateRequest,
                         responses={status.HTTP_200_OK: ProductDetailSerializer()})
    def post(self, request):
        create_data = super().get_request_data(ProductDetailCreateRequest(data=request.data))

        product_id = create_data.get('product')
        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            raise NotFound(detail="Product not found")

        create_data['product'] = product

        try:
            product_detail = self.product_detail_repository.create_product_detail(create_data)
            return SuccessResponse(data_=ProductDetailSerializer(product_detail).data).send()
        except:
            raise APIException(detail=f"Error creating product detail")

class ProductDetailDetailView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    product_detail_repository = ProductDetailRepository()

    @swagger_auto_schema(responses={status.HTTP_200_OK: ProductDetailSerializer()})
    def get(self, request, pk):
        product_detail = self.product_detail_repository.get_product_detail(product_detail_id=pk)
        if product_detail is None:
            raise NotFound(detail="Product Detail not found")
        else:
            return SuccessResponse(data_=ProductDetailSerializer(product_detail).data).send()

    @swagger_auto_schema(request_body=ProductDetailDynamicRequest,
                         responses={status.HTTP_200_OK: ProductDetailSerializer()})
    def put(self, request, pk):
        try:
            update_data = super().get_request_data(serialized_request=ProductDetailDynamicRequest(data=request.data))
            product_detail = self.product_detail_repository.update_product_detail(product_detail_id=pk,
                                                                                  product_detail=update_data)
            if product_detail is None:
                raise NotFound(detail="Product Detail not found")
            else:
                return SuccessResponse(data_=ProductDetailSerializer(product_detail).data).send()
        except:
            raise APIException()

    def delete(self, request, pk):
        product_detail = self.product_detail_repository.get_product_detail(product_detail_id=pk)
        deleted = self.product_detail_repository.soft_delete_product_detail(product_detail_id=pk)
        if deleted is None:
            raise NotFound(detail="Product Detail not found")
        else:
            return SuccessResponse(data_=ProductDetailSerializer(product_detail).data).send()
