from django.shortcuts import render
from .models import Question, Choice
from .forms import QuestionForm, ChoiceForm
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView

def questions_list(request):
	# Grabs ALL the records of the Question model and stores them
	# in a variable called questions.
	questions = Question.objects.all()

	# Context refers to the variables that your HTML file will use,
	# passed on from the view which the template is connected to.
	# We will see later how this is used.
	context = {'questions': questions}

	# Render has three variables:
	# 1. The request variable
	# 2. The template which this view is connected to
	# 3. The context, if there is any
	return render(request, 'test_app/questions_list.html', context)

class QuestionListView(ListView):
	# Shows ALL the records of the Question model
	model = Question

	# Specifies the name of the object containing all Question records
	# which the template will use. Default name is object_list.
	context_object_name = 'questions'

	# Specifies where the corresponding template is located
	template_name = 'test_app/questions_list.html'

def choices_list(request, pk):
	# Grabs the Question record with the given primary key and
	# stores it in a variable called question.
	question = Question.objects.get(pk=pk)

	# Same as above
	context = {'question': question}

	# Same as above
	return render(request, 'test_app/choices_list.html', context)

class QuestionDetailView(DetailView):
	# Shows the single record of the Question model given its primary key.
	# Note that if you intend to pass the primary key to a DetailView 
	# from the urls.py, it MUST be called pk.
	model = Question
	context_object_name = 'question'
	template_name = 'test_app/choices_list.html'

# View for adding questions to the database
def questions_add(request):
	if request.method == 'POST':
		# If this is a POST request (i.e. user is uploading data to the server)...

		# ...then "fill out" the QuestionForm with the data the user uploaded
		form = QuestionForm(request.POST)

		# If the uploaded data is valid with no errors, then save the form (meaning
		# the data gets added to the database), and redirect the user to the
		# questions_list view
		if form.is_valid():
			form.save()
			return redirect('questions_list')
	else:
		# If not a POST request (i.e. a GET request), then just load the form
		# without any data
		form = QuestionForm()

	# Pass that form (either containing the data or an empty form) to the template
	context = {'form' : form}
	return render(request, 'test_app/questions_add.html', context)

class QuestionFormView(FormView):
    template_name = 'test_app/questions_add.html'
    form_class = QuestionForm
    # Where your user will get redirected after the form is validated
    success_url = '/questions/'

# Views for adding choices to a question
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

class ChoiceFormView(FormView):
    template_name = 'test_app/choices_add.html'
    form_class = ChoiceForm
    # Where your user will get redirected after the form is validated
    success_url = '/choices/add/'
