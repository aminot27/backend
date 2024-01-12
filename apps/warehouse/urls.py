from django.urls import path

from apps.warehouse.api_views.brand_views import BrandsView, BrandDetailView, BrandView
from apps.warehouse.api_views.category_views import CategoriesView, CategoryView, CategoryDetailView
from apps.warehouse.api_views.unit_views import UnitView, UnitsView, UnitDetailView
from apps.warehouse.api_views.presentation_views import PresentationView, PresentationsView, PresentationDetailView
from apps.warehouse.api_views.product_presentation_views import ProductPresentationView, ProductPresentationsView, ProductPresentationDetailView
from apps.warehouse.api_views.product_views import ProductView, ProductsView, ProductDetailView
from apps.warehouse.api_views.specification_views import SpecificationView, SpecificationsView, SpecificationDetailView
from apps.warehouse.api_views.specification_detail_views import SpecificationDetailView_2, SpecificationDetailsView, SpecificationDetailDetailView
from apps.warehouse.api_views.subcategory_views import SubcategoriesView, SubcategoryView, SubcategoryDetailView
from apps.warehouse.api_views.product_subcategory_views import ProductSubcategoryView, ProductSubcategoriesView, ProductSubcategoryDetailView
from apps.warehouse.api_views.product_input_views import ProductInputView, ProductInputsView, ProductInputDetailView
from apps.warehouse.api_views.product_output_views import ProductOutputView, ProductOutputsView, ProductOutputDetailView
from apps.warehouse.api_views.product_detail_views import ProductDetailView_2, ProductDetailsView, ProductDetailDetailView

from apps.warehouse.api_views.product_views import ProductSKUView

urlpatterns = [
    path('brand/', BrandView.as_view(), name='create_brand'),
    path('brand/<int:pk>/', BrandDetailView.as_view(), name='modify_brand'),
    path('brands/filter/', BrandsView.as_view(), name='filter_brands'),

    path('categories/filter/', CategoriesView.as_view(), name='filter_categories'),
    path('category/', CategoryView.as_view(), name='create_category'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='modify_category'),

    path('subcategories/filter/', SubcategoriesView.as_view(), name='filter_subcategories'),
    path('subcategory/', SubcategoryView.as_view(), name='create_subcategory'),
    path('subcategory/<int:pk>/', SubcategoryDetailView.as_view(), name='modify_subcategory'),

    path('product_subcategory/', ProductSubcategoryView.as_view(), name='create_product_subcategory'),
    path('product_subcategories/filter/', ProductSubcategoriesView.as_view(), name='filter_product_subcategories'),
    path('product_subcategory/<int:pk>/', ProductSubcategoryDetailView.as_view(), name='modify_product_subcategory'),

    path('unit/', UnitView.as_view(), name='create_unit'),
    path('units/filter/', UnitsView.as_view(), name='filter_units'),
    path('unit/<int:pk>/', UnitDetailView.as_view(), name='modify_unit'),

    path('presentation/', PresentationView.as_view(), name='create_presentation'),
    path('presentations/filter/', PresentationsView.as_view(), name='filter_presentations'),
    path('presentation/<int:pk>/', PresentationDetailView.as_view(), name='modify_presentation'),

    path('product_presentation/', ProductPresentationView.as_view(), name='create_product_presentation'),
    path('product_presentations/filter/', ProductPresentationsView.as_view(), name='filter_product_presentations'),
    path('product_presentation/<int:pk>/', ProductPresentationDetailView.as_view(), name='modify_product_presentation'),

    path('product/', ProductView.as_view(), name='create_product'),
    path('products/filter/', ProductsView.as_view(), name='filter_products'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='modify_product'),

    path('specification/', SpecificationView.as_view(), name='create_specification'),
    path('specifications/filter/', SpecificationsView.as_view(), name='filter_specifications'),
    path('specification/<int:pk>/', SpecificationDetailView.as_view(), name='modify_specification'),

    path('specification_detail/', SpecificationDetailView_2.as_view(), name='create_specification_detail'),
    path('specification_details/filter/', SpecificationDetailsView.as_view(), name='filter_specification_details'),
    path('specification_detail/<int:pk>/', SpecificationDetailDetailView.as_view(), name='modify_specification_detail'),

    path('product_input/', ProductInputView.as_view(), name='create_product_input'),
    path('product_inputs/filter/', ProductInputsView.as_view(), name='filter_product_inputs'),
    path('product_input/<int:pk>/', ProductInputDetailView.as_view(), name='modify_product_input'),

    path('product_output/', ProductOutputView.as_view(), name='create_product_output'),
    path('product_outputs/filter/', ProductOutputsView.as_view(), name='filter_product_outputs'),
    path('product_output/<int:pk>/', ProductOutputDetailView.as_view(), name='modify_product_output'),

    path('product_detail/', ProductDetailView_2.as_view(), name='create_product_detail'),
    path('product_details/filter/', ProductDetailsView.as_view(), name='filter_product_details'),
    path('product_detail/<int:pk>/', ProductDetailDetailView.as_view(), name='modify_product_detail'),

    path('products/sku/<str:sku>/', ProductSKUView.as_view(), name='product-sku'),
]

