from django.urls import path

from . import views
from .views import UnpublishProductView, DeleteProductView, ProductFilter

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='home_view'),
    path('contacts/', views.ContactsTemplateView.as_view(), name='contacts_view'),
    path('products', views.ProductListView.as_view(), name='products'),
    path('products/filter/', ProductFilter.as_view(), name='product_filter'),
    path('products_details/<int:pk>', views.ProductDetailView.as_view(), name='products_details'),
    path('products_create', views.ProductCreateView.as_view(), name='products_create'),
    path('products_update/<int:pk>', views.ProductUpdateView.as_view(), name='products_update'),
    path('products_delete/<int:pk>', views.ProductDeleteView.as_view(), name='products_delete'),
    path('product/<int:pk>/unpublish/', UnpublishProductView.as_view(), name='unpublish_product'),
    path('product/<int:pk>/delete/', DeleteProductView.as_view(), name='delete_product'),

]
