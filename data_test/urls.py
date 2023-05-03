
from django.urls import path
from . import views

app_name = 'dt'

urlpatterns =[
    path('test1',views.read_time_value, name='read_time_value'),   
    path('test2',views.read_time_value2, name='read_time_value2'),                   
    ]
