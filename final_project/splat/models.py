from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    account = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    session_id = models.CharField(max_length=500, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    refresh_token = models.CharField(max_length=500)
    access_token = models.CharField(max_length=500)
    expires_in = models.DateTimeField()
    token_type = models.CharField(max_length=500)
    fave_artists = models.ManyToManyField('splat.Artist', through="TopArtist")

class Artist(models.Model):
    name = models.CharField(max_length=100)
    spotify_id = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    popularity = models.IntegerField()
    uri = models.CharField(max_length=100)


class TopArtist(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    affinity = models.IntegerField()


