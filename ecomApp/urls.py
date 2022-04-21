from django.urls import path
from ecomApp import views

urlpatterns = [
    path('add_category',views.add_category,name='add_category'),
    path('add_brand',views.add_brand,name='add_brand'),
    path('add_product',views.add_product,name='add_product'),
    path('add_multiple',views.add_multiple,name='add_multiple'),
    path('edit_brand/<int:pk>',views.edit_brand,name='edit_brand'),
    path('edit_category/<int:pk>',views.edit_category,name='edit_category'),
    path('edit_product/<int:pk>',views.edit_product,name='edit_product'),
    path('delete_brand/<int:pk>',views.delete_brand,name='delete_brand'),
    path('delete_category/<int:pk>',views.delete_category,name='delete_category'),
    path('delete_product/<int:pk>',views.delete_product,name='delete_product'),
    path('show_category',views.show_category,name='show_category'),
    path('show_brand',views.show_brand,name='show_brand'),
    path('product_table',views.product_table,name='product_table'),
    path('show_product/<int:pk>',views.show_product,name='show_product'),
    path('show_all',views.show_all,name='show_all'),
    path('brand_product',views.brand_product,name='brand_product'),
    path('category_product',views.category_product,name='category_product'),
    path('product_details/<int:pk>',views.product_details,name='product_details'),
    path('sign_up',views.sign_up,name='sign_up'),
    path('log_in',views.log_in,name='log_in'),
    path('log_out',views.log_out,name='log_out'),
    path('home',views.home,name='home'),
    path('cart/<int:pk>',views.cart,name='cart'),
    path('show_cart',views.show_cart,name='show_cart'),
]