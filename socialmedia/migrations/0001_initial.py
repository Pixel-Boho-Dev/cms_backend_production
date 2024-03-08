# Generated by Django 4.2.4 on 2024-02-06 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achievements_icon', models.ImageField(upload_to='achievements_icons/')),
                ('alt_img_text', models.TextField(blank=True, max_length=300, null=True)),
                ('alt_img_title', models.TextField(blank=True, max_length=300, null=True)),
                ('alt_img_Caption', models.TextField(blank=True, max_length=300, null=True)),
                ('alt_img_description', models.TextField(blank=True, max_length=300, null=True)),
                ('achievements_title', models.CharField(max_length=100)),
                ('achievements_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Highlight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('highlights_title', models.CharField(max_length=100)),
                ('highlights_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_main_title', models.CharField(max_length=100)),
                ('service_main_description', models.TextField()),
                ('features_main_title', models.CharField(max_length=100)),
                ('features_main_description', models.TextField()),
                ('highlights_main_title', models.CharField(max_length=100)),
                ('highlights_main_description', models.TextField()),
                ('industries_main_title', models.CharField(max_length=100)),
                ('industries_main_description', models.TextField()),
                ('markets_main_title', models.CharField(max_length=100)),
                ('markets_main_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('industry_image', models.ImageField(upload_to='industry_images/')),
                ('alt_img_text', models.TextField(blank=True, max_length=300, null=True)),
                ('alt_img_title', models.TextField(blank=True, max_length=300, null=True)),
                ('alt_img_Caption', models.TextField(blank=True, max_length=300, null=True)),
                ('alt_img_description', models.TextField(blank=True, max_length=300, null=True)),
                ('industry_title', models.CharField(max_length=100)),
                ('industry_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_url', models.URLField()),
                ('place_name', models.CharField(max_length=100)),
                ('phone_number1', models.CharField(max_length=20)),
                ('phone_number2', models.CharField(blank=True, max_length=20, null=True)),
                ('description', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('market_image', models.ImageField(upload_to='market_images/')),
                ('alt_img_text', models.TextField(blank=True, max_length=300, null=True)),
                ('alt_img_title', models.TextField(blank=True, max_length=300, null=True)),
                ('alt_img_Caption', models.TextField(blank=True, max_length=300, null=True)),
                ('alt_img_description', models.TextField(blank=True, max_length=300, null=True)),
                ('market_title', models.CharField(max_length=100)),
                ('market_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MetaTagsHome',
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
                ('og_image', models.ImageField(blank=True, null=True, upload_to='meta_tags_home/')),
                ('og_description', models.CharField(blank=True, max_length=150, null=True)),
                ('og_site_name', models.CharField(blank=True, max_length=150, null=True)),
                ('og_locale', models.CharField(blank=True, max_length=150, null=True)),
                ('twitter_card', models.CharField(blank=True, max_length=150, null=True)),
                ('twitter_site', models.CharField(blank=True, max_length=150, null=True)),
                ('twitter_title', models.CharField(blank=True, max_length=150, null=True)),
                ('twitter_description', models.CharField(blank=True, max_length=150, null=True)),
                ('twitter_image', models.ImageField(blank=True, null=True, upload_to='meta_tags_home/')),
                ('twitter_image_alt', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='service_icons/')),
                ('alt_img_text', models.TextField(blank=True, max_length=300, null=True)),
                ('alt_img_title', models.TextField(blank=True, max_length=300, null=True)),
                ('alt_img_Caption', models.TextField(blank=True, max_length=300, null=True)),
                ('alt_img_description', models.TextField(blank=True, max_length=300, null=True)),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('link', models.URLField()),
                ('icon', models.ImageField(upload_to='socialmedia_icons/')),
                ('alt_img_text', models.TextField(blank=True, max_length=300, null=True)),
                ('alt_img_title', models.TextField(blank=True, max_length=300, null=True)),
                ('alt_img_Caption', models.TextField(blank=True, max_length=300, null=True)),
                ('alt_img_description', models.TextField(blank=True, max_length=300, null=True)),
            ],
        ),
    ]
