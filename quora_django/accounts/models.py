from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

class profile(models.Model):
	#user = models.OneToOneField(User, on_delete=models.CASCADE)
	fullname = models.CharField(max_length=100, default='')
	gender = models.CharField(max_length=10,default='')
	contact = models.CharField(max_length=10, null=True, blank=True)
	photo = models.FileField(blank=True, null=True)


	def get_absolute_url(self):
		return reverse('accounts:profile')



