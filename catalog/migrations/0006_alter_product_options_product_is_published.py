# Generated by Django 5.0.6 on 2024-05-14 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_product_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'permissions': [('can_change_description', 'Can change description'), ('can_change_category', 'Can change category'), ('set_published_status', 'Can publish product')], 'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
        migrations.AddField(
            model_name='product',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Признак публикации'),
        ),
    ]
