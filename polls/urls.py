
from django.urls import path

from polls.views import index, list_questions, question_detail, create_question, create_choice

urlpatterns = [
    path('', index, name='home'),
    path('list_questions/', list_questions, name='questions'),
    path('question_detail/<int:question_id>/',
         question_detail,
         name='question_detail'),
    path('create_question/', create_question, name='create_question'),
    path('create_choice/',
         create_choice,
         name='create_choice'),

]