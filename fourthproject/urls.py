"""fourthproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from fourthapp import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='indexpage'),
    path('loginpage/', views.loginpage, name='loginpage'),
    path('homepage/', views.homepage, name='homepage'),
    path('profilepage/', views.profilepage, name='profilepage'),
    path('registerpage/', views.registerpage, name='registerpage'),
    path('logoutuser/', views.logoutuser, name='logoutuser')
]
# path('logout/', auth_view.LogoutView.as_view(template_name='fourthapp/logout.html'), name='logout')
# path('out/', views.outpage, name='outpage'),
