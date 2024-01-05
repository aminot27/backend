from apps.warehouse.models.specification_detail_model import SpecificationDetail

class SpecificationDetailRepository:

    @staticmethod
    def get_specification_detail(specification_detail_id):
        return SpecificationDetail.objects.get_one(specification_detail_id)

    @staticmethod
    def get_specification_details(*values, **params):
        return SpecificationDetail.objects.filter(*values, **params)

    @staticmethod
    def post_specification_details(*values, **params):
        return SpecificationDetail.objects.get_many(*values, **params)

    @staticmethod
    def create_specification_detail(specification_detail):
        return SpecificationDetail.objects.create_one(**specification_detail)

    @staticmethod
    def update_specification_detail(specification_detail_id, specification_detail):
        return SpecificationDetail.objects.update_one(obj_primary_key=specification_detail_id, **specification_detail)

    @staticmethod
    def log_delete_specification_detail(specification_detail_id):
        return SpecificationDetail.objects.log_delete_one(primary_key=specification_detail_id)

    @staticmethod
    def soft_delete_specification_detail(specification_detail_id):
        return SpecificationDetail.objects.soft_delete_one(primary_key=specification_detail_id)
