from apps.warehouse.models.presentation_model import Presentation


class PresentationRepository:

    @staticmethod
    def get_presentation(presentation_id):
        return Presentation.objects.get_one(presentation_id)

    @staticmethod
    def get_presentations(*values, **params):
        return Presentation.objects.filter(*values, **params)

    @staticmethod
    def post_presentations(*values, **params):
        return Presentation.objects.get_many(*values, **params)

    @staticmethod
    def create_presentation(presentation):
        return Presentation.objects.create_one(**presentation)

    @staticmethod
    def update_presentation(presentation_id, presentation):
        return Presentation.objects.update_one(obj_primary_key=presentation_id, **presentation)

    @staticmethod
    def log_delete_presentation(presentation_id):
        return Presentation.objects.log_delete_one(primary_key=presentation_id)

    @staticmethod
    def soft_delete_presentation(presentation_id):
        return Presentation.objects.soft_delete_one(primary_key=presentation_id)
