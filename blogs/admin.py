from django.contrib import admin

from blogs.models import Blog


# Register your models here.
@admin.register(Blog)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('headline', 'contents', 'created_at', 'count',)
    search_fields = ('name', 'description',)
