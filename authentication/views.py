from django.http.response import Http404
from django.http import JsonResponse
from rest_framework import permissions
from rest_framework import generics,mixins
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import (
    LoginSerializer, RegisterSerializer, UserSerializer, TokenSerializer)
from django.contrib.auth.models import User
from rest_framework.views import APIView




def create_auth_token(user):
    token1,_= Token.objects.get_or_create(user=user)
    serializer=TokenSerializer(token1)
    return Response(serializer.data)
   

class LoginView(generics.GenericAPIView):
    """
    TODO:
    Implement login functionality, taking username and password
    as input, and returning the Token.
    """
    pass


class RegisterView(APIView):

    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            x=request.data['username']
            y=User.objects.filter(username=x)
            z=create_auth_token(y[0])
            return Response(z)
            '''serializer.save()
            x=request.data['username']
            y=User.objects.filter(username=x)
            z=create_auth_token(y)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)'''






      

    


class UserProfileView(generics.RetrieveAPIView):
    """
    TODO:
    Implement the functionality to retrieve the details
    of the logged in user.
    """
    pass