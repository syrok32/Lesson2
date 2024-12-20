from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='home_view'),
    path('contacts/', views.ContactsTemplateView.as_view(), name='contacts_view'),
    path('products', views.ProductListView.as_view(), name='products'),
    path('products_details/<int:pk>', views.ProductDetailView.as_view(), name='products_details')
]
