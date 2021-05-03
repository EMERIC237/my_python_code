from django.urls import path
from .views import (
    IndexView,
    DetailView,
    ResultsView,
    vote,
)

app_name= 'polls'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    #ex: /polls/
    path('<int:pk>/',DetailView.as_view(), name='detail'), #question_id changed to pk
    #ex: /polls/5/
    path('<int:pk>/results',ResultsView.as_view(), name='results'),
    #ex: /polls/5/results
    path('<int:question_id>/vote',vote, name='vote'),
    #ex: /polls/5/vote
]