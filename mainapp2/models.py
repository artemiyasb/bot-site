from django.db import models
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    username = models.TextField(unique=True)
    password = models.TextField()
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
 
    
