"""
URL configuration for inmueblesApp project.

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
from django.contrib.auth.views import LoginView
from registro_inmuebles.views import index, about, Welcome, contact, success, registro, perfil_usuario, modificar_usuario, agregar_inmueble, lista_inmuebles, editar_inmueble, eliminar_inmueble
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name= "index"),
    path("about/", about, name= "about"),
     path('welcome/', Welcome.as_view(), name='welcome'),
    path("contact/", contact, name= "contact"),
    path("success/", success, name= "success"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', include('django.contrib.auth.urls'), name='login'),
    path('logout/', include('django.contrib.auth.urls'), name='logout'),
    path('password_change/', include('django.contrib.auth.urls'), name='password_change'),
    path('password_change/done/', include('django.contrib.auth.urls'), name='password_change_done'),
    path('password_reset/', include('django.contrib.auth.urls'), name='password_reset'),
    path('password_reset/done/', include('django.contrib.auth.urls'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', include('django.contrib.auth.urls'), name='password_reset_confirm'),
    path('reset/done/', include('django.contrib.auth.urls'), name='password_reset_complete'),
    path('registro/', registro, name='registro'),
    path('profile/', perfil_usuario, name='profile'),
    path('modificar_usuario/', modificar_usuario, name='modificar_usuario'),
    path('agregar_inmueble/', agregar_inmueble, name='agregar_inmueble'),
    path('lista_inmuebles/', lista_inmuebles, name='lista_inmuebles'),
    path('editar_inmueble/<int:id>/', editar_inmueble, name='editar_inmueble'),
    path('eliminar_inmueble/<int:id>/', eliminar_inmueble, name='eliminar_inmueble'),


]
