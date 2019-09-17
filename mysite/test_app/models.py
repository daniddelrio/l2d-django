from django.db import models

class Question(models.Model):
	title = models.CharField(max_length=255)
	date_published = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name