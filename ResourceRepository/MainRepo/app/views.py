"""
Definition of views.
"""

from asyncio.windows_events import NULL
from datetime import datetime
from turtle import title
from urllib import request
from django.shortcuts import get_object_or_404, render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.http import HttpRequest
from app.models import *
from app.forms import DataForm, DeleteForm, RegisterForm

# @login_required
def OverView(request):
    repoDatas = RepoData.objects.all()    
    return render(request ,'app/OverView.html' , {"repoDatas" : repoDatas})
# @login_required
def Data(request):
    if request.method == "GET":
        form = DataForm()
        return render(request,'app/DataForm.html',{'form' : form})
    if request.method == "POST":
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Add')


def Delete(request):
    if request.method == "GET":
        form = DeleteForm()
        return render(request, 'app/DeleteDataForm.html' , {'form':form})

    if request.method == "POST":
        form = DeleteForm(request.POST)
        if form.is_valid():
            query = RepoData.objects.filter(title = form.title)
            query.delete()
            return redirect('Delete')

def sign_up(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request,'app/register.html',{'form':form})
    
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect('register')
        else:
            return render(request, 'app/register.html', {'form': form})
        

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
