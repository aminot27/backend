from django.db import models
from apps.warehouse.models.product_model import Product
from master_serv.models.base_model import BaseModel

class ProductInput(BaseModel):
    product_input_id = models.AutoField(verbose_name='Id', primary_key=True)
    product = models.ForeignKey(Product, db_column='product_id', verbose_name='Product',
                                on_delete=models.DO_NOTHING, null=False)
    quantity = models.PositiveIntegerField(verbose_name='Quantity', default=0)
    movement_date = models.DateTimeField(verbose_name='Movement Date', auto_now_add=True)
    reason = models.CharField(verbose_name='Reason', max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'warehouse_product_input'
        ordering = ['product_input_id']
        verbose_name = 'Product Input'
        verbose_name_plural = 'Product Inputs'

    def __str__(self):
        return '{} - {}'.format(str(self.product.name), str(self.movement_date))
