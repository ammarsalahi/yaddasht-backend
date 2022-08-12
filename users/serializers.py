from dataclasses import fields
from rest_framework import serializers
from users.models import User
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=('email','password','username','id')
        kwargs={'pasword':{'write_only':True}}

    def create(self, validated_data):
        user=User.objects.create_publicuser(**validated_data)
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):

    email=serializers.EmailField(write_only=True)
    password=serializers.CharField(write_only=True) 

    def validate(self, attrs):
        user=authenticate(**attrs)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('not login')
    

         


