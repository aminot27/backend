from apps.warehouse.models.product_detail_model import ProductDetail

class ProductDetailRepository:

    @staticmethod
    def get_product_detail(product_detail_id):
        return ProductDetail.objects.get_one(product_detail_id)

    @staticmethod
    def get_product_details(*values, **params):
        return ProductDetail.objects.filter(*values, **params)

    @staticmethod
    def post_product_details(*values, **params):
        return ProductDetail.objects.get_many(*values, **params)

    @staticmethod
    def create_product_detail(product_detail):
        return ProductDetail.objects.create_one(**product_detail)

    @staticmethod
    def update_product_detail(product_detail_id, product_detail):
        return ProductDetail.objects.update_one(obj_primary_key=product_detail_id, **product_detail)

    @staticmethod
    def log_delete_product_detail(product_detail_id):
        return ProductDetail.objects.log_delete_one(primary_key=product_detail_id)

    @staticmethod
    def soft_delete_product_detail(product_detail_id):
        return ProductDetail.objects.soft_delete_one(primary_key=product_detail_id)
