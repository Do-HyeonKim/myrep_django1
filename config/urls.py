"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dt/', include('data_test.urls')),
    path('dt2/', include('data_test2.urls')),
    path('dt3/', include('data_test3.urls')),
    path('test/', include('scheduler_test.urls')),
    path('query/', include('query_test.urls')),
    path('query2/', include('query_test2.urls')),
    path('web/', include('webcra.urls')),
    path('test3/', include('test3.urls')),
]
