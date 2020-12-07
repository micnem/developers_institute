# Generated by Django 3.1.3 on 2020-12-07 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family_id', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='animal',
            name='family',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.family'),
        ),
    ]
