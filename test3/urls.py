
from django.urls import path
from . import views



app_name = 'test3'
urlpatterns =[
     path('test', views.test, name='test'),
     path('test2', views.test2, name='test2'),
     path('test3', views.test3, name="test3")
    ]
