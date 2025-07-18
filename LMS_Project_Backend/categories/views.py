from django.shortcuts import render, redirect
from .models import Category
from .serializers import CategorySerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions

# Create your views here.

class CategoryView(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        categories = Category.objects.all()
        serializers = CategorySerializer(categories , many = True).data
        return Response(serializers)
    
    def post(self , request) :
        serializers = CategorySerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data , status = status.HTTP_201_CREATED)
        
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)