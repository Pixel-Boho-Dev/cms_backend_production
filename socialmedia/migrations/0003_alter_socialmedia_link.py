# Generated by Django 4.2.4 on 2024-03-09 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialmedia', '0002_homehighlights_delete_highlight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmedia',
            name='link',
            field=models.URLField(max_length=1000),
        ),
    ]
