from django.shortcuts import render

# Create your views here.

from app.forms import *


def registration(request):
    UFO=UserForm()
    PFO=ProfileForm()
    d={'ufo':UFO,'pfo':PFO}
    return render(request,'registration.html',d)