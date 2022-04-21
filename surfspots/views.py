from rest_framework import generics
from rest_framework.response import Response
from surfspots.models import Surfspot
from surfspots.serializer import SurfspotSerializer

# Create your views here.
# class ShowListView(APIView):
#   def get(self, _request):
#     surfspots = Surfspot.objects.all()
#     serialized_surfspots = SurfspotSerializer(surfspots, many=True)
#     return Response(serialized_surfspots.data)

class ShowListView(generics.ListCreateAPIView):
  queryset = Surfspot.objects.all()
  serializer_class = SurfspotSerializer

class ShowDetailView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Surfspot.objects.all()
  serializer_class = SurfspotSerializer
