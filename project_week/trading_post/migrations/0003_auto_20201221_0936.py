# Generated by Django 3.1.4 on 2020-12-21 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trading_post', '0002_auto_20201221_0830'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='points',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='position',
            field=models.IntegerField(null=True),
        ),
    ]