# Generated by Django 5.0.1 on 2024-03-14 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('footer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footer',
            name='icon',
            field=models.ImageField(upload_to='AppFooter/'),
        ),
    ]
