from rest_framework import serializers
from surfspots.models import Surfspot

class SurfspotSerializer(serializers.ModelSerializer):
  class Meta:
    model = Surfspot
    fields = '__all__'