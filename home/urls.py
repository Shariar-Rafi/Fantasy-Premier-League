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
    path("Coach",views.Coach,name = 'Coach'),
    path("PlayerReg",views.PlayerReg,name = 'PlayerReg'),
    path("MySquad",views.MySquad,name = 'MySquad'),
    path("TermsOfService",views.TermsOfService,name = 'TermsOfService'),
    path("PlayerProfile",views.PlayerProfile,name = 'PlayerProfile'),
    path("logout",views.LogoutPage,name = 'logout'),


path(
        'ChangePass/',
        auth_views.PasswordChangeView.as_view(
            template_name='regi/changePass.html',
            success_url = '/PlayerProfile'
        ),
        name='ChangePass'
    ),

]