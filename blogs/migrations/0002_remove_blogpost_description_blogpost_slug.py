# Generated by Django 4.2.4 on 2024-06-26 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='description',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='slug',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]
