from django.shortcuts import render
from .models import Question, Choice
from .forms import QuestionForm, ChoiceForm
from django.shortcuts import redirect

def questions_list(request):
	questions = Question.objects.all()
	context = {'questions': questions}
	return render(request, 'test_app/questions_list.html', context)

def choices_list(request, pk):
	question = Question.objects.filter(pk=pk).first()
	choices = Choice.objects.filter(question=question)
	context = {'question': question, 'choices' : choices}
	return render(request, 'test_app/choices_list.html', context)

def questions_add(request):
	if request.method == 'POST':
		form = QuestionForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('questions_list')
	else:
		form = QuestionForm()

	context = {'form' : form}
	return render(request, 'test_app/questions_add.html', context)

def choices_add(request):
	if request.method == 'POST':
		form = ChoiceForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('choices_add')
	else:
		form = ChoiceForm()
		
	context = {'form' : form}
	return render(request, 'test_app/choices_add.html', context)
