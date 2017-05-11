from django.db import models
from django.contrib.auth.models import User

# Blinks
class Blink(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
	title = models.CharField(max_length=250)
	author = models.CharField(max_length=250)
	image = models.CharField(max_length=1000)
	url = models.CharField(max_length=1000)
	rating = models.IntegerField()
	description = models.CharField(max_length=2000)
	tags = models.CharField(max_length=1000)

	def __str__(self):
		return self.title + " - " + self.author

# Tasks
class Task(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
	title = models.CharField(max_length=250)
	sub_tasks = models.CharField(max_length=1000)
	task_type = models.IntegerField()

	def __str__(self):
		return self.title

class BlinkNotes(models.Model):
	owner = models.ForeignKey(Blink, on_delete=models.CASCADE, default=0)
	note = models.CharField(max_length=2000)