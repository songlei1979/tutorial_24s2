
from django.urls import path

from polls.views import index, list_questions, question_detail, create_question, create_choice, \
    all_questions, one_question, create_question_generic

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
    path('all_questions',
         all_questions.as_view(),
         name='all_questions'),
    path('one_question/<int:pk>',
         one_question.as_view(),
         name='one_question'),
    path('create_question_generic',
         create_question_generic.as_view(),
         name='create_question_generic'),

]