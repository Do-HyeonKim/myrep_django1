
from django.urls import path
from . import views



app_name = 'query2'
urlpatterns =[
     path('test', views.test, name='test'),
    #  path('', views., name=''),
    ]
