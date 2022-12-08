from django.http import HttpRequest
from django.shortcuts import render

from Models.familiar.forms import FormularioFamiliar
from Models.familiar.models import familiar


class FormularioFamiliarView(HttpRequest):
    def index(request):
        familiar = FormularioFamiliar()
        return render(request, "FamiliarIndex.html", {"form":familiar})

    def procesar_formulario(request):
        familiar=FormularioFamiliar(request.POST)
        if familiar.is_valid():
            familiar.save()
            familiar=FormularioFamiliar()
        return render (request, "FamiliarIndex.html", {"form":familiar, "mensaje":"OK"})
    def ListarFamiliares(request):
        familiares = familiar.objects.all()
        return render (request, "ListaFamiliares.html",{"familiares":familiares})
    def edit (request, id_familiar):
        Familiar = familiar.objects.filter(id=id_familiar).first()
        form=FormularioFamiliar(instance=Familiar)
        return render(request,"familiarEdit.html",{"form":form,'Familiar':Familiar})
    def actualizar_Familiar(request, id_familiar):
        Familiar = familiar.objects.get(pk=id_familiar)
        form = FormularioFamiliar(request.POST, instance=Familiar)
        if form.is_valid():
            form.save()
        familiares = familiar.objects.all()
        return render (request, "ListaFamiliares.html", {"familiares": familiares, "mensajeActualizacion":"OK"})
    def delete(request, id_familiar):
        Familiar = familiar.objects.get(pk=id_familiar)
        Familiar.delete()
        familiares = familiar.objects.all()
        return render (request, "ListaFamiliares.html", {'familiares': familiares, "mensaje":"OK"})



