from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return HttpResponse(f'HELLO WORLD <a href="/logout">Logout</a>')
    return redirect('UALogin')
        
