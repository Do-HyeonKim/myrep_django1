
from django.urls import path
from . import views



app_name = 'web'
urlpatterns =[
     path('test', views.test, name='test'),
     path('test2', views.test2, name='test2'),
     path('test3', views.test3, name='test3'),
     path('login_test', views.login_test, name='login_test'),
    ]
