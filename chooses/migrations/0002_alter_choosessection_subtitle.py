# Generated by Django 4.2.4 on 2024-05-16 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chooses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choosessection',
            name='subtitle',
            field=models.TextField(),
        ),
    ]
