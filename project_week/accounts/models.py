from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Player(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    account = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    