from django.urls import path
from surfspots.views import ShowListView
from . import views

urlpatterns = [
  path('', ShowListView.as_view())
]