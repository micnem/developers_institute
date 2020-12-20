import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'film_project.settings')

import django
django.setup()

import random

from film_app.models import Director

from faker import Faker

fake = Faker()




def populate(n=5):
    for entry in range(n):
        full_name = fake.name()
        first_name = full_name.split()[0]
        last_name = full_name.split()[1]


        director = Director.objects.get_or_create(first_name=first_name, last_name=last_name)


if __name__ == '__main__':
    print('Populating....')
    populate(100)
    print('Finished populating')



