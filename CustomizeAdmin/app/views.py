from django.shortcuts import render

# Create your views here.

from app.forms import *
from django.http import HttpResponse

def displayTopic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}

    if request.method=='POST':
        DTFO=TopicForm(request.POST)
        if DTFO.is_valid():
            DTFO.save()
            return HttpResponse('succesfull!!!')
        else:
            return HttpResponse('Invalid')
    return render(request,'displayTopic.html',d)

def displayWebpage(request):
    EWFO=WebpageForm()
    d={'EWFO':EWFO}

    if request.method=='POST':
        DWFO=WebpageForm(request.POST)
        if DWFO.is_valid():
            DWFO.save()
            return HttpResponse('succesfull!!!')
        else:
            return HttpResponse('Invalid')
    return render(request,'displayWebpage.html',d)

def GetDataFromUrl(request,name):
    return HttpResponse(f'Hii {name},Have A Nice Day Buddy!!!')