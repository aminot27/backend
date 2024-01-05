from django.core.exceptions import FieldError
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from apps.warehouse.repositories.product_repository import ProductRepository
from apps.warehouse.serializers.product_serializers import ProductSerializer, ProductDynamicResponse, ProductCreateRequest, \
    ProductUpdateRequest
from master_serv.serializers.filter_request_format_serializer import FilterRequestFormatSerializer
from master_serv.utils.success_response import SuccessResponse
from master_serv.views.base_view import BaseAPIView
from rest_framework.exceptions import APIException, NotFound, ValidationError

from apps.warehouse.models.brand_model import Brand


class ProductsView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    product_repository = ProductRepository()

    """
    Get all records view
    """

    @swagger_auto_schema(responses={status.HTTP_200_OK: ProductSerializer(many=True)})
    def get(self, request):
        try:
            products = self.product_repository.get_products()
            return SuccessResponse(data_=ProductSerializer(products, many=True).data).send()
        except:
            raise APIException()

    """
    Get all filtered records by params and return the given values
    """

    @swagger_auto_schema(request_body=FilterRequestFormatSerializer,
                         responses={status.HTTP_200_OK: ProductDynamicResponse(many=True)})
    def post(self, request):
        params, values = super().get_filter_request_data(request)
        products = self.product_repository.post_products(*values, **params)
        if type(products) is FieldError:
            raise ValidationError(products)
        else:
            return SuccessResponse(data_=ProductDynamicResponse(products, many=True, fields=values).data).send()


class ProductView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    product_repository = ProductRepository()

    @swagger_auto_schema(request_body=ProductCreateRequest, responses={status.HTTP_200_OK: ProductSerializer()})
    def post(self, request):
        create_data = super().get_request_data(ProductCreateRequest(data=request.data))

        brand_id = create_data.get('brand')
        try:
            brand = Brand.objects.get(pk=brand_id)
        except Brand.DoesNotExist:
            raise NotFound(detail="Brand not found")

        create_data['brand'] = brand

        try:
            product = self.product_repository.create_product(create_data)
            return SuccessResponse(data_=ProductSerializer(product).data).send()
        except:
            raise APIException(detail="Error creating product")

class ProductDetailView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    product_repository = ProductRepository()

    """
    Filter a record by id
    """

    @swagger_auto_schema(responses={status.HTTP_200_OK: ProductSerializer()})
    def get(self, request, pk):
        product = self.product_repository.get_product(product_id=pk)
        if product is None:
            raise NotFound(detail="Product not found")
        else:
            return SuccessResponse(data_=ProductSerializer(product).data).send()

    @swagger_auto_schema(request_body=ProductUpdateRequest, responses={status.HTTP_200_OK: ProductSerializer()})
    def put(self, request, pk):
        try:
            update_data = super().get_request_data(serialized_request=ProductUpdateRequest(data=request.data))
            product = self.product_repository.update_product(product_id=pk, product=update_data)
            if product is None:
                raise NotFound(detail="Product not found")
            else:
                return SuccessResponse(data_=ProductSerializer(product).data).send()
        except:
            raise APIException()

    def delete(self, request, pk):
        product = self.product_repository.get_product(product_id=pk)
        deleted = self.product_repository.soft_delete_product(product_id=pk)
        if deleted is None:
            raise NotFound(detail="Product not found")
        else:
            return SuccessResponse(data_=ProductSerializer(product).data).send()
