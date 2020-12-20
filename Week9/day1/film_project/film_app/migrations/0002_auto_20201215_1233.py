# Generated by Django 3.1.4 on 2020-12-15 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('film_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='created_in_country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='film_app.country'),
        ),
    ]
