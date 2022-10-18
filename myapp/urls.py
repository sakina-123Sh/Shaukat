from django.contrib import admin
from django.urls import path
from.views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register(r'Emp-view-set',EmployeeTableViewSet ,basename='EmployeeTable')

urlpatterns = [

    path('',home,name="home"),
    path('post_emp',Post_emp,name='Post_emp'),
    path('patch_emp/',patch_Emp,name="patch-emp"),
    path('get_emp/',get_emp,name='get_emp'),
    path('emp/',EmployeeView.as_view()),


]

urlpatterns += router.urls
