from rest_framework.serializers import ModelSerializer , CharField , ValidationError

from .models import CustomUser

class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["username" , "email" , "phone" , "address" , "password" , "conform_password"]
        
        