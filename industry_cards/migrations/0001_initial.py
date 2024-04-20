

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IndustryCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=100)),
                ('image', models.ImageField(upload_to='industry_images/')),
                ('alt_img_text', models.TextField(blank=True, max_length=300, null=True)),
                ('alt_img_title', models.TextField(blank=True, max_length=300, null=True)),
                ('alt_img_caption', models.TextField(blank=True, max_length=300, null=True)),
                ('alt_img_description', models.TextField(blank=True, max_length=300, null=True)),
            ],
        ),

        migrations.CreateModel(
            name='IndustryTitles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),

