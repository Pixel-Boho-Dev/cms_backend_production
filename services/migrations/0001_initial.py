# Generated by Django 4.2.4 on 2024-07-06 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('socialmedia', '0004_alter_achievement_order_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetaTagsservices',
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
                ('og_image', models.ImageField(blank=True, null=True, upload_to='meta_tags_services/')),
                ('og_description', models.CharField(blank=True, max_length=150, null=True)),
                ('og_site_name', models.CharField(blank=True, max_length=150, null=True)),
                ('og_locale', models.CharField(blank=True, max_length=150, null=True)),
                ('twitter_card', models.CharField(blank=True, max_length=150, null=True)),
                ('twitter_site', models.CharField(blank=True, max_length=150, null=True)),
                ('twitter_title', models.CharField(blank=True, max_length=150, null=True)),
                ('twitter_description', models.CharField(blank=True, max_length=150, null=True)),
                ('twitter_image', models.ImageField(blank=True, null=True, upload_to='meta_tags_services/')),
                ('twitter_image_alt', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SpecializedService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='specializedservice_images/')),
                ('alt_img_text', models.TextField(blank=True, max_length=300, null=True)),
                ('alt_img_title', models.TextField(blank=True, max_length=300, null=True)),
                ('alt_img_Caption', models.TextField(blank=True, max_length=300, null=True)),
                ('alt_img_description', models.TextField(blank=True, max_length=300, null=True)),
                ('link', models.URLField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='SpecializedSubService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_title', models.TextField()),
                ('header_image', models.ImageField(upload_to='specializedsubservice-header_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Subheading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subheading', models.CharField(max_length=200)),
                ('related_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socialmedia.service')),
            ],
        ),
        migrations.CreateModel(
            name='SubService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='subservice_images/')),
                ('sub_title', models.CharField(max_length=200)),
                ('alt_img_text', models.TextField(blank=True, max_length=300, null=True)),
                ('alt_img_title', models.TextField(blank=True, max_length=300, null=True)),
                ('alt_img_Caption', models.TextField(blank=True, max_length=300, null=True)),
                ('alt_img_description', models.TextField(blank=True, max_length=300, null=True)),
                ('related_heading', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.subheading')),
            ],
        ),
    ]
