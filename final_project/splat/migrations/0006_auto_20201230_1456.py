# Generated by Django 3.1.3 on 2020-12-30 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('splat', '0005_auto_20201230_1329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='images',
        ),
        migrations.AddField(
            model_name='artist',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]