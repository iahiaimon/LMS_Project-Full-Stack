from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated , AllowAny , IsAdminUser

from .serializers import CourseSerializer
from .models import Course

# Create your views here.

class CourseView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        courses = Course.objects.all()
        serializers = CourseSerializer(courses , many = True).data
        return Response(serializers)
    
    def post(self , request):
        serializers = CourseSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data , status= status.HTTP_201_CREATED)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    