from django.shortcuts import render
from django.http import HttpResponse

from .models import CustomUser
from .serializers import UserSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions

# Create your views here.

class UserView(APIView):
    def get(self , request):
        user = CustomUser.objects.all()
        serializers = UserSerializer( user , many = True ).data
        return Response(serializers)
    
    def post(self , request):
        serializers = UserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data , status=status.HTTP_201_CREATED)
        
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
