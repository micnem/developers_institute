# Generated by Django 3.1.4 on 2020-12-10 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0007_auto_20201210_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(default='default@default.com', max_length=254, unique=True),
            preserve_default=False,
        ),
    ]