from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request) :
    #use simple HttpResponse
    #return HttpResponse('<h1>Hello World :</h1>')

    #Use Template
    #return render(request,'home.html')

    # use Template with dynamic value
    return render(request,'home.html',{'name' : 'Amit'})

def add(request):

    #When Get method use GET Instead of POST, 
    #But for Post request we need to add {% csrf_token %} in view page in form tag,else we will get error
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    res = num1 + num2

    return render(request,'result.html',{'result' : res})