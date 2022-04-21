from rest_framework import generics
from rest_framework.response import Response
from restaurants.models import Restaurant
from surfspots.models import Surfspot
from surfspots.serializer import SurfspotSerializer

class ShowListView(generics.ListCreateAPIView):
  queryset = Restaurant.objects.all()
  serializer_class = SurfspotSerializer

class ShowDetailView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Restaurant.objects.all()
  serializer_class = SurfspotSerializer