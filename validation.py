import re
from django.contrib.auth.models import User

def validation(username,password,email,first_name,last_name):
    if not username or not email or not password or not first_name or not last_name:
        return 'Please fill all the details!'   		
    elif not username.isalpha():  
        return 'Invalid Username'      
    elif not re.match  (r'[^@]+@[^@]+\.[^@]+',email):   
        return 'Invalid Email address'   
    elif not first_name.isalpha():  
        return 'Invalid First name' 
    elif not last_name.isalpha():  
        return 'Invalid Last name'   
    return ''      
def validate_email(email):
    account = None
    try:
        account = User.objects.get(email=email)
    except User.DoesNotExist:
        return None
    if account != None:
        return email
def validate_username(username):
    account = None
    try:
        account = User.objects.get(username=username)
    except User.DoesNotExist:
        return None
    if account != None:
        return username    
