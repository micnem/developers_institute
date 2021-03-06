# Generated by Django 3.1.3 on 2020-12-30 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('splat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='account',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='username',
        ),
        migrations.AddField(
            model_name='profile',
            name='access_token',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='expires_in',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='refresh_token',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='token_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]
