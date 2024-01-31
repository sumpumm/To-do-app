from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',index),
    path('about',about),
    path('contact',contact),
    path('create',create),
    path('task/<pk>',mark_completed),
    path('edit/<pk>',edit),
    path('delete/<pk>',delete),
    
    
]