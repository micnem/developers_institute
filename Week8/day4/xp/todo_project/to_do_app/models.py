from django.db import models

# Create your models here.

class Category(models.Model):
    WORK = 'Work'
    HOME = 'Home'
    STUDIES = 'Studies'
    SOCIAL = 'Social'
    SHOPPING = 'Shopping'

    CATEGORY_CHOICES= [
        (WORK, 'Work'),
        (HOME, 'Home'),
        (STUDIES, 'Studies'),
        (SOCIAL, 'Social'),
        (SHOPPING, 'Shopping'),
    ]

    name = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default=WORK)
    image = models.URLField(null=True)

    def __str__(self):
        return self.name

class Todo(models.Model):
    title = models.CharField(max_length=100)
    details= models.TextField(max_length=300)
    has_been_done= models.BooleanField(default=False)
    date_creation = models.DateField(auto_now_add=True)
    date_completion = models.DateField(null=True, blank = True)
    deadline_date= models.DateField(null=True, blank = True)
    category = models.ManyToManyField(Category)

