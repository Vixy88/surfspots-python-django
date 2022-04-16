from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def get_surfspots(request):
  return JsonResponse({"name": "Burgau", "Country": "Portugal"})

