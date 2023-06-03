from django.urls import path
from . import views

urlpatterns = [
    path('input/', views.input_product, name='input_product'),
    path('products/', views.product_list, name='product_list'),
    path('export/csv/', views.export_products_csv, name='export_products_csv'),
]

# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('input/', views.input_product, name='input_product'),
    path('export/csv/', views.export_products_csv, name='export_products_csv'),
]