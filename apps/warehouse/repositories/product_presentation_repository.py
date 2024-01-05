from apps.warehouse.models.product_presentation import ProductPresentation


class ProductPresentationRepository:

    @staticmethod
    def get_product_presentation(product_presentation_id):
        return ProductPresentation.objects.get_one(product_presentation_id)

    @staticmethod
    def get_product_presentations(*values, **params):
        return ProductPresentation.objects.filter(*values, **params)

    @staticmethod
    def post_product_presentations(*values, **params):
        return ProductPresentation.objects.get_many(*values, **params)

    @staticmethod
    def create_product_presentation(product_presentation):
        return ProductPresentation.objects.create_one(**product_presentation)

    @staticmethod
    def update_product_presentation(product_presentation_id, product_presentation):
        return ProductPresentation.objects.update_one(obj_primary_key=product_presentation_id, **product_presentation)

    @staticmethod
    def log_delete_product_presentation(product_presentation_id):
        return ProductPresentation.objects.log_delete_one(primary_key=product_presentation_id)

    @staticmethod
    def soft_delete_product_presentation(product_presentation_id):
        return ProductPresentation.objects.soft_delete_one(primary_key=product_presentation_id)
