from django.http import JsonResponse

# Create your views here.
def get_surfspots(request):
  print("Here is the request", request)
  return JsonResponse({"name": "Burgau", "Country": "Portugal"})

