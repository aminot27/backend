from django.db import models

from apps.warehouse.models.product_model import Product
from apps.warehouse.models.subcategory_model import Subcategory
from master_serv.models.base_model import BaseModel

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class ProductSubcategory(BaseModel):
    product_subcategory_id = models.AutoField(verbose_name='Id', primary_key=True)
    product = models.ForeignKey(Product, verbose_name='Product', db_column='product_id', on_delete=models.DO_NOTHING,
                                null=False)
    subcategory = models.ForeignKey(Subcategory, verbose_name='Product Subcategory', db_column='subcategory_id',
                                    on_delete=models.DO_NOTHING,
                                    null=False)

    class Meta:
        db_table = 'warehouse_product_subcategory'
        ordering = ['product_subcategory_id']
        verbose_name = 'Product Subcategory'
        verbose_name_plural = 'Product Subcategories'

    def __str__(self):
        return '{}'.format(str(self.product.name) + ' - ' + str(self.subcategory.description))

    def save(self, *args, **kwargs):
        if not self.pk:
            category_code = self.subcategory.category.code
            subcategory_code = self.subcategory.code
            product_code = self.product.product_code

            new_sku = f"{category_code}{subcategory_code}{product_code}"

            self.product.sku = new_sku
            self.product.save()

        super(ProductSubcategory, self).save(*args, **kwargs)


@receiver(post_save, sender=ProductSubcategory)
def update_sku(sender, instance, **kwargs):
    category_code = instance.subcategory.category.code
    subcategory_code = instance.subcategory.code
    product_code = instance.product.product_code

    new_sku = f"{category_code}{subcategory_code}{product_code}"

    if instance.product.sku != new_sku:
        instance.product.sku = new_sku
        instance.product.save()