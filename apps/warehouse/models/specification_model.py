from django.db import models

from apps.warehouse.models.product_model import Product
from master_serv.models.base_model import BaseModel


class Specification(BaseModel):
    specification_id = models.AutoField(verbose_name='Id', primary_key=True)
    product = models.ForeignKey(Product, db_column='product_id', on_delete=models.DO_NOTHING, verbose_name='Product',
                                null=False)
    name = models.CharField(verbose_name='Name', max_length=50, blank=False, null=False, default='-')

    class Meta:
        db_table = 'warehouse_specification'
        ordering = ['specification_id']
        verbose_name = 'Specification'
        verbose_name_plural = 'Specifications'

    def __str__(self):
        return '{}'.format(str(self.name))
