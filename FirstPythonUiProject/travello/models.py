from django.db import models

# Create your models here.

class Destination:
    id : int
    name : str
    description : str
    price : int
    img : str
    offer : bool

#For Django modal we need to use equalsTo(=) instead of colon(:),Because we assign a value
class DestinationWithDb(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to = 'pics')
    offer = models.BooleanField(default = False)
