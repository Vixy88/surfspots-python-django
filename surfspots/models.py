from django.db import models

from restaurants.models import Restaurant

# Create your models here.

class Surfspot(models.Model):
  """  SURFSPOT MODEL """
  
  name = models.CharField(max_length=100, default=None)
  country = models.CharField(max_length=100, default=None)
  address = models.CharField(max_length=100, default=None)
  city = models.CharField(max_length=100, null=True, blank=True)
  postcode = models.CharField(max_length=100, default=None)
  latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, default='0')
  longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, default='0')
  image = models.CharField(max_length=250, default=None)
  magic_seaweed_link = models.CharField(max_length=250, default=None)
  google_directions_link = models.CharField(max_length=300, default=None, null=True, blank=True)
  restaurants_nearby = models.ManyToManyField(Restaurant, blank=True, related_name="surfspots_nearby")
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    """ Represents the class objects as a string """
    return f'{self.name} | Country: {self.country} | City: {self.city}'

print(Surfspot)
