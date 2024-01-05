from apps.warehouse.models.product_output_model import ProductOutput

class ProductOutputRepository:

    @staticmethod
    def get_product_output(product_output_id):
        return ProductOutput.objects.get_one(product_output_id)

    @staticmethod
    def get_product_outputs(*values, **params):
        return ProductOutput.objects.filter(*values, **params)

    @staticmethod
    def post_product_outputs(*values, **params):
        return ProductOutput.objects.get_many(*values, **params)

    @staticmethod
    def create_product_output(product_output):
        return ProductOutput.objects.create_one(**product_output)

    @staticmethod
    def update_product_output(product_output_id, product_output):
        return ProductOutput.objects.update_one(obj_primary_key=product_output_id, **product_output)

    @staticmethod
    def log_delete_product_output(product_output_id):
        return ProductOutput.objects.log_delete_one(primary_key=product_output_id)

    @staticmethod
    def soft_delete_product_output(product_output_id):
        return ProductOutput.objects.soft_delete_one(primary_key=product_output_id)