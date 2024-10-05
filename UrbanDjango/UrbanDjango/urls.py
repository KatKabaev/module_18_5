"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.views.generic import TemplateView
from task2.views import index, Index2
from task4.views import platform, game, cart
from task5.views import sign_up_by_django, sign_up_by_html

urlpatterns = [
    path('admin/', admin.site.urls),
    path('func/', index),
    path('class/', Index2.as_view()),
    path('platform/', platform),
    path('platform/games/', game),
    path('platform/cart/', cart),
    path('html_sign_up/', sign_up_by_html),
    path('django_sign_up/', sign_up_by_django),
]