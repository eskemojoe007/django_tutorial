from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from django.views import generic
from django.utils import timezone

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
        # return Question.objects

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


# # Create your views here.
# def index(request):
#     # return HttpResponse("Welcome...ya filthy animal")
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     return render(request,'polls/index.html',context={'latest_question_list':latest_question_list})
#
# def detail(request,question_id):
#     question = get_object_or_404(Question,pk=question_id)
#     return render(request,'polls/detail.html',context={'question':question})
#     # return HttpResponse("Looking at detail for {}".format(question_id))
#
# def results(request,question_id):
#     question = get_object_or_404(Question,pk=question_id)
#     return render(request,'polls/results.html',context={'question':question})
#     # return HttpResponse("Looking at results for {}".format(question_id))

def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)

    try:
        choice_pk = request.POST['choice']
        selected_choice = question.choice_set.get(pk=choice_pk)
    except (KeyError, Choice.DoesNotExist):
        return render(request,'polls/detail.html',
            context={'question':question,'error_message':"You didn't select a choice"})
    else:
        selected_choice.votes +=1
        selected_choice.save()

    return HttpResponseRedirect(reverse('polls:results',args=(question_id,)))
