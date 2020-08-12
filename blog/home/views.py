from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from .models import blog,suggestion
from django.contrib import messages
from django.contrib.auth import (login,authenticate,logout)
from .forms import AddPostForm,user_form

# Create your views here.
def index(request):
    data=blog.objects.all()
    return render(request,'home/index.html',context={"data": data,"var": 0})

def register(request):
    return render(request,'home/register.html',context={})

def login_request(request):
    if request.user.is_authenticated :
        return render(request,'home/add_your_blog.html',context={})
    else:
        return render(request,'home/login.html',context={})

def check_user(request):
    if request.method == "POST":
        form = user_form(request.POST)
        username=request.POST.get("username")
        email=request.POST.get("email")
        try:
            checker = User.objects.get(email=email)
            messages.info(request,"This email is already registered")
            return render(request,"home/register.html",context={"wrong_email": True})
        except:
            try:
                checker = User.objects.get(username=username)
                messages.info(request,"Try some different username")
                return render(request,"home/register.html",context={"wrong_username": True})
            except:
                print(form.is_valid())
                if form.is_valid():
                    first_name = User.POST.get("first_name")
                    last_name = User.POST.get("last_name")   
                    password = User.POST.get("password2")
                    user = User.objects.create(username=username, email=email, first_name=first_name, last_name=last_name)
                    user.set_password(password)
                    user.save()
                    messages.info(request,"You have been successfully registered")
                    return render(request,'home/addblog.html',context={})
                else:
                    return render(request,"home/register.html",context={"wrong_password": True})
    else:
        return HttpResponse("<h1>404: ERROR- This page can not be accessed by anyone</h1>")

def check_account(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return render(request,'home/add_your_blog.html',context={})
        else:
            return HttpResponse("<h1>Username or Password does not matched</h1>")
    
    else:
        return HttpResponse("<h1>404: ERROR- This page can not be accessed by anyone</h1>")

def createblog(request):
    if request.method == "POST":
        form = AddPostForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            form.save()        
        data=blog.objects.all()
        return render(request,'home/index.html',context={"data": data,"var": 0})
    else:
        return redirect('login_request')

def logout_request(request):
    logout(request)
    return redirect("index")


def suggestion_form(request):
    if request.method == "GET":
        name=request.GET.get("name")
        email=request.GET.get("email")
        suggest=request.GET.get("suggestion")

        suggestion.objects.create(name=name, email=email, suggestion=suggest)
        return HttpResponse("<h1>Your suggestion is successfully submitted. This is very important to us and we will try to update ourselves.")

def description(request):
    if request.method== "GET":
        ID=request.GET.get("ID")
        user=blog.objects.get(id=ID)
        return render(request,"home/description.html",context={"user": user})
    else:
        return redirect('index')