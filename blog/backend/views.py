from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django. contrib. auth import authenticate

# Create your views here.
def home(request):
    return render(request,'backend/home.html',context={})

def check_staff_account(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            return redirect("backend_mainmenu")
        elif user is not None:
            return HttpResponse("<h1>You do not have staff access. You can't go to backend page.</h1>")
        else:
            return HttpResponse("<h1>You have entered wrong username or password</h1>")
            
    else:
        return HttpResponse("<h1>404: ERROR- This page can not be accessed by anyone</h1>")

def backend_mainmenu(request):
    return HttpResponse("<h1>We are working on it, please wait for some days.</h1>")