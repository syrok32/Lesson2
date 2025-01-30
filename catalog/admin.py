from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

    search_fields = ('name', 'description',)

@admin.register(Product)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description')

class AuthorAdmin(admin.ModelAdmin):
    pass


# Register your models here.
