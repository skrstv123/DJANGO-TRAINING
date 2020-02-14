from django.db import models
from django.contrib.auth.models import User

# Create your models here.
	

class UserData(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	bio = models.TextField(max_length = 500, blank = True)
	gender = models.CharField(max_length = 30)
	dob = models.DateField()
	location = models.CharField(max_length=30)
	# followings = models.TextField(max_length = 500, blank = True)

class posts(models.Model):
	user = models.TextField(max_length = 500, blank = True)
	post = models.TextField(max_length = 500, blank = True)
	head = models.CharField(max_length = 30)
	date = models.CharField(max_length = 30)
