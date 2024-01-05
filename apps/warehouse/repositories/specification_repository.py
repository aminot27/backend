from apps.warehouse.models.specification_model import Specification

class SpecificationRepository:

    @staticmethod
    def get_specification(specification_id):
        return Specification.objects.get_one(specification_id)

    @staticmethod
    def get_specifications(*values, **params):
        return Specification.objects.filter(*values, **params)

    @staticmethod
    def post_specifications(*values, **params):
        return Specification.objects.get_many(*values, **params)

    @staticmethod
    def create_specification(specification):
        return Specification.objects.create_one(**specification)

    @staticmethod
    def update_specification(specification_id, specification):
        return Specification.objects.update_one(obj_primary_key=specification_id, **specification)

    @staticmethod
    def log_delete_specification(specification_id):
        return Specification.objects.log_delete_one(primary_key=specification_id)

    @staticmethod
    def soft_delete_specification(specification_id):
        return Specification.objects.soft_delete_one(primary_key=specification_id)
