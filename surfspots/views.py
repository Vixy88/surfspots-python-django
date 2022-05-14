from rest_framework import generics
from surfspots.models import Surfspot
from surfspots.serializer import SurfspotSerializer
from backend.permissions import IsCreator
class ShowListView(generics.ListCreateAPIView):
  queryset = Surfspot.objects.all()
  serializer_class = SurfspotSerializer

class ShowDetailView(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = [IsCreator]
  queryset = Surfspot.objects.all()
  serializer_class = SurfspotSerializer
