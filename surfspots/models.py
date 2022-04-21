from django.db import models

# Create your models here.

class Surfspot(models.Model):
  """  SURFSPOT MODEL """
  
  name = models.CharField(max_length=100, default=None)
  country = models.CharField(max_length=100, default=None)
  address = models.CharField(max_length=100, default=None)
  postcode = models.CharField(max_length=100, default=None)
  image = models.CharField(max_length=250, default=None)
  magic_seaweed_link = models.CharField(max_length=250, default=None)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    """ Represents the class objects as a string """
    return f'{self.name} | Country: {self.country}'

print(Surfspot)
