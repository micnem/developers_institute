# Generated by Django 3.1.4 on 2020-12-10 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0002_auto_20201210_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='rented',
            field=models.BooleanField(default=False),
        ),
    ]
