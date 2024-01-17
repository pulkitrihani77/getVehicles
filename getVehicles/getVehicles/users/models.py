from django.db import models

# Create your models here.

class contactModel(models.Model):

    def __str__(self):
        return self.first_name + " " + self.last_name
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    feedback = models.CharField(max_length=500)