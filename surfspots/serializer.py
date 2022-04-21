from rest_framework import serializers
from surfspots.models import Surfspot

class SurfspotSerializer(serializers.ModelSerializer):
  class Meta:
    model = Surfspot
    fields = '__all__'

  def create(self, data):
    surfspot = Surfspot(**data) # **data means all data is passed
    
    surfspot.save()
    return surfspot

  def update(self, surfspot, data):
    surfspot.name = data.get('name', surfspot.name)
    surfspot.country = data.get('country', surfspot.country)
    surfspot.address = data.get('address', surfspot.address)
    surfspot.postcode = data.get('postcode', surfspot.postcode)
    surfspot.image = data.get('image', surfspot.image)
    surfspot.magic_seaweed_link = data.get('magic_seaweed_link', surfspot.magic_seaweed_link)

    surfspot.save()
    return surfspot