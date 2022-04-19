from django.http import JsonResponse
from rest_framework import views, response
from surfspots.models import Surfspot
from surfspots.serializer import SurfspotSerializer

# Create your views here.
class ShowListView(views.APIView):
  def get(self, _request):
    # Gives me all the objects in the database as python objects
    # these python objects are instances of the Porkdishes class
    surfspots = Surfspot.objects.all()
    serialized_surfspots = SurfspotSerializer(surfspots, many=True)
    return response.Response(serialized_surfspots.data)


class ShowDetailView(views.APIView):
  def get(self, _request, pk):
    surfspot = Surfspot.objects.get(id=pk)
    serialized_surfspot = SurfspotSerializer(surfspot, many=False)
    return response.Response(serialized_surfspot.data)

