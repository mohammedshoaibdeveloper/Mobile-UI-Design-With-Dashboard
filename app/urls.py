from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('mobile', views.mobile,name='mobile'),
    path('contact', views.contact,name='contact'),
    path('detail/<int:id>', views.detail,name='detail'),
    
    
]