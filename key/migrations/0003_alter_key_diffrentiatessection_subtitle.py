
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('key', '0002_key_diffrentiatessection_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='key_diffrentiatessection',
            name='subtitle',
            field=models.TextField(),
        ),
    ]
