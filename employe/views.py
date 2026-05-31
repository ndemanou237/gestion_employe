from django.shortcuts import render,redirect
from .models import Employe
from .forms import EmployeForm

def liste_employes(request):
    employes = Employe.objects.all()
    context = {
        'employes':employes
        }
    return render(request, "employe/list.html", context)

def ajouter_employer(request):
    form = EmployeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('liste_employes')
    context = {
        'form':form
        }
    return render(request, "employe/formulaire.html", context)

