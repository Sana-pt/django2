from django.contrib.auth.forms import UserCreationForm
from .models import *
class CustomUser1(UserCreationForm):
    class Meta:
        model = CustomUser 
        fields = ('username','password1','password2','phone_number','address')