"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import index,register,login_request,check_user,check_account,createblog,suggestion_form,logout_request,description

urlpatterns = [
    path('',index,name="index"),
    path('register/',register,name="register"),
    path('login_request/',login_request,name="login_request"),
    path('check_user/',check_user,name="check_user"),
    path('check_account/',check_account,name="check_account"),
    path('createblog/',createblog,name="createblog"),
    path('suggestion_form/',suggestion_form,name="suggestion_form"),
    path('logout_request/',logout_request,name="logout_request"),
    path('description/',description,name="description"),
]
