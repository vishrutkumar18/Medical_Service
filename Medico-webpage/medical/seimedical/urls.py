"""medical URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('reports', views.reports, name='reports'),
    path('contact', views.contact, name='contact'),
    path('sevices', views.services, name='services.html'),
    path('kmedic', views.kmedic, name='kmedic'),
    path('fmedic', views.fmedic, name='fmedic'),
    path('petient', views.petient, name='petient.html'),
    path('corporate', views.corporate, name='corporate.html'),
    path('certi', views.certi, name="certi.html"),
    path('showdata', views.showdata, name='showdata.html')
]
