from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'index.html',{'name':"Home"})


def course(request):
    return render(request,'course.html')


def blogs(request):
    return render(request,'blogs.html')


def contact(request):
    return render(request,'contact.html')


def about(request):
    return render(request,'about.html')



