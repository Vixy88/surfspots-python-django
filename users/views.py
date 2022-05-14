from rest_framework import generics
from rest_framework.permissions import AllowAny
from backend.permissions import IsSelf

from users.models import SurfSpotsUser

from users.serializers import RegisterSerializer, UserSerializer


class RegisterView(generics.CreateAPIView):
    """
    CreateAPIView ensures only a create operation is possible
    """
    permission_classes = [AllowAny]
    queryset = SurfSpotsUser.objects.all()
    serializer_class = RegisterSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsSelf]
    queryset = SurfSpotsUser.objects.all()
    serializer_class = UserSerializer