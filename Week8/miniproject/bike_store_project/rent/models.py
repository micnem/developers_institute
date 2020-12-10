from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(null= False, unique=True)
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    def __str__(self):
        return self.first_name

class Vehicle(models.Model):
    vehicle_type = models.ForeignKey(
        'VehicleType',
        on_delete=models.CASCADE, 
    )
    date_created = models.DateField(auto_now_add=True)
    real_cost = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.ForeignKey(
        'VehicleSize',
        on_delete=models.CASCADE, 
    )
    def __str__(self):
        return f"Vehicle: {self.id}, type: {self.vehicle_type.name}"


class VehicleType(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class VehicleSize(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class RentalRate(models.Model):
    daily_rate = models.DecimalField(max_digits=6, decimal_places=2)
    vehicle_type = models.ForeignKey(
        'VehicleType',
        on_delete=models.CASCADE,
    )
    vehicle_size = models.ForeignKey(
        'VehicleSize',
        on_delete=models.CASCADE,
    )


class Rental(models.Model):
    rental_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(blank=True, null=True)
    customer = models.ForeignKey(
        'Customer',
        on_delete=models.CASCADE,
    )
    vehicle = models.ForeignKey(
        'Vehicle',
        on_delete=models.CASCADE,
    )
    def rate(self):
        rr = RentalRate.objects.get(vehicle_type=self.vehicle.vehicle_type, vehicle_size = self.vehicle.size)
        if self.return_date:
            td = self.return_date - self.rental_date
            return rr.daily_rate  * td.days
        return
       


