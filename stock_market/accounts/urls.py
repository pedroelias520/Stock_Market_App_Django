from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.signup_screen, name='signup'),
    path('register/', views.register, name='register'),
    path('login/', views.login_screen, name='login'),
    path('log_user/', views.log_user, name='log_user'),
    path('logout/', views.logout_user, name='logout')
]