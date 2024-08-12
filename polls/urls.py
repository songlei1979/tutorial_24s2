
from django.urls import path

from polls.views import index, list_questions, question_detail

urlpatterns = [
    path('', index, name='home'),
    path('list_questions/', list_questions, name='questions'),
    path('question_detail/<int:question_id>/',
         question_detail,
         name='question_detail'),

]