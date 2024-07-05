# Generated by Django 4.2.4 on 2024-07-05 07:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('industry_cards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='industrycard',
            name='order_by',
            field=models.IntegerField(default=1, unique=True, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
    ]
