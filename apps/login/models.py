from __future__ import unicode_literals
from django.db import models 
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.forms.widgets import DateInput
import bcrypt

class UserManager(models.Manager):
	def register(self, postData):
		errors = []

		
		if(len(postData['name']) <2):
			errors.append("First name must be at least 2 characters")
		if(len(postData['alias']) <2):
			errors.append("Last name must be at least 2 characters")
		if(len(postData['email']) <6):
			errors.append("Email must be at least 6 characters")
		if(len(postData['password']) <8):
			errors.append("Password must be at least 8 characters")
		if(postData['password'] != postData['password_confirmation']):
			errors.append("Password and password confirmation don't match")

		try:
			validate_email(postData['email'])
		except ValidationError as e:
			errors.append("Email must be in a valid format")
		else:
			print("Email worked!")

		if errors:
			return {'err_messages': errors}

		else:
			hash_pw = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
			user = User.objects.create(name = postData['name'], alias = postData ['alias'], email = postData['email'], password = hash_pw)

			return {'success': user}

		
class User(models.Model):
	name = models.CharField(max_length=255)
	alias = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	# date_of_birth = models.DateField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = UserManager()





















