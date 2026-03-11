from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import GeeksForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import

def say_hello(request):
    if request.method == 'GET':
        return render(request, 'hello.html')

def contact_view(request):
    if request.method=='POST':
        name=request.POST.get('user_name')
        message=request.POST.get("user_message")

        print(f"Message from {name}:{message}")
        return HttpResponse("Thank you for your message!")
    return render(request, 'contact_form.html')

def home_view(request):
    context ={}
    context['form']=GeeksForm()
    return render(request,"home.html",context)

def home1(request):
    return render(request, "home.html", {
        'gretings': 'Welcome to the Home Page!',
        'users': [{'id':1, 'name':'Alice'}, {'id':2, 'name':'Bob'}]
    })

def login_view(request):
    if request.method == 'POST':
        username=request.POST['Username']