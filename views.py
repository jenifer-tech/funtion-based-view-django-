from user.serializers import RegisterSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.response import Response 
from rest_framework.authtoken.models import Token
from user.validation import validate_email,validate_username,validation

@api_view(['POST'])
def register_view(request):
    if request.method=='POST':
        data = {}
        username    =   request.data.get('username') 
        password    =   request.data.get('password')
        email       =   request.data.get('email')
        first_name  =   request.data.get('first_name') 
        last_name   =   request.data.get('last_name')          

        error_msg=validation(username,password,email,first_name,last_name)
        if error_msg:
            return Response({"message":error_msg},status=status.HTTP_400_BAD_REQUEST)

        if validate_email(email) != None:
            data['error_message'] = 'That email is already in use.'
            data['response'] = 'Error'
            return Response(data,status=status.HTTP_400_BAD_REQUEST)

        
        if validate_username(username) != None:
            data['error_message'] = 'That username is already in use.'
            data['response'] = 'Error'
            return Response(data,status=status.HTTP_400_BAD_REQUEST) 

        serializer=RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)



@api_view(['POST'])
def login_view(request):
    if request.method=='POST':
        username=request.data.get("username")
        password=request.data.get("password")
        if username is None or password is None:
            return Response({'error':'Please provide both username and password'},status=status.HTTP_400_BAD_REQUEST)
        user=authenticate(username=username,password=password)    
        if not user:
            return Response({'error':'Invalid Credentials'},status=status.HTTP_404_NOT_FOUND)
        token,created=Token.objects.get_or_create(user=user)   
        return Response({'token':token.key})






