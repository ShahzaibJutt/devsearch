import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
	name = models.CharField(max_length=200, null=True, blank=True)
	email = models.EmailField(max_length=500, null=True, blank=True)
	username = models.CharField(max_length=200, null=True, blank=True)
	location = models.CharField(max_length=200, null=True, blank=True)
	shor_intro = models.CharField(max_length=500, null=True, blank=True)
	bio = models.TextField(blank=True, null=True)
	profile_image = models.ImageField(blank=True, null=True, upload_to='profiles/',default='profiles/user-default.png')
	social_github = models.CharField(max_length=200, null=True, blank=True)
	social_linkedin = models.CharField(max_length=200, null=True, blank=True)
	social_twitter = models.CharField(max_length=200, null=True, blank=True)
	social_website = models.CharField(max_length=200, null=True, blank=True)
	social_youtube = models.CharField(max_length=200, null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

	def __str__(self): # Ask this from Dawood Bhai
		return str(self.user.username)

class Skill(models.Model):
	owner = models.ForeignKey(Profile,on_delete=models.CASCADE, null=True, blank=True)
	name = models.CharField(max_length=200,null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

	def __str__(self):
		return self.name
