from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):

    return render(request,'home/home.html')


def login(request):
    context = {
        'page':{
            'title':'Login'
        }
    }
    return render(request,'user/login.html',context=context)

def register(request):
    context = {
        'page':{
            'title':'Register'
        }
    }
    return render(request,'user/register.html',context=context)


def profile(request):
    context = {
        'page': {
            'title': 'Register'
        }
    }
    return render(request, 'user/profile.html', context=context)