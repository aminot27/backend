from django.db import models
from master_serv.models.base_model import BaseModel
from apps.warehouse.models.unit_model import Unit


class Presentation(BaseModel):
    presentation_id = models.AutoField(verbose_name='Id', primary_key=True)
    unit = models.ForeignKey(Unit, verbose_name='Unit', db_column='unit_id', on_delete=models.DO_NOTHING,
                             null=False)
    quantity = models.IntegerField(verbose_name='Quantity', default=0)
    description = models.CharField(verbose_name='Presentation', max_length=20, blank=False, null=False, default='-')
    is_min = models.BooleanField(verbose_name='IsMin', blank=False, null=False, default=True)

    class Meta:
        db_table = 'warehouse_presentation'
        ordering = ['presentation_id']
        verbose_name = 'Presentation'
        verbose_name_plural = 'Presentations'

    def __str__(self):
        return '{}'.format(str(self.description))
