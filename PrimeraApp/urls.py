"""PrimeraApp URL Configuration

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
from django.urls import path

from Models.familiar.views import FormularioFamiliarView
from View.HomeView import HomeView
urlpatterns = [
    #path('admin/', admin.site.urls)
    path('', HomeView.home, name='home'),
    path('formulario/', HomeView.formulario, name='formulario'),
    path('registrarFamiliar/', FormularioFamiliarView.index, name='registrarFamiliar'),
    path('guardarFamiliar/', FormularioFamiliarView.procesar_formulario, name='guardarFamiliar'),
    path('ListaFamiliares/', FormularioFamiliarView.ListarFamiliares, name='ListaFamiliares'),
    path('editarFamiliares/<int:id_familiar>', FormularioFamiliarView.edit, name="editarFamiliar"),
    path('actualizarFamiliares/<int:id_familiar>', FormularioFamiliarView.actualizar_Familiar, name='actualizarFamiliares'),
    path('eliminarFamiliares/<int:id_familiar>', FormularioFamiliarView.delete, name='eliminarFamiliares'),

]
