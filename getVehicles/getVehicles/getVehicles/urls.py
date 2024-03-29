"""
URL configuration for getVehicles project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from users import views as user_view
from cars import views as car_view
from  django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',car_view.index,name="index"),
    path('cars/',include('cars.urls')),
    path('register/',user_view.register,name="register"),
    path('login/',user_view.OwnLoginView.as_view(),name='login'),
    path('logout/',user_view.logout_user,name="logout_user"),
    path('contact/',user_view.getContact,name="getContact"),
]