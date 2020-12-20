# Generated by Django 3.1.4 on 2020-12-17 13:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hotel', '0002_auto_20201217_0938'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='account',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
