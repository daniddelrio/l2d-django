from django.shortcuts import render
from .models import Question, Choice

def questions_list(request):
	questions = Question.objects.all()
	context = {'questions': questions}
	return render(request, 'test_app/questions_list.html', context)

def choices_list(request, pk):
	question = Question.objects.filter(pk=pk).first()
	choices = Choice.objects.filter(question=question)
	context = {'question': question, 'choices' : choices}
	return render(request, 'test_app/choices_list.html', context)
