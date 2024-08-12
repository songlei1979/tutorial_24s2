from django.shortcuts import render

from polls.models import Question


# Create your views here.

def index(request):
    return render(request, 'index.html')


def list_questions(request):
    questions = Question.objects.all()
    return render(request,
                  'list_questions.html',
                  {'questions': questions})

def question_detail(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request,
                  'question_detail.html',
                  {'question': question})