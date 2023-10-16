"""
Definition of forms.
"""

from dataclasses import fields
from pyexpat import model
from turtle import title
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.translation import gettext_lazy as _

from app.models import RepoData , RepoComments 

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
    
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        exclude = ('user_permissions','groups','is_superuser','last_login','is_staff','is_active','password','date_joined')

class DataForm(forms.ModelForm):
    class Meta:
        model = RepoData
        exclude = ('user',)
        
class DeleteForm(forms.Form):
    title = forms.CharField(max_length=25)
    
class searchForm(forms.Form):
    search = forms.CharField(max_length=250)
    
class commentForm(forms.ModelForm):
    class Meta:
        model = RepoComments
        exclude = ('user',)
