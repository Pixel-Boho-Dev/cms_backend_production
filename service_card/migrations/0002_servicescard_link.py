# Generated by Django 4.2.4 on 2024-07-03 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_card', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicescard',
            name='link',
            field=models.URLField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
