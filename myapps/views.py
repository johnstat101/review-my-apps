import profile
from django.shortcuts import render
from .models import Profile

def index(request):
    '''
    '''
    profile = Profile.objects.all()
    return render(request,'index.html',{"profile": profile})
