# Generated by Django 4.2.4 on 2024-06-26 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specializedsubservice',
            name='alt_img_Caption',
        ),
        migrations.RemoveField(
            model_name='specializedsubservice',
            name='alt_img_description',
        ),
        migrations.RemoveField(
            model_name='specializedsubservice',
            name='alt_img_text',
        ),
        migrations.RemoveField(
            model_name='specializedsubservice',
            name='alt_img_title',
        ),
        migrations.RemoveField(
            model_name='specializedsubservice',
            name='description',
        ),
        migrations.RemoveField(
            model_name='specializedsubservice',
            name='image',
        ),
        migrations.RemoveField(
            model_name='specializedsubservice',
            name='title',
        ),
        migrations.AddField(
            model_name='specializedsubservice',
            name='header_image',
            field=models.ImageField(default=0, upload_to='specializedsubservice-header_images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specializedsubservice',
            name='header_title',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='specializedservice',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='specializedservice',
            name='title',
            field=models.TextField(),
        ),
    ]