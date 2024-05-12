from django.shortcuts import render
from .forms import CustomerForm

# Create your views here.

def homepage(request):
    
    return render(request, 'main/index.html', )

def doLogin(request):
    if request.method == 'post':
        pass
    customer_form = CustomerForm()

    return render(request, 'cafeapp/login.html', {'form_fields':customer_form})