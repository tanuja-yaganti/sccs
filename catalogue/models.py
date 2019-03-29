from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone

class Component(models.Model):
	name = models.CharField(max_length=500,null=True)
	version = models.CharField(max_length=500,null=True)
	license = models.CharField(max_length=500,null=True)
	primary_language = models.CharField(max_length=500,null=True)
	keywords = models.CharField(max_length=500,null=True)
	homepage_URL = models.CharField(max_length=500,null=True)
	download_URL = models.CharField(max_length=500,null=True)
	created_date = models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.name