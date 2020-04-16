from django.shortcuts import render,HttpResponse

# Create your views here.
def homepage(request):
    return HttpResponse(
        "<h1>Hi there. </h1> My name is vikas."
        )