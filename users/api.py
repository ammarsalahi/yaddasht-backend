from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.serializers import UserLoginSerializer, UserSerializer
from django.contrib.auth.models import auth
from rest_framework import status
from knox.models import AuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics


class UserViewGeneric(generics.RetrieveUpdateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=UserSerializer
    def get_object(self):
        return self.request.user


class UserSignup(APIView):

    def post(self,request,format=None):
        serializer=UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({
            'token':AuthToken.objects.create(user)[1]
        })

class UserSignin(APIView):
    
    def post(self,request,format=None):
        serializer=UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data   
        return Response({
            'token':AuthToken.objects.create(user)[1]
        })


@api_view(['POST'])
def userLogout(request):
    if request.method=='POST':
        auth.logout(request)
        return Response(status=status.HTTP_200_OK)    
    
@api_view(['GET'])
def get_device(request):
    if request.user_agent.is_mobile:
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)