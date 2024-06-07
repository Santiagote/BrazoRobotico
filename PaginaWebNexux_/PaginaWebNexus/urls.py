"""
URL configuration for PaginaWebNexus project.

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
from django.urls import path

from IngresoPaginaWeb.views import home, controles, descripcion, registro, Login
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('controles/', controles, name='controles'),
    path('grabar_objetos/', views.vista_grabar_objetos, name='grabar_objetos'),
    path('recoger_objetos/', views.vista_recoger_objetos, name='recoger_objetos'),
    path('descripcion/', descripcion, name='descripcion'),
    path('registro/', registro, name='registro'),
    path('Login/', Login, name='Login'),
]


