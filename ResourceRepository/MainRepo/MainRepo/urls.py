"""
Definition of urls for MainRepo.
"""

from datetime import datetime
from django.urls import path, re_path
from django.conf import settings
from django.contrib import admin
from django.views.static import serve
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('OverView/', views.OverView , name = 'OverView'),
    path('OverView/Add',views.Data, name = 'Add'),
    path('OverView/Delete',views.Delete,name = 'Delete'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('register/',views.sign_up,name='register'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG :
    urlpatterns += [
        re_path(r'^OverView/media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT,}),
        ]
