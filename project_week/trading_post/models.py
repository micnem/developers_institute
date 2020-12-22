from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Driver(models.Model):
    name = models.CharField(unique=True, max_length=200)
    position = models.IntegerField(null=True)
    points = models.IntegerField(null=True)
    nationality = models.CharField(max_length=200)
    team = models.ForeignKey('Team', on_delete=models.CASCADE)
    f1_id = models.IntegerField(null=True)
    image = models.ImageField(default='default_pic.jpg')
    
    def __str__(self):
        return f'{self.name}'
class Team(models.Model):
    name = models.CharField(max_length=200)
    f1_id = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.name}'

class Card(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.driver}'