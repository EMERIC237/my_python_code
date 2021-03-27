from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>HELLO WORLD</h1>")
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Our contact</h1>")
    return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
    my_context = {
        "my_goal": "better future for me and others",
        "my_plan": "Using coding to ameliorate the world",
        "my_list": [1,2,3,4,5,6,7,8,9,0,1,2,3,444,576,905,44,56,65,67,565,44,345,46643,5],
        "my_routine": ["learn","try","correct","take note"] 
    }
    #return HttpResponse("<h1>We tell you about us</h1>")
    return render(request, "about.html", my_context)


def blog_view(request, *args, **kwargs):
    #return HttpResponse("<h1>OUR BLOG</h1>")
    return render(request, "blog.html", {})
