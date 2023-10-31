from django.contrib import admin
from django.urls import path
from prediction import views
from django.contrib.auth import views as auth_views

urlpatterns =[
 path("generate_prediction",views.generate_prediction,name = 'generate_prediction'),
 
]



