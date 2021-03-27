#This is a hard code of the my_site views In "my_side" django project.
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Choice, Question
# Create your views here.
#display the latest few questions
#using 'loader'
'''def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))'''

#using 'render'
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template_name ='polls/index.html'
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, template_name, context)

    
#displays a question text, with no results but with a form to vote.
def detail(request, question_id):
    '''try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404(" Question does not exit")'''
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question
    }
    return render(request,'polls/detail.html', context)

#displays results for a particular question.
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

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

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
