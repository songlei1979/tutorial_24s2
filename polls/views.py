from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from polls.models import Question, Choice


# Create your views here.

def index(request):
    return render(request, 'index.html')


def list_questions(request):
    recent_published_questions = []
    questions = Question.objects.all()
    for question in questions:
        if question.was_published_recently():
            recent_published_questions.append(question)
    return render(request,
                  'list_questions.html',
                  {'questions': recent_published_questions})

def question_detail(request, question_id):
    question = Question.objects.get(id=question_id)
    return render(request,
                  'question_detail.html',
                  {'question': question})

def create_question(request):
    if request.method == 'POST':
        question_text = request.POST.get('question_text')
        question = Question(question_text=question_text)
        question.save()
        return render(request,
                      'create_question.html',
                      {'message': question.question_text
                                  + " created"})
    else:
        return render(request,
                      'create_question.html',
                      {'message': ''})


def create_choice(request):
    if request.method == 'POST':
        choice_text = request.POST.get('choice_text')
        question_id = request.POST.get('question_id')
        question = Question.objects.get(id=question_id)
        print(question)
        choice = Choice(question=question, choice_text=choice_text)
        print(choice)
        choice.save()
        return render(request,
                      'create_choice.html',
                      {'message': choice.choice_text
                                  + " created",
                       'question_id': question_id})


class all_questions(ListView):
    model = Question
    template_name = 'all_questions.html'

class one_question(DetailView):
    model = Question
    template_name = 'one_question.html'

class create_question_generic(CreateView):
    model = Question
    fields = ['question_text']
    template_name = 'create_question_generic.html'


