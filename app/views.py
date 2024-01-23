from django.shortcuts import render

# Create your views here.

from app.forms import *
from django.http import HttpResponse,HttpResponseRedirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse

def registration(request):
    UFO=UserForm()
    PFO=ProfileForm()
    d={'ufo':UFO,'pfo':PFO}
    
    if request.method=='POST' and request.FILES:
        ufd=UserForm(request.POST)
        pfd=ProfileForm(request.POST,request.FILES)

        if ufd.is_valid() and pfd.is_valid():
            MUFDO=ufd.save(commit=False)
            pw=ufd.cleaned_data['password']
            MUFDO.set_password(pw)
            MUFDO.save()

            MPFDO=pfd.save(commit=False)
            MPFDO.username=MUFDO
            MPFDO.save()

            send_mail('Registration',
                      'You are register Successful',
                      'kanhaachary692@gmail.com',
                      [MUFDO.email],
                      fail_silently=False)
            
            
            return HttpResponse('Registration Is Successful')
        else:
            return HttpResponse('Invalid Data')
    
    return render(request,'registration.html',d)

def home(request):
    if request.session.get('username'):
        username=request.session.get('username')
        d={'username':username}
        return render(request,'home.html',d)
    return render(request,'home.html')

def user_login(request):
    if request.method=='POST':
        username=request.POST['un']
        password=request.POST['pw']
        AUO=authenticate(username=username,password=password)

        if AUO and AUO.is_active:
            login(request,AUO)
            request.session['username']=username
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse('Invalid Credentials')

    return render(request,'user_login.html')