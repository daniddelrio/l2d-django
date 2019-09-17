# l2d-django

Django boilerplate code for L2D

Steps:
1. Run `python manage.py makemigrations` and `python manage.py migrate` to migrate your database.
2. Go to localhost:8000/questions/add/ to add a question.
3. Go to localhost:8000/choices/add/ to add some choices. In the dropdown field for the form, select the question that you made previously.
4. You can view the list of questions in localhost:8000/questions/. Click "View Choices" on any of the questions.
5. You should be able to see the choices you made for that question.