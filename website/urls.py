from unicodedata import name
from django.contrib import admin
from django.urls import path
from website import views
from django.contrib.auth.views import LoginView,LogoutView 

urlpatterns = [
    path("",views.home, name="home"),
    path("loginpage/",LoginView.as_view(template_name="loginpage.html"),name="loginpage"),
    path("registpage/",views.registpage, name="registpage"),
    path("logout/",LogoutView.as_view(next_page="home"),name="logout"),
    path("inputpage/",views.inputpage, name='inputpage',),
    path("outputpage/",views.outputpage, name='outputpage',)
]

