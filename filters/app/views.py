from django.shortcuts import render

# Create your views here.

def builtin_filters(request):
    from datetime import datetime
    dt=datetime.now()
    d={'data':'tHiS is KALim baSha','dt':dt,'c':1}
    return render(request,'builtin_filters.html',d)

def userdefined_filters(request):
    d={'data':'hIi thIs iS KalIm BashA'}
    return render(request,'userdefined_filters.html',d)