from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from .models import blog

# Create your views here.
def index(request):
    data=blog.objects.all()
    return render(request,'home/index.html',context={"data": data,"var": 0})

def register(request):
    return render(request,'home/register.html',context={})

def addblog(request):
    return render(request,'home/addblog.html',context={})

def check_user(request):
    if request.method == "POST":
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")

        try:
            user = User.objects.get(username=username)
            return HttpResponse("<h1>Username already exists in database</h1>")
        except:
            try:
                user = User.objects.get(email=email)
                return HttpResponse("<h1>Email is already registered</h1>")

            except:
                User.objects.create(username=username, password=password, email=email)
                return render(request,'home/addblog.html',context={})

def check_account(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        try:
            checker = User.objects.get(username=username, password=password)
            return render(request,"home/add_your_blog.html",context={"value": True})
        except:
            return HttpResponse("<h1>Username or Password does not matched</h1>")

def createblog(request):
    if request.method == "POST":
        author=request.POST.get("author")
        description=request.POST.get("description")
        heading=request.POST.get("heading")

        blog.objects.create(author=author, brief=description, heading=heading)
        data=blog.objects.all()
        return render(request,'home/index.html',context={"data": data,"var": 0})