# Generated by Django 4.0 on 2024-01-11 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0006_productdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='SKU'),
        ),
        migrations.AlterField(
            model_name='product',
            name='warranty_level',
            field=models.CharField(blank=True, choices=[('Marca', 'Marca'), ('Mayorista', 'Mayorista')], max_length=10, null=True, verbose_name='Warranty Level'),
        ),
    ]
