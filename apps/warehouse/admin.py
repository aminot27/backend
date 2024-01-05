from django.contrib import admin

# Register your models here.
from apps.warehouse.models.brand_model import Brand
from apps.warehouse.models.category_model import Category
from apps.warehouse.models.presentation_model import Presentation
from apps.warehouse.models.product_model import Product
from apps.warehouse.models.product_presentation import ProductPresentation
from apps.warehouse.models.product_subcategory_model import ProductSubcategory
from apps.warehouse.models.specification_detail_model import SpecificationDetail
from apps.warehouse.models.specification_model import Specification
from apps.warehouse.models.subcategory_model import Subcategory
from apps.warehouse.models.unit_model import Unit


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Brand._meta.fields]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.fields]


@admin.register(Presentation)
class PresentationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Presentation._meta.fields]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]


@admin.register(ProductPresentation)
class ProductPresentationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductPresentation._meta.fields]


@admin.register(ProductSubcategory)
class ProductSubcategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductSubcategory._meta.fields]


@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Specification._meta.fields]


@admin.register(SpecificationDetail)
class SpecificationDetailAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SpecificationDetail._meta.fields]


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Subcategory._meta.fields]


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Unit._meta.fields]
