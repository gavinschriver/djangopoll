from django.http.response import Http404
from django.template import loader
from polls.models import Choice, Question
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.http import HttpResponse

# Create your views here.

def index(req):
    latest_question_list = get_list_or_404(Question.objects.order_by('-pub_date')[:5])
    return render(req, 'polls/index.html',{'latest_question_list' : latest_question_list})


def detail(req, question_id):
    try:
        q = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        raise Http404("no question there sir")
    return render(req, 'polls/detail.html', {'ques' : q})

def results(req, q_id):
    response = "You're looking at the results for question %s"
    return HttpResponse(response % q_id)

def vote(req, ques_id):
    return HttpResponse("Time to vote on question %s" % ques_id)   

def peep(req, peep_id):
    r = get_object_or_404(Choice,id=peep_id)
    return render(req, 'polls/peep.html', {'choice_text' : r.choice_text, 'random_nonsense' : 'you are PEEPIN THIS MY MAN'})

def your_face(req):
    return HttpResponse("your dang ol FACE i SAID")
