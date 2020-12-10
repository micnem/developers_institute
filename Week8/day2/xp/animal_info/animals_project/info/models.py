from django.db import models 

class Animal(models.Model):
    legs = models.IntegerField()
    weight = models.IntegerField()
    speed = models.IntegerField()
    image = models.ImageField(upload_to='upload/')
    family = models.ForeignKey(
        'Family',
        on_delete=models.CASCADE,
    )

class Family(models.Model):
    name =  models.CharField(max_length=50)