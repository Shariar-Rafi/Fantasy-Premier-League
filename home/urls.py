from django.contrib import admin
from django.urls import path
from home import views
from django.contrib.auth import views as auth_views

urlpatterns =[
    path("",views.index,name = 'home'),
    path("home",views.index,name = 'home'),
    path("AboutUS",views.AboutUS,name = 'AboutUS'),
    path("ContactUS",views.ContactUS,name = 'ContactUS'),
    path("Player",views.Player,name = 'Player'),
    path("PlayerReg",views.PlayerReg,name = 'PlayerReg'),
    path("MyHomePage",views.MyHomePage,name = 'MyHomePage'),
    path("TermsOfService",views.TermsOfService,name = 'TermsOfService'),
    path("MyProfile",views.MyProfile,name = 'MyProfile'),
    path("logout",views.LogoutPage,name = 'logout'),
    path("Prediction",views.Prediction,name = 'Prediction'),
    


path(
        'ChangePass/',
        auth_views.PasswordChangeView.as_view(
            template_name='regi/changePass.html',
            success_url = '/PlayerProfile'
        ),
        name='ChangePass'
    ),

]