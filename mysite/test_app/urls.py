from django.urls import path
from . import views

urlpatterns = [
   # path('questions/', views.questions_list, name='questions_list'),
   path('questions/', views.QuestionListView.as_view(), name='questions_list'),
   # path('questions/<int:pk>/', views.choices_list, name='choices_list'),
   path('questions/<int:pk>/', views.QuestionDetailView.as_view(), name='choices_list'),
   # path('questions/add/', views.questions_add, name='questions_add'),
   path('questions/add/', views.QuestionFormView.as_view(), name='questions_add'),
   # path('choices/add/', views.choices_add, name='choices_add'),
   path('choices/add/', views.ChoiceFormView.as_view(), name='choices_add'),
]