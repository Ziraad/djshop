# Generated by Django 4.2.4 on 2023-10-20 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_product_created_at_product_created_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(related_name='categories', to='catalog.category'),
        ),
    ]
