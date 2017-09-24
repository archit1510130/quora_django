from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse



class profile(models.Model):
    user = models.CharField(max_length=100,default='')
    fullname = models.CharField(max_length=100,default='')
    def __str__(self):
        return self.User.username

    def get_absolute_url(self):
        return reverse('accounts:profile')








