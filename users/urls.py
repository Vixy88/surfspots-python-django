from django.urls import path

from users.views import RegisterView, UserDetailView

urlpatterns = [

    path('register', RegisterView.as_view()),
    path('<str:pk>/', UserDetailView.as_view())

]