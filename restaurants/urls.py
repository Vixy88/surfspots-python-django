from django.urls import path
from restaurants.views import ShowListView, ShowDetailView
from . import views

urlpatterns = [
  path('', ShowListView.as_view()),
  path('<str:pk>/', ShowDetailView.as_view())
]