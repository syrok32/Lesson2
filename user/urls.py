from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import RegisterView

app_name = 'user'
urlpatterns = [
    path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('register/',  RegisterView.as_view(template_name='user/register.html'), name='register')

]
