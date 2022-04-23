from rest_framework import generics
from rest_framework.response import Response
from restaurants.models import Restaurant
from restaurants.serializer import RestaurantSerializer

class ShowListView(generics.ListCreateAPIView):
  queryset = Restaurant.objects.all()
  serializer_class = RestaurantSerializer

class ShowDetailView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Restaurant.objects.all()
  serializer_class = RestaurantSerializer