from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField


class CustomUser(AbstractUser):
    username = models.CharField(null=False)
    email = models.EmailField(unique=True, blank=True)
    avatar = models.ImageField(null=True, upload_to='avatars/', blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    country = CountryField(blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'


    def __str__(self):
        return self.email