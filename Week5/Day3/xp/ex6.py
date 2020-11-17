from faker import Faker
fake = Faker()

users = []

def gen(list_name):
    user = {
        "name": fake.name(),
        "address": fake.address()
    }
    users.append(user)