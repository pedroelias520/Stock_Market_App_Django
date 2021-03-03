from django.urls import path, include

from . import views

urlpatterns = [
    path('/', views.Home, name='home'),
    path('insert_operation/',views.InserirOperacao,name='add_operation'),   
    path('insert_user/',views.InsertUser,name='login_form'),  
    path('accounts/', include('accounts.urls')),   
]