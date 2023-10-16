"""
Definition of views.
"""

from asyncio.windows_events import NULL
from datetime import datetime
from django.contrib.auth.models import User
from turtle import title
from urllib import request
from django.shortcuts import get_object_or_404, render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.http import HttpRequest
from django.urls import is_valid_path
from app.models import *
from app.forms import DataForm, DeleteForm, RegisterForm, commentForm, searchForm

# @login_required
def OverView(request):
    
    if request.method == "GET":
        searchform = searchForm(request.GET)
        repoDatas = RepoData.objects.all()  
        return render(request ,'app/OverView.html' , {"repoDatas" : repoDatas,"searchForm" : searchform})
    
    if request.method == "POST":
        searchform = searchForm(request.POST)
        if searchform.is_valid():
            repoDatas = RepoData.objects.filter(title__icontains = searchform.cleaned_data['search'])
            return render(request,'app/OverView.html',{"searchForm" : searchform,"repoDatas" : repoDatas})
# @login_required
def Data(request):
    if request.method == "GET":
        form = DataForm()
        return render(request,'app/DataForm.html',{'form' : form})
    if request.method == "POST":
        form = DataForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
        return redirect('Add')



def Delete(request):
    if request.method == "GET":
        form = DeleteForm()
        return render(request, 'app/DeleteDataForm.html' , {'form':form})

    if request.method == "POST":
        form = DeleteForm(request.POST)
        if form.is_valid():
            query = RepoData.objects.filter(title = form.cleaned_data['title'])
            query.delete()
            return redirect('Delete')

def comment(request):
    if request.method == "GET":
        comments = RepoComments.objects.all()
        return render(request,'app/comment.html',{'comments': comments})

def AddComment(request):
    if request.method == "GET":
        form = commentForm(request.GET)
        return render(request,'app/AddComment.html',{'form': form})
    if request.method == "POST":
        form = commentForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('comment')

def user(request,username):
    if request.method == "GET":
        user = get_object_or_404(User,username = username)
        return render(request,'app/user.html',{'user':user})

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
