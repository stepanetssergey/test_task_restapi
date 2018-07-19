from django.shortcuts import render
from rest_framework.views import APIView

from rest_framework import viewsets
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from . import models
from . import serializers


class UserAPIView(viewsets.ModelViewSet):
    
    serializer_class = serializers.UserAPISerializer
    queryset = models.UserAPI.objects.all()


class LoginViewSet(viewsets.ViewSet):
    
    """Get token from name and password post"""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        return ObtainAuthToken().post(request)
        
