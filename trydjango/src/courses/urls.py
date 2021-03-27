from django.urls import path 
from .views import (
    CourseView,
    CourseListView,
    CourseCreateView,
    CourseUpdateView,
    CourseDeleteView,
    my_fbv,

    #Mylistview,
)

app_name = 'courses'
urlpatterns = [
    #path('',my_fbv,name='course_list'),
    path('',CourseListView.as_view(),name='courses_list'),
    #path('',Mylistview.as_view(),name='courses_list'),
    path('<int:id>/',CourseView.as_view(),name='courses_detail'),
    path('create/',CourseCreateView.as_view(),name='courses_create'),
    path('<int:id>/update/',CourseUpdateView.as_view(),name='courses_update'),
    path('<int:id>/delete/',CourseDeleteView.as_view(),name='courses_delete'),
]