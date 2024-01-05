from django.core.exceptions import FieldError
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from apps.warehouse.models.category_model import Category
from apps.warehouse.repositories.subcategory_repository import SubcategoryRepository
from apps.warehouse.serializers.subcategory_serializers import SubcategorySerializer, SubcategoryDynamicResponse, SubcategoryCreateRequest, \
    SubcategoryUpdateRequest
from master_serv.serializers.filter_request_format_serializer import FilterRequestFormatSerializer
from master_serv.utils.success_response import SuccessResponse
from master_serv.views.base_view import BaseAPIView
from rest_framework.exceptions import APIException, NotFound, ValidationError

class SubcategoriesView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    subcategory_repository = SubcategoryRepository()

    @swagger_auto_schema(responses={status.HTTP_200_OK: SubcategorySerializer(many=True)})
    def get(self, request):
        try:
            subcategories = self.subcategory_repository.get_subcategories()
            return SuccessResponse(data_=SubcategorySerializer(subcategories, many=True).data).send()
        except:
            raise APIException()

    @swagger_auto_schema(request_body=FilterRequestFormatSerializer,
                         responses={status.HTTP_200_OK: SubcategoryDynamicResponse(many=True)})
    def post(self, request):
        params, values = super().get_filter_request_data(request)
        subcategories = self.subcategory_repository.post_subcategories(*values, **params)
        if type(subcategories) is FieldError:
            raise ValidationError(subcategories)
        else:
            return SuccessResponse(
                data_=SubcategoryDynamicResponse(subcategories, many=True, fields=values).data).send()

class SubcategoryView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    subcategory_repository = SubcategoryRepository()

    @swagger_auto_schema(request_body=SubcategoryCreateRequest, responses={status.HTTP_200_OK: SubcategorySerializer()})
    def post(self, request):
        create_data = super().get_request_data(SubcategoryCreateRequest(data=request.data))

        category_id = create_data.get('category')
        try:
            category = Category.objects.get(pk=category_id)
        except Category.DoesNotExist:
            raise NotFound(detail="Category not found")

        create_data['category'] = category

        try:
            subcategory = self.subcategory_repository.create_subcategory(create_data)
            return SuccessResponse(data_=SubcategorySerializer(subcategory).data).send()
        except:
            raise APIException(detail="Error creating subcategory")

class SubcategoryDetailView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    subcategory_repository = SubcategoryRepository()

    @swagger_auto_schema(responses={status.HTTP_200_OK: SubcategorySerializer()})
    def get(self, request, pk):
        subcategory = self.subcategory_repository.get_subcategory(subcategory_id=pk)
        if subcategory is None:
            raise NotFound(detail="Subcategory not found")
        else:
            return SuccessResponse(data_=SubcategorySerializer(subcategory).data).send()

    @swagger_auto_schema(request_body=SubcategoryUpdateRequest, responses={status.HTTP_200_OK: SubcategorySerializer()})
    def put(self, request, pk):
        try:
            update_data = super().get_request_data(serialized_request=SubcategoryUpdateRequest(data=request.data))
            subcategory = self.subcategory_repository.update_subcategory(subcategory_id=pk, subcategory=update_data)
            if subcategory is None:
                raise NotFound(detail="Subcategory not found")
            else:
                return SuccessResponse(data_=SubcategorySerializer(subcategory).data).send()
        except:
            raise APIException()

    def delete(self, request, pk):
        subcategory = self.subcategory_repository.get_subcategory(subcategory_id=pk)
        deleted = self.subcategory_repository.soft_delete_subcategory(subcategory_id=pk)
        if deleted is None:
            raise NotFound(detail="Subcategory not found")
        else:
            return SuccessResponse(data_=SubcategorySerializer(subcategory).data).send()
