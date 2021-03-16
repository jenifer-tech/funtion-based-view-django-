from rest_framework import serializers
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id','username','password','email','first_name','last_name')
        
    def create(self,validate_data):
        user=User.objects.create_user(username=validate_data['username'],
                                        password=validate_data['password'],
                                        email=validate_data['email'],
                                        first_name=validate_data['first_name'],
                                        last_name=validate_data['last_name'],
        )
        return user
