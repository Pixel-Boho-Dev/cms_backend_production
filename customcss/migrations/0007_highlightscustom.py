# Generated by Django 4.2.4 on 2024-05-24 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customcss', '0006_merge_0004_footercustom_0005_acheievementcustom'),
    ]

    operations = [
        migrations.CreateModel(
            name='HighlightsCustom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
    ]
