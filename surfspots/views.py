from django.http import JsonResponse
from rest_framework import views, response
from surfspots.models import Surfspot
from surfspots.serializer import SurfspotSerializer

# Create your views here.
class ShowListView(views.APIView):
  def get(self, _request):
    # Gives me all the objects in the database as python objects
    # these python objects are instances of the Porkdishes class
    recipes = Surfspot.objects.all()
    serialized_surfspots = SurfspotSerializer(recipes, many=True)
    return response.Response(serialized_surfspots.data)

