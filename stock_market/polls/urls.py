from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('insert_operation/',views.InserirOperacao,name='add_operation'),   
    path('insert_user/',views.InsertUser,name='login_form'),   
]