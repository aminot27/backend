from django.core.exceptions import FieldError
from drf_yasg.utils import swagger_auto_schema
from flask import Response
from rest_framework import status
from rest_framework.exceptions import APIException, ValidationError, NotFound
from rest_framework.permissions import IsAuthenticated

from apps.warehouse.models.category_model import Category
from apps.warehouse.repositories.category_repository import CategoryRepository
from apps.warehouse.serializers.category_serializers import CategorySerializer, CategoryDynamicResponse, \
    CategoryUpdateRequest, CategoryCreateRequest
from master_serv.serializers.filter_request_format_serializer import FilterRequestFormatSerializer
from master_serv.utils.success_response import SuccessResponse
from master_serv.views.base_view import BaseAPIView


class CategoriesView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    category_repository = CategoryRepository()

    @swagger_auto_schema(responses={status.HTTP_200_OK: CategorySerializer(many=True)})
    def get(self, request):
        try:
            category = self.category_repository.get_categories()
            return SuccessResponse(data_=CategorySerializer(category, many=True).data).send()
        except:
            raise APIException()

    @swagger_auto_schema(request_body=FilterRequestFormatSerializer,
                         responses={status.HTTP_200_OK: CategoryDynamicResponse(many=True)})
    def post(self, request,  *args, **kwargs):
        params, values = super().get_filter_request_data(request)
        categories = self.category_repository.get_categories(*values, **params)
        if type(categories) is FieldError:
            category = Category.objects.create(**request.data)
            return Response({'category_id': category.id}, status=status.HTTP_201_CREATED)
            raise ValidationError(categories)
        else:
            return SuccessResponse(data_=CategoryDynamicResponse(categories, many=True, fields=values).data).send()
        category = Category.objects.create(**request.data)
        return Response({'category_id': category.id}, status=status.HTTP_201_CREATED)



class CategoryView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    category_repository = CategoryRepository()
    """
    Create new category record
    """

    @swagger_auto_schema(request_body=CategoryCreateRequest(),
                         responses={status.HTTP_200_OK: CategorySerializer()})
    def post(self, request):
        create_data = super().get_request_data(CategoryCreateRequest(data=request.data))
        try:
            category = self.category_repository.create_category(category=create_data)
            return SuccessResponse(data_=CategoryCreateRequest(category).data).send()
        except:
            raise APIException(detail="Error creating category")


class CategoryDetailView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    category_repository = CategoryRepository()
    """
    Filter category by category_id
    """

    @swagger_auto_schema(responses={status.HTTP_200_OK: CategorySerializer()})
    def get(self, request, pk):
        category = self.category_repository.get_category(category_id=pk)
        if category is None:
            raise NotFound(detail="Category not found")
        else:
            return SuccessResponse(data_=CategorySerializer(category).data).send()

    @swagger_auto_schema(request_body=CategoryUpdateRequest,
                         responses={status.HTTP_200_OK: CategorySerializer()})
    def put(self, request, pk):
        try:
            update_data = super().get_request_data(serialized_request=CategoryUpdateRequest(data=request.data))
            category = self.category_repository.update_category(category_id=pk, category=update_data)
            if category is None:
                raise NotFound("Category not found")
            else:
                return SuccessResponse(data_=CategorySerializer(category).data).send()
        except:
            raise APIException()

    def delete(self, request, pk):
        category = self.category_repository.get_category(category_id=pk)
        deleted = self.category_repository.soft_delete_category(category_id=pk)
        if deleted is None:
            raise NotFound(detail="Category not found")
        else:
            return SuccessResponse(data_=CategorySerializer(category).data).send()
