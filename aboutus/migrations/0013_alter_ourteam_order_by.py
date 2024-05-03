# Generated by Django 4.2.4 on 2024-05-03 12:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0012_ourstorytitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourteam',
            name='order_by',
            field=models.IntegerField(unique=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
