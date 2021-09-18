import os
os.environ.setdefault ("DJANGO_SETTINGS_MODULE", "ProTwo.settings")

import django
django.setup()

import random
from  appTwo.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range (N):
        #create the fake data for that entry
        fake_first = fakegen.first_name()
        fake_last = fakegen.last_name()
        fake_email = fakegen.email()

        #create the new Webpage entry
        usr = User.objects.get_or_create(first_name = fake_first, last_name = fake_last, email = fake_email)[0]

if __name__ == "__main__":
    print ("populating script!")
    populate (5)
    print ("populating complete gonorreas!")
