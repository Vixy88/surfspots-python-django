from django.db import models


# Create your models here.

class Restaurant(models.Model):
  """  RESTAURANT MODEL """
  
  name = models.CharField(max_length=100, default=None)
  country = models.CharField(max_length=100, default=None)
  address = models.CharField(max_length=100, default=None)
  city = models.CharField(max_length=100, default=None)
  postcode = models.CharField(max_length=100, default=None)
  image = models.CharField(max_length=250, default=None)
  website = models.CharField(max_length=200, default=None)
  email = models.CharField(max_length=200, default=None)
  google_directions_link = models.CharField(max_length=300, default=None)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    """ Represents the class objects as a string """
    return f'{self.name} | Country: {self.country} | City: {self.city}'

print(Restaurant)
