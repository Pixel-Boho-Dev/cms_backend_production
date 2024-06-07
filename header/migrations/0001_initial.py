# Generated by Django 4.2.4 on 2024-06-05 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeHeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='header_images/')),
                ('url', models.URLField()),
                ('alt_img_text', models.TextField(blank=True, max_length=300, null=True)),
                ('alt_img_title', models.TextField(blank=True, max_length=300, null=True)),
                ('alt_img_Caption', models.TextField(blank=True, max_length=300, null=True)),
                ('alt_img_description', models.TextField(blank=True, max_length=300, null=True)),
                ('slug', models.CharField(blank=True, max_length=200, null=True, unique=True)),
            ],
        ),
    ]