# Generated by Django 4.2.4 on 2024-04-12 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('key', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='key_diffrentiatesSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='key_diffrentiates',
            name='subtitle',
        ),
        migrations.RemoveField(
            model_name='key_diffrentiates',
            name='title',
        ),
    ]
