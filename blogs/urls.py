from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    path('blog/create/', views.BlogCreateView.as_view(), name='blog_create'),
    path('blog/update/<int:pk>', views.BlogUpdateView.as_view(), name='blog_update'),
    path('blog/delete/<int:pk>', views.BlogDeletelView.as_view(), name='blog_del'),
    path('blog/ditail/<int:pk>', views.BloglDetailView.as_view(), name='blog_det'),
    path('blog/list', views.BloglListView.as_view(), name='blog_list'),]

