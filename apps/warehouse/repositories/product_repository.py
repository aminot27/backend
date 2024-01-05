from apps.warehouse.models.product_model import Product

class ProductRepository:

    @staticmethod
    def get_product(product_id):
        return Product.objects.get_one(product_id)

    @staticmethod
    def get_products(*values, **params):
        return Product.objects.filter(*values, **params)

    @staticmethod
    def post_products(*values, **params):
        return Product.objects.get_many(*values, **params)

    @staticmethod
    def create_product(product):
        return Product.objects.create_one(**product)

    @staticmethod
    def update_product(product_id, product):
        return Product.objects.update_one(obj_primary_key=product_id, **product)

    @staticmethod
    def log_delete_product(product_id):
        return Product.objects.log_delete_one(primary_key=product_id)

    @staticmethod
    def soft_delete_product(product_id):
        return Product.objects.soft_delete_one(primary_key=product_id)
