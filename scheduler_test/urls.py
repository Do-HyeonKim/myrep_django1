
from django.urls import path
from . import views
from . import scheduler

app_name = 'test'
urlpatterns =[
     path('start',scheduler.scheduler_start, name='scheduler_start'),   
     path('run', views.run, name='run'),
     path('run2', views.run2, name='run2'),
    ]
