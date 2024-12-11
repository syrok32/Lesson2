from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home_view, name='home_view'),
    path('contacts/', views.contacts_view, name='contacts_view'),
    path('products', views.product_list, name='products'),
    path('products_details/<int:product_id>', views.detail_products, name='products_details')
]
