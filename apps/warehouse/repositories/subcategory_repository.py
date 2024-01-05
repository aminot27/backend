from apps.warehouse.models.subcategory_model import Subcategory

class SubcategoryRepository:

    @staticmethod
    def get_subcategory(subcategory_id):
        return Subcategory.objects.get_one(subcategory_id)

    @staticmethod
    def get_subcategories(*values, **params):
        return Subcategory.objects.filter(*values, **params)

    @staticmethod
    def post_subcategories(*values, **params):
        return Subcategory.objects.get_many(*values, **params)

    @staticmethod
    def create_subcategory(subcategory):
        return Subcategory.objects.create_one(**subcategory)

    @staticmethod
    def update_subcategory(subcategory_id, subcategory):
        return Subcategory.objects.update_one(obj_primary_key=subcategory_id, **subcategory)

    @staticmethod
    def log_delete_subcategory(subcategory_id):
        return Subcategory.objects.log_delete_one(primary_key=subcategory_id)

    @staticmethod
    def soft_delete_subcategory(subcategory_id):
        return Subcategory.objects.soft_delete_one(primary_key=subcategory_id)
