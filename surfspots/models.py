from django.db import models

# Create your models here.

class Surfspot(models.Model):
  """  SURFSPOT MODEL """
  
  name = models.CharField(max_length=100)
  country = models.CharField(max_length=100)
  address = models.CharField(max_length=100)
  postcode = models.CharField(max_length=100)
  created = models.DateTimeField(auto_now_add=True)
