# Generated by Django 5.1.4 on 2025-01-30 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_product_is_public'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name'], 'permissions': [('can_unpublish_product', 'Сan unpublish product')], 'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
    ]
