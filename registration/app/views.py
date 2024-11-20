from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail     #for sending mail
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def registration(request):
    EUFO=UserForm()
    EPFO=ProfileForm()
    d={'EUFO':EUFO,'EPFO':EPFO}

    if request.method=='POST' and request.FILES :
        NMUFDO=UserForm(request.POST)   #NMUFDO means non-modifiable user form data object we have to perform some operations on the data
        NMPFDO=ProfileForm(request.POST,request.FILES)

        if NMUFDO.is_valid() and NMPFDO.is_valid():
            #userform operations to convert password into encrypted data bcz password has to store in the form of encrypted data
            MUFDO=NMUFDO.save(commit=False)    #defaultly commit=True means we cannot modify the data now we have to change commit=False to modify it && MUFDO means modifiable user form data object
            pw=NMUFDO.cleaned_data['password']   #we're getting password to encrypt it from cleaned_data dictionary
            MUFDO.set_password(pw)    #set_password is a method which will encrypt the data and update to the database
            MUFDO.save()

            #profile-form operations   while we're getting the data from frontend we are getting only two datas but the actual colums in these table is 3 we're not getting the parent table data thats why we have to perform this operation
            MPFDO=NMPFDO.save(commit=False)
            MPFDO.username=MUFDO   #here we are giving that object to parent table data
            MPFDO.save()

            send_mail(
                'Registraion',     #subject to give in mail
                'Registration Successfull!!!',     #message body to give in mail
                'kalimbasha01@gmail.com',   #from mail id to send the mail
                [MUFDO.email],   #to whom we have to send the mail
                fail_silently=False    #to give error if something error occurs we have to use false value else true value
                )

            return HttpResponse('Registration Successfull!!!')
        else:
            return HttpResponse('Invalid Data')
    return render(request,'registration.html',d)

def user_login(request):
    if request.method=='POST':
        usn=request.POST['un']
        pwd=request.POST['pw']
        AUO=authenticate(username=usn,password=pwd)
        if AUO:
            if AUO.is_active:
                login(request,AUO)
                request.session['username']=usn
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse('User is Not Active...')
        return HttpResponse('Invalid Credentials')
    return render(request,'user_login.html')

def home(request):
    if request.session.get('username'):
        username=request.session.get('username')
        d={'username':username}
        #print(username)
        return render(request,'home.html',d)
    return render(request,'home.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required
def profile_display(request):
    username=request.session.get('username')
    UO=User.objects.get(username=username)
    PO=profile.objects.get(username=UO)
    d={'UO':UO,'PO':PO}
    return render(request,'profile_display.html',d)

@login_required
def change_password(request):
    if request.method=='POST':
        password=request.POST['password']
        username=request.session.get('username')
        UO=User.objects.get(username=username)
        UO.set_password(password)
        UO.save()
        return render(request,'home.html')
    return render(request,'change_password.html')

def reset_password(request):
    if request.method=='POST':
        un=request.POST['username']
        pw=request.POST['password']
        LUO=User.objects.filter(username=un)
        if LUO:
            UO=LUO[0]
            UO.set_password(pw)
            UO.save()
            return HttpResponse('Password reset Done...')
        else:
            return HttpResponse('User Not Available !!!')
    return render(request,'reset_password.html')
