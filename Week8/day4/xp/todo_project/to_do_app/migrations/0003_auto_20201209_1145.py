# Generated by Django 3.1.4 on 2020-12-09 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_app', '0002_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date_creation',
            field=models.DateField(auto_now_add=True),
        ),
    ]
