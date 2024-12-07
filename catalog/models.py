from django.db import models


# Create your models here.




class Category(models.Model):
    name = models.CharField(max_length=25, verbose_name='название категории')
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = ('категории')
        ordering = ['name']


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='имя')
    description = models.CharField(max_length=200, verbose_name='описание')
    image = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name='фото')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='ПРОДУКТЫ')
    price = models.IntegerField(verbose_name='цена')
    created_at = models.DateField()
    updated_at = models.DateField()

    def __str__(self):
        return f'{self.name}{self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['name']
