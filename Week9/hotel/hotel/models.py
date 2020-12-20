from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    account = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    
class RoomType(models.Model):
    ROOM_SIZES = (
        ('S', 'Single'),
        ('D', 'Double'),
        ('X', 'Suite')
    )
    ROOM_PRICES = (
        ('A', 50.00),
        ('B', 100.00),
        ('C', 200.00)
    )
    size = models.CharField(max_length=1, choices=ROOM_SIZES)
    price_per_night = models.CharField(max_length=1, choices=ROOM_PRICES)

    def __str__(self):
        return self.size
    

class Room(models.Model):
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)
    

class Booking(models.Model):
    room_number = models.ForeignKey(Room, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField(blank=True, null=True)


class Review(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, unique=False)