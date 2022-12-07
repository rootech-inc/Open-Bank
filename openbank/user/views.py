import random

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect

from home.models import Account,AccountMore




# Create your views here.
def home(request):
    return render(request, 'home/home.html')


def user_auth(request):
    if request.method == 'POST':
        form = request.POST
        username = form['username']
        password = form['password']
        n = form['next']
        if len(n) > 0:
            next = form['next']
        else:
            next = 'home'
        user = authenticate(request, username=username, password=password)
        try:
            # check if user is valid
            try:
                auth_login(request, user)
                # Redirect to a success page.
                return redirect(next)
            except Exception as e:
                messages.error(request,
                               f"There is an error logging in, {e}")
                return redirect('login')

        except Exception as e:
            messages.error(request, f"There was an error {e}")
            return redirect('login')

    else:
        return HttpResponse('We Missing')


def sign_up(request):
    if request.method == 'POST':
        form = request.POST
        first_name = form['first_name']
        last_name = form['last_name']
        country = form['country']
        city = form['city']
        address = form['address']
        contct_method = form['contct_method']
        email = form['email']
        mobile = form['mobile']

        password = form['password']

        # generate username
        number = '{:03d}'.format(random.randrange(1, 9999))
        username = '{}{}'.format(last_name, number)

        # save username
        new_user_instance = User.objects.create_user(username=username, password=password, email=email,
                                                     first_name=first_name, last_name=last_name)

        try:
            new_user_instance.save()
            new_user_instance.is_active = False
            new_user_pk = new_user_instance.pk
            Account(acct_name=f"{first_name} {last_name}",acct_pref=number,city=city,address=address,owner=User.objects.get(pk=new_user_pk)).save()

            subject = 'welcome to Open Bank'
            message = f'Hi {first_name} {last_name}, thank you for registering. your username is {username} and password is {password} logn at ocean t explore the power in collaboration '
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, email_from, recipient_list)
            messages.error(request, "Please check your email to activate your account")
            return redirect('login')
        except Exception as e:
            messages.error(request, "Error Saving User")
            return HttpResponse(f"{e} {email}")
    else:
        return HttpResponse("Unaccepted Form Method")




def login(request):
    if request.method == 'GET' and 'next' in request.GET:
        n_next = request.GET['next']
    else:
        n_next = '/'
    context = {
        'page': {
            'title': 'Login', 'next': n_next
        }
    }
    return render(request, 'user/login.html', context=context)


def register(request):
    context = {
        'page': {
            'title': 'Register'
        }
    }
    return render(request, 'user/register.html', context=context)


def profile(request):
    context = {
        'page': {
            'title': 'Register'
        }
    }
    return render(request, 'user/profile.html', context=context)
