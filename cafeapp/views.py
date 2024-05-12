from django.shortcuts import render
from .forms import SignUpForm, LoginForm
from django.views import View

# Create your views here.

def homepage(request):
    return render(request, 'main/index.html')

class LoginView(View):

    def get(self, request):
        login_form = LoginForm()
        return render(request, 'cafeapp/login.html', {'login_form':login_form})
    
    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            pass
        return render(request, 'cafeapp/login.html', {'login_form':login_form})


def doLogin(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            login_form = login_form.cleaned_data
            print(login_form)
        else:
            print(login_form.errors) #  For debugging

    else:
        login_form = LoginForm()
    return render(request, 'cafeapp/login.html', {'login_form':login_form} )

def signup(request):
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            form = signup_form.cleaned_data
            print(form)

    signup_form= SignUpForm()
    return render(request, 'cafeapp/signup.html', {'signup_form':signup_form})