from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.IntegerField(null=True, blank=True)
    email = models.EmailField()
    adress =  models.TextField()
    
    def __str__(self):
        return self.user.username

class CooperativeInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    email = models.EmailField(max_length=70, blank=True)
    phone_number = models.IntegerField()