from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse

def insertSchool(request):
    ESFO=SchoolForm()
    d={'ESFO':ESFO}

    if request.method=='POST':
        DSFO=SchoolForm(request.POST)
        if DSFO.is_valid():
            SCID=request.POST['SchoolID']
            SCName=request.POST['SchoolName']
            SFO=School.objects.get_or_create(Scid=SCID,Sname=SCName)
            d1={'SFO':SFO}
            return HttpResponse('Object Inserted')
    return render(request,'insertSchool.html',d)

def insertStudent(request):
    ESFO=StudentForm()
    d={'ESFO':ESFO}

    if request.method=='POST':
        DSFO=StudentForm(request.POST)
        if DSFO.is_valid():
            SCID=request.POST['SchoolId']
            SCO=School.objects.get(Scid=SCID)
            STid=request.POST['Stuid']
            STName=request.POST['Stuname']
            # STLoc=request.POST['location']
            # STMob=request.POST['Mobile_No']
            email=request.POST['Email']
            Remail=request.POST['remail']
            SFO=Student.objects.get_or_create(Scid=SCO,Stid=STid,Stname=STName,loc=STLoc,Mobile=STMob,email=email)
            d1={'SFO':SFO}
            return HttpResponse('Object Inserted')
        else:
            return HttpResponse('Invalid Data')
    return render(request,'insertStudent.html',d)