from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Film(models.Model):
    title = models.CharField(max_length=50)
    release_date = models.DateField(default='2020-12-13')
    created_in_country = models.ForeignKey(
        'Country',
        on_delete=models.PROTECT
    )
    available_in_countries = models.ManyToManyField(Country, related_name='film_available_in')
    director = models.ManyToManyField(Director)

