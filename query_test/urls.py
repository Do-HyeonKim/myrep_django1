
from django.urls import path
from . import views



app_name = 'query'
urlpatterns =[
     path('test', views.test, name='test'),
    #  path('', views., name=''),
    ]
