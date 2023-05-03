
from django.urls import path
from . import views

app_name = 'dt2'
urlpatterns =[
     path('test1',views.microseconds_to_date, name='microseconds_to_date'),   
     path('test2',views.date_to_microseconds, name='date_to_microseconds'),  
     path('test3',views.json_test, name='json_test'),  
    ]
