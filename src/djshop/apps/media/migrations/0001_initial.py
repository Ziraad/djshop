# Generated by Django 4.2.4 on 2023-09-24 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=128, null=True)),
                ('image', models.ImageField(height_field='height', upload_to='images/', width_field='width')),
                ('width', models.IntegerField(editable=False)),
                ('height', models.IntegerField(editable=False)),
                ('file_hash', models.CharField(db_index=True, editable=False, max_length=40)),
                ('file_size', models.PositiveIntegerField(editable=False, null=True)),
                ('focal_point_x', models.PositiveIntegerField(blank=True, null=True)),
                ('focal_point_y', models.PositiveIntegerField(blank=True, null=True)),
                ('focal_point_width', models.PositiveIntegerField(blank=True, null=True)),
                ('focal_point_height', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
    ]
