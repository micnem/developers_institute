# Generated by Django 3.1.3 on 2020-12-07 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0004_auto_20201207_1313'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='family_id',
            new_name='family',
        ),
    ]
