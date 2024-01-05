from django.db import models
from master_serv.models.base_model import BaseModel


class Brand(BaseModel):
    brand_id = models.AutoField(verbose_name='Id', primary_key=True)
    name = models.CharField(verbose_name='Name', max_length=15, blank=False, null=False)

    class Meta:
        db_table = 'warehouse_brand'
        ordering = ['brand_id']
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return '{}'.format(str(self.name))
