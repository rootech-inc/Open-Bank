from django.shortcuts import render


# Create your views here.
def transactions(request):
    context = {
        'page':'Transactions'
    }
    return render(request, 'transactions/dashboard.html',context=context)

def view(request,chain):
    context = {
        'page': 'View'
    }
    return render(request, 'transactions/view-transaction.html', context=context)