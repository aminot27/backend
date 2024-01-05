from django.db import models
from apps.warehouse.models.product_model import Product
from apps.warehouse.models.presentation_model import Presentation
from master_serv.models.base_model import BaseModel


class ProductPresentation(BaseModel):
    product_presentation_id = models.AutoField(verbose_name='Id', primary_key=True)
    product = models.ForeignKey(Product, db_column='product_id', verbose_name='Product', on_delete=models.DO_NOTHING,
                                null=False)
    presentation = models.ForeignKey(Presentation, db_column='presentation_id', verbose_name='Presentation',
                                     on_delete=models.DO_NOTHING, null=False)

    class Meta:
        db_table = 'warehouse_product_presentation'
        ordering = ['product_presentation_id']
        verbose_name = 'Product Presentation'
        verbose_name_plural = 'Product Presentations'

    def __str__(self):
        return '{}'.format(str(self.product.name) + ' - ' + str(self.presentation.description))
