from django.urls import path
from .views import homepage, doLogin, signup

urlpatterns=[
    path('', homepage, name='home'),
    path('login/', doLogin, name='login'),
    path('signup/',signup,name='signup')
]