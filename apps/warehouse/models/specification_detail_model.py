from django.db import models

from apps.warehouse.models.specification_model import Specification
from master_serv.models.base_model import BaseModel


class SpecificationDetail(BaseModel):
    specification_detail_id = models.AutoField(verbose_name='Id', primary_key=True)
    specification = models.ForeignKey(Specification, db_column='specification_id', on_delete=models.DO_NOTHING,
                                      verbose_name='Specification', null=False)
    key = models.CharField(verbose_name='Key', max_length=20, blank=True, null=True)
    value = models.CharField(verbose_name='Value', max_length=50, blank=False, null=False, default='-')

    class Meta:
        db_table = 'warehouse_specification_detail'
        ordering = ['specification_detail_id']
        verbose_name = 'Specification Detail'
        verbose_name_plural = 'Specification Detail'

    def __str__(self):
        return '{}'.format(str(self.key) + ' - ' + str(self.value))
