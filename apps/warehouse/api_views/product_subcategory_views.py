from django.core.exceptions import FieldError
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from apps.warehouse.models.product_model import Product
from apps.warehouse.models.subcategory_model import Subcategory
from apps.warehouse.repositories.product_subcategory_repository import ProductSubcategoryRepository
from apps.warehouse.serializers.product_subcategory_serializers import ProductSubcategorySerializer, ProductSubcategoryDynamicResponse, ProductSubcategoryCreateRequest, \
    ProductSubcategoryUpdateRequest
from master_serv.serializers.filter_request_format_serializer import FilterRequestFormatSerializer
from master_serv.utils.success_response import SuccessResponse
from master_serv.views.base_view import BaseAPIView
from rest_framework.exceptions import APIException, NotFound, ValidationError


class ProductSubcategoriesView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    product_subcategory_repository = ProductSubcategoryRepository()

    """
    Get all records view
    """

    @swagger_auto_schema(responses={status.HTTP_200_OK: ProductSubcategorySerializer(many=True)})
    def get(self, request):
        try:
            product_subcategories = self.product_subcategory_repository.get_product_subcategories()
            return SuccessResponse(data_=ProductSubcategorySerializer(product_subcategories, many=True).data).send()
        except:
            raise APIException()

    """
    Get all filtered records by params and return the given values
    """

    @swagger_auto_schema(request_body=FilterRequestFormatSerializer,
                         responses={status.HTTP_200_OK: ProductSubcategoryDynamicResponse(many=True)})
    def post(self, request):
        params, values = super().get_filter_request_data(request)
        product_subcategories = self.product_subcategory_repository.post_product_subcategories(*values, **params)
        if type(product_subcategories) is FieldError:
            raise ValidationError(product_subcategories)
        else:
            return SuccessResponse(data_=ProductSubcategoryDynamicResponse(product_subcategories, many=True, fields=values).data).send()
class ProductSubcategoryView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    product_subcategory_repository = ProductSubcategoryRepository()

    @swagger_auto_schema(request_body=ProductSubcategoryCreateRequest, responses={status.HTTP_200_OK: ProductSubcategorySerializer()})
    def post(self, request):
        create_data = super().get_request_data(ProductSubcategoryCreateRequest(data=request.data))

        product_id = create_data.get('product')
        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            raise NotFound(detail="Product not found")

        create_data['product'] = product

        subcategory_id = create_data.get('subcategory')
        try:
            subcategory = Subcategory.objects.get(pk=subcategory_id)
        except Subcategory.DoesNotExist:
            raise NotFound(detail="Subcategory not found")

        create_data['subcategory'] = subcategory


        try:
            product_subcategory = self.product_subcategory_repository.create_product_subcategory(create_data)
            return SuccessResponse(data_=ProductSubcategorySerializer(product_subcategory).data).send()
        except:
            raise APIException(detail="Error creating product subcategory")


class ProductSubcategoryDetailView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    product_subcategory_repository = ProductSubcategoryRepository()

    """
    Filter a record by id
    """

    @swagger_auto_schema(responses={status.HTTP_200_OK: ProductSubcategorySerializer()})
    def get(self, request, pk):
        product_subcategory = self.product_subcategory_repository.get_product_subcategory(product_subcategory_id=pk)
        if product_subcategory is None:
            raise NotFound(detail="Product Subcategory not found")
        else:
            return SuccessResponse(data_=ProductSubcategorySerializer(product_subcategory).data).send()

    @swagger_auto_schema(request_body=ProductSubcategoryUpdateRequest, responses={status.HTTP_200_OK: ProductSubcategorySerializer()})
    def put(self, request, pk):
        try:
            update_data = super().get_request_data(serialized_request=ProductSubcategoryUpdateRequest(data=request.data))
            product_subcategory = self.product_subcategory_repository.update_product_subcategory(product_subcategory_id=pk, product_subcategory=update_data)
            if product_subcategory is None:
                raise NotFound(detail="Product Subcategory not found")
            else:
                return SuccessResponse(data_=ProductSubcategorySerializer(product_subcategory).data).send()
        except:
            raise APIException()

    def delete(self, request, pk):
        product_subcategory = self.product_subcategory_repository.get_product_subcategory(product_subcategory_id=pk)
        deleted = self.product_subcategory_repository.soft_delete_product_subcategory(product_subcategory_id=pk)
        if deleted is None:
            raise NotFound(detail="Product Subcategory not found")
        else:
            return SuccessResponse(data_=ProductSubcategorySerializer(product_subcategory).data).send()
