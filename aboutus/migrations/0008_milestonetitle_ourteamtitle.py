# Generated by Django 4.2.4 on 2024-04-22 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0007_certificatetitle_remove_certifications_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='MilestoneTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='OurTeamTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
    ]
