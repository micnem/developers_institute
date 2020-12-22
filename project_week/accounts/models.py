from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from trading_post.models import Driver, Card
import random
# Create your models here.
class Player(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    account = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    def deal_cards(self):
        drivers_list = Driver.objects.all()
        weights = [i/100 for i in range(1, drivers_list.count()+1)]
        
        drivers = random.choices(drivers_list, weights, k=10)

        for driver in drivers:
            c = Card.objects.create(driver=driver, owner=self.account)
            
            c.save()


@receiver(post_save, sender=User)
def create_profile(sender, created, instance, **kwargs):
    if created:
        profile = Player.objects.create(account=instance)

        profile.deal_cards()



