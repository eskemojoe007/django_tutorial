from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question, Choice

# Create your views here.
def index(request):
    # return HttpResponse("Welcome...ya filthy animal")
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    return render(request,'polls/index.html',context={'latest_question_list':latest_question_list})

def detail(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',context={'question':question})
    # return HttpResponse("Looking at detail for {}".format(question_id))

def results(request,question_id):
    return HttpResponse("Looking at results for {}".format(question_id))

def vote(request,question_id):
    return HttpResponse("Looking at vote for {}".format(question_id))
