"""
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class User(User):
    #password = models.CharField(max_length = 256)
    
    def Meta():
        proxy = True

    def __str__():
        return f'I am user: {self.username}' 
        """