from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    phone_number=models.CharField(max_length=100)
    address=models.CharField(max_length=100)

    class Meta:
        permissions =[
            ("can_view_protected_page","can view protected page"),
        ]

class usermodel(models.Model):
    user_id=models.IntegerField(primary_key=True)
    user_name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

class newuser(models.Model):
    usern_id=models.IntegerField(primary_key=True)
    usern_name=models.CharField(max_length=100)
    passwordn=models.CharField(max_length=100)
    
    
