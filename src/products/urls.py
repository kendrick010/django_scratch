from django.urls import path

from .views import (
    product_detail_view, 
    product_create_view, 
    dynamic_lookup_view, 
    product_delete_view, 
    product_list_view
)

app_name = "products"
urlpatterns = [
    path('create/', product_create_view, name='create'),
    path('product/', product_detail_view, name='product'),
    path('product/<int:id>/', dynamic_lookup_view, name='product_id'),
    path('product/<int:id>/delete/', product_delete_view, name='product_delete'),
    path('product/list/', product_list_view, name='products_list'),
]