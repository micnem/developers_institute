# Generated by Django 3.1.3 on 2020-12-31 13:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('splat', '0007_auto_20201231_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='account',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
