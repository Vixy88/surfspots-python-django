from rest_framework import serializers
from restaurants.models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):
  surfspots_nearby = serializers.SlugRelatedField(slug_field="city")
  class Meta:
    model = Restaurant
    fields = '__all__'

  def create(self, data):
    restaurant = Restaurant(**data) # **data means all data is passed
    
    restaurant.save()
    return restaurant

  def update(self, restaurant, data):
    restaurant.name = data.get('name', restaurant.name)
    restaurant.country = data.get('country', restaurant.country)
    restaurant.address = data.get('address', restaurant.address)
    restaurant.city = data.get('city', restaurant.address)
    restaurant.postcode = data.get('postcode', restaurant.postcode)
    restaurant.image = data.get('image', restaurant.image)
    restaurant.website = data.get('website', restaurant.website)
    restaurant.google_directions_link = data.get('google_directions_link', restaurant.google_directions_link)

    restaurant.save()
    return restaurant