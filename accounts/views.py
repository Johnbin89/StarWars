from accounts.serializers import UserRegisterSerializer
from rest_framework import generics, permissions


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]