from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """ Return the last five published questions (not
        including those set to be published in the future) """
        all_non_future_questions = Question.objects.filter(pub_date__lte=timezone.now())
        return all_non_future_questions.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    template_name = 'polls/detail.html'
    model = Question

    """ Excludes any questions tha aren't published yet. """
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    template_name = 'polls/results.html'
    model = Question

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #Redisplay the question voting form.
        context = {
                    'question': question,
                    'error_message': "You didn't select a choice.",

        }
        return render(request, 'polls/detail.html',context)

    else:
        selected_choice.votes += 1
        selected_choice.save()

        #Always return an HttpResponseRedirect after successfully dealing
        #with POST data. This prevents data from being twice if a user hits the Back button

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
