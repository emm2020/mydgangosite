from django.shortcuts import render
from django.shortcuts import HttpResponse

def home(request):
    # return HttpResponse('This is the first page')
    return render(request, 'home.html')

def about(request):
    # return HttpResponse('hi there! Im hello world')
    return render(request, 'about.html')
