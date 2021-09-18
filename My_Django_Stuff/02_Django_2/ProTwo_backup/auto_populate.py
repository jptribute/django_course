import os
os.environ.setdefault ("Modulo de django config", "ProTwo.settings")

import django
django.setup()

import random
from  appTwo.models import User
import faker as Faker
fakegen = Faker()
