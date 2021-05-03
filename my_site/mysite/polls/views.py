from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import Choice, Question
# Create your views here.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list' #(change the default 'question_list' for ListView to our own variable 'lates_quetion_list')

    def get_queryset(self):
        '''return the last five published questions'''
        return Question.objects.order_by('-pub_date')[:5]
    
#displays a question text, with no results but with a form to vote.
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

#displays results for a particular question.
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

#displays results for a particular question.
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #redisplay the question voting form
        return render(request, 'polls/detail.html', {
            'question':question,
            'error_message': "You didn't select a choice, Please do so."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))