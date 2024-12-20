from django.db import models

class Blog(models.Model):
    headline = models.CharField(max_length=25, verbose_name='название')
    contents = models.CharField(max_length=200, verbose_name='описание')
    image = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name='фото')
    created_at = models.DateField(auto_now_add=True, verbose_name= 'дата')
    verified = models.BooleanField(default=False, verbose_name='валид')
    count = models.IntegerField(verbose_name='просмотры', default=0)

    def __str__(self):
        return self.headline

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = ('блоги')


