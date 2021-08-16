from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def UAlogin(request):
    if request.user.is_authenticated:
        return redirect('AMHome')
    return render(request, "UtilityApp/login.html")

def loginuser(request):
    if request.method == "POST":
        username = request.POST['unme']
        password = request.POST['pss']
        thisuser = authenticate(request, username = username, password = password)
        if thisuser is not None:
            login(request, thisuser)
            return redirect('AMHome')
        else:
            return redirect('UALogin')

    else:
        return redirect('UALogin')

def UAlogout(request):
    logout(request)
    return redirect('AMHome')
    

def UAsignup(request):
    return render(request, "UtilityApp/signup.html")

def signupuser(request):
    if request.method == "POST":
        name = request.POST['fnme']
        email = request.POST['eml']
        username = request.POST['']
        pss = request.POST['pss']
        pss1 = request.POST['pss1']
        
        return redirect('UALogin')
    else:
        return redirect('UASignup') 