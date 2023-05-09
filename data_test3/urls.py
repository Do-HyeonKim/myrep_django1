
from django.urls import path
from . import views

app_name = 'dt3'
urlpatterns =[
     path('test1',views.test_find_column, name='test_find_column'),   
    ]
