from django import forms
from .models import Question, Choice

class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ['title']

class ChoiceForm(forms.ModelForm):
	class Meta:
		model = Choice
		fields = ['question', 'name']