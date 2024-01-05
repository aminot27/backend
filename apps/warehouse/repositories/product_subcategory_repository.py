from apps.warehouse.models.product_subcategory_model import ProductSubcategory

class ProductSubcategoryRepository:

    @staticmethod
    def get_product_subcategory(product_subcategory_id):
        return ProductSubcategory.objects.get_one(product_subcategory_id)

    @staticmethod
    def get_product_subcategories(*values, **params):
        return ProductSubcategory.objects.filter(*values, **params)

    @staticmethod
    def post_product_subcategories(*values, **params):
        return ProductSubcategory.objects.get_many(*values, **params)

    @staticmethod
    def create_product_subcategory(product_subcategory):
        return ProductSubcategory.objects.create_one(**product_subcategory)

    @staticmethod
    def update_product_subcategory(product_subcategory_id, product_subcategory):
        return ProductSubcategory.objects.update_one(obj_primary_key=product_subcategory_id, **product_subcategory)

    @staticmethod
    def log_delete_product_subcategory(product_subcategory_id):
        return ProductSubcategory.objects.log_delete_one(primary_key=product_subcategory_id)

    @staticmethod
    def soft_delete_product_subcategory(product_subcategory_id):
        return ProductSubcategory.objects.soft_delete_one(primary_key=product_subcategory_id)
