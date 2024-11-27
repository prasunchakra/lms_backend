from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from api import serializer as api_serializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from userauths.models import User

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = api_serializer.MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = api_serializer.RegisterSerializer

