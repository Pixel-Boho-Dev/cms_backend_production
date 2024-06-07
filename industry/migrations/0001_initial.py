# Generated by Django 4.2.4 on 2024-06-05 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IndustriesPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='industries_page-images/')),
                ('alt_img_text', models.TextField(blank=True, max_length=300, null=True)),
                ('alt_img_title', models.TextField(blank=True, max_length=300, null=True)),
                ('alt_img_Caption', models.TextField(blank=True, max_length=300, null=True)),
                ('alt_img_description', models.TextField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MetaTagsIndustries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charset', models.CharField(blank=True, max_length=150, null=True)),
                ('viewport', models.CharField(blank=True, max_length=150, null=True)),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('description', models.CharField(blank=True, max_length=150, null=True)),
                ('keywords', models.CharField(blank=True, max_length=150, null=True)),
                ('author', models.CharField(blank=True, max_length=150, null=True)),
                ('robots', models.CharField(blank=True, max_length=150, null=True)),
                ('copyright', models.CharField(blank=True, max_length=150, null=True)),
                ('referrer', models.CharField(blank=True, max_length=150, null=True)),
                ('og_title', models.CharField(blank=True, max_length=150, null=True)),
                ('og_type', models.CharField(blank=True, max_length=150, null=True)),
                ('og_url', models.CharField(blank=True, max_length=150, null=True)),
                ('og_image', models.ImageField(blank=True, null=True, upload_to='meta_tags_industries/')),
                ('og_description', models.CharField(blank=True, max_length=150, null=True)),
                ('og_site_name', models.CharField(blank=True, max_length=150, null=True)),
                ('og_locale', models.CharField(blank=True, max_length=150, null=True)),
                ('twitter_card', models.CharField(blank=True, max_length=150, null=True)),
                ('twitter_site', models.CharField(blank=True, max_length=150, null=True)),
                ('twitter_title', models.CharField(blank=True, max_length=150, null=True)),
                ('twitter_description', models.CharField(blank=True, max_length=150, null=True)),
                ('twitter_image', models.ImageField(blank=True, null=True, upload_to='meta_tags_industries/')),
                ('twitter_image_alt', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
    ]