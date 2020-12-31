# Generated by Django 3.1.3 on 2020-12-29 17:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('spotify_id', models.CharField(max_length=100)),
                ('images', models.ImageField(upload_to='')),
                ('popularity', models.IntegerField()),
                ('uri', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TopArtist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('affinity', models.IntegerField()),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='splat.artist')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='splat.profile')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='fave_artists',
            field=models.ManyToManyField(through='splat.TopArtist', to='splat.Artist'),
        ),
    ]