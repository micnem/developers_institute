# Generated by Django 3.1.3 on 2020-12-07 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_remove_family_family_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='family',
            new_name='family_id',
        ),
    ]