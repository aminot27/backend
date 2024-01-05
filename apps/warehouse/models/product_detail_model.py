from django.db import models
from apps.warehouse.models.product_model import Product
from master_serv.models.base_model import BaseModel

class ProductDetail(BaseModel):
    product_detail_id = models.AutoField(verbose_name='Id', primary_key=True)
    product = models.ForeignKey(Product, db_column='product_id', verbose_name='Product',
                                on_delete=models.DO_NOTHING, null=False)
    serial_number = models.CharField(max_length=20, verbose_name='Serial Number')


    class Meta:
        db_table = 'warehouse_product_detail'
        ordering = ['product_detail_id']
        verbose_name = 'Product Detail'
        verbose_name_plural = 'Product Details'

    def __str__(self):
        return '{} - {}'.format(str(self.product.name), str(self.serial_number))