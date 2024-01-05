from django.core.exceptions import FieldError
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from apps.warehouse.repositories.presentation_repository import PresentationRepository
from apps.warehouse.serializers.presentation_serializers import PresentationSerializer, PresentationDynamicResponse, PresentationCreateRequest, \
    PresentationUpdateRequest
from master_serv.serializers.filter_request_format_serializer import FilterRequestFormatSerializer
from master_serv.utils.success_response import SuccessResponse
from master_serv.views.base_view import BaseAPIView
from rest_framework.exceptions import APIException, NotFound, ValidationError

from apps.warehouse.models.unit_model import Unit


class PresentationsView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    presentation_repository = PresentationRepository()

    """
    Get all records view
    """

    @swagger_auto_schema(responses={status.HTTP_200_OK: PresentationSerializer(many=True)})
    def get(self, request):
        try:
            presentations = self.presentation_repository.get_presentations()
            return SuccessResponse(data_=PresentationSerializer(presentations, many=True).data).send()
        except:
            raise APIException()

    """
    Get all filtered records by params and return the given values
    """

    @swagger_auto_schema(request_body=FilterRequestFormatSerializer,
                         responses={status.HTTP_200_OK: PresentationDynamicResponse(many=True)})
    def post(self, request):
        params, values = super().get_filter_request_data(request)
        presentations = self.presentation_repository.post_presentations(*values, **params)
        if type(presentations) is FieldError:
            raise ValidationError(presentations)
        else:
            return SuccessResponse(data_=PresentationDynamicResponse(presentations, many=True, fields=values).data).send()


class PresentationView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    presentation_repository = PresentationRepository()

    @swagger_auto_schema(request_body=PresentationCreateRequest, responses={status.HTTP_200_OK: PresentationSerializer()})
    def post(self, request):
        create_data = super().get_request_data(PresentationCreateRequest(data=request.data))

        unit_id = create_data.get('unit')
        try:
            unit = Unit.objects.get(pk=unit_id)
        except Unit.DoesNotExist:
            raise NotFound(detail="Unit not found")

        create_data['unit'] = unit

        try:
            presentation = self.presentation_repository.create_presentation(create_data)
            return SuccessResponse(data_=PresentationSerializer(presentation).data).send()
        except:
            raise APIException(detail="Error creating presentation")




class PresentationDetailView(BaseAPIView):
    permission_classes = [IsAuthenticated]
    presentation_repository = PresentationRepository()

    """
    Filter a record by id
    """

    @swagger_auto_schema(responses={status.HTTP_200_OK: PresentationSerializer()})
    def get(self, request, pk):
        presentation = self.presentation_repository.get_presentation(presentation_id=pk)
        if presentation is None:
            raise NotFound(detail="Presentation not found")
        else:
            return SuccessResponse(data_=PresentationSerializer(presentation).data).send()

    @swagger_auto_schema(request_body=PresentationUpdateRequest, responses={status.HTTP_200_OK: PresentationSerializer()})
    def put(self, request, pk):
        try:
            update_data = super().get_request_data(serialized_request=PresentationUpdateRequest(data=request.data))
            presentation = self.presentation_repository.update_presentation(presentation_id=pk, presentation=update_data)
            if presentation is None:
                raise NotFound(detail="Presentation not found")
            else:
                return SuccessResponse(data_=PresentationSerializer(presentation).data).send()
        except:
            raise APIException()

    def delete(self, request, pk):
        presentation = self.presentation_repository.get_presentation(presentation_id=pk)
        deleted = self.presentation_repository.soft_delete_presentation(presentation_id=pk)
        if deleted is None:
            raise NotFound(detail="Presentation not found")
        else:
            return SuccessResponse(data_=PresentationSerializer(presentation).data).send()
