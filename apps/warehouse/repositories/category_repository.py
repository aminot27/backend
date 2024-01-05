from apps.warehouse.models.category_model import Category

class CategoryRepository:

    @staticmethod
    def get_category(category_id):
        return Category.objects.get_one(category_id)

    @staticmethod
    def get_categories(*values, **params):
        return Category.objects.get_many(*values, **params)

    @staticmethod
    def create_category(category):
        return Category.objects.create_one(**category)

    @staticmethod
    def update_category(category_id, category):
        return Category.objects.update_one(obj_primary_key=category_id, **category)

    @staticmethod
    def log_delete_category(category_id):
        return Category.objects.log_delete_one(primary_key=category_id)

    @staticmethod
    def soft_delete_category(category_id):
        return Category.objects.soft_delete_one(primary_key=category_id)
