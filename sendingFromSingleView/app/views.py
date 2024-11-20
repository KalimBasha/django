from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse

def singleView(request):
    ETFO=TopicForm()
    EWFO=WebpageForm()
    EAFO=AccessForm()   

    d={'ETFO':ETFO,'EWFO':EWFO,'EAFO':EAFO}

    if request.method=='POST' and request.FILES :
        NMTFDO=TopicForm(request.POST)
        NMWFDO=WebpageForm(request.POST,request.FILES)
        NMAFDO=AccessForm(request.POST,request.FILES)

        if NMTFDO.is_valid() and NMWFDO.is_valid():
            TO=NMTFDO.save()   #while saving it will give the database object but we have to give the child table data as model data object so save into another variable and give it

            MWFDO=NMWFDO.save(commit=False)
            MWFDO.topic_name=TO
            MWFDO.save()

            MAFDO=NMAFDO.save(commit=False)
            MAFDO.name=MWFDO
            MAFDO.save()

            return HttpResponse('Success!!!')
        else:
            return HttpResponse('Invalid Data')
    return render(request,'singleView.html',d)