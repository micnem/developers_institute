# Generated by Django 3.1.3 on 2020-12-30 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('splat', '0003_auto_20201230_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='access_token',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='refresh_token',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='token_type',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
