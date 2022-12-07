import random

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from home.models import Account, AccountMore

from home.forms import MoreAccountNew


@login_required()
def home(request):
    user = request.user
    if AccountMore.objects.filter(acct=Account.objects.get(owner=request.user)).count() < 1:
        acct = Account.objects.get(owner=request.user)
        context = {
            'oct':
                {
                    '1': '{:03d}'.format(random.randrange(1, 9999)),
                    '2': '{:03d}'.format(random.randrange(1, 9999)),
                    '3': '{:03d}'.format(random.randrange(1, 9999)),
                },
            'acct': acct,
        }
        return render(request, 'home/create_account.html', context=context)
    else:
        context = {
            'my_accts': AccountMore.objects.get(acct=Account.objects.get(owner=request.user))
        }
        return render(request, 'home/home.html', context=context)


@login_required()
def save_acct(request):
    if request.method == 'POST':
        form = MoreAccountNew(request.POST)

        if form.is_valid():
            try:
                form.save()
                return redirect('home')
            except Exception as e:
                return HttpResponse(e)
        else:
            return HttpResponse(f"INVALID FORM {form}")
