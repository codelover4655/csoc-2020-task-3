from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class TokenSerializer(serializers.Serializer):
    token=serializers.CharField(max_length=200)
   
    


class LoginSerializer(serializers.Serializer):
    # TODO: Implement login functionality
    pass


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username', 'password','first_name','email']

  


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username', 'password','first_name','email']

  

    
    