from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.core.exceptions import ObjectDoesNotExist

from .models import Question, Choice

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    template = loader.get_template('polls/index.html')

    context = {
                'latest_question_list': latest_question_list,
    }

    #response = "List of latest questions added:<br><br>"
    #response += '<br>'.join([q.question_text for q in latest_question_list])
    #return HttpResponse(template.render(context,request))
    return render(request,'polls/index.html', context)


def detail(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question' : question})

    #Longest way to do it:
    #try:
    #    question = Question.objects.get(pk=question_id)
    ##    response = "You are looking at question %s.<br>" + question_text
    #except Question.DoesNotExist:
    #    raise Http404("Question does not exist.")
    ##    response = "Question number %s does not exist."



def results(request,question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You are voting on question %s." % question_id)
