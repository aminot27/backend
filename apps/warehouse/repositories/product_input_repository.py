from apps.warehouse.models.product_input_model import ProductInput

class ProductInputRepository:

    @staticmethod
    def get_product_input(product_input_id):
        return ProductInput.objects.get_one(product_input_id)

    @staticmethod
    def get_product_inputs(*values, **params):
        return ProductInput.objects.filter(*values, **params)

    @staticmethod
    def post_product_inputs(*values, **params):
        return ProductInput.objects.get_many(*values, **params)

    @staticmethod
    def create_product_input(product_input):
        return ProductInput.objects.create_one(**product_input)

    @staticmethod
    def update_product_input(product_input_id, product_input):
        return ProductInput.objects.update_one(obj_primary_key=product_input_id, **product_input)

    @staticmethod
    def log_delete_product_input(product_input_id):
        return ProductInput.objects.log_delete_one(primary_key=product_input_id)

    @staticmethod
    def soft_delete_product_input(product_input_id):
        return ProductInput.objects.soft_delete_one(primary_key=product_input_id)
