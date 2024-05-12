from django.urls import path
from .views import homepage, doLogin

urlpatterns=[
    path('', homepage, name='home'),
    path('login/', doLogin, name='login'),
]