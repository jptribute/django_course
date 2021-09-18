from django.db import models

# Create your models here.
class User (models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return self
