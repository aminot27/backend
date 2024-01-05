from django.db import models

from master_serv.models.base_model import BaseModel


class Unit(BaseModel):
    unit_id = models.AutoField(verbose_name='Id', primary_key=True)
    name = models.CharField(verbose_name='Name', max_length=10, blank=False, null=False)
    abbreviation = models.CharField(verbose_name='Abbreviation', max_length=5, blank=False, null=False)

    class Meta:
        db_table = 'warehouse_unit'
        ordering = ['unit_id']
        verbose_name = 'Unit'
        verbose_name_plural = 'Units'

    def __str__(self):
        return '{}'.format(str(self.name) + ' - ' + str(self.abbreviation))
