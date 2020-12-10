import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bike_store.settings')

import django
django.setup()

import random

from rent.models import Customer

from faker import Faker

fake = Faker()


def add_customer():
    c = Customer.objects.get_or_create()



def populate(n=5):
    for entry in range(n):
        full_name = fake.name()
        first_name = full_name.split()[0]
        last_name = full_name.split()[1]
        email = fake.email()
        phone_number = fake.msisdn()
        address = fake.address()
        city = fake.city()
        country = fake.country()

        customer = Customer.objects.get_or_create(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number, address=address, city=city, country=country)


if __name__ == '__main__':
    print('Populating....')
    populate(100)
    print('Finished populating')



