from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('insert_operation_screen/',views.GotoInsertOperation,name='insert_operation_screen'),
    path('check_operations_screen/',views.GotoListOperation,name='check_operations_screen'),
    path('insert_operation/',views.InsertOperations,name='insert_operation'),
    path('check_operations',views.checkOperations,name='check_operation',),
    path('search_operations',views.SearchOperations,name='search_operations')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)