"""normal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URL conf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from begin import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', auth_views.home, name='home'),
    path('detail/', auth_views.detail, name='detail'),
    path('advice/', auth_views.advice, name='advice'),
    path('login/', auth_views.login,name='login'),
    path('logout/', auth_views.logout, name='logout'),
    path('sign_up/', auth_views.sign_up, name='sign_up'),

]
